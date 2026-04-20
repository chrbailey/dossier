# P3 Evidence Capture — Cycle 1

**Contract:** RLC.DOSSIER.SIGNAL.001
**Phase:** P3-evidence-capture
**Status:** completed
**Date:** 2026-03-19

## Summary

Processed 38 candidates from P2 (37 content items + 1 silence event). All evidence successfully inserted into the evidence store with zero duplicates and zero failures.

## Counts

| Metric | Value |
|--------|-------|
| Total candidates | 38 |
| New evidence inserted | 38 |
| Duplicates found | 0 |
| Silence events | 1 (emad-mostaque) |
| Capture failures | 0 |
| URLs fetched via WebFetch | 20 |
| URLs using P2 snippets (X/Twitter or blocked) | 17 |
| Fetch errors (rate limit/403) | 3 (VentureBeat 429, CNBC paywall, NVIDIA investor 403) |

## Evidence by Source

### karpathy (6 items)
| Hash | Type | Date | Key Signal |
|------|------|------|------------|
| `6e55245d3c3ccf3b` | post | 2026-03-07 | autoresearch repo release, 630 lines |
| `57a10659da6a0d93` | thread | 2026-03-08 | SETI@home vision for distributed agent research |
| `81af4f315709b5a0` | post | 2026-03-10 | 700 experiments, 20 improvements, 11% speedup |
| `d2f0bfee537d2bd0` | post | 2026-03-11 | Intelligence brownouts concept, oauth outage |
| `0c523b2957a53299` | article | 2026-03-17 | Fortune: 'The Karpathy Loop', Shopify 19% gain |
| `6042801faeb2d2dc` | article | 2026-03-08 | VentureBeat coverage (snippet only, 429) |

### dario-amodei (4 items)
| Hash | Type | Date | Key Signal |
|------|------|------|------------|
| `c2534531ea7d66c2` | announcement | 2026-02-26 | DoW red lines: autonomous weapons, mass surveillance |
| `24b66bac5b274d6d` | article | 2026-03-04 | Called OpenAI military messaging 'straight up lies' |
| `e355de5d222c8095` | article | 2026-03-09 | Claude consciousness claims, 15-20% self-assessed probability |
| `283dc6b0c22ff775` | announcement | 2026-03-05 | Supply chain risk designation, will challenge in court |

### sama (5 items)
| Hash | Type | Date | Key Signal |
|------|------|------|------------|
| `da0a5c75e9ef2cb1` | post | 2026-03-03 | DoW agreement messaging |
| `4beb3ac1d43f8f3f` | announcement | 2026-03-05 | GPT-5.4 launch, 33% fewer hallucinations |
| `95a16e417182437f` | article | 2026-03-12 | Congressional grilling on defense work |
| `24f013471228f386` | article | 2026-03-12 | AI killing labor-capital balance, 'nobody knows' |
| `7b175469aefafdfb` | post | 2026-03-14 | AI will be better CEO than him |

### demis-hassabis (2 items)
| Hash | Type | Date | Key Signal |
|------|------|------|------------|
| `5ff17ca895677477` | article | 2026-03-10 | AlphaGo at 10, AGI = world models + search + tools |
| `cc9b02d8f1db229c` | post | 2026-03-12 | Google-Boston Dynamics robotics partnership |

### yann-lecun (5 items)
| Hash | Type | Date | Key Signal |
|------|------|------|------------|
| `a3bbba44b025d714` | post | 2026-03-10 | AMI Labs $1B funding announcement |
| `9eb3f5ee976ad78e` | article | 2026-03-11 | $1.03B at $3.5B valuation, anti-LLM thesis |
| `fcb789393cb1a4a2` | post | 2026-03-12 | Meta departure context, LLM vs world models |
| `ec49e92dd019e90a` | post | 2026-03-15 | AI only looks intelligent, cannot understand physical world |
| `d8fc04bb732a86e3` | post | 2026-03-10 | Jim Fan congrats on AMI Labs launch |

### jim-fan (3 items)
| Hash | Type | Date | Key Signal |
|------|------|------|------------|
| `76729852ddac3051` | announcement | 2026-03-16 | GTC 2026 speaker, GEAR team featured |
| `5fded98bd4b2e77f` | article | 2026-03-17 | GTC 2026: Vera Rubin, 110 robots, Nemotron Coalition |
| `e864a5ee46ee371e` | announcement | 2026-03-17 | NVIDIA open model families (snippet only, 403) |

### harrison-chase (4 items)
| Hash | Type | Date | Key Signal |
|------|------|------|------------|
| `d2bc816fa63fd3d8` | announcement | 2026-03-16 | LangChain-NVIDIA enterprise platform |
| `2dfdb786cbb01147` | announcement | 2026-03-15 | Deep Agents: planning, memory, context isolation |
| `b986a06c3d7c567c` | post | 2026-03-15 | Agent UI/UX investment, #useStream hooks |
| `6942f5b54d56e06f` | interview | 2026-03-15 | Matt Turck interview on agent stack future |

### swyx (3 items)
| Hash | Type | Date | Key Signal |
|------|------|------|------------|
| `41b926b5aac3832a` | article | 2026-03-14 | Thought leadership framework, 6 ranked principles |
| `907fd3c53c761b26` | article | 2026-03-13 | Latent Space: independent LLM evals, smiling curve |
| `45c395743b788aeb` | post | 2026-03-12 | 'Claude Code: no evals' observation |

### simon-willison (5 items)
| Hash | Type | Date | Key Signal |
|------|------|------|------------|
| `e5d7d70cd6573273` | article | 2026-03-19 | OpenAI acquires Astral (uv/ruff), competitive dynamics |
| `bccddbaf0b2fd8b3` | article | 2026-03-18 | Snowflake Cortex prompt injection sandbox escape |
| `6e3868118d66f8bb` | article | 2026-03-16 | Coding agents for data analysis, NICAR workshop |
| `e1baf641f835cd8d` | post | 2026-03-14 | Agentic Engineering Patterns guide |
| `13e7b4d4fb25f7d1` | article | 2026-03-08 | Weizenbaum quote on AI delusional thinking |

### emad-mostaque (1 silence event)
| Hash | Type | Date | Key Signal |
|------|------|------|------------|
| `dae517ad6fdf263f` | silence | 2026-03-19 | No verified content since Feb 2026 |

## Fetch Method Breakdown

- **Full WebFetch (20 URLs):** Fortune (3), Anthropic (2), TechCrunch (1), GatewayPundit (1), DeepMind (1), NVIDIA blog (1), LangChain blog (1), MarkTechPost (1), swyx.io (1), Latent Space (1), Simon Willison (5)
- **P2 Snippets — X/Twitter inaccessible (14 URLs):** All x.com URLs returned JS-disabled error pages
- **P2 Snippets — rate limited/blocked (3 URLs):** VentureBeat (429), CNBC (paywall), NVIDIA investor relations (403)

## Raw Artifacts

All 38 evidence items written to:
`/Volumes/OWC drive/Dev/dossier/output/signal-curation/raw/cycle-1/`

Files: `{source_id}_{N}.md` format (37 content files + 1 silence file)

## Notes

- X/Twitter content consistently inaccessible via WebFetch (JS rendering required). P2 search snippets preserved as evidence — these capture the signal adequately for scoring purposes.
- Three article URLs returned errors (429, paywall, 403). P2 snippets used as fallback.
- All content trimmed to signal-relevant text (300-1500 chars), not full page dumps.
- Evidence store confirmed zero duplicates — this is the first insertion pass for Cycle 1.
