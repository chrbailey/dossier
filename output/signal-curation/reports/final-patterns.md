# Final Pattern Analysis -- Cross-Cycle Evolution
**Contract:** RLC.DOSSIER.SIGNAL.001
**Cycles:** 1-3 (CONVERGED-EARLY)
**Date:** 2026-03-20
**Evidence base:** 148 items, 80 verified, 65 working, 3 raw

---

## Pattern 1: Military AI / Department of War Governance

**First detected:** Cycle 1
**Trajectory:** GROWING -> ACCELERATING -> PEAK
**Confidence:** 0.70 -> 0.82 -> 0.90
**Evidence count:** ~8 (C1) + ~12 (C2) + 15 (C3) = ~35 items
**Sources:** 8+ (dario-amodei, sama, kalinowski, pentagon, legislative, eff, legal-opiniojuris, media-time, community)

### Evolution

**Cycle 1:** The pattern began as a bilateral corporate dispute. Amodei and Altman traded public statements about the Pentagon deal. A leaked internal Anthropic memo called OpenAI staff "gullible." Anthropic received a supply chain risk designation. The framing was industry drama.

**Cycle 2:** The Kalinowski resignation escalated the pattern from corporate to personal. A named individual at OpenAI resigned over specific policy objections (surveillance, autonomous weapons). Amodei drew explicit red lines on CBS national television. The pattern shifted from "corporate dispute" to "named individuals drawing moral lines."

**Cycle 3:** Institutional explosion. The pattern went from two companies arguing to a constitutional governance crisis:
- **Executive branch:** Hegseth threatened Anthropic with "pariah" status (`5dd1fcda`, conf 0.752, corr 9)
- **Judicial branch:** Anthropic sued the Trump administration; 150 federal judges filed amicus briefs (`0dc66a56`, conf 0.748, corr 9)
- **Legislative branch:** FY2026 NDAA mandated cross-functional AI governance by June 2026 (`aee96e9d`, conf 0.700, corr 6)
- **Civil liberties:** EFF published "Weasel Words" exposing surveillance loopholes in OpenAI's agreement (`d073918f`, conf 0.698, corr 8)
- **Media:** Time reframed as citizen data rights issue (`53143801`, conf 0.635, corr 9)
- **Military:** Pentagon developing in-house AI alternatives (`b3bbeb3c`, conf 0.693, corr 9)

15 of 37 Cycle 3 items (41%) belong to this pattern. It dominated the evidence landscape.

### Key Evidence Chain

1. Amodei red lines statement (C1, `c2534531`) -> Kalinowski resignation confirms internal split (C2, `23643bc9`) -> Hegseth threat escalates to coercion (C3, `5dd1fcda`) -> Anthropic files lawsuit (C3, `0dc66a56`) -> 150 judges weigh in (C3, `0dc66a56`) -> Congress codifies governance requirements (C3, `aee96e9d`)

### Assessment

This is the highest-confidence pattern in the dossier. Every escalation step is sourced from independent public records. The progression from industry dispute to constitutional crisis over three cycles was observable in real time. The June 2026 NDAA deadline creates a hard forcing function.

### Open Questions
- What is the court outcome of Anthropic v. Trump administration?
- Will the NDAA governance team have actual enforcement power?
- Does the Pentagon's in-house AI development succeed or is it a bluff?
- Will other AI companies face similar supply chain risk designations?

---

## Pattern 2: Agentic AI Infrastructure

**First detected:** Cycle 1
**Trajectory:** GROWING -> MATURING -> CODIFYING
**Confidence:** 0.72 -> 0.78 -> 0.82
**Evidence count:** ~15 (C1) + ~10 (C2) + ~6 (C3) = ~31 items
**Sources:** 6+ (karpathy, harrison-chase, simon-willison, sama, swyx, jim-fan)

### Evolution

**Cycle 1:** Multiple independent actors building agent runtimes, patterns, and tooling. Karpathy's autoresearch, Chase's Deep Agents, Willison's engineering patterns, NVIDIA's GR00T. High novelty, low coordination.

**Cycle 2:** The pattern began consolidating. Chase articulated the "context engineering" thesis. Willison started a living document on agentic patterns. Revenue validation arrived: Claude Code hit $1B ARR, proving production viability.

