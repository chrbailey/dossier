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
