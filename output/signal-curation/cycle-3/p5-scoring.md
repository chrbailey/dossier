# Phase 5: Scoring -- Cycle 3

**Contract:** RLC.DOSSIER.SIGNAL.001
**Date:** 2026-03-20
**Cycle:** 3

---

## Raw -> Working Promotion Analysis

**Cycle 3 raw items evaluated:** 38
**Threshold:** composite >= 0.3
**Promoted:** 37
**Rejected:** 1

### Promoted (raw -> working)

| ID | Hash | Source | Composite | Notes |
|----|------|--------|-----------|-------|
| 103 | c6b0cc1dcc4b31bc | anthropic | 0.758 | Opus 4.6 system card, answer thrashing |
| 123 | 5dd1fcda2d8294c0 | pentagon | 0.752 | Hegseth pariah threat, surveillance scope |
| 120 | 0dc66a56ab5b4b0f | dario-amodei | 0.748 | Anthropic sues Trump admin |
| 113 | 41eb0f910c373dc2 | yann-lecun | 0.738 | V-JEPA 2.85x speedup, SOTA |
| 104 | 681b2b9b3da17c66 | academic | 0.733 | SAE deception features, consciousness drops to 16% |
| 101 | 23643bc9399c8048 | kalinowski | 0.718 | Direct LinkedIn resignation post |
| 119 | aee96e9d770b7d59 | legislative | 0.700 | FY2026 NDAA AI governance provisions |
| 126 | d073918f3623925c | eff | 0.698 | EFF "Weasel Words" surveillance loophole |
| 122 | b3bbeb3c16ade542 | pentagon | 0.693 | Pentagon in-house AI alternatives |
| 118 | 0f75d694e6d25874 | legal-opiniojuris | 0.688 | Legal analysis of guardrails clash |
| 116 | 2b173860c1af3392 | legal-akerman | 0.682 | Enterprise risk from consciousness claims |
| 109 | 238b2ef5bf94c580 | demis-hassabis | 0.672 | World models: SIMA 2, Genie 3 |
| 125 | eb7b49b3c1284851 | sama | 0.672 | OpenAI Pentagon agreement text |
| 100 | 136662e118f76398 | kalinowski | 0.670 | Kalinowski resignation - surveillance + lethal autonomy |
| 121 | 52c6fc5ab931e14b | sama | 0.662 | Altman admitted rushing deal |
| 127 | bac7c4cfe1b83961 | dario-amodei | 0.647 | Amodei leaked memo apology |
| 117 | c38dd3252696ca5a | legal-compliance | 0.635 | Enterprise procurement hardening |
| 129 | 53143801295fcbb1 | media-time | 0.635 | Time: data rights reframing |
| 105 | a1cfb41e30dc87ef | academic | 0.635 | SILENCE: No SAE consciousness replication |
| 133 | a065d4027b69de17 | jim-fan | 0.632 | GTC 2026: GR00T N2, DreamZero |
| 124 | 8cdc4e5de29f96f3 | dario-amodei | 0.632 | Anthropic two redlines statement |
| 114 | b8ddf4ccaa05330e | yann-lecun | 0.627 | LeCun AMI Labs X announcement |
| 112 | 41190c48f96468fd | yann-lecun | 0.623 | AMI Labs $1.03B seed details |
| 102 | ff4848b6017a3c34 | kalinowski | 0.615 | SILENCE: Kalinowski post-resignation |
| 115 | 1a9ea4f35d718cf5 | swyx | 0.605 | Latent Space AMI Labs coverage |
| 130 | 488fb00fcf84403c | karpathy | 0.585 | Autoresearch release, Shopify adoption |
| 106 | 94021221cf562675 | simon-willison | 0.585 | Willison Astral acquisition analysis |
| 108 | 13696add259b3d11 | community | 0.575 | HN dev sentiment on Python infra |
| 128 | 1b07b7dc78e25dd5 | media-time | 0.570 | Time Anthropic profile |
| 131 | 73be110a3f60f431 | harrison-chase | 0.565 | LangChain + NVIDIA, Deep Agents 9.9k |
| 110 | 45423f85392d6960 | demis-hassabis | 0.560 | Hassabis Davos 2026, world models |
| 135 | 3e9dedb8dfcb8c3f | simon-willison | 0.560 | Agentic engineering patterns ch.12 |
| 136 | 9b15c17f9999d20b | academic | 0.547 | SAE comprehensive survey |
| 107 | df7aa5fbda55bfe2 | sama | 0.530 | Astral acquisition announcement |
| 111 | b1474c200a20ab7f | demis-hassabis | 0.502 | Hassabis Fortune interview |
| 132 | 79a7f1877961bca7 | swyx | 0.458 | Latent Space podcast expansion |
| 134 | beb1f19ed98f45d8 | emad-mostaque | 0.355 | Mostaque - Great Decoupling |

### Rejected (below threshold)

| ID | Hash | Source | Composite | Reason |
|----|------|--------|-----------|--------|
| 148 | d411d0e63fb9e6ae | swyx | 0.000 | No signals attached. Search null result -- no content to score. |

---

## Working -> Verified Promotion Analysis

**Working items evaluated:** 108
**Threshold:** composite >= 0.5 AND corroboration >= 1
**Candidates:** 0

No items qualify for verified promotion. All 108 working items have corroboration_count = 0. Cross-evidence corroboration has not been computed for any cycle. This is a systemic gap -- corroboration scoring should be implemented before Cycle 4.

---

## Human Review Triggers

### Flagged: ID 103 (anthropic) -- contradiction = 0.70

**Content:** Opus 4.6 system card documented "answer thrashing" -- model computes correct answer but training overrides it. Sparse autoencoder analysis shows internal conflict traces.

**Why flagged:** Contradiction score at the 0.70 threshold. This item makes claims about AI internal states that could be interpreted as evidence for/against consciousness. The Opus system card is a primary source from the model's developer, but the interpretation of SAE traces as "internal conflict" is contested.

**Recommendation:** HOLD for human review. The consciousness-related interpretation is high-stakes and the evidence admits multiple explanations (see Phase 7 hypotheses if promoted).

### Monitored: 7 additional items with contradiction > 0.5

These items all relate to the Pentagon/DoW cluster where contradiction is expected due to adversarial positioning between parties. No human review required -- contradiction is structural, not evidentiary.

- ID 123 (pentagon, 0.65): Hegseth threat vs. industry guardrails
- ID 104 (academic, 0.65): SAE research contradicts consciousness claims
- ID 121 (sama, 0.60): Altman self-contradiction on deal quality
- ID 126 (eff, 0.55): EFF vs. OpenAI agreement language
- ID 125 (sama, 0.55): Agreement text vs. EFF critique
- ID 116 (legal-akerman, 0.55): Legal risk framing vs. Anthropic position
- ID 101 (kalinowski, 0.55): Resignation vs. continued OpenAI narrative

---

## Promotion Summary

| Transition | Count | Action |
|-----------|-------|--------|
| raw -> working | 37 | Execute in P7 |
| raw -> rejected | 1 | ID 148 (no signals) |
| working -> verified | 0 | Blocked by corroboration = 0 |
| human review hold | 1 | ID 103 (consciousness/contradiction) |

---

## Scoring Distribution (Cycle 3)

- Mean composite: 0.626
- Median composite: 0.635
- Max: 0.758 (ID 103, anthropic)
- Min promoted: 0.355 (ID 134, mostaque)
- Items > 0.7: 5 (13.2%)
- Items 0.5-0.7: 27 (71.1%)
- Items 0.3-0.5: 5 (13.2%)
- Items < 0.3: 1 (2.6%)
