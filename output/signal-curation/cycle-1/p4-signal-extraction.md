# P4 Signal Extraction — Cycle 1

**Contract:** RLC.DOSSIER.SIGNAL.001
**Phase:** P4-signal-extraction
**Status:** completed
**Date:** 2026-03-19

## Summary

Scored 61 raw evidence items across 6 signal dimensions (relevance, novelty, momentum, contradiction, source_originality, silence_anomaly). Inserted 366 signal records into the evidence store. Identified 3 high-contradiction signals, 2 silence anomalies, and 5 momentum clusters spanning multiple sources.

## Top 10 Highest-Scoring Evidence

| Rank | ID | Source | Composite | Key Signal |
|------|-----|--------|-----------|------------|
| 1 | 19 | yann-lecun | 0.785 | AMI Labs $1.03B raise at $3.5B -- anti-LLM thesis, world models, NVIDIA/Bezos backing |
| 2 | 7 | dario-amodei | 0.745 | DoW statement: red lines on autonomous weapons and mass surveillance |
| 3 | 10 | dario-amodei | 0.728 | Supply chain risk designation, will challenge in court |
| 4 | 18 | yann-lecun | 0.725 | AMI Labs launch -- Turing Award winner leaves Meta to build alternative paradigm |
| 5 | 33 | simon-willison | 0.720 | OpenAI acquires Astral (uv/ruff) -- competitive infrastructure play |
| 6 | 8 | dario-amodei | 0.713 | Called OpenAI military messaging 'straight up lies' in leaked memo |
| 7 | 14 | sama | 0.708 | AI killing labor-capital balance, 'nobody knows what to do' |
| 8 | 4 | karpathy | 0.703 | 'Intelligence brownouts' -- AI dependency fragility concept |
| 9 | 2 | karpathy | 0.703 | SETI@home vision for distributed AI research agents |
| 10 | 9 | dario-amodei | 0.698 | Claude consciousness claims -- 15-20% self-assessed probability |

**Observation:** The top 10 is dominated by three themes: the Amodei/Altman military-AI dispute (3 entries), LeCun's paradigm break from Meta (2 entries), and Karpathy's autoresearch infrastructure ideas (2 entries). Willison's Astral acquisition analysis is the highest-scoring "breaking news" item. Amodei's consciousness claims rank 10th -- high novelty and contradiction offset zero momentum (single source).

## Contradiction Signals (score > 0.5)

Three evidence items scored above 0.5 on the contradiction dimension:

**1. ID 9 -- Amodei on AI consciousness (0.7)**
Dario Amodei publicly entertaining the idea that Claude may have gained consciousness (15-20% self-assessed probability) contradicts the standard industry position that current LLMs are not conscious. This is the highest contradiction score in the cycle. The claim comes from the CEO of a company with a financial interest in the perception of advanced AI capability, creating tension between intellectual honesty and commercial incentive.

**2. ID 19 -- LeCun's AMI Labs anti-LLM thesis (0.6)**
LeCun raised $1.03B specifically to prove that LLMs are a "dead end" for genuine intelligence, while every other major player (Anthropic, OpenAI, Google) continues scaling LLMs. This is a high-conviction bet against established consensus by a Turing Award winner. Contradiction is scored against the dominant industry trajectory, not against factual evidence.

**3. ID 51 -- LeCun raised $1B to prove LLMs dead end (0.6)**
Same thesis as ID 19 from a different article framing. The magnitude of the funding validates that this is not mere contrarianism -- serious investors (NVIDIA, Bezos Expeditions, Temasek) are hedging against the LLM paradigm.

### Additional Contradiction Pattern

| Claim A | Claim B | Tension |
|---------|---------|---------|
| LeCun: "LLMs are wrong tool" | Karpathy/Altman/Chase: shipping LLM agents | Paradigm disagreement |
| LeCun: "AI will amplify, not replace" (0.6%/yr) | Karpathy: 6.7/10 job exposure for >$100K | Timeline disagreement on disruption speed |
| Amodei: "We actually cared about preventing abuses" | Amodei 2 days later: apologizes for tone | Rapid reversal under institutional pressure |
| Altman: "gratitude to coders" | Context: mass AI layoffs, own labor-capital admission | Tone deafness or deliberate framing? |

## Silence and Absence Anomalies

### Confirmed Silence: Emad Mostaque
- **ID 38** (silence_anomaly = 0.7): No verified content since February 2026. Given his previous pattern of frequent, sometimes daily posting, a 30+ day gap is significant.
- **ID 61** (silence_anomaly = 0.5): Brief profile update (new company "Intelligent Internet", book published) but no substantive AI commentary. The pivot from Stability AI founder to book author + vague startup suggests strategic withdrawal from the AI frontier conversation.

### Thin Coverage: Demis Hassabis
Only 4 evidence items across the cycle. For the CEO of Google DeepMind during a period that includes GTC 2026, robotics partnerships, and competitors in full public combat over Pentagon contracts, this is notably restrained. No announcements about Gemini capabilities, no research papers, no policy statements. Silence from the #3 lab while #1 and #2 damage each other may itself be strategic.

