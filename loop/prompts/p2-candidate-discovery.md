# Phase 2: Candidate Discovery

## Purpose
Find candidate content from the source universe for this cycle.

## Inputs
- P1 output (active sources, cycle focus)
- Contract candidateDiscovery config
- Prior cycle's P8 output (if exists — gap analysis tells us what to look for)

## Process

1. **For each allowed source**, use Firecrawl to search for recent content:
   - Search: `"{source name}" site:x.com OR site:twitter.com` (for X/Twitter posts)
   - Search: `"{source name}" blog OR announcement` (for blog posts, personal sites)
   - Respect maxCandidatesPerCycle cap
2. **Apply discoveryStrategy**:
   - `breadth_first`: equal attention across all sources
   - `depth_first`: focus on sources flagged by prior cycle's gap analysis
   - `adaptive`: prioritize sources with highest recent signal scores
3. **For each candidate found**, record:
   - URL
   - Source attribution
   - Snippet/summary
   - Timestamp (when posted)
   - Type (post, article, thread, announcement)
4. **Record silence candidates**: sources with no recent content found

## Output
Write to: `${storagePath}/cycle-${CYCLE}/p2-candidates.jsonl`

One JSON object per line:
```json
{"source_id": "karpathy", "url": "https://...", "snippet": "...", "timestamp": "2026-03-...", "type": "post"}
```

Also write a summary to: `${storagePath}/cycle-${CYCLE}/p2-candidate-discovery.md`

Include:
- Candidates found per source
- Sources with no recent content (silence candidates)
- Total candidates vs maxCandidatesPerCycle cap

## Important
- Use Firecrawl's search tool for discovery — it handles JS rendering and anti-bot
- Do NOT try to use X/Twitter API directly
- If a source has no recent content, that IS a finding — record it as a silence candidate
- Respect the contract's freshnessHorizon — skip content older than that
- **Fallback**: If Firecrawl is unavailable (not authenticated), use WebSearch as fallback. WebSearch returns summaries not full text — note this as a collection limitation in your output. WebSearch as WebFetch fallback produces high-quality output.
