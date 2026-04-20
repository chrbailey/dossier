# P4 Signal Extraction -- Cycle 2

**Contract:** RLC.DOSSIER.SIGNAL.001
**Phase:** P4-signal-extraction
**Status:** completed
**Date:** 2026-03-19
**Cycle:** 2

## Summary

Scored 36 Cycle 2 evidence items across 6 signal dimensions. Inserted 216 signal records into the evidence store. Cycle 2 composite scores are lower on average than Cycle 1 (mean 0.577 vs ~0.62) due to corroboration penalty on novelty -- many items reinforce Cycle 1 patterns rather than introducing new ones. The highest-scoring item is the Kalinowski resignation (0.760), which represents genuinely new evidence in the military-AI cluster.

## Top 10 Highest-Scoring Cycle 2 Evidence

| Rank | ID | Source | Composite | Key Signal |
|------|-----|--------|-----------|------------|
| 1 | 81 | sama | 0.760 | Kalinowski resigns from OpenAI over Pentagon guardrails -- named objections to surveillance + autonomous weapons |
| 2 | 75 | dario-amodei | 0.698 | Morgan Stanley: "no wall", radical acceleration in 2026, rice-on-chessboard at 40th square, $19B ARR |
| 3 | 77 | dario-amodei | 0.695 | Expanded consciousness claims: sparse autoencoder activations fire BEFORE output generation |
| 4 | 78 | dario-amodei | 0.693 | Lexology legal analysis: enterprise risk if AI may be conscious -- new legal territory |
| 5 | 68 | demis-hassabis | 0.670 | AGI within 5-10 years -- explicitly longer than Altman (2026-27) and Amodei (2026) |
| 6 | 69 | demis-hassabis | 0.660 | Questions AI startup valuations ("billions with no product") -- apparent AMI Labs reference |
| 7 | 83 | sama | 0.642 | Dev tooling competitive matrix: Anthropic = Bun (JS), OpenAI = Astral (Python) |
| 8 | 95 | simon-willison | 0.637 | Astral acquisition strategic risk analysis, MIT fork safeguard, Douglas Creager quote |
| 9 | 92 | jim-fan | 0.635 | Physical AGI as "next grand challenge", Foundation Agent roadmap |
| 10 | 70 | demis-hassabis | 0.608 | Hassabis spending "a lot of time on world models" + Gemini metrics (650M MAU, 2B Search) |

