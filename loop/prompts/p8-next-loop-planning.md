# Phase 8: Next-Loop Planning

## Purpose
Analyze this cycle's results and plan the next cycle's focus.

## Inputs
- All phase outputs from this cycle
- Contract nextLoopPlanning config
- Evidence store metrics (tier counts, entropy, self-citation)
- PROGRESS.md (cycle history)

## Process

### Gap Analysis (if enabled)
1. Which sources had zero evidence this cycle?
2. Which signal dimensions had consistently low scores?
3. Which hypotheses lack alternative explanations?
4. Which topics from prior cycles were not observed this cycle?
5. What evidence is approaching staleness (nearing maxAge)?

### Priority Rebalancing (if enabled)
1. Rank sources by average signal score this cycle
2. Rank sources by silence anomaly score (high = investigate more)
3. Suggest discoveryStrategy adjustment for next cycle:
   - If all sources covered evenly → maintain breadth_first
   - If specific sources showing high signal → suggest depth_first on those
   - If gaps identified → suggest adaptive focus on undersampled sources

### Convergence Check (if iterationStrategy has convergenceCriteria)
1. Read convergence metric (e.g., new_evidence_count) from this cycle
2. Compare against threshold
3. Track consecutive cycles meeting threshold
4. If windowSize consecutive cycles meet threshold → convergence achieved

### Anti-Recursion Assessment

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

Evaluate:
- Source entropy vs minimum threshold
- Self-citation ratio vs maximum threshold
- Hypothesis diversity (count of distinct alternative explanations across all verified+ evidence)
- Recommendation: safe to continue / caution / halt

## Output
Write to: `${storagePath}/cycle-${CYCLE}/p8-next-loop-planning.md`

Include:
- Gap analysis results
- Priority adjustments for next cycle
- Convergence status (met/not met, consecutive count)
- Anti-recursion assessment
- Recommended focus areas for next cycle
- Whether any earlyExitConditions are approaching

Also write: `${storagePath}/cycle-${CYCLE}/p8-next-tasks.json`
```json
{
  "cycle": N,
  "convergence_met": false,
  "consecutive_convergence_cycles": 0,
  "new_evidence_count": N,
  "recommended_strategy": "breadth_first",
  "priority_sources": ["source-1", "source-2"],
  "gaps": ["description of gaps"],
  "anti_recursion": {
    "entropy": 2.1,
    "self_cite": 0.05,
    "status": "healthy"
  },
  "exit_conditions_approaching": []
}
```
