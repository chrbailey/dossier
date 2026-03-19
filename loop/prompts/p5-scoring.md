# Phase 5: Scoring

## Purpose
Apply promotion thresholds from the contract to determine which evidence qualifies for tier advancement.

## Inputs
- P4 output (signals JSONL, signal extraction summary)
- Contract scoring config (promotionThresholds, humanReviewTriggers)
- Evidence store (current tier distribution)

## Process

1. **Query all evidence** for this contract:

```bash
cd "/Volumes/OWC drive/Dev/dossier"
python3 -c "
from scripts.evidence_store import EvidenceStore
import json
store = EvidenceStore()
print(json.dumps(store.tier_counts('${CONTRACT_ID}')))
store.close()
"
```

2. **For each evidence item**, check if it meets the promotion threshold for the next tier:
   - Confidence >= threshold.minConfidence?
   - Corroboration >= threshold.minCorroboration?
   - Age <= threshold.maxAge hours?
   - If threshold.requiresHumanReview → flag for review, do NOT auto-promote

3. **Check human review triggers**:
   - `confidence_regression`: any evidence whose confidence dropped since last cycle
   - `accusatory_claim`: any evidence with accusatory content
   - `high_contradiction_score`: contradiction signal > 0.7
   - `synchronized_silence_detected`: from P4's negative evidence

4. **Generate promotion candidates list** — evidence that qualifies for the next tier
5. **Generate hold list** — evidence that needs human review before promotion

## Output
Write to: `${storagePath}/cycle-${CYCLE}/p5-scoring.md`

Include:
- Promotion candidates (hash, current tier, target tier, confidence, corroboration)
- Hold items (hash, trigger reason, current confidence)
- Tier distribution before and after (if auto-promotions are applied)
- Any regression warnings