**Observation:** Cycle 2's top 10 is dominated by four themes: the military-AI cluster deepening with Kalinowski's resignation (#1), Amodei's scaling and consciousness claims (#2, #3, #4), Hassabis emerging as a distinct voice in the scaling/world-models debate (#5, #6, #10), and the dev tooling arms race crystallizing (#7, #8). Hassabis has gone from thin coverage in Cycle 1 (4 items, noted as potentially strategic silence) to one of the most signal-rich sources in Cycle 2 (5 items, 3 in top 10).

---

## Cross-Cycle Delta Analysis

### [NEW] Patterns Not Present in Cycle 1

**1. Consciousness Liability (IDs 77, 78)**
Amodei's consciousness claims existed in Cycle 1 (ID 9), but Cycle 2 introduces two new dimensions: (a) technical evidence via sparse autoencoders showing activations before output generation, and (b) legal liability analysis examining enterprise risk. This has moved from a speculative CEO statement to a multi-domain concern (technical + legal + commercial). This is a genuinely new pattern.

**2. Internal Dissent at Labs (ID 81)**
Kalinowski's resignation from OpenAI -- with named, specific objections to domestic surveillance and autonomous weapons -- is the first evidence of a named executive departing a frontier lab over policy disagreement with a military partner. Cycle 1 had the Amodei-Altman dispute, but that was inter-company. This is intra-company dissent. Qualitatively different signal.

**3. Dev Tooling Arms Race as Explicit Strategy (IDs 82, 83, 95)**
Cycle 1 noted the Astral acquisition (ID 33). Cycle 2 reframes it as a deliberate competitive strategy: Anthropic acquired Bun for JavaScript, OpenAI acquired Astral for Python. The competitive matrix is now explicit. Willison's analysis of MIT licensing as a "fork safeguard" adds a new dimension of open-source governance.

**4. Physical AGI Roadmap (IDs 90, 92)**
Jim Fan's articulation of "Physical AGI as the next grand challenge" and the Foundation Agent concept is new. Cycle 1 covered GTC announcements and GR00T, but this is the first time physical embodiment is framed as a distinct AGI path -- not just robotics applications, but a fundamental research direction.

**5. Hassabis Competitive Positioning (ID 69)**
Hassabis publicly questioning startup valuations ("billions with no product") while positioned as the established #3 lab is new behavior. In Cycle 1, Hassabis was notably restrained. The shift from silence to active competitive commentary is a behavioral signal.

### [STRONGER] Patterns That Gained Evidence

**1. Military-AI Cluster** (Cycle 1: 3 sources, Cycle 2: 3 sources + internal dissent)
Strengthened significantly. Cycle 1 had Amodei-Altman public dispute. Cycle 2 adds Kalinowski resignation (internal OpenAI dissent), Amodei's CBS red lines (national TV), and the broader pattern of named individuals drawing lines. The cluster now spans external dispute, internal resignation, and public policy statements.

**2. World Models Convergence** (Cycle 1: 2 sources, Cycle 2: 3 sources)
Strengthened. LeCun/AMI Labs continues (3 more items), but Hassabis now explicitly says he's spending "a lot of time on world models" -- confirming the convergence hypothesis from Cycle 1. Hassabis simultaneously running Gemini (LLM) and world models research creates internal tension at Google that wasn't visible before.

**3. Agentic AI Infrastructure** (Cycle 1: 5 sources, Cycle 2: 6 sources)
Broadest cluster, now includes all non-Mostaque sources. Chase's context engineering thesis sharpened ("when agents mess up, they mess up because they do not have the right context"). Willison published a living document guide. Karpathy's autoresearch gaining community adoption. The pattern has moved from "people are building agents" to "people are codifying agent patterns."

**4. Scaling Debate** (Cycle 1: 2-3 sources, Cycle 2: 3 sources with sharper disagreement)
Amodei: "no wall", 40th square on chessboard, radical acceleration. Hassabis: 5-10 years, "maybe one or two more breakthroughs." LeCun: LLMs are wrong approach entirely. The timeline spread has widened -- Amodei is most aggressive, Hassabis most conservative among those who believe in scaling, LeCun rejects the premise.

### [WEAKER] Patterns That Lost Momentum

**1. AI Labor Impact** (Cycle 1: 2 sources with novel framing, Cycle 2: 1 source repeating)
Altman repeated labor displacement messaging at BlackRock (ID 79) but with less novelty -- adding IMF/Goldman stats rather than new insight. Karpathy had no new labor-impact items in Cycle 2. The "nobody knows what to do" framing from Cycle 1 was more impactful. This is becoming ambient noise rather than advancing.

**2. Karpathy Autoresearch** (Cycle 1: 6 items, high originality, Cycle 2: 3 items, mostly coverage)
Cycle 1 had Karpathy's original tweets and the SETI@home vision. Cycle 2 has journalistic coverage (The New Stack, Cryptonomist) and the GitHub repo -- derivative rather than original. The idea is now in "coverage" phase, not "discovery" phase. Community debate on reproducibility (ID 84) is the only new signal.

### [REVERSED] Contradictions of Cycle 1 Findings

**1. Hassabis Silence Was a Search Artifact**
Cycle 1 flagged Hassabis's thin coverage (4 items) as potentially strategic silence. Cycle 2 recovered 5 items including an India AI summit keynote, competitive commentary on valuations, explicit world-models focus, and AGI timeline statements. He was not silent -- Cycle 1 search coverage was incomplete. The "thin coverage" observation is invalidated.

**2. Emad Mostaque Silence Partially Reversed**
Cycle 1 scored Mostaque silence at 0.7. Cycle 2 found confirmed public appearances (Abundance Summit, ii.inc whitepaper, "beyond transformers" statements). Silence is downgraded from 0.7 to ~0.28 average. He is low-volume, not absent. However, his output remains unsubstantiated relative to competitors.

### [GONE] Cycle 1 Patterns With No Cycle 2 Continuation

**1. OpenAI-Anthropic Direct Confrontation**
Cycle 1 had Amodei calling OpenAI messaging "straight up lies" (ID 8), apologies (IDs 43, 48), and active renegotiation. Cycle 2 has no new inter-company hostility. Both companies have moved to separate positioning (Amodei on consciousness/scaling, Altman on acquisitions/labor). The public feud appears to have de-escalated.

**2. "Intelligence Brownouts" / AI Dependency Fragility**
Karpathy's "intelligence brownouts" concept (Cycle 1, ID 4) -- AI agents going offline during cloud outages and the planet "losing IQ points" -- had no continuation. Nobody picked it up. A novel concept that may have been too early.

**3. World/AgentKit Crypto-AI Convergence**
Altman's World launch with AgentKit and Coinbase x402 (Cycle 1, ID 45) had zero follow-up. AI-crypto intersection appears to have lost momentum in this window.

---

## Updated Momentum Clusters

| Cluster | Sources (Cycle 2) | Items | Delta |
|---------|-------------------|-------|-------|
| **Agentic AI** | Karpathy, Chase, Willison, Fan, swyx, Amodei (via Claude Code) | 15 | Broadened -- now includes financial signal (Claude Code ARR) |
| **Military AI** | Amodei, Altman, Kalinowski | 4 | Deepened -- internal dissent adds new dimension |
| **World Models** | LeCun, Hassabis, (Mostaque marginal) | 8 | Strengthened -- Hassabis confirmed convergence |
| **Scaling Debate** | Amodei, Hassabis, LeCun | 5 | Sharpened -- wider timeline spread |
| **Dev Tooling Arms Race** | Altman (OpenAI/Astral), Amodei (Anthropic/Bun), Willison | 4 | NEW as explicit strategic cluster |
| **Consciousness Debate** | Amodei, legal analysts | 3 | NEW cluster -- technical + legal + commercial |
| **Physical AI / Robotics** | Fan, Hassabis | 4 | Strengthened -- "Physical AGI" framing |
| **AI Labor Impact** | Altman | 2 | Weakened -- Karpathy dropped out |

---

## Contradiction Analysis

### High Contradiction Items (score >= 0.45)

**1. ID 77 -- Amodei consciousness: sparse autoencoder evidence (0.65)**
Technical evidence (activations firing before output) supporting AI consciousness contradicts the baseline assumption across the industry. The interpretability team's findings add empirical weight to what was previously philosophical speculation. If replicable, this fundamentally changes the ethics discussion.

**2. ID 81 -- Kalinowski resignation (0.55)**
A named OpenAI robotics leader resigning over Pentagon guardrails directly contradicts OpenAI's public narrative of "responsible military deployment." Internal dissent at this level suggests the governance framework was insufficient, not just a PR problem.

**3. ID 68 -- Hassabis: AGI 5-10 years (0.55)**
Hassabis says "maybe one or two more breakthroughs" needed. Amodei says "no wall" and "radical acceleration." These are not compatible timelines from the CEO of the #3 lab and the CEO of the #2 lab. Either one of them is wrong, or they are defining AGI differently.

**4. ID 78 -- Legal liability of consciousness claims (0.50)**
If a CEO publicly entertains AI consciousness and enterprises deploy that AI, what are the legal obligations? Lexology analysis opens a genuinely unexplored liability domain. Contradicts the assumption that consciousness is a philosophical question with no commercial relevance.

**5. ID 71 -- AMI Labs CEO: "world models will be the next buzzword" (0.50)**
LeBrun predicting that "every company will call itself a world model company" simultaneously validates the thesis (world models are important enough to become a buzzword) and undermines it (if everyone claims it, the term loses meaning). Anti-LLM thesis remains the strongest structural contradiction in the dataset.

### Cross-Source Contradiction Matrix

| Position A | Position B | Tension Level |
|------------|------------|---------------|
| Amodei: "no wall", 40th square | Hassabis: 5-10 years, breakthroughs needed | HIGH -- incompatible timelines |
| Amodei: AI may be conscious | Industry consensus: LLMs not conscious | HIGH -- empirical vs default assumption |
| LeCun: LLMs are dead end | Amodei $19B ARR from LLM products | HIGH -- paradigm disagreement |
| Hassabis: questions billion-dollar seeds "with no product" | LeCun: raised $1B for AMI Labs | MEDIUM -- competitive critique |
| OpenAI: "responsible military use" | Kalinowski: resigned over insufficient guardrails | MEDIUM -- internal vs external narrative |
| Altman: AI utility "sold by the meter" | Altman: "nobody knows what to do" about labor | LOW -- optimistic framing vs honest admission |

---

## Silence and Absence Update

### Emad Mostaque: Upgraded from Silence to Low-Volume
- **Cycle 1 score:** 0.60 average silence_anomaly (IDs 38, 61)
- **Cycle 2 score:** 0.28 average silence_anomaly (IDs 96, 97)
- **Status:** Confirmed public appearance at Abundance Summit (March 8-12). Published whitepaper at ii.inc. Making claims about "beyond transformers" and GPT-5 level at $0.10/M tokens by end of 2026.
- **Assessment:** No longer silent, but output is low-volume and unsubstantiated compared to other sources. Trust score remains low (0.3). "Universal Basic AI" and "Intelligence-Backed Capital" are vague enough to avoid falsification.

### Demis Hassabis: Silence Artifact Resolved
- **Cycle 1 flag:** "Thin coverage" -- 4 items, noted as potentially strategic restraint
- **Cycle 2 reality:** 5 items, 3 in top 10. Active at India AI Summit, media interviews, competitive commentary.
- **Assessment:** Cycle 1 under-coverage was a search artifact, not a behavioral signal. Hassabis is active and positioning Google/DeepMind as the mature player against "hot startups." Silence anomaly score: 0.0 across all Cycle 2 items.

### New Silence Observations

**Kalinowski Post-Resignation:** After the March 8 resignation statement (ID 81), no further public commentary detected. A high-profile departure typically generates follow-up interviews, opinion pieces, or advisory positions. The single statement followed by silence may indicate legal constraints (NDA, separation agreement) or deliberate restraint.

**No Mira Murati Signal:** Despite being listed as a GTC 2026 speaker (Cycle 1, ID 23), Murati generated no independent evidence in either cycle. She remains invisible in this dataset -- neither confirming nor denying any particular direction for her rumored venture.

---

## Dimension Distribution (Cycle 2)

| Dimension | Mean | Highest | Lowest |
|-----------|------|---------|--------|
| relevance | 0.82 | 0.92 (IDs 75, 81) | 0.60 (ID 64) |
| novelty | 0.51 | 0.85 (ID 81) | 0.30 (ID 64) |
| momentum | 0.89 | 1.0 (34 items) | 0.0 (IDs 96, 97) |
| contradiction | 0.22 | 0.65 (ID 77) | 0.0 (IDs 64, 65) |
| source_originality | 0.64 | 0.85 (IDs 81, 95) | 0.45 (IDs 72, 84) |
| silence_anomaly | 0.02 | 0.30 (ID 96) | 0.0 (34 items) |

### Cycle 1 vs Cycle 2 Dimension Comparison

| Dimension | Cycle 1 Mean | Cycle 2 Mean | Delta | Interpretation |
|-----------|-------------|-------------|-------|----------------|
| relevance | 0.80 | 0.82 | +0.02 | Stable -- Cycle 2 sources remain on-topic |
| novelty | 0.66 | 0.51 | -0.15 | Expected drop -- corroboration lowers novelty |
| momentum | 0.82 | 0.89 | +0.07 | Clusters have strengthened |
| contradiction | 0.24 | 0.22 | -0.02 | Stable |
| source_originality | 0.68 | 0.64 | -0.04 | Slight drop -- more coverage, less primary thought |
| silence_anomaly | 0.03 | 0.02 | -0.01 | Silence anomalies largely resolved |

The primary driver of lower Cycle 2 composite scores is the 0.15 drop in novelty. This is methodologically correct -- Cycle 2 largely corroborates and extends Cycle 1 patterns rather than discovering new ones. The exceptions (Kalinowski resignation, consciousness liability, dev tooling arms race crystallization) are reflected in their higher scores.

## Anti-Recursion Check
- Source entropy: 3.257 (minimum: 1.5) -- HEALTHY
- Self-citation ratio: 0.0 (maximum: 0.2) -- CLEAN
- All evidence from external sources -- no self-referential contamination
- Cycle 2 novelty penalty applied correctly: corroborating items scored lower

## Artifacts

- **Signal records:** 216 entries in `data/evidence.db` signals table (cycle_number=2)
- **JSONL output:** `output/signal-curation/cycle-2/p4-signals.jsonl` (36 lines)
- **This report:** `output/signal-curation/cycle-2/p4-signal-extraction.md`
- **Cumulative:** 582 total signal records (366 Cycle 1 + 216 Cycle 2)
