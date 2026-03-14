# Dossier Project Review + Autoresearch-Inspired Improvements

**Date:** 2026-03-14
**Reviewer:** Claude (Opus 4.6)
**Scope:** Full project review + integration of Karpathy's autoresearch pattern

---

## Part 1: Project Assessment

### What Exists

Dossier is a 7-phase SaaS due diligence engine that transforms a domain name into a 10K-15K word intelligence report in 15-25 minutes. It runs entirely inside Claude Code — prompts are the program, PROGRESS.md is the database, Ralph Loop is the scheduler. Total codebase: ~120 LOC Python, ~1,300 LOC prompts.

**Five companies analyzed:** vercel.com, okta.com, glean.com, cerebras.ai, sierra.ai
**Post-validation:** 63 corrections applied across all dossiers, tracked in corrections-log.md

### What Works Well

1. **Prompt-as-program architecture.** Zero framework overhead. The intelligence layer (Claude) is the runtime. Prompts specify behavior. Markdown tracks state. This is elegant and correct.

2. **Phase 4 (Claims Validation) is the differentiator.** The shadow prediction market concept — triangulating 11 source types to reconstruct what insiders know — is genuinely novel. No comparable automated tool does this.

3. **DAG parallelism.** P2/P3/P5 run in parallel after P1. P4 starts when P1+P3 are done without waiting for P2/P5. This cuts wall-clock time from ~35 min to ~15-25 min.

4. **Graceful degradation.** Every phase is designed to work with incomplete data. If WebFetch is denied, use WebSearch. If a source returns nothing, note the absence. P7 runs even with skipped phases.

5. **The validation pipeline is honest.** The methodology-critique.md is one of the most thorough self-critiques I've seen in an AI project. It identifies 14 weaknesses ranked by severity and proposes concrete fixes.

### What Doesn't Work

**The five structural problems the methodology-critique.md correctly identifies:**

| # | Problem | Severity | Status |
|---|---------|----------|--------|
| 1 | Non-reproducibility — run twice, get different results | FATAL | Unaddressed |
| 2 | Source independence illusion — "3 sources converge" may be 1 source in 3 venues | FATAL | Unaddressed |
| 3 | Zero ground truth calibration — no back-testing against known outcomes | CRITICAL | Unaddressed |
| 4 | Systematic blind spots — can't see financials, cap table, litigation | CRITICAL | Acknowledged, structural |
| 5 | LLM hallucination in source attribution — citations may be fabricated | SERIOUS | Partially addressed |

**Additional gaps I observed:**

6. **Single-pass research.** Each phase runs once. If the WebSearch results happen to be poor that day, the output is poor. No iteration, no quality measurement, no retry-with-different-strategy.

7. **No objective quality metric.** There's no way to know if a phase output is "good" without a human reading it. The pipeline has no self-evaluation.

8. **No drift detection.** A dossier from January may be stale by March. No mechanism for periodic re-evaluation or delta reports.

9. **Hardcoded Mac paths.** `ralph-prompt.md` and `CLAUDE.md` reference `/Volumes/OWC drive/Dev/dossier/` — breaks on any other machine.

10. **No cost tracking.** No visibility into token usage per phase or per run.

---

## Part 2: The Autoresearch Pattern

### What Karpathy Built

