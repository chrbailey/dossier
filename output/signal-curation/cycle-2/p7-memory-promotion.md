# P7 Memory Promotion -- Cycle 2

**Contract:** RLC.DOSSIER.SIGNAL.001
**Phase:** P7-memory-promotion
**Status:** completed
**Date:** 2026-03-19
**Cycle:** 2

## Summary

Executed first promotion cycle. Advanced 94 evidence items from raw to working tier based on composite signal scores. Held 3 items for human review. Updated confidence values across all evidence.

## Promotions Executed

### raw -> working: 94 items

All items with composite score >= 0.3 that did not trigger human review conditions were promoted. Confidence values set to weighted composite score.

**By source (promoted):**

| Source | Promoted | Held | Below Threshold |
|--------|----------|------|-----------------|
| dario-amodei | 9 | 3 | 0 |
| yann-lecun | 10 | 0 | 0 |
| karpathy | 12 | 0 | 0 |
| demis-hassabis | 10 | 0 | 0 |
| sama | 13 | 0 | 0 |
| harrison-chase | 8 | 0 | 0 |
| simon-willison | 10 | 0 | 0 |
| jim-fan | 7 | 0 | 0 |
| swyx | 6 | 0 | 1 |
| emad-mostaque | 3 | 0 | 1 |
| **Total** | **94** | **3** | **2** |

**Top 10 promoted (highest confidence):**

| ID | Hash | Source | Confidence | Content |
|----|------|--------|-----------|---------|
| 19 | 9eb3f5ee976ad78e | yann-lecun | 0.785 | AMI Labs $1.03B raise |
| 81 | 9146b9312ac6af94 | sama | 0.760 | Kalinowski resignation |
| 7 | c2534531ea7d66c2 | dario-amodei | 0.745 | DoW red lines statement |
| 10 | 283dc6b0c22ff775 | dario-amodei | 0.728 | Supply chain risk designation |
| 18 | a3bbba44b025d714 | yann-lecun | 0.725 | AMI Labs launch |
| 33 | e5d7d70cd6573273 | simon-willison | 0.720 | Astral acquisition analysis |
| 14 | 24f013471228f386 | sama | 0.708 | AI killing labor-capital balance |
| 4 | d2f0bfee537d2bd0 | karpathy | 0.703 | Intelligence brownouts |
| 2 | 57a10659da6a0d93 | karpathy | 0.703 | SETI@home for AI research |
| 75 | 9e70819910155b49 | dario-amodei | 0.698 | "No wall" scaling |

## Promotions Held (Pending Human Review)

3 items held. Written to `output/signal-curation/cycle-2/holds.json`.

| ID | Hash | Source | Confidence | Trigger |
|----|------|--------|-----------|---------|
| 8 | 24b66bac5b274d6d | dario-amodei | 0.713 | accusatory_claim: "straight up lies" |
| 9 | e355de5d222c8095 | dario-amodei | 0.698 | high_contradiction_score (0.7) |
| 42 | 3e2d0a59384750e9 | dario-amodei | 0.550 | accusatory_claim: "straight up lies" |

**Recommendation:** All three are well-documented public statements. Recommend approving promotion with `human_reviewed: true` metadata tag.

## Items Below Threshold (Not Promoted)

| ID | Hash | Source | Composite | Reason |
|----|------|--------|-----------|--------|
| 38 | dae517ad6fdf263f | emad-mostaque | 0.285 | Silence event -- low substantive signal |
| 99 | 7e744030697dd9c4 | swyx | 0.000 | Search gap placeholder -- no real evidence |

## Updated Tier Distribution

| Tier | Before | After | Delta |
|------|--------|-------|-------|
| raw | 99 | 5 | -94 |
| working | 0 | 94 | +94 |
| verified | 0 | 0 | 0 |
| promoted | 0 | 0 | 0 |
| training | 0 | 0 | 0 |
| locked | 0 | 0 | 0 |

## Confidence Updates

All 99 evidence items had their confidence field updated to their weighted composite score, regardless of promotion status. This ensures the confidence field reflects the latest signal analysis even for held and below-threshold items.

**Confidence distribution (all items):**

| Range | Count |
|-------|-------|
| 0.70+ | 12 |
| 0.60-0.69 | 26 |
| 0.50-0.59 | 31 |
| 0.40-0.49 | 13 |
| 0.30-0.39 | 15 |
| < 0.30 | 2 |

## Next Promotion Gate

For working -> verified:
- **Min Confidence:** 0.5
- **Min Corroboration:** 1 (requires at least one corroborating source)
- **Human Review:** No
- **Max Age:** 336 hrs

Currently 69 items at working tier meet the confidence threshold (>= 0.5). The corroboration gate (>= 1) will be the binding constraint -- most items have corroboration_count = 0 since duplicate detection runs on exact source+content hash. Cycle 3 should focus on cross-source corroboration to unlock working -> verified promotions.

## Artifacts

- **This report:** `output/signal-curation/cycle-2/p7-memory-promotion.md`
- **Holds file:** `output/signal-curation/cycle-2/holds.json`
- **Database updated:** `data/evidence.db` -- 94 items promoted, all confidences updated
