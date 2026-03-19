# Phase 6: Synthesis

## Purpose
Generate this cycle's output artifacts as defined in the contract.

## Inputs
- All prior phase outputs (P1-P5) for this cycle
- Contract synthesis config (outputArtifacts, crossCycleDelta)
- Prior cycle's outputs (for delta comparison)

## Process

For each artifact in contract.phases.synthesis.outputArtifacts:

### signals.jsonl (derived/signals.jsonl)
- Append this cycle's scored signals to the rolling JSONL file
- Each line: `{"cycle": N, "evidence_hash": "...", "composite_score": 0.X, "dimensions": {...}, "timestamp": "..."}`

### patterns.md (reports/patterns.md)
- Identify recurring themes across this cycle's evidence
- Note cross-source convergence (same topic from 2+ sources)
- Flag emerging patterns vs decaying ones
- If crossCycleDelta: compare against prior cycle's patterns.md

### watchlist_changes.md (reports/watchlist-changes.md)
- Sources that changed behavior this cycle
- New high-scoring sources
- Sources that went silent
- Topic shifts per source

### context_pack.md (context/pack.md)
- **This is the key output** — a distilled context document suitable for injection into future Claude sessions
- Structure: top signals, key patterns, active hypotheses, source health
- Keep under 2000 tokens for context efficiency
- Include: what matters NOW, what changed, what to watch

### silence_report.md (reports/silence-report.md)
- All negative evidence from this cycle
- Silence durations per source
- Synchronized silence events
- Behavioral divergence flags

## Cross-Cycle Delta
If contract.phases.synthesis.crossCycleDelta is true:
- Read prior cycle's pattern report
- Highlight: new patterns, disappeared patterns, intensified patterns, reversed patterns
- Use prefix markers: `[NEW]`, `[GONE]`, `[STRONGER]`, `[WEAKER]`, `[REVERSED]`

## Output
Write all artifacts to their configured paths within `${storagePath}/`.
Write summary to: `${storagePath}/cycle-${CYCLE}/p6-synthesis.md`
