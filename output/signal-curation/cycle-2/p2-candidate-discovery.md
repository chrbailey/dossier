# P2 Candidate Discovery — Cycle 2

**Contract:** RLC.DOSSIER.SIGNAL.001
**Phase:** P2-candidate-discovery
**Status:** completed
**Date:** 2026-03-19
**Strategy:** ADAPTIVE (depth-first on gaps, breadth on remainder)

## Summary

Discovered 36 candidates across 10 sources. Adaptive strategy successfully closed the major Cycle 1 gaps:
- **swyx**: 4 new items found (Cycle 1 had 3 — nearly doubled)
- **Demis Hassabis**: 5 new items found (Cycle 1 had 2 — more than tripled)
- **Emad Mostaque**: 2 new items found (Cycle 1 had only a silence event)

## Candidate Counts by Source

| Source | Cycle 1 | Cycle 2 New | Cycle 2 Corroborate | Notes |
|--------|---------|-------------|---------------------|-------|
| swyx | 3 | 4 | 0 | Gap closed: found newsletter, podcast ep, AIE Europe, 2026 vision |
| demis-hassabis | 2 | 5 | 0 | Gap closed: India summit, book, bubble comments, AGI timeline, sustainability critique |
| yann-lecun | 5 | 3 | ~2 | Depth: TechCrunch details, AINews coverage, AMI website |
| dario-amodei | 4 | 5 | ~2 | CBS red lines interview, Morgan Stanley scaling, ARR $19B, consciousness legal analysis |
| sama | 5 | 5 | ~2 | BlackRock speech, AI utility prediction, Kalinowski resignation, Astral acquisition details |
| karpathy | 6 | 3 | ~3 | Cryptonomist coverage, New Stack, GitHub repo |
| harrison-chase | 4 | 3 | ~1 | Context engineering thesis, Sequoia podcast, Nemotron Coalition |
| jim-fan | 3 | 3 | ~1 | GTC robotics strategy deep dive, Sequoia podcast, $1T AI vision |
| simon-willison | 5 | 3 | ~1 | Pragmatic Summit talk, Agentic Engineering Patterns guide, Astral analysis |
| emad-mostaque | 1 | 2 | 0 | Silence event → active: agents mainstream, Abundance Summit appearance |

## HIGH PRIORITY Gap Analysis

### swyx (GAP CLOSED)
Cycle 1 found zero March blog posts — confirmed as accurate. swyx.io only published "How to Thought Lead" (March 14) as a blog post. However, swyx's primary content output is through:
1. **Latent Space podcast** — March 5 episode with Felix Rieseberg on Claude Cowork
2. **AI News newsletter** (news.smol.ai) — daily publication continuing through March
3. **AI Engineer conference organization** — AIE Europe April 8-10 London (announced/promoted in March)
4. **Latent Space Substack** — "Scaling without Slop" 2026 vision piece (Jan 23, still circulating)

The "zero content" finding from Cycle 1 was a search artifact — swyx's output is primarily podcast/newsletter, not blog posts.

### Demis Hassabis (GAP CLOSED)
Cycle 1 found only 2 items. Cycle 2 reveals Hassabis has been active but in a different mode:
1. **India AI Impact Summit** (Feb 19) — AGI 5-10 years away, international cooperation
2. **AI bubble critique** — questioned sustainability of $B seed rounds "with no product"
3. **AGI timeline conservatism** — explicitly longer than Altman/Amodei estimates
4. **Infinity Machine biography** — Sebastian Mallaby book dropping March 31
5. **Gemini metrics** — 650M MAU, 2B via Search AI Overviews

Hassabis's relative quiet is strategic — DeepMind is in execution mode, not announcement mode. The sustainability comments may be a veiled shot at AMI Labs.

### Yann LeCun / AMI Labs (DEPTH ADDED)
Core signal ($1B raise) already captured. Cycle 2 adds:
1. TechCrunch deep-dive with LeBrun quotes and investor details
2. Latent Space AINews community analysis ($4.5B valuation figure)
3. AMI Labs website positioning: "Real World. Real Intelligence."

## MEDIUM PRIORITY Findings

### Sam Altman — 5 new items
Major new signals:
- **BlackRock Infrastructure Summit** (March 13): "Hard to outwork a GPU" — strongest job displacement warning yet
- **Caitlin Kalinowski resignation** (March 8): OpenAI robotics leader quit over Pentagon guardrail concerns
- **Astral acquisition** (March 19): uv/Ruff/ty — direct competitive response to Anthropic's Bun acquisition
- **AI as utility** prediction: intelligence "sold by the meter"

### Dario Amodei — 5 new items
Major new signals:
- **CBS interview** (March 1): Named two red lines explicitly, called government response "retaliatory"
- **Morgan Stanley TMT**: "We do not see a wall" — scaling acceleration, ARR $19B, $6B added in February alone
- **Consciousness legal analysis**: Lexology piece on enterprise liability implications
- **Claude Code $1B milestone**: Revenue catalyst for the $19B ARR

### Others
- **Karpathy**: Community coverage amplifying (Cryptonomist, New Stack), but no new primary content after March 17
- **Harrison Chase**: Context engineering thesis crystallizing as his signature concept
- **Jim Fan**: GTC 2026 details — GR00T N2 previewed, data-to-compute paradigm shift
- **Simon Willison**: Agentic Engineering Patterns guide is a major new artifact
- **Emad Mostaque**: NOT silent — spoke at Abundance Summit, publishing on agents + transformer succession

## Search Methods Used

| Method | Count | Notes |
|--------|-------|-------|
| WebSearch | 14 queries | Primary discovery |
| WebFetch (success) | 13 URLs | Content extraction |
| WebFetch (failed) | 4 URLs | 2x 403, 1x 429, 1x header error |

## Artifacts

- `p2-candidates.jsonl`: 36 candidate records
- This file: discovery narrative
