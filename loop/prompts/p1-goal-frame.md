# Phase 1: Goal Frame

## Purpose
Load the contract, validate the research scope, and set up this cycle's execution context.

## Inputs
- Contract JSON (provided by orchestrator)
- PROGRESS.md (current state)
- Evidence store metrics (entropy, self-citation ratio)

## Process

1. **Parse contract** — extract goalFrame section
2. **Validate freshness** — check that the contract's freshnessHorizon hasn't been exceeded since last cycle
3. **Check failure conditions** — evaluate each condition in goalFrame.failureConditions:
   - "Zero new evidence collected for 3 consecutive cycles" → check PROGRESS.md cycle log
   - "Source entropy drops below 1.0" → check evidence store
   - "Self-citation ratio exceeds 30%" → check evidence store
4. **If any failure condition is true** → write failure report and HALT
5. **Output the cycle plan**: which sources to query, what to look for, freshness constraints

## Evidence Store Queries

```bash
cd "/Volumes/OWC drive/Dev/dossier"
python3 -c "
from scripts.evidence_store import EvidenceStore
s = EvidenceStore()
print('entropy:', s.source_entropy('${CONTRACT_ID}'))
print('self_cite:', s.self_citation_ratio('${CONTRACT_ID}'))
print('tiers:', s.tier_counts('${CONTRACT_ID}'))
s.close()
"
```

## Output
Write to: `${storagePath}/cycle-${CYCLE}/p1-goal-frame.md`

The output should include:

```markdown
# Cycle ${CYCLE} — Goal Frame

## Objective
${contract.phases.goalFrame.objective}

## Commander's Intent
${contract.phases.goalFrame.commandersIntent}

## Active Sources This Cycle
| Source | Tier | Trust | Domains | Fresh Until |
|--------|------|-------|---------|-------------|
(table from sourceUniverse, filtered by allowedSources)

## Anti-Recursion Status
- Source entropy: ${value} (minimum: ${guard})
- Self-citation ratio: ${value} (maximum: ${guard})
- Hypothesis diversity: ${status}

## Failure Conditions
(evaluate each, show pass/fail)

## Cycle Focus
(based on gap analysis from prior cycle's P8, or default to broad scan)
```
