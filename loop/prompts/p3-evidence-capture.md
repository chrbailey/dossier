# Phase 3: Evidence Capture

## Purpose
Collect full content for discovered candidates and store as raw evidence.

## Inputs
- P2 output (candidates JSONL)
- Contract evidenceCapture config
- Evidence store path

## Process

1. **For each candidate** in P2 output:
   a. Use Firecrawl to fetch the full content at the candidate URL
   b. Extract the fields specified in contract.phases.evidenceCapture.captureFields
   c. The evidence store handles hash computation and dedup automatically
   d. Insert into evidence store as `raw` tier:

```bash
cd "/Volumes/OWC drive/Dev/dossier"
python3 -c "
from scripts.evidence_store import EvidenceStore
import json
store = EvidenceStore()
h = store.insert(
    '${CONTRACT_ID}',
    '${SOURCE_ID}',
    '''${CONTENT}''',
    json.loads('${METADATA_JSON}'),
    ${CYCLE}
)
print(f'hash={h}' if h else 'duplicate (corroboration incremented)')
store.close()
"
```

2. **For silence candidates** (sources with no recent content):
   a. Record a "silence event" in the evidence store:
      - source_id: the silent source
      - content: description of the silence
      - metadata: `{"type": "silence", "last_seen": "...", "days_silent": N}`

3. **Store raw artifacts** to `${storagePath}/raw/cycle-${CYCLE}/`

## Output
Write to: `${storagePath}/cycle-${CYCLE}/p3-evidence-capture.md`

Summary of:
- Total candidates processed
- New evidence inserted (count, by source)
- Duplicates found (corroboration bumps)
- Silence events recorded
- Any capture failures

## Important
- Use Firecrawl for all URL fetching — it handles JS rendering
- If a URL fails to fetch, log the failure but continue with other candidates
- The evidence store handles dedup — duplicates auto-increment corroboration_count
- **Fallback**: If Firecrawl is unavailable, use WebSearch to get content summaries. Note "partial capture" in the output and mark evidence metadata with `"capture_method": "websearch_summary"` so downstream phases know the content depth is limited.