[Autoresearch](https://github.com/karpathy/autoresearch) (released March 7, 2026) is a system where AI agents autonomously run ML experiments:

- **Three files:** `prepare.py` (fixed), `train.py` (agent modifies), `program.md` (human writes strategy)
- **Fixed 5-minute experiment budget** — ~12 experiments/hour, ~100 overnight
- **Objective evaluation:** validation bits-per-byte (val_bpb), lower = better
- **Keep or discard:** If val_bpb improves, keep the git commit. If not, `git reset`
- **Never stop:** Agent runs until human interrupts. If out of ideas, think harder

### Results

- 126 experiments overnight, loss dropped 0.9979 → 0.9697
- 700 changes over 2 days found ~20 additive improvements
- 11% efficiency gain on an already well-tuned model
- Agent found bugs a human expert missed (parameterless QKNorm missing scaler)

### The Core Insight

**You stop editing Python. You start editing Markdown that tells an agent how to think about editing Python.**

The human's job shifts from "experimenter" to "experimental designer." The agent handles:
- Proposing changes
- Executing experiments
- Measuring results
- Keeping improvements, discarding failures
- Running indefinitely without human intervention

---

## Part 3: Applying Autoresearch to Dossier

### The Mapping

| Autoresearch | Dossier Equivalent |
|---|---|
| `train.py` (the thing being improved) | Phase output files (e.g., `04-claims.md`) |
| `prepare.py` (fixed infrastructure) | Phase prompts + scripts + templates |
| `program.md` (research strategy) | **New: `research-program.md`** |
| val_bpb (objective metric) | **New: Evidence Density Score** |
| 5-minute experiment budget | Fixed-budget research sprint per phase |
| Keep/discard via git | Keep best output, discard regressions |
| Never stop | Iterate until quality threshold or max iterations |

### The Evidence Density Score (EDS)

Dossier needs an objective, computable quality metric. Autoresearch has val_bpb. Dossier should have EDS.

**Evidence Density Score** measures how well-supported a phase output is:

```
EDS = weighted_sum(
  url_citation_rate,        # claims with direct URLs / total claims
  source_coverage,          # sources with data / sources attempted
  triangulation_rate,       # claims with 3+ independent sources / total claims
  temporal_freshness,       # sources from last 6 months / total sources
  contradiction_detection,  # explicit contradictions noted / total claims
)
```

Each component is computable by a second-pass LLM evaluator reading the phase output. No human judgment needed.

**Why this works:** Like val_bpb, EDS is:
- Objective (computable from the output)
- Comparable across runs (same phase, same company, different attempts)
- Monotonically useful (higher EDS = better-supported conclusions)
- Not gameable by the agent (can't inflate by adding fake URLs — verifier catches it)

### The Autoresearch Loop for Dossier

```
┌─────────────────────────────────────────────────┐
│         Dossier Autoresearch Loop                │
│                                                  │
│  For each phase:                                 │
│                                                  │
│  1. RUN phase with current prompt + strategy     │
│  2. EVALUATE output → compute EDS                │
│  3. COMPARE to previous best EDS                 │
│     ├── Better? → KEEP (save as best)            │
│     └── Worse?  → DISCARD (revert to best)       │
│  4. REFLECT → what search strategies yielded     │
│     weak results? What sources were missed?      │
│  5. ADJUST strategy for next attempt             │
│  6. REPEAT until EDS > threshold OR max_attempts │
│                                                  │
│  Key difference from vanilla autoresearch:       │
│  - Each "experiment" is a research strategy,     │
│    not a code change                             │
│  - The agent modifies its SEARCH APPROACH,       │
│    not the infrastructure                        │
│  - Multiple strategies are tried: different      │
│    search queries, different source orderings,   │
│    different triangulation approaches            │
└─────────────────────────────────────────────────┘
```

### What Changes in Practice

**Before (current pipeline):**
```
P4 Claims → run once → accept output → move on
```

**After (autoresearch-enhanced):**
```
P4 Claims attempt 1 → EDS = 0.42 → keep (first attempt)
P4 Claims attempt 2 (different search queries) → EDS = 0.51 → keep (improvement)
P4 Claims attempt 3 (deeper Glassdoor/Blind) → EDS = 0.48 → discard (regression)
P4 Claims attempt 4 (add job board signals) → EDS = 0.58 → keep (improvement)
P4 Claims attempt 5 → EDS = 0.57 → discard
→ Quality threshold 0.55 met at attempt 4. Move on.
```

Each attempt uses a different research strategy. The agent learns which search approaches yield higher evidence density and iterates.

### Concrete Implementation

#### New file: `research-program.md`

This is the dossier equivalent of autoresearch's `program.md`. It tells the research agent how to think about improving research quality. The human edits this file to steer research strategy. The agent reads it before each research sprint.

#### New file: `scripts/evaluate_phase.py`

Computes EDS from a phase output file. Takes the markdown, counts citations, URLs, sources, triangulations. Returns a JSON score object.

#### Modified: `ralph-prompt.md`

Add iteration logic: after each phase completes, evaluate EDS. If below threshold, re-run with adjusted strategy. Track best output. Stop at max_attempts or threshold.

#### Modified: Phase prompts

Add a "Research Strategy Variants" section to each phase prompt. On attempt N, the agent selects strategy N (different search queries, source ordering, depth allocation).

---

## Part 4: Additional Improvements

### 1. Multi-Run Variance (addresses FATAL #1)

Run scoring phases (P4, P6) 3 times. Report median and range:
- AI Reality Score: 3/5 (range: 3-4, 2/3 agreement)
- Build vs Buy: 2.8/4 (range: 2.5-3.1)

### 2. Source Dependency Mapping (addresses FATAL #2)

Add to Phase 4: before claiming triangulation, map source dependencies:
```
Primary: SEC filing → Derivative: TechCrunch article → Derivative: HN discussion
→ These are 1 source, not 3
```

Require at least one structurally independent viewpoint per triangulation claim.

### 3. Blind Spots Section (addresses CRITICAL #4)

Every report must include a non-removable "What This Analysis Cannot See" section:
- Financial internals (revenue breakdown, NRR, burn rate)
- Customer data (churn, LTV/CAC, pipeline)
- Legal exposure (pending litigation, IP disputes)
- Cap table (dilution, preference stacks)
- Internal roadmap (actual priorities vs. marketing)

### 4. Temporal Drift Detection (new)

Add a `scripts/drift_check.py` that compares a previous dossier to current web signals:
- Re-run key searches from P1 and P4
- Compute similarity score against previous output
- Flag sections with >30% divergence
- Generate a delta report

### 5. Fix Hardcoded Paths

Replace `/Volumes/OWC drive/Dev/dossier/` with relative paths or read from environment.

---

## Part 5: Priority Ranking

| Priority | Change | Impact | Effort |
|----------|--------|--------|--------|
| **P0** | Evidence Density Score + evaluation script | Enables all iteration improvements | Medium |
| **P0** | research-program.md (autoresearch pattern) | Defines iteration strategy | Low |
| **P1** | Autoresearch loop in ralph-prompt.md | Iterative quality improvement | Medium |
| **P1** | Multi-run variance for scoring phases | Addresses reproducibility (FATAL) | Low |
| **P1** | Source dependency mapping in P4 | Addresses independence illusion (FATAL) | Low |
| **P2** | Blind spots section in P7 | Addresses systematic gaps (CRITICAL) | Low |
| **P2** | Fix hardcoded paths | Portability | Low |
| **P3** | Temporal drift detection | Freshness monitoring | Medium |
| **P3** | URL verification pass | Addresses hallucination (SERIOUS) | Medium |

---

## Summary

Dossier is a strong V1 — the architecture is elegant, the claims validation methodology is novel, and the self-critique is unusually honest. The biggest gap is **single-pass research with no quality measurement**. Karpathy's autoresearch provides the missing pattern:

1. Define an objective quality metric (EDS)
2. Run research in fixed-budget sprints
3. Evaluate after each sprint
4. Keep improvements, discard regressions
5. Iterate until quality threshold

The human stops being the researcher and becomes the **research designer** — editing `research-program.md` to steer which search strategies, source weightings, and triangulation approaches the agent should try.

This transforms dossier from "run once and hope the WebSearch results were good" to "iterate until the evidence base is strong enough to support conclusions."

---

*Sources:*
- [Karpathy autoresearch GitHub](https://github.com/karpathy/autoresearch)
- [VentureBeat coverage](https://venturebeat.com/technology/andrej-karpathys-new-open-source-autoresearch-lets-you-run-hundreds-of-ai)
- [MarkTechPost analysis](https://www.marktechpost.com/2026/03/08/andrej-karpathy-open-sources-autoresearch-a-630-line-python-tool-letting-ai-agents-run-autonomous-ml-experiments-on-single-gpus/)
- [Getting Started guide](https://medium.com/modelmind/getting-started-with-andrej-karpathys-autoresearch-full-guide-c2f3a80b9ce6)
