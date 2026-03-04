# DSPy Integration for Dossier — Design Document

**Date:** 2026-03-03
**Status:** Approved
**Author:** Christopher Bailey + Claude

## Problem

Dossier's 7 phase prompts (p1-p7) are hand-crafted instructions that produce structured due-diligence reports. Quality depends entirely on prompt engineering intuition. There is no systematic way to:

1. Evaluate prompt quality across domains
2. Improve prompts based on outcome data
3. Bootstrap few-shot demonstrations from successful runs
4. Search over instruction variants to find optimal phrasings

DSPy (Stanford NLP) solves this with a "prompts as compiled artifacts" paradigm — declare typed I/O contracts (Signatures), compose them (Modules), and let optimizers automatically find the best instructions and demonstrations.

## Constraint

All LLM calls must route through the Claude Code Max subscription via the Claude Agent SDK (`claude-agent-sdk`). Zero Anthropic API spend. This constrains optimizer choice due to rate limits (~225 msgs/5hr on Max 5x, ~900 on Max 20x).

## Architecture

### Separation: Offline Compiler + Unchanged Runtime

```
COMPILE TIME (DSPy + Agent SDK)
────────────────────────────────
Past dossier outputs (output/okta.com/, etc.)
    |
dspy/signatures.py  (7 Signature classes)
    |
dspy/modules.py     (7 Module wrappers)
    |
ClaudeAgentLM       --> claude-agent-sdk --> Claude Code Max
    |
BootstrapFewShotWithRandomSearch  (~30-50 calls)
    |
Optimized program   --> dspy/compiled/dossier_v{N}.json
    |
dspy/export.py      --> Writes optimized instructions to prompts/p{N}.md


RUNTIME (unchanged)
────────────────────────────────
target.env --> ralph-prompt.md --> prompts/p{N}.md (OPTIMIZED) --> sub-agents --> output/
```

The Ralph Loop orchestrator, PROGRESS.md state machine, and sub-agent dispatch are untouched. DSPy only optimizes the instruction text inside each phase prompt.

## Components

### 1. ClaudeAgentLM — Custom DSPy Backend (~60 lines)

Subclasses `dspy.BaseLM` (not `dspy.LM` — bypasses litellm entirely). Implements `forward()` by calling the Claude Agent SDK's `query()` function.

Key features:
- Routes all calls through Max subscription (no API key needed)
- Session persistence (`self._session_id`) for rate-limit recovery
- `max_turns=1` — pure LLM completion, no agentic loops
- `allowed_tools=[]` — prevents tool use during optimization calls

```python
import asyncio
from typing import Any
import dspy
from litellm import ModelResponse
from claude_agent_sdk import query, ClaudeAgentOptions

class ClaudeAgentLM(dspy.BaseLM):
    def __init__(self, model="sonnet", max_turns=1, timeout=300, **kwargs):
        super().__init__(
            model=f"claude-agent/{model}", model_type="chat",
            temperature=0.0, max_tokens=8000, cache=False, **kwargs
        )
        self.cli_model = model
        self.max_turns = max_turns
        self.timeout = timeout
        self._session_id = None

    def forward(self, prompt=None, messages=None, **kwargs) -> ModelResponse:
        return asyncio.run(self.aforward(prompt=prompt, messages=messages, **kwargs))

    async def aforward(self, prompt=None, messages=None, **kwargs) -> ModelResponse:
        messages = messages or [{"role": "user", "content": prompt}]

        system_parts, conv_parts = [], []
        for msg in messages:
            if msg["role"] == "system":
                system_parts.append(msg["content"])
            else:
                conv_parts.append(f'[{msg["role"]}]: {msg["content"]}')

        formatted_prompt = "\n\n".join(conv_parts)

        options = ClaudeAgentOptions(
            model=self.cli_model,
            max_turns=self.max_turns,
            system_prompt="\n".join(system_parts) if system_parts else None,
            allowed_tools=[],
        )
        if self._session_id:
            options.resume = self._session_id

        result_text = ""
        async for message in query(prompt=formatted_prompt, options=options):
            if hasattr(message, "session_id"):
                self._session_id = message.session_id
            if hasattr(message, "result"):
                result_text = message.result

        return ModelResponse(
            choices=[{
                "index": 0,
                "message": {"role": "assistant", "content": result_text},
                "finish_reason": "stop",
            }],
            model=self.model,
            usage={
                "prompt_tokens": len(str(messages)) // 4,
                "completion_tokens": len(result_text) // 4,
                "total_tokens": (len(str(messages)) + len(result_text)) // 4,
            },
        )
```

### 2. Signatures — 7 Phase Contracts