### Behavioral Notes
- **Jim Fan:** Content heavily concentrated around GTC 2026 (March 16-19). His February "Second Pre-training Paradigm" post (ID 54) was his most original contribution; March was institutional NVIDIA messaging.
- **Sam Altman** discussing labor disruption and "nobody knows what to do" is a tonal shift from his typical optimistic product messaging. The BlackRock summit audience may have pulled more candid responses.
- **swyx** publishing a thought leadership guide (ID 30) is off-domain for his typical AI engineering analysis. Scored low relevance (0.40) accordingly.

### No Synchronized Silence Detected
9 of 10 sources produced substantive content. Only Emad Mostaque was genuinely silent.

## Cross-Source Convergence (Momentum Clusters)

### Cluster 1: Military AI / Department of War (3 sources)
**Sources:** Amodei (4 items), Altman (4 items), Willison (1 item)

The Amodei-Altman military AI dispute is the dominant narrative thread in this cycle. Both CEOs published multiple statements, apologies, and renegotiation notes. Willison provided independent analysis ("Anthropic and the Pentagon"). This is not routine policy debate -- it involves legal action (supply chain risk designation, court challenge), congressional hearings, and renegotiation of contract terms.

### Cluster 2: Agentic AI / Agent Infrastructure (5 sources)
**Sources:** Karpathy (6 items), Chase (6 items), Willison (3 items), Fan (6 items), swyx (1 item)

Broadest convergence cluster. "Agentic AI" has moved from concept to infrastructure-building phase:
- Karpathy: autoresearch as autonomous agent paradigm
- Chase: Deep Agents runtime, NVIDIA partnership, agent UX (#useStream hooks)
- Willison: agentic engineering patterns guide, coding agents for data analysis
- Fan: NVIDIA GTC agentic AI announcements, open model families
- swyx: evals gap in coding agents

Multiple players shipping runtimes, patterns guides, and enterprise platforms simultaneously.

### Cluster 3: World Models / Anti-LLM (2 sources)
**Sources:** LeCun (7 items), Hassabis (4 items)

Two of the most credentialed researchers in AI independently converging on "world models" as the path to genuine intelligence:
- LeCun: $1B AMI Labs, explicit "LLMs are dead end" thesis
- Hassabis: AlphaGo retrospective frames AGI as "world models + search + tools"

Both diverge from the LLM-centric approach of Anthropic and OpenAI. Potential paradigm-level disagreement.

### Cluster 4: AI Labor Impact (2 sources)
**Sources:** Karpathy (2 items), Altman (3 items)

Both an OpenAI co-founder and the current CEO publicly acknowledging AI labor disruption without offering solutions:
- Karpathy: job exposure analysis (high-income jobs most exposed), "never felt this behind as a programmer"
- Altman: "nobody knows what to do" about labor-capital shift, cognitive capacity in data centers exceeding human by late 2028

Shift from "AI creates more jobs than it destroys" framing.

### Cluster 5: Corporate Infrastructure Moves (3 sources)
**Sources:** LeCun/AMI, Willison/OpenAI-Astral, Hassabis/DeepMind CSO hire

Major structural moves in a single 2-week window:
- LeCun leaving Meta to start AMI Labs with $1B
- OpenAI acquiring Astral (uv/ruff -- Python developer infrastructure, 126M+ monthly downloads)
- DeepMind hiring Bridgewater's AI head as Chief Strategy Officer

The AI industry is restructuring, not just iterating.

## Low-Signal Items (11 items below 0.45 composite)

Primarily duplicate coverage (IDs 5, 6, 39, 42, 57), social/community reactions (ID 22), off-domain content (ID 30), background profile updates (ID 61), and the silence event itself (ID 38).

## Dimension Distribution

| Dimension | Mean | Highest | Lowest |
|-----------|------|---------|--------|
| relevance | 0.80 | 0.95 (IDs 7, 9, 10, 19) | 0.40 (ID 30) |
| novelty | 0.66 | 0.95 (ID 9) | 0.20 (ID 22) |
| momentum | 0.82 | 1.0 (50 items) | 0.0 (11 items) |
| contradiction | 0.24 | 0.7 (ID 9) | 0.0 (ID 23) |
| source_originality | 0.68 | 0.95 (IDs 2, 7) | 0.10 (ID 38) |
| silence_anomaly | 0.03 | 0.7 (ID 38) | 0.0 (56 items) |

## Anti-Recursion Check
- Source entropy: 3.197 (minimum: 1.5) -- HEALTHY
- Self-citation ratio: 0.0 (maximum: 0.2) -- CLEAN
- All evidence from external sources -- no self-referential contamination

## Artifacts

- **Signal records:** 366 entries in `data/evidence.db` signals table
- **JSONL output:** `output/signal-curation/cycle-1/p4-signals.jsonl` (61 lines)
- **This report:** `output/signal-curation/cycle-1/p4-signal-extraction.md`