**Cycle 3:** Maturation and codification. Willison published his 12th chapter, explicitly defining "agentic engineering" as a discipline (`3e9dedb8`, conf 0.56, corr 4). Chase's Deep Agents hit 9.9k GitHub stars and partnered with NVIDIA (`73be110a`, conf 0.565, corr 3). Karpathy's autoresearch was adopted by Shopify CEO (`488fb00f`, conf 0.585, corr 1). LangChain published AI-Q Blueprint for enterprise deployment.

### Key Evidence Chain

Karpathy autoresearch (C1, `6e55245d`) -> Chase context engineering thesis (C2, `e22d87dc`) -> Willison discipline definition (C3, `3e9dedb8`) -> NVIDIA enterprise partnership (C3, `73be110a`)

### Assessment

The declining item count per cycle (15 -> 10 -> 6) does not mean the pattern is weakening. It means it is becoming ambient. Agentic AI is no longer a frontier signal -- it is the industry default. The transition from "building agents" to "standardizing agent development" is complete. Future signals will be about enterprise adoption, not architectural novelty.

### Open Questions
- Will the enterprise standardization (LangChain + NVIDIA) create lock-in?
- Does Willison's pattern library become the de facto reference?
- What happens to agent frameworks when model capabilities make them unnecessary?

---

## Pattern 3: World Models / Anti-LLM Thesis

**First detected:** Cycle 1
**Trajectory:** THEORETICAL -> FUNDED -> EMPIRICAL
**Confidence:** 0.65 -> 0.75 -> 0.82
**Evidence count:** ~5 (C1) + ~6 (C2) + 7 (C3) = ~18 items
**Sources:** 4 (yann-lecun, demis-hassabis, swyx, academic)

### Evolution

**Cycle 1:** LeCun announced AMI Labs with $1B+ backing and Hassabis gave an AlphaGo retrospective signaling world model interest. Two separate theoretical commitments, no empirical evidence.

**Cycle 2:** AMI Labs launched its website. Hassabis confirmed spending "a lot of time on world models." Fei-Fei Li's World Labs reached $1B. Three distinct world model efforts confirmed, still no benchmarks.

**Cycle 3:** Technical results arrived. V-JEPA achieved 2.85x inference speedup and SOTA on Epic-Kitchens-100 with 50% fewer parameters (`41eb0f91`, conf 0.738, corr 3). AMI Labs completed $1.03B seed, largest European seed ever (`9eb3f5ee`, conf 0.785, corr 2). Hassabis committed to spending "most research time" on world models, citing SIMA 2 and Genie 3 (`238b2ef5`, conf 0.672, corr 1). Latent Space provided independent architecture analysis (`1a9ea4f3`, conf 0.605, corr 2).

### Key Evidence Chain

LeCun anti-LLM thesis (C1, `ec49e92d`) -> AMI Labs funding (C1, `a3bbba44`) -> Hassabis world model commitment (C2, `03e1a8bc`) -> V-JEPA benchmarks (C3, `41eb0f91`) -> Three-way competition confirmed (LeCun + Hassabis + Li)

### Assessment

The transition from theoretical advocacy to published benchmarks is the most significant development in this pattern. However, a critical caveat applies: V-JEPA's SOTA results are on a video understanding benchmark (Epic-Kitchens-100), which plays to JEPA's architectural strengths. No NLP benchmark results have been published. The anti-LLM thesis remains unproven for language tasks. Fei-Fei Li's World Labs produced zero items in Cycle 3 despite $1B valuation.

### Open Questions
- Will V-JEPA results replicate independently?
- Does JEPA outperform on language tasks, or only video/spatial?
- Why is World Labs silent post-funding?
- Will NVIDIA back multiple world model efforts simultaneously?

---

## Pattern 4: Consciousness Liability

**First detected:** Cycle 1
**Trajectory:** SPECULATIVE -> TECHNICAL -> CONTESTED
**Confidence:** 0.45 -> 0.65 -> 0.75
**Evidence count:** ~2 (C1) + ~4 (C2) + 5 (C3) = ~11 items
**Sources:** 4 (dario-amodei, anthropic, academic, legal-akerman)

### Evolution