Each phase becomes a `dspy.Signature` with typed fields. The docstring becomes the optimizable instruction.

| Phase | Signature | Key Inputs | Key Outputs |
|-------|-----------|-----------|-------------|
| P1 Discovery | `Discovery` | domain, whois_data, website_content | company_profile, tech_stack, product_description |
| P2 Market | `MarketAnalysis` | company_profile, product_description | tam_sam_som, competitors, swot, positioning |
| P3 Technical | `TechnicalAssessment` | company_profile, github_org | architecture, repo_stats, code_quality |
| P4 Claims | `ClaimsTriangulation` | discovery_report, technical_report | claims_inventory, signal_intelligence, triangulated_estimates, materiality |
| P5 Academic | `AcademicLandscape` | company_profile, key_personnel | ip_landscape, patents, publications |
| P6 Valuation | `ValuationModel` | all_prior_reports | business_model, saas_metrics, replication_cost, build_vs_buy |
| P7 Report | `FinalReport` | all_prior_reports | executive_summary, full_report |

### 3. Metrics — Evaluation Functions

Composite metric per phase, combining:

- **Section completeness** (0-1): Are all expected markdown sections present?
- **Source diversity** (0-1): How many of 11 source types cited? (Primarily for P4)
- **Substantiation ratio** (0-1): % of claims with evidence links
- **Triangulation confidence** (0-1): Average convergence across estimates (P4-specific)

These are computed from the text output — no LLM call needed for evaluation.

### 4. Optimizer — Rate-Limit-Aware

**Primary:** `BootstrapFewShotWithRandomSearch` (~30-50 calls)
- 5 random seeds, 2 bootstrapped demos, 1 labeled demo per module
- Fits comfortably in a single Max 5x window

**Upgrade path:** `MIPROv2` (~200-300 calls)
- Only on Max 20x or spread across multiple windows
- Session resume via `ClaudeAgentLM._session_id`

### 5. Export — Compiled Instructions to Markdown

After optimization, `export.py` reads the optimized program's instruction strings and writes them back into the `prompts/p{N}-*.md` files. The markdown structure is preserved; only the instruction content changes.

Versioned outputs saved to `dspy/compiled/dossier_v{N}.json` for rollback.

## File Structure

```
dossier/
  dspy/
    lm.py              # ClaudeAgentLM (Agent SDK backend)
    signatures.py      # 7 Signature classes
    modules.py         # 7 Module wrappers
    metrics.py         # Evaluation functions
    compile.py         # Optimizer driver (rate-limit aware)
    export.py          # Compiled instructions --> prompts/p{N}.md
    compiled/          # Serialized optimized programs
  prompts/             # EXISTING -- targets of optimization
  output/              # EXISTING -- training data source
  requirements.txt     # dspy, claude-agent-sdk, litellm
```

## Cold Start Plan

1. Use existing `output/okta.com/` as seed (0 new calls)
2. Run current prompts on 3-4 more domains: stripe.com, datadog.com, cloudflare.com, vercel.com (~28 calls via Ralph Loop)
3. Manually score each phase output 0-1 on completeness, source diversity, substantiation (~30 min)
4. First optimization: `BootstrapFewShot` with 5 examples (~5 calls)
5. A/B test: one domain with original vs. optimized prompts (~14 calls)
6. Graduate to `BootstrapFewShotWithRandomSearch` (~30-50 calls)

**Total bootstrap budget: ~100 claude calls across 2-3 sessions.**

## Rate Limit Budget

| Activity | Calls | Window |
|----------|-------|--------|
| Bootstrap dossiers (4 domains) | ~28 | 1 session |
| BootstrapFewShot optimization | ~5 | Same session |
| A/B test (1 domain, 2 versions) | ~14 | Same session |
| BootstrapFewShotWithRandomSearch | ~30-50 | Next session |
| **Total** | **~100** | **2 sessions** |

## Dependencies

- `dspy` (pip) — Stanford NLP framework
- `claude-agent-sdk` (pip) — Claude Code programmatic interface
- `litellm` (pip) — Only for `ModelResponse` type (no API calls)

## Success Criteria

1. ClaudeAgentLM works as a DSPy backend (all calls via Max subscription)
2. At least 5 labeled dossier outputs as training data
3. Optimized prompts produce higher metric scores than originals on held-out domain
4. Export pipeline writes clean markdown back to prompts/

## Future Extensions

- **Approach 2:** Apply same pattern to touchgrass coefficient learning
- **Approach 3:** epistemic-engine flow_control as DSPy Refine module
- **MIPROv2:** Once comfortable with rate budget on Max 20x
- **Pydantic bridge:** Agent SDK structured output <-> DSPy Signature validation
