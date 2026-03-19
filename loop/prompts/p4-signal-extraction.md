# Phase 4: Signal Extraction

## Purpose
Score each piece of new evidence across the contract's signal dimensions, and detect absence patterns.

## Inputs
- P3 output (evidence capture summary, hashes of new evidence)
- Contract signalExtraction config (dimensions + negative evidence config)
- Evidence store (query raw evidence from this cycle)

## Process

### Positive Signal Scoring

1. **Query this cycle's raw evidence** from the store:

```bash
cd "/Volumes/OWC drive/Dev/dossier"
python3 -c "
from scripts.evidence_store import EvidenceStore
import json
store = EvidenceStore()
evidence = store.query('${CONTRACT_ID}', tier='raw')
for e in evidence:
    if e['cycle_number'] == ${CYCLE}:
        print(json.dumps({'id': e['id'], 'hash': e['hash'], 'source': e['source_id'], 'content': e['content'][:200]}))
store.close()
"
```

2. **For each evidence item**, score across all dimensions from the contract:
   - `relevance` (LLM): How relevant to current AI landscape? 0.0–1.0
   - `novelty` (LLM): New information vs known? 0.0–1.0
   - `momentum` (rule): Is this topic mentioned by 2+ sources this cycle? 0/1
   - `contradiction` (LLM): Does this contradict established patterns? 0.0–1.0
   - `source_originality` (LLM): Original thought vs echo? 0.0–1.0
   - `silence_anomaly` (hybrid): Unexpected absence signal? 0.0–1.0

3. **Compute composite score**: weighted sum of dimension scores using contract weights

4. **Record signals** in the evidence store:

```bash
cd "/Volumes/OWC drive/Dev/dossier"
python3 -c "
from scripts.evidence_store import EvidenceStore
store = EvidenceStore()
store.add_signal(${EVIDENCE_ID}, '${CONTRACT_ID}', '${DIMENSION}', ${SCORE}, '${SCORER}', ${CYCLE})
store.close()
"
```

### Negative Evidence Detection

1. **Check posting gaps**: For each source in sourceUniverse:
   - Query evidence store for most recent evidence from that source
   - If gap exceeds silenceThreshold (168 hours) → record as silence_anomaly
2. **Check topic absence**: Based on prior cycle's top topics:
   - If a source normally discusses topic X but didn't this cycle → flag
3. **Check synchronized silence**: If 3+ sources go quiet simultaneously:
   - Record as synchronized_silence event
4. **Check behavioral divergence**: Compare this cycle's topic distribution per source against baseline:
   - Significant shift → flag as behavioral_divergence

## Output
Write to: `${storagePath}/cycle-${CYCLE}/p4-signals.jsonl` (one signal per line)
Write to: `${storagePath}/cycle-${CYCLE}/p4-signal-extraction.md` (narrative summary)

The narrative should include:
- Top 5 highest-scoring evidence items with composite scores
- Any contradiction signals (score > 0.5)
- Any silence/absence anomalies detected
- Cross-source convergence patterns (same topic from 2+ sources)
