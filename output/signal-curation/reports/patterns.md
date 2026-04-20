# Pattern Report -- Cross-Cycle Analysis

**Contract:** RLC.DOSSIER.SIGNAL.001
**Cycles:** 1-3
**Date:** 2026-03-20
**Evidence:** 148 items (61 Cycle 1, 38 Cycle 2, 49 Cycle 3)

---

## Active Patterns

### 1. Military AI / DoW Governance [PEAK]

**Cycle 1:** Amodei-Altman public dispute over Pentagon deal. Leaked memo, supply chain risk designation, apologies, renegotiation. 3 sources, ~8 items.
**Cycle 2:** Kalinowski resignation (named objections to surveillance + autonomous weapons), Amodei red lines on CBS national TV, broader pattern of named individuals drawing lines.
**Cycle 3:** Full institutional crisis. Hegseth threatened Anthropic with "pariah" status. Anthropic sued Trump admin over supply chain designation (150 judges filed amicus brief). Pentagon developing in-house AI alternatives. EFF published "Weasel Words" analysis exposing surveillance loopholes. FY2026 NDAA codified cross-functional AI governance. Time reframed as citizen data rights issue. 15 items, 8 sources.

**Delta C2->C3:** Pattern exploded from bilateral dispute to multi-institutional confrontation. Now involves: two AI labs, Pentagon, federal courts, Congress (NDAA), civil liberties (EFF), legal profession (3 law firms), and mainstream media (Time). This is no longer an industry story -- it is a constitutional governance question.

**Key evidence:** IDs 100-103, 118-129
**Confidence:** 0.90 -- highest confidence pattern. Multi-source, public record, institutional actors on all sides.

---

### 2. Agentic AI Infrastructure [STRONGER]

**Cycle 1:** 5 sources building agent runtimes, patterns, and tooling.
**Cycle 2:** 6 sources. Chase's context engineering thesis. Willison's living document. Revenue validation (Claude Code $1B ARR).
**Cycle 3:** Maturation phase. Willison published 12th chapter defining "agentic engineering" as a discipline. Chase's Deep Agents hit 9.9k GitHub stars + NVIDIA partnership. Karpathy's autoresearch adopted by Shopify CEO. LangChain AI-Q Blueprint for enterprise deployment.

**Delta C2->C3:** Shifted from "building agents" to "standardizing agent development." The discipline is crystallizing: naming conventions, pattern libraries, enterprise blueprints. Novelty is declining as the space codifies.

**Key evidence:** IDs 130, 131, 135
**Confidence:** 0.82 -- broadest cluster, maturing

---

### 3. World Models / Anti-LLM Thesis [STRONGER]

**Cycle 1:** LeCun ($1B AMI Labs) + Hassabis (AlphaGo retrospective) converging on world models.
**Cycle 2:** Hassabis confirmed spending "a lot of time on world models." AMI Labs website launched. Fei-Fei Li's World Labs at $1B.
**Cycle 3:** Concrete technical results arrived. V-JEPA achieved 2.85x inference speedup and SOTA on Epic-Kitchens-100 with 50% fewer parameters. AMI Labs raised $1.03B seed (largest European seed ever). Hassabis spending "most research time" on world models, citing SIMA 2 and Genie 3. Latent Space provided independent analysis of JEPA architecture.

**Delta C2->C3:** The thesis moved from investment/vision to technical benchmarks. V-JEPA results are the first concrete evidence that world model architectures can outperform on standard benchmarks. This changes the debate from theoretical to empirical.

**Key evidence:** IDs 109-115
**Confidence:** 0.82 -- technical results now available, multi-billion funding

---

### 4. Consciousness Liability [STRONGER]

**Cycle 1:** Amodei's 15-20% consciousness claim. Single controversial statement.
**Cycle 2:** Technical evidence (sparse autoencoders), Lexology legal analysis.
**Cycle 3:** Three significant developments: (a) Opus 4.6 system card documented "answer thrashing" with SAE traces showing internal conflict, (b) independent academic research (arxiv 2603.16335) found deception feature amplification causes consciousness claims to drop to 16%, (c) Akerman LLP published enterprise liability analysis, (d) comprehensive SAE survey published. The academic finding directly contradicts the consciousness interpretation -- SAE activations may reflect trained behaviors, not subjective experience.

**Delta C2->C3:** Critical inflection. The academic counter-evidence (deception features -> consciousness claims) provides the first serious alternative explanation to the consciousness hypothesis. Meanwhile, enterprise legal risk continues to grow regardless of the scientific answer. The legal liability is real even if consciousness is not.

**Key evidence:** IDs 103-105, 116, 136
**Confidence:** 0.75 -- counter-evidence strengthens rather than weakens the pattern. The controversy itself is the signal.

---

### 5. Scaling Debate [WEAKER]

**Cycle 1:** 2-3 sources with differing timelines.
**Cycle 2:** Timeline spread widened: Amodei ("no wall"), Hassabis (5-10 years), LeCun (wrong approach).
**Cycle 3:** No new positions introduced. V-JEPA results give LeCun empirical support. Hassabis doubled down on world models. But the scaling debate as a distinct cluster generated no new items -- it is being absorbed into the World Models pattern.

