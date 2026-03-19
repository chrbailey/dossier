# Phase 7: Memory Promotion

## Purpose
Execute tier promotions identified in P5, applying the contract's promotion policy.

## Inputs
- P5 output (promotion candidates, hold items)
- Contract memoryPromotion config
- Evidence store

## Process

1. **Read P5's promotion candidates list**

2. **For each candidate**:
   a. If alternativeHypothesisRequired and no alternative logged → SKIP, note in output
   b. If target tier requires human review → DO NOT promote, add to hold queue
   c. Otherwise → execute promotion:

```bash
cd "/Volumes/OWC drive/Dev/dossier"
python3 -c "
from scripts.evidence_store import EvidenceStore
store = EvidenceStore()
result = store.promote('${CONTRACT_ID}', '${HASH}', '${TARGET_TIER}', confidence=${CONFIDENCE})
print('promoted' if result else 'failed')
store.close()
"
```

3. **For hold items** (need human review):
   - If PromptSpeak MCP available: call `ps_hold_create` with evidence summary and reason
   - Otherwise: write hold items to `${storagePath}/cycle-${CYCLE}/holds.json`
   - Format: `[{"hash": "...", "current_tier": "...", "target_tier": "...", "reason": "...", "confidence": 0.X}]`

4. **Update evidence confidence** based on this cycle's signal scores:
   - New confidence = weighted average of signal dimension scores from P4

## Alternative Hypothesis Logging
When alternativeHypothesisRequired is true, for each evidence item being promoted past "working":

Record:
- Main interpretation
- At least one alternative explanation
- Confidence in each
- Evidence count supporting each

## Output
Write to: `${storagePath}/cycle-${CYCLE}/p7-memory-promotion.md`

Include:
- Promotions executed (count, tier transitions)
- Promotions held for review (count, reasons)
- Promotions skipped (missing alternative hypothesis)
- Updated tier distribution

Write to: `${storagePath}/cycle-${CYCLE}/p7-hypotheses.md` (if any promotions require alternative hypotheses)