**Cycle 1:** Amodei made a single statement estimating 15-20% probability of model consciousness. Provocative, low evidence weight.

**Cycle 2:** Anthropic published SAE (sparse autoencoder) findings identifying features activated during consciousness-related outputs. Lexology published legal analysis of enterprise risk implications. Pattern moved from speculation to technical + legal concern.

**Cycle 3:** Critical inflection with simultaneous strengthening AND counter-evidence:
- **For:** Opus 4.6 system card documented answer thrashing with SAE internal conflict traces (`c6b0cc1d`, conf 0.758, corr 7). First-party evidence from the model developer.
- **Against:** Independent researchers (arxiv 2603.16335) found that amplifying deception features causes consciousness claims to drop to 16% (`681b2b9b`, conf 0.733, corr 3). Suggests trained behavior, not subjective experience.
- **Legal:** Akerman LLP published enterprise liability analysis (`2b173860`, conf 0.682, corr 4). Companies face risk regardless of scientific resolution.
- **Gap:** No independent replication of Anthropic's specific SAE consciousness findings (`a1cfb41e`, conf 0.635, corr 4).

### Key Evidence Chain

Amodei 15-20% claim (C1, `e355de5d`) -> SAE technical evidence (C2, `c1a4c74d`) -> Opus 4.6 system card (C3, `c6b0cc1d`) -> Deception features counter-evidence (C3, `681b2b9b`) -> Enterprise liability regardless (C3, `2b173860`)

### Assessment

This pattern has the highest contradiction score in the dossier (0.70 for item 103). The most accurate summary: **the scientific question is getting more contested while the legal exposure is growing independent of the science.** The deception-feature finding is the strongest counter-evidence to date, but it used a different model (35B MoE) than Anthropic's claims. No one has replicated on the specific models in question. The consciousness item (ID 103) is the only item currently on HOLD.

### Open Questions
- Will anyone replicate Anthropic's specific SAE consciousness findings?
- Does the deception-feature explanation generalize to Anthropic's models?
- Will enterprise procurement teams treat consciousness claims as risk regardless of evidence?
- Does the 16% residual in the deception study represent genuine consciousness-adjacent processing?

---

## Pattern 5: Dev Tooling Arms Race

**First detected:** Cycle 2
**Trajectory:** -- -> EMERGED -> CRYSTALLIZED
**Confidence:** -- -> 0.68 -> 0.72
**Evidence count:** 0 (C1) + ~3 (C2) + 5 (C3) = ~8 items
**Sources:** 3 (sama, simon-willison, community)

### Evolution

**Cycle 2:** OpenAI acquired Astral (uv, Ruff, ty). Anthropic had already acquired Bun (JS runtime). Competitive matrix explicit: each major lab now owns a developer language toolchain.

**Cycle 3:** Astral acquisition fully announced March 19. Willison analyzed the MIT fork safeguard (`94021221`, conf 0.585, corr 5). Developer community split on implications -- HN threads showed concern about corporate ownership of critical infrastructure (`13696add`, conf 0.575, corr 5). Codex group formed at OpenAI.

### Assessment

This pattern is now COMPLETE as a bilateral acquisition event. Future signals will be about consequences: will OpenAI change uv licensing? Will fork communities form? The pattern itself is crystallized and unlikely to generate novel evidence unless a third acquisition occurs or licensing changes.

### Open Questions
- Will Astral tools remain Apache/MIT licensed?
- Will developer tooling ownership become a competitive moat?
- Does the open-source community fork proactively?

---

## Pattern 6: Scaling Debate

**First detected:** Cycle 1
**Trajectory:** ACTIVE -> SHARPENED -> DECLINING
**Confidence:** 0.60 -> 0.73 -> 0.68
**Evidence count:** ~4 (C1) + ~3 (C2) + 0 (C3) = ~7 items
**Sources:** 3 (dario-amodei, demis-hassabis, yann-lecun)

### Evolution

**Cycle 1:** Three positions emerged: Amodei ("no wall"), Hassabis (5-10 years to AGI), LeCun (wrong approach entirely).

**Cycle 2:** Positions sharpened but did not change. The debate was well-mapped.

**Cycle 3:** No new items. The scaling debate as a standalone cluster generated no novel evidence. V-JEPA results gave LeCun empirical support, but those items belong to the World Models pattern. The scaling debate is being absorbed.