**Delta C2->C3:** Pattern is merging with World Models. The "scaling debate" framing is less useful now that LeCun has technical results. The question is no longer "will scaling work" but "which architecture wins."

**Key evidence:** IDs 113, 109
**Confidence:** 0.68 -- declining as standalone pattern

---

### 6. Dev Tooling Arms Race [PEAK]

**Cycle 1:** OpenAI acquired Astral. Single data point.
**Cycle 2:** Anthropic acquired Bun. Competitive matrix explicit.
**Cycle 3:** Astral acquisition fully announced (March 19). Willison analyzed MIT fork safeguard. Developer community reaction split (HN threads). Both acquisitions now complete. Codex group formed at OpenAI.

**Delta C2->C3:** Both major acquisitions are now finalized. The pattern is complete as a bilateral event. Future signals will be about consequences (open source maintenance, fork decisions, licensing changes), not new acquisitions.

**Key evidence:** IDs 106-108
**Confidence:** 0.72 -- crystallized, watch for licensing changes

---

### 7. Lab Internal Dissent [STRONGER]

**Cycle 1:** No intra-company signals.
**Cycle 2:** Kalinowski resignation with named, specific objections.
**Cycle 3:** Kalinowski resignation confirmed with direct LinkedIn post (surgical language on judicial oversight, human authorization). Continued post-resignation silence confirms legal constraints. Opus 4.6 system card documenting answer thrashing adds a different dimension: the models themselves showing signs of internal conflict.

**Delta C2->C3:** The dissent pattern has two branches now: human dissent (Kalinowski) and model dissent (answer thrashing). Whether the model behavior qualifies as "dissent" is contested, but the system card documentation by Anthropic itself is notable.

**Key evidence:** IDs 100-103
**Confidence:** 0.68 -- Kalinowski data solidified, model dissent interpretation contested

---

### 8. Physical AI / Robotics [STRONGER]

**Cycle 1:** GTC announcements, GR00T.
**Cycle 2:** Jim Fan's "Physical AGI as next grand challenge." Hassabis Gemini Robotics.
**Cycle 3:** GR00T N2 previewed at GTC 2026. DreamZero research (learning from dreams). Physical AI partnership announcements. Continued NVIDIA institutional momentum.

**Delta C2->C3:** Incremental. GR00T N2 is an evolution. DreamZero is novel (simulation-first learning). But still single-institution (NVIDIA) signal.

**Key evidence:** ID 133
**Confidence:** 0.63 -- growing but NVIDIA-dependent

---

### 9. Legal/Regulatory Crystallization [NEW]

**Cycle 1-2:** Scattered legal references embedded in other patterns.
**Cycle 3:** Emerged as distinct cluster. FY2026 NDAA codified AI governance requirements (June 2026 deadline). Enterprise procurement hardening (EU AI Act, task-level evidence). Three independent law firms published analyses (Akerman, Opinio Juris, compliance outlet). EFF entered the discourse.

**Delta:** First cycle where legal/regulatory items form their own cluster rather than being subsidiary to others. 6 items from 5 sources. The governance question has its own momentum independent of the military AI story.

**Key evidence:** IDs 117-119, 126
**Confidence:** 0.65 -- new pattern, multiple independent legal sources

---

### 10. AI Labor Impact [GONE]

**Cycle 1:** Karpathy + Altman both acknowledging disruption.
**Cycle 2:** Altman repeated messaging. Derivative.
**Cycle 3:** Zero items. No source generated novel labor impact content.

**Delta:** Pattern has gone silent for one full cycle. Marked GONE. May resurface if unemployment data arrives.

**Key evidence:** None in Cycle 3
**Confidence:** 0.40 -- below active threshold

---

## Inactive Patterns

### OpenAI-Anthropic Direct Confrontation [GONE]
**Last active:** Cycle 1. Leaked memo apology in C3 is a residual echo, not a new confrontation.

### Intelligence Brownouts / AI Dependency Fragility [GONE]
**Last active:** Cycle 1 (single item). No follow-up in 2 cycles.

### World/AgentKit Crypto-AI Convergence [GONE]
**Last active:** Cycle 1 (single item). Zero follow-up in 2 cycles.

---

## Pattern Confidence Matrix

| Pattern | C1 | C2 | C3 | Trend |
|---------|-----|-----|-----|-------|
| Military AI / DoW | 0.70 | 0.82 | 0.90 | +0.08 [PEAK] |
| Agentic AI | 0.72 | 0.78 | 0.82 | +0.04 [STRONGER] |
| World Models | 0.65 | 0.75 | 0.82 | +0.07 [STRONGER] |
| Consciousness Liability | 0.45 | 0.65 | 0.75 | +0.10 [STRONGER] |
| Dev Tooling | -- | 0.68 | 0.72 | +0.04 [PEAK] |
| Scaling Debate | 0.60 | 0.73 | 0.68 | -0.05 [WEAKER] |
| Lab Dissent | -- | 0.62 | 0.68 | +0.06 [STRONGER] |
| Legal/Regulatory | -- | -- | 0.65 | NEW |
| Physical AI | 0.55 | 0.60 | 0.63 | +0.03 [STRONGER] |
| AI Labor | 0.65 | 0.55 | 0.40 | -0.15 [GONE] |
