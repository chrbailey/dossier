# Dossier — SaaS Due Diligence Engine

## What This Is

Automated SaaS company evaluation pipeline. Runs inside Claude Code — sub-agents handle 7 analysis phases, Ralph Loop drives iterative execution until all phases complete.

## How To Run

```bash
# 1. Set target
edit target.env  # DOMAIN=example.com

# 2. Run pipeline (Ralph Loop)
# /ralph-loop --max-iterations 20 --completion-promise "DOSSIER_COMPLETE"
# Paste contents of ralph-prompt.md when prompted

# 3. Find results
ls output/{domain}/
```

## Project Rules

### File Conventions
- Phase outputs go to `output/{domain}/0N-phase.md`
- Raw data goes to `output/{domain}/raw/*.json`
- Progress tracking in `output/{domain}/PROGRESS.md`
- Sub-agent prompts in `prompts/p{N}-{phase}.md`

### Sub-Agent Behavior
- Each phase sub-agent reads PROGRESS.md to understand prior work
- Sub-agents write their output files directly
- After completing a phase, update PROGRESS.md
- If a phase fails, log the blocker and move on

### Tool Resilience
- Phase prompts must specify the **information needed**, not just the tool to use
- Sub-agents inherit parent permission settings — WebFetch may be denied while WebSearch works
- WebSearch as WebFetch fallback produces high-quality output (search snippets often include richer metadata than raw HTML)
- Always tell sub-agents: "WebFetch may be unavailable — use WebSearch as fallback"
- Design for graceful degradation: if a data source is blocked, note the gap and continue

### Helper Scripts
- Python scripts in `scripts/` are called via Bash
- They output JSON to stdout — redirect to raw/ files
- Venv at `scripts/.venv/`

### Don't
- Don't hardcode domains — always read from target.env or PROGRESS.md
- Don't skip phases — if blocked, note the blocker and continue
- Don't overwrite prior phase outputs without reason

## Verification

```bash
# Check structure
ls "/Volumes/OWC drive/Dev/dossier/"

# Test helpers
cd "/Volumes/OWC drive/Dev/dossier"
scripts/.venv/bin/python scripts/whois_lookup.py example.com
scripts/.venv/bin/python scripts/arxiv_search.py "machine learning" 3

# Check phase outputs after a run
cat output/*/PROGRESS.md
```

## Phase DAG

```
P1 Discovery ──┬──→ P2 Market ────────┐
               ├──→ P3 Technical ──┐  │
               └──→ P5 Academic    │  │
                                   ▼  │
               P4 Claims (P1+P3) ──┤  │
                                   ▼  ▼
               P6 Valuation (all) ────┤
                                      ▼
               P7 Report (all) → DONE
```

## Research Loop Mode

In addition to SaaS due diligence (the original mode), Dossier supports contract-driven research loops.

### How To Run

```bash
# 1. Check/edit the contract
cat contracts/signal-curation.json

# 2. Run the loop via Ralph Loop
export CONTRACT=contracts/signal-curation.json
# /ralph-loop --max-iterations 10 --completion-promise "LOOP_COMPLETE"
# When prompted, read loop/ralph-prompt-loop.md and execute
```

### File Conventions
- Contracts: `contracts/*.json`
- Loop orchestrator: `loop/ralph-prompt-loop.md`
- Phase prompts: `loop/prompts/p{N}-{phase}.md`
- Evidence database: `data/evidence.db`
- Cycle outputs: `output/{contract-storage-path}/cycle-{N}/`
- Reports: `output/{contract-storage-path}/reports/`
- Context packs: `output/{contract-storage-path}/context/`

### Evidence Store
```bash
# Query evidence
python3 -c "from scripts.evidence_store import EvidenceStore; s = EvidenceStore(); print(s.tier_counts('RLC.DOSSIER.SIGNAL.001')); s.close()"

# Check anti-recursion
python3 -c "from scripts.evidence_store import EvidenceStore; s = EvidenceStore(); print('entropy:', s.source_entropy('RLC.DOSSIER.SIGNAL.001')); print('self_cite:', s.self_citation_ratio('RLC.DOSSIER.SIGNAL.001')); s.close()"
```

### Self-Citation Thresholds
- Recursion guard warns at 20% (`control.recursionGuards.maxSelfCitationRatio`)
- Early exit halts at 30% (`control.earlyExitConditions`)
- This gives a 10% buffer between warning and hard stop

### PromptSpeak Governance
When PromptSpeak MCP tools are available:
- Frame validation at cycle start
- Hold gates at checkpoint intervals
- Audit logging on completion
- Frame: `⊕◇⟳▶α` (strict, technical, iterative, execute, primary)