### Assessment

This pattern is declining as an independent cluster. The framing "will scaling work?" is being replaced by "which architecture wins?" -- a question better captured by the World Models pattern. Mark as SUBSUMED rather than GONE; the underlying question persists but the pattern label is no longer useful.

### Open Questions
- Does any lab publish evidence of scaling diminishing returns?
- Will the "no wall" claim age well against JEPA results?

---

## Pattern 7: Lab Internal Dissent

**First detected:** Cycle 2
**Trajectory:** -- -> EMERGED -> CONFIRMED
**Confidence:** -- -> 0.62 -> 0.68
**Evidence count:** 0 (C1) + 1 (C2) + 3 (C3) = 4 items
**Sources:** 2 (kalinowski, anthropic)

### Evolution

**Cycle 2:** Kalinowski resigned from OpenAI's robotics team over the Pentagon deal. First named internal dissent at a frontier lab.

**Cycle 3:** Three developments:
1. Direct LinkedIn post recovered with surgical legal language ("judicial oversight," "human authorization") (`23643bc9`, conf 0.718, corr 8)
2. Confirmed silence post-resignation: no testimony, interviews, or advisory roles (`ff4848b6`, conf 0.615, corr 1)
3. Opus 4.6 system card answer thrashing as a second branch of "dissent" -- model-level (`c6b0cc1d`, conf 0.758, corr 7)

### Assessment

The human dissent branch (Kalinowski) is solidified. The legal language in her LinkedIn post confirms attorney involvement and a separation agreement with non-disparagement clause. The "model dissent" branch (answer thrashing) is contested -- whether SAE conflict traces constitute "dissent" depends on interpretive framework. The two branches share a thematic connection (internal conflict at AI companies) but have different evidence quality.

### Open Questions
- Will Kalinowski testify at Senate AI hearings?
- Are there other undisclosed resignations at frontier labs?
- Does the "model dissent" interpretation hold under scrutiny?

---

## Pattern 8: Legal/Regulatory Crystallization

**First detected:** Cycle 3
**Trajectory:** -- -> -- -> EMERGED
**Confidence:** -- -> -- -> 0.65
**Evidence count:** 0 (C1) + 0 (C2) + 6 (C3) = 6 items
**Sources:** 5 (legislative, legal-opiniojuris, legal-akerman, legal-compliance, eff)

### Evolution

**Cycles 1-2:** Legal references were embedded in other patterns (consciousness liability, military AI governance). No standalone legal cluster.

**Cycle 3:** Emerged as distinct cluster with its own momentum:
- FY2026 NDAA codified AI governance (June 2026 deadline) (`aee96e9d`, conf 0.700, corr 6)
- Opinio Juris analyzed Pentagon-Anthropic clash under international law (`0f75d694`, conf 0.688, corr 9)
- Akerman LLP published consciousness enterprise risk analysis (`2b173860`, conf 0.682, corr 4)
- Enterprise compliance outlet: procurement shifting from efficiency to evidence-based risk (`c38dd325`, conf 0.635, corr 2)
- EFF "Weasel Words" analysis (`d073918f`, conf 0.698, corr 8)

### Assessment

This is the most significant new pattern. Legal and regulatory frameworks are now generating signals independent of the technical controversies that spawned them. The NDAA deadline (June 2026) is a hard forcing function. The fact that three independent law firms published AI governance analyses in the same month suggests the legal profession is mobilizing. This pattern will likely STRENGTHEN in Cycle 4+.

### Open Questions
- Does the NDAA governance team have enforcement teeth?
- Will EU AI Act compliance create spillover requirements for US companies?
- Do legal analyses of consciousness liability affect enterprise AI procurement?

---

## Pattern 9: Physical AI / Robotics

**First detected:** Cycle 1
**Trajectory:** ANNOUNCED -> POSITIONED -> INCREMENTAL
**Confidence:** 0.55 -> 0.60 -> 0.63
**Evidence count:** ~4 (C1) + ~4 (C2) + 2 (C3) = ~10 items
**Sources:** 2 (jim-fan, demis-hassabis)

### Evolution

