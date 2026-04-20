# P5 Scoring -- Cycle 2

**Contract:** RLC.DOSSIER.SIGNAL.001
**Phase:** P5-scoring
**Status:** completed
**Date:** 2026-03-19
**Cycle:** 2

## Summary

Applied promotion thresholds to all 99 evidence items (61 Cycle 1 + 36 Cycle 2 + 2 supplemental). All items are currently at raw tier. Used weighted composite signal scores as confidence values.

### Promotion Rule Applied: raw -> working
- **Min Confidence:** 0.3
- **Min Corroboration:** 0
- **Human Review:** No (unless triggered by hold conditions)
- **Max Age:** 168 hrs (all items within window -- March 2026)

## Results

| Category | Count |
|----------|-------|
| Total evidence items | 99 |
| Above threshold (>= 0.3) | 97 |
| Below threshold (< 0.3) | 2 |
| Auto-promote to working | 94 |
| Hold for human review | 3 |

### Items Below Threshold (NOT promoted)

| ID | Hash | Source | Composite | Reason |
|----|------|--------|-----------|--------|
| 38 | dae517ad6fdf263f | emad-mostaque | 0.285 | Silence event with low signal -- no substantive content to promote |
| 99 | 7e744030697dd9c4 | swyx | 0.000 | No signals scored -- placeholder for search gap, not real evidence |

### Items Held for Human Review

| ID | Hash | Source | Composite | Review Trigger |
|----|------|--------|-----------|---------------|
| 8 | 24b66bac5b274d6d | dario-amodei | 0.713 | accusatory_claim: "straight up lies" |
| 42 | 3e2d0a59384750e9 | dario-amodei | 0.550 | accusatory_claim: "straight up lies" |
| 9 | e355de5d222c8095 | dario-amodei | 0.698 | high_contradiction_score (0.7) |

**Assessment of holds:**
- **IDs 8 and 42** both contain Amodei's accusation that OpenAI's military messaging was "straight up lies." This is a direct, named accusation from one CEO against a competitor. Hold is appropriate -- the evidence is real and public, but promotion should confirm the framing is factual reporting, not editorialization.
- **ID 9** is Amodei's consciousness claim (15-20% probability). The 0.7 contradiction score reflects that this contradicts industry consensus. Hold is appropriate -- this is the single highest-contradiction item in the dataset and should be reviewed before advancing.

All three holds are from Cycle 1, source dario-amodei. None of the 36 Cycle 2 items triggered holds.

## Composite Score Distribution

| Range | Count | Percentage |
|-------|-------|-----------|
| 0.70+ | 12 | 12.1% |
| 0.60-0.69 | 26 | 26.3% |
| 0.50-0.59 | 31 | 31.3% |
| 0.40-0.49 | 13 | 13.1% |
| 0.30-0.39 | 15 | 15.2% |
| < 0.30 | 2 | 2.0% |

**Mean composite:** 0.589
**Median composite:** 0.585
**Std deviation:** ~0.11

### Top 10 Promotion Candidates (highest composite)

| Rank | ID | Source | Composite | Cycle | Key Signal |
|------|-----|--------|-----------|-------|------------|
| 1 | 19 | yann-lecun | 0.785 | 1 | AMI Labs $1.03B raise -- anti-LLM thesis |
| 2 | 81 | sama | 0.760 | 2 | Kalinowski resignation from OpenAI |
| 3 | 7 | dario-amodei | 0.745 | 1 | DoW red lines statement |
| 4 | 10 | dario-amodei | 0.728 | 1 | Supply chain risk designation |
| 5 | 18 | yann-lecun | 0.725 | 1 | AMI Labs launch -- LeCun leaves Meta |
| 6 | 33 | simon-willison | 0.720 | 1 | OpenAI acquires Astral analysis |
| 7 | 14 | sama | 0.708 | 1 | AI killing labor-capital balance |
| 8 | 4 | karpathy | 0.703 | 1 | Intelligence brownouts concept |
| 9 | 2 | karpathy | 0.703 | 1 | SETI@home for AI research agents |
| 10 | 75 | dario-amodei | 0.698 | 2 | "No wall" scaling, $19B ARR |

### Score by Source (mean composite)

| Source | Items | Mean Composite | Highest |
|--------|-------|---------------|---------|
| dario-amodei | 12 | 0.659 | 0.745 |
| yann-lecun | 10 | 0.628 | 0.785 |
| karpathy | 12 | 0.605 | 0.703 |
| demis-hassabis | 10 | 0.592 | 0.677 |
| sama | 13 | 0.588 | 0.760 |
| harrison-chase | 8 | 0.597 | 0.677 |
| simon-willison | 10 | 0.556 | 0.720 |
| jim-fan | 7 | 0.571 | 0.648 |
| swyx | 7 | 0.413 | 0.603 |
| emad-mostaque | 4 | 0.382 | 0.465 |

## Human Review Trigger Analysis

### Triggers Evaluated
- **confidence_regression:** N/A -- first scoring cycle, no prior confidence to regress from
- **accusatory_claim:** Flagged 2 items (IDs 8, 42) containing "straight up lies"
- **high_contradiction_score:** Flagged 1 item (ID 9) with contradiction >= 0.7
- **synchronized_silence_detected:** Not triggered -- Mostaque silence downgraded in Cycle 2, no synchronized pattern

### Triggers NOT Fired (considered but not warranted)
- ID 77 (Amodei consciousness, contradiction 0.65): Below 0.7 threshold
- ID 81 (Kalinowski resignation, contradiction 0.55): Factual reporting, not accusatory
- IDs 96, 97 (Mostaque): Low-signal items, no accusatory content

## Artifacts

- **This report:** `output/signal-curation/cycle-2/p5-scoring.md`
- **Holds file:** `output/signal-curation/cycle-2/holds.json`
- **Promotions executed in:** P7-memory-promotion
