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

### Quality Gates (Autoresearch Pattern)
- Each phase output is scored by `scripts/evaluate_phase.py` (Evidence Density Score)
- Phases re-run with different strategies if EDS is below threshold
- See `research-program.md` for thresholds, strategy variants, and source weighting
- The human edits `research-program.md` to steer research strategy; agents execute it

## Verification

```bash
# Test helpers
python3 scripts/whois_lookup.py example.com
python3 scripts/arxiv_search.py "machine learning" 3

# Evaluate phase output quality
python3 scripts/evaluate_phase.py output/example.com/04-claims.md

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