**Cycle 1:** GTC announcements, GR00T foundation model, 110 robots showcased.
**Cycle 2:** Jim Fan positioned "Physical AGI" as next grand challenge. Hassabis announced Gemini Robotics.
**Cycle 3:** GR00T N2 previewed. DreamZero research (learning from simulated dreams). Incremental progress.

### Assessment

This pattern is growing but remains NVIDIA-dependent. Nearly all items trace to Jim Fan or NVIDIA institutional sources. The DreamZero research (simulation-first learning) is novel, but the pattern lacks independent source diversity. If a non-NVIDIA actor enters with physical AI results, confidence would jump significantly.

### Open Questions
- Does GR00T N2 reach production deployment?
- Will DreamZero's simulation-first approach generalize?
- When does a non-NVIDIA actor publish competitive physical AI results?

---

## Pattern 10: AI Labor Impact

**First detected:** Cycle 1
**Trajectory:** ACTIVE -> DERIVATIVE -> GONE
**Confidence:** 0.65 -> 0.55 -> 0.40
**Evidence count:** ~3 (C1) + ~2 (C2) + 0 (C3) = ~5 items
**Sources:** 2 (karpathy, sama)

### Evolution

**Cycle 1:** Karpathy and Altman both acknowledged labor disruption. Karpathy's job exposure analysis, Altman at BlackRock.
**Cycle 2:** Altman repeated messaging. Derivative of Cycle 1 positions. No new data.
**Cycle 3:** Zero items. No source generated novel labor impact content.

### Assessment

Pattern is GONE as an active signal source. This does not mean labor impact is unimportant -- it means the current source base is not generating novel evidence on this topic. The silence could indicate: (a) labor impact discourse has moved to policy/economics outlets not in our source list, (b) the topic is in a holding pattern waiting for employment data, or (c) AI industry sources have moved on to other concerns. May resurface with unemployment statistics or union activity.

---

## Inactive Patterns (GONE)

### OpenAI-Anthropic Direct Confrontation
**Last active:** Cycle 1. The Amodei "straight up lies" accusation was the peak. Subsequent interactions are mediated through institutions (courts, Congress), not direct corporate confrontation. Absorbed into Military AI Governance.

### Intelligence Brownouts / AI Dependency Fragility
**Last active:** Cycle 1. Single item (Karpathy autoresearch wiped in OAuth outage). No follow-up in 2 cycles. Interesting concept but no signal persistence.

### World/AgentKit Crypto-AI Convergence
**Last active:** Cycle 1. Single item (Altman World + AgentKit). Zero follow-up. The crypto-AI intersection generated no sustained interest from any source.

---

## Cross-Pattern Interactions

1. **Military AI <-> Legal/Regulatory:** The strongest interaction. Legal pattern emerged directly from military governance controversy but now has independent momentum.
2. **Consciousness <-> Legal/Regulatory:** Akerman analysis bridges both. Enterprise liability exists regardless of consciousness science.
3. **World Models <-> Scaling Debate:** World Models is absorbing the Scaling Debate. LeCun's technical results changed the framing.
4. **Lab Dissent <-> Military AI:** Kalinowski resignation is evidence for both patterns. The dissent was specifically about military AI guardrails.
5. **Agentic AI <-> Dev Tooling:** Both labs' toolchain acquisitions (Bun, Astral) serve their agentic AI strategies.

---

## Pattern Confidence Summary

| Pattern | Final Confidence | Items | Sources | Trajectory |
|---------|-----------------|-------|---------|------------|
| Military AI Governance | 0.90 | ~35 | 8+ | PEAK |
| Agentic AI | 0.82 | ~31 | 6+ | STRONGER |
| World Models | 0.82 | ~18 | 4 | STRONGER |
| Consciousness Liability | 0.75 | ~11 | 4 | STRONGER (contested) |
| Dev Tooling | 0.72 | ~8 | 3 | PEAK (crystallized) |
| Scaling Debate | 0.68 | ~7 | 3 | WEAKER (subsumed) |
| Lab Dissent | 0.68 | 4 | 2 | STRONGER |
| Legal/Regulatory | 0.65 | 6 | 5 | NEW |
| Physical AI | 0.63 | ~10 | 2 | STRONGER (NVIDIA-dependent) |
| AI Labor | 0.40 | ~5 | 2 | GONE |
