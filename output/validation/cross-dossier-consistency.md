# Cross-Dossier Validation Report

**Date:** 2026-02-19 (updated 2026-03-16 to include Okta)
**Analyst:** Validation Agent (Claude Opus 4.6)
**Scope:** 5 completed dossiers -- Okta, Sierra AI, Vercel, Glean, Cerebras
**Purpose:** Scoring calibration, consistency checks, contradiction detection, gap identification

> **Update Note (2026-03-16):** This report was originally scoped to 4 companies. Okta (NASDAQ: OKTA) has been integrated into all comparison tables. Okta is the only public company in the set, providing SEC-verified financial data that serves as a calibration anchor. Full cross-portfolio analysis including gap remediation, portfolio thesis, and scenario modeling is in `output/cross-portfolio-analysis.md` and `output/portfolio-thesis.md`.

---

## 1. Scoring Calibration: AI Reality Scores

### Current Scores

| Company | AI Reality Score | Justification Summary |
|---------|:----------------:|----------------------|
| Okta | 3.0/5 | Applied ML in production (Identity Threat Protection, behavioral analytics), active ML hiring, but marketed as "AI-native" when still building foundational ML services. No publications. |
| Vercel | 3.2/5 | AI application company with real revenue (v0 $42M ARR), no proprietary models, integration layer |
| Sierra | 3.5/5 | Multi-model orchestration with real enterprise deployment, no proprietary model, "LLM wrapper" criticism |
| Glean | 4.0/5 | Genuine applied ML at scale (search ranking, entity extraction, GraphRAG), no publications |
| Cerebras | 5.0/5 | Hardware IS the AI product, wafer-scale chip, NeurIPS/ICLR papers, Gordon Bell Prize |

### Calibration Assessment

**Cerebras 5.0/5 -- JUSTIFIED.**
Cerebras is the only company in the set producing frontier hardware and publishing at top ML/HPC venues. The WSE-3 is not a wrapper around someone else's technology -- it is foundational technology. Gordon Bell Prize involvement (Special Prize 2022, finalist 3 consecutive years), NeurIPS/ICLR publications, and independently verified performance benchmarks all support a maximum score. There is no inflation here. A 5.0 means "the AI IS the product, built from the ground up," and Cerebras is the only company in this set that meets that bar.

**Glean 4.0/5 -- ARGUABLY 0.5 POINTS TOO HIGH.**
The 4.0 score is the most generous in the set relative to the evidence. The justification states "genuine applied ML at scale" -- which is true. But key countervailing evidence:
- Zero academic publications from any Glean employee
- Zero technical blog posts with implementation depth on the Knowledge Graph
- VentureBeat describes the core technology as "GraphRAG" -- a well-documented open technique
- No research scientists on staff (Applied Scientists only)
- The "proprietary Knowledge Graph" claim is unverifiable and likely overstated

Compare to Sierra at 3.5, which has tau-bench (1,099 GitHub stars, adopted by Anthropic/OpenAI), a research team that published at Princeton/Google, and named researchers with public Google Scholar profiles. Sierra has more verifiable AI depth than Glean, yet scores lower.

**Recommended adjustment:** Glean should be 3.5/5, tied with Sierra. Both are excellent applied ML companies with no proprietary models and no frontier research. The 0.5 point difference between them is not supported by the evidence -- if anything, Sierra has more verifiable AI credentials (tau-bench, named researchers).

**Sierra 3.5/5 -- APPROPRIATELY CALIBRATED.**
The score correctly captures that Sierra has real engineering sophistication (multi-model orchestration, voice pipeline, supervisor architecture) but relies entirely on third-party models. The tau-bench research output and named researchers (Narasimhan, Shinn) are genuine differentiators, but the "LLM wrapper" criticism from competitors (Cognigy, Teneo) and Blind users is credible. 3.5 accurately reflects "sophisticated applied engineering, not foundational AI."

**Vercel 3.2/5 -- APPROPRIATELY CALIBRATED.**
Vercel is the most clearly an "AI application company, not AI infrastructure company" in the set. v0 uses third-party LLMs. The AI SDK is an integration layer. No proprietary models, no training infrastructure, no GPU fleet, no research publications. The 0.3 point gap below Sierra makes sense -- Sierra at least has a research team and published benchmarks. Vercel's AI is commercially successful but technically the shallowest of the four.

### Recommended Score Adjustments

| Company | Current | Recommended | Change | Reason |
|---------|:-------:|:-----------:|:------:|--------|
| Vercel | 3.2 | **3.2** | None | Correctly positioned |
| Sierra | 3.5 | **3.5** | None | Correctly positioned |
| Glean | 4.0 | **3.5** | -0.5 | Zero publications, unverifiable "proprietary" claims, comparable depth to Sierra |
| Cerebras | 5.0 | **5.0** | None | Correctly positioned |

---

## 2. Build vs Buy Calibration

### Current Scores

| Company | Build vs Buy Score | Core Tech Score | Data/Content Score | Network/Trust Score |
|---------|:------------------:|:--------------:|:------------------:|:------------------:|
| Okta | 3.25/4 | 2.5 (Open standards, Keycloak exists) | 3.5 (7,000+ OIN connectors, compliance certs) | 4.0 (17K customers, Gartner Leader 9yr, brand trust) |
| Glean | 2.7/4 | ~2.0 (Search, RAG easy) | 4.0 (Data/network effects) | 4.0 (GTM) |
| Sierra | 2.82/4 | 2.25 | 3.17 | 4.0 (Founder network) |
| Vercel | 2.95/4 | 2.5 | 3.0 | 4.0 (Next.js community) |
| Cerebras | 3.5/4 | 4.0 (WSE chip) | 4.0 (Yield data) | 4.0 (Customers) |

### Is Glean (2.7) rated easier to replicate than Vercel (2.95)?

**Yes, and this is WRONG. The scores should be closer to equal, or Glean should be slightly harder.**

The evidence does not support Glean being easier to replicate than Vercel:

1. **Glean's connector moat is operationally deeper than Vercel's deployment platform.** Glean has 100+ deep, bidirectional enterprise connectors, each representing $30K-$250K in development and $10K-$50K/year in maintenance. The total connector investment is $5-15M with $2-5M/year carrying cost. The nearest open-source competitor (Onyx) has 40 connectors after 3+ years. In contrast, Vercel's deployment platform has been replicated by multiple companies (Netlify, Railway, Render, Cloudflare Pages).

2. **Glean's cross-source permissions engine has no open-source equivalent.** Resolving ACLs across 100+ heterogeneous enterprise systems at query time is genuinely hard engineering. Vercel's equivalent (git-push deploy, CDN, serverless) is built on well-understood infrastructure patterns.

3. **The scoring discrepancy comes from weighting.** Vercel's 4.0 for "Network Effects / Community" (Next.js 138K stars) receives 20% weight, pulling its composite above Glean. But Glean's connector ecosystem (scored 4.0) receives only implicit weight through the "Core Technology" category, which also includes the easily-replicable RAG and search components that dilute it.

**The real issue:** Glean's composite is dragged down by the RAG/Assistant component scoring 1/4 (easy) and UI scoring 1/4 (easy). These are small portions of the product but significantly dilute the average. Vercel's composite is pulled up by the community moat getting its own 20% weighted category.

**Recommendation:** Either (a) re-weight Glean's connector ecosystem as its own category at 20% weight (comparable to Vercel's community moat treatment), which would raise the score to ~2.9-3.0, or (b) acknowledge that the current scores are slightly miscalibrated and Glean's true replicability is ~2.85-2.95, on par with Vercel. The 0.25 gap (2.7 vs 2.95) overstates the difference.

### Is the Cerebras gap (3.5 vs the rest) justified?

**Yes, emphatically.** The 0.55-0.80 gap between Cerebras and the software companies is, if anything, understated.

Cerebras' core moat is physical hardware that required $2.55B and 10 years to develop. The WSE-3 chip cannot be replicated by any software team, agent swarm, or startup. It requires a national-scale semiconductor program. The TSMC sole-source fabrication relationship adds another dimension of irreplicability.

Every other company in this set can be replicated by a well-funded software team in 2-4 years for $100-250M. Cerebras cannot be replicated for less than $2-4B over 10-15 years. The Build vs Buy score framework (1-4 scale) is not granular enough to capture this difference. If the scale went to 10, Cerebras would be an 8-9 while the software companies would remain 5-7.

### Recommended Build vs Buy Adjustments

| Company | Current | Recommended | Change | Reason |
|---------|:-------:|:-----------:|:------:|--------|
| Glean | 2.7 | **2.85-2.95** | +0.15-0.25 | Connector moat underweighted; parity with Vercel warranted |
| Sierra | 2.82 | **2.82** | None | Correctly positioned |
| Vercel | 2.95 | **2.95** | None | Correctly positioned |
| Cerebras | 3.5 | **3.5** | None | If anything, understated |

---

## 3. Verdict Calibration

### Current Verdicts

| Company | Verdict | Valuation | Multiple | Growth |
|---------|---------|-----------|----------|--------|
| Okta | PROCEED WITH CAUTION | $14.7B (mkt cap) | 5.5x EV/Rev | 11% |
| Sierra | PROCEED WITH CAUTION | $10B | 67-100x ARR | 400-500% |
| Vercel | PROCEED WITH CAUTION | $9.3B | 46.5x ARR | 80-100% |
| Glean | PROCEED WITH CAUTION | $7.2B | 36x ARR | 100% |
| Cerebras | STRONG CANDIDATE | $23B | 19-85x revenue | 245-535% |

### Could any PROCEED WITH CAUTION be upgraded?

**Glean is the strongest upgrade candidate.** Compared to Sierra and Vercel:
- Glean has verified $200M ARR with 100% growth (9-month doubling)
- Lowest revenue multiple of the three software companies (36x vs 46.5x and 67-100x)
- Most defensible operational moat (100+ connectors, no competitor close)
- Clearest enterprise product-market fit (G2 4.7/5, Gartner 4.5/5 across 126 reviews)
- Model-agnostic architecture hedges the foundation model risk that plagues Sierra

However, three factors prevent an upgrade:
1. **Internal culture deterioration is the worst of the four companies.** Glassdoor declining, Blind at 3.7/5 with "rapid decline" and "sinking ship" language. CEO criticized for micromanagement across multiple independent sources. This is a material execution risk.
2. **Microsoft Copilot is an existential-class threat** with no clear resolution. 90% of Fortune 500 already use Copilot at half Glean's price.
3. **The "proprietary Knowledge Graph" moat claim is unverifiable**, making the technology story less compelling than the operational (connectors) story.

**Verdict: Maintain PROCEED WITH CAUTION for Glean.** The culture and Microsoft risks are real. But note: Glean offers the best risk-adjusted entry point of the three software companies due to the lower multiple.

**Sierra and Vercel should not be upgraded.** Both have material structural concerns:
- Sierra: Undisclosed financial metrics beyond ARR, "LLM wrapper" vulnerability, Gap.com incident
- Vercel: Pricing friction generating customer attrition, Cloudflare competitive threat, CEO reputational risk

**Could any be downgraded?** Sierra comes closest to a downgrade. At 67-100x ARR with zero disclosed SaaS health metrics (NRR, gross margin, burn rate, churn), the valuation demands extraordinary trust. The "LLM wrapper" criticism is credible and the Gap.com jailbreak incident reveals real operational risk. However, the revenue trajectory ($0 to $150M in 26 months) is genuinely exceptional and the founder pedigree is unmatched. Maintaining PROCEED WITH CAUTION is correct, but Sierra is the weakest of the three caution candidates.

### Is STRONG CANDIDATE for Cerebras justified?

**Yes, with the stated caveats.**

The STRONG CANDIDATE verdict is appropriate because Cerebras occupies a fundamentally different risk category:

1. **The technology moat is real and physical.** No other company in this set has a moat that would require $2-4B and 10-15 years to replicate. Software companies' moats are always somewhat permeable.

2. **The OpenAI $10B+ deal is the most significant customer validation in the set.** It is not just revenue -- it is the world's leading AI company choosing Cerebras for production workloads (GPT-5.3-Codex-Spark), sending a market signal that no marketing campaign could buy.

3. **Competitive consolidation creates scarcity value.** Groq acquired by NVIDIA, SambaNova by Intel, Graphcore restructured. Cerebras has no comparable independent competitor at scale.

**However, the three risks flagged in the executive summary are all material:**

- **TSMC sole-source dependency** is an existential risk that no software company faces. A Taiwan crisis halts all production. This is not priced into the 3.5 Build vs Buy score because the score measures replication difficulty, not supply chain fragility.
- **Customer concentration shifting from G42 (87%) to OpenAI (estimated 60-75%)** means the structural risk has changed customers but not structure. And OpenAI is developing its own chip with Broadcom.
- **NVIDIA Rubin (H2 2026)** will narrow the speed advantage from 20x+ to potentially 3-5x. The competitive window is 6-12 months.

**The verdict is justified IF the timing caveat is taken seriously.** STRONG CANDIDATE does not mean "safe." It means "the opportunity is exceptional enough to warrant aggressive diligence and potential engagement." The time-sensitivity is the most important qualifier -- this is a STRONG CANDIDATE *now*, and the window closes within 12 months.

---

## 4. Comparative Contradictions

### 4.1 Market Size Estimates -- Overlapping Markets

**Finding: Market sizing is inconsistent across dossiers operating in adjacent spaces.**

| Company | Market Cited | Size | Overlap |
|---------|-------------|------|---------|
| Sierra | Conversational AI market | $14.8B (2024), $41.4B by 2030 | Overlaps with Glean (enterprise AI assistants) |
| Sierra | Contact center AI segment | $4.2B | Narrower, less overlap |
| Glean | Enterprise AI search | $8-12B SAM | Partially overlaps with Sierra (enterprise AI agents) |
| Glean | Agentic AI (expanded TAM) | $32-55B by 2030 | Overlaps with Sierra's projected agent market |
| Vercel | Frontend cloud + AI coding tools | $30-45B combined | Minimal overlap with others |
| Cerebras | AI inference compute | $50-104B by 2030 | Infrastructure layer beneath all three software companies |

**Contradiction:** Sierra's conversational AI market ($41.4B by 2030) and Glean's agentic AI TAM ($32-55B by 2030) both cite the broader "enterprise AI" opportunity but from different angles. If you add them together naively, the combined "enterprise AI agent" market would be $73-96B by 2030. This likely double-counts because enterprise AI agents that search company data (Glean's territory) and enterprise AI agents that handle customer conversations (Sierra's territory) draw from overlapping budget pools -- the "enterprise AI" line item in CIO budgets.

**Impact:** Neither dossier accounts for the possibility that Glean and Sierra compete for the same enterprise AI budget. A Fortune 500 CIO allocating $5M/year to "AI agents" might split that between customer-facing (Sierra) and employee-facing (Glean), not fund both at full projected levels. The TAM for each company should be discounted by the cannibalization from adjacent AI agent vendors.

### 4.2 Revenue Multiples Are Not Treated Consistently

**Finding: The dossiers apply different frameworks to similar multiples without cross-referencing.**

| Company | Multiple | Dossier's Assessment | Comparable Used |
|---------|----------|---------------------|-----------------|
| Sierra | 67-100x ARR | "Elevated but within AI-company range" | Anthropic (~50x), OpenAI (~100x) |
| Vercel | 46.5x ARR | "Extremely high" | Cloudflare (15-18x), Datadog (15-18x), Cursor (~50x) |
| Glean | 36x ARR | "Aggressive but not unprecedented" | Snowflake at $200M ARR (~100x), Datadog (~40x) |
| Cerebras | 19-85x revenue | "Aggressive on trailing, defensible on forward" | NVIDIA (22x), Marvell (15x), Astera Labs (30x) |

**Contradiction:** Sierra at 67-100x is called "elevated but within range" while Vercel at 46.5x is called "extremely high." Sierra's multiple is 44-115% higher than Vercel's, yet receives milder language. This inconsistency exists because Sierra's dossier compares to foundation model companies (Anthropic, OpenAI) while Vercel's dossier compares to public cloud/developer companies (Cloudflare, Datadog). The choice of comparable set determines the verdict more than the actual multiple.

**A consistent framework would note:** All four companies trade at significant premiums to public market medians (6-8x for SaaS, 10-20x for high-growth cloud). The premium ordering by justified difficulty should be: Cerebras > Sierra/Glean > Vercel, based on growth rate and moat depth. Currently, the multiple ordering is: Sierra (67-100x) > Vercel (46.5x) > Glean (36x), which inversely correlates with the justified ordering (Glean has the most defensible moat and equal growth rate to Sierra, yet has the lowest multiple).

**Recommended action:** Add a cross-reference table to each P6 report comparing the target's multiple to the other three dossiers, not just external comparables. This would immediately surface that Sierra at 67-100x is the hardest to justify relative to Glean at 36x with comparable growth.

### 4.3 "No Proprietary Model" Criticism Applied Inconsistently

**Finding:** Sierra is heavily criticized as an "LLM wrapper" with no proprietary model. Vercel is similarly characterized as an "AI application company, not AI research company." But Glean -- which also has no proprietary model and uses third-party LLMs (Claude, Gemini, GPT) -- receives significantly less criticism on this dimension.

| Company | Uses Third-Party Models? | Proprietary Model? | Criticism Level |
|---------|:------------------------:|:------------------:|:---------------:|
| Sierra | Yes (OpenAI, Anthropic, Meta, proprietary mix) | No (claims "proprietary" in constellation but unverified) | HIGH ("LLM wrapper" is a central risk) |
| Vercel | Yes (v0 uses Anthropic/OpenAI) | No | MEDIUM ("AI application company") |
| Glean | Yes (Claude, Gemini, GPT via Model Hub) | No | LOW (positioned as "model-agnostic" strength) |

**Contradiction:** Glean's lack of a proprietary model is framed as a strength ("model-agnostic architecture means Glean survives regardless of which LLM wins"). Sierra's lack of a proprietary model is framed as a critical vulnerability ("LLM wrapper"). The underlying technology dependence is identical -- both are orchestration layers over third-party foundation models -- but the narrative framing differs.

**The difference is partially justified:** Sierra competes in CX where the model quality directly determines resolution quality (the customer interacts with the model's output). Glean competes in search where the retrieval/ranking layer (which IS proprietary) matters more than the generation layer. But the inconsistent framing should be acknowledged.

### 4.4 Employee Sentiment Treated With Different Severity

| Company | Glassdoor | Blind | Narrative Impact on Verdict |
|---------|-----------|-------|----------------------------|
| Okta | 3.7/5 (~200+ reviews) | Mgmt 3.0/5, "PIP culture", offshoring concerns | Listed as structural concern; annual layoff cycle (3 consecutive Feb layoffs) |
| Sierra | 5.0/5 (11 reviews) | Mixed, "snake-oily" threads | Noted as yellow flag; thin sample acknowledged |
| Vercel | 4.1/5 (115 reviews) | 3.9/5 (37 reviews), Mgmt 3.1/5 | Listed as Key Risk #3 |
| Glean | 4.2/5 (80 reviews) | 3.7/5 (51 reviews), WLB 3.1/5 | Listed as Key Risk #2 |
| Cerebras | 4.1/5 (57 reviews) | 3.8/5 (32 reviews), Mgmt 3.1/5 | Mentioned as "STABLE with CONCERNS" |

**Finding:** Vercel and Glean get penalized heavily for culture issues (Key Risk #2 and #3 respectively), while Cerebras -- with nearly identical Glassdoor/Blind scores and the same management rating (3.1/5 on Blind) -- gets a much gentler treatment ("STABLE with CONCERNS") that does not affect the STRONG CANDIDATE verdict. This inconsistency is partially justified by Cerebras' hardware moat making team retention somewhat less critical (the chip exists regardless of attrition), but the inconsistency should be acknowledged.

Sierra gets the gentlest treatment despite the "snake-oily" Blind threads, likely because the Glassdoor sample (11 reviews) is too thin to draw conclusions. This is correctly handled -- thin data gets discounted rather than amplified.

### 4.5 OpenAI Appears in Multiple Dossiers as Customer AND Risk Factor

- **Vercel:** OpenAI listed as a verified customer (ChatGPT interface on Next.js/Vercel)
- **Sierra:** No OpenAI relationship noted
- **Glean:** No OpenAI relationship noted
- **Cerebras:** OpenAI is the $10B+ anchor customer and primary revenue driver

**Missing cross-reference:** OpenAI's financial exposure is relevant across dossiers. OpenAI has $600B+ in total cloud and compute commitments (noted in Cerebras P4) against ~$13B revenue. If OpenAI faces financial stress, this affects Cerebras (primary revenue source), Vercel (customer), and potentially the broader enterprise AI market that Sierra and Glean depend on. No dossier flags this systemic risk.

---

## 5. Missing Analysis: What VCs Would Immediately Ask

### 5.1 CRITICAL MISSING: NRR for All Four Companies

**Not a single dossier has verified NRR data.** This is the most important SaaS metric after revenue growth, and it is absent across the board.

| Company | NRR Estimate | Confidence | VC Reaction |
|---------|:------------:|:----------:|-------------|
| Okta | 106% (disclosed, declining from 120%) | HIGH | "NRR below 110% for an identity platform with 76% GM = expansion is stalling. Where's the second act?" |
| Sierra | 120-150% | LOW | "Show me cohort data or I can't underwrite the durability of $150M ARR" |
| Vercel | 110-120% | LOW | "At 46.5x, I need to see NRR > 130% to believe the flywheel works" |
| Glean | 120-140% | LOW | "If NRR is below 120%, the 100% growth is all new logos, which is expensive and fragile" |
| Cerebras | N/A (hardware) | -- | Hardware metrics apply differently (backlog, utilization, repeat orders) |

**Recommendation:** Every dossier should explicitly state: "NRR is undisclosed. This is the single most important missing data point. No investment recommendation can be finalized without it." The current dossiers mention it but bury it among other gaps.

### 5.2 CRITICAL MISSING: Gross Margin Comparisons

Only Vercel and Cerebras have estimated gross margins. Sierra and Glean do not.

| Company | Gross Margin | Confidence | Issue |
|---------|:------------:|:----------:|-------|
| Okta | 76% | HIGH (SEC filing) | Strong SaaS margins; 98% subscription revenue. Calibration anchor for the portfolio. |
| Sierra | 40-65% (est.) | LOW | Multi-model inference costs are high; outcome-based pricing absorbs cost variance |
| Vercel | ~76% | MEDIUM | Reported by Getlatka; strong for cloud infra |
| Glean | 65-75% (est.) | LOW | LLM API costs + GCP infrastructure |
| Cerebras | 38-41% | HIGH (S-1) | Below all semiconductor peers except Intel Gaudi |

**Observation:** If we take the midpoints, the ordering is: Vercel (76%) > Glean (70%) > Sierra (52%) > Cerebras (40%). This is the inverse of the AI Reality Scores. The companies with the most genuine AI depth (Cerebras, Sierra) have the worst margins because inference compute is expensive. This is a fundamental structural observation that no individual dossier surfaces.

A VC would immediately ask: "How do these companies' margin structures constrain their growth? Can Sierra sustain 400%+ growth if each new customer adds inference cost at 35-60% of revenue?"

### 5.3 MISSING: Capital Efficiency Comparison

| Company | Capital Raised | ARR/Revenue | Revenue per $1 Raised |
|---------|:-------------:|:---:|:---------------------:|
| Okta | $187M (IPO) + retained earnings | $2,610M | $13.90 (17 years of compounding; calibration anchor) |
| Sierra | $635M | $150M | $0.24 |
| Vercel | $863M | $200M | $0.23 |
| Glean | $765M | $200M | $0.26 |
| Cerebras | $2,550M | $272-500M | $0.11-0.20 |

**Observation:** The three software companies are remarkably similar in capital efficiency ($0.23-$0.26 ARR per dollar raised). Cerebras is less efficient, which is expected for hardware. A VC would ask: "Sierra raised $635M and is burning $15-30M/month. At what ARR does Sierra become self-sustaining? Is $635M enough?" None of the dossiers model the path to profitability with enough specificity.

### 5.4 MISSING: Founder/CEO Risk Assessment Depth

Each dossier mentions founder risk but none systematically assesses:
- **Key-person insurance:** Does the company have it?
- **Succession planning:** Is there a credible #2?
- **Attention fragmentation:** Sierra (Bret Taylor is also OpenAI board chair), Vercel (CEO controversy), Glean (CEO micromanagement), Cerebras (CEO personally closing deals)
- **Equity alignment:** Only Sierra mentions founder equity stake (25%). The others do not.

### 5.5 MISSING: Competitive Interaction Between These Four Companies

None of the dossiers acknowledge that the four target companies serve overlapping parts of the AI infrastructure stack:

```
Layer 4: AI Applications (End Users)
  |-- Sierra (customer-facing AI agents)
  |-- Glean (employee-facing AI search/agents)
  |
Layer 3: AI Development Platform
  |-- Vercel (AI app deployment, v0, AI SDK)
  |
Layer 2: AI Inference Compute
  |-- Cerebras (inference hardware/cloud)
  |
Layer 1: Foundation Models
  |-- OpenAI, Anthropic, Google (model providers)
```

Cerebras provides compute to OpenAI, which provides models to Sierra, Glean, and Vercel. Vercel provides deployment infrastructure that Sierra or Glean could theoretically use. A VC portfolio perspective would ask: "If I invest in all four, what is my correlated risk if the AI spending cycle cools?"

### 5.6 MISSING: Regulatory and Compliance Risk Comparison

| Company | Regulatory Exposure | Assessment |
|---------|-------------------|------------|
| Okta | SOC 1/2/3, ISO 27001/17/18, FedRAMP High, HIPAA, GDPR | MEDIUM -- highest compliance portfolio in the set; SEC public company obligations |
| Sierra | HIPAA (R1 healthcare), GDPR (EU customers), state AI regulation | HIGH -- customer-facing AI in regulated industries |
| Vercel | Standard cloud compliance (SOC 2, ISO 27001) | LOW -- infrastructure, not application-level |
| Glean | HIPAA, GDPR, enterprise data governance, EU AI Act | HIGH -- processes enterprise data across regulated industries |
| Cerebras | CFIUS, ITAR/EAR, Taiwan geopolitical, export controls | VERY HIGH -- hardware supply chain, national security adjacency |

No dossier discusses the EU AI Act's potential impact on enterprise AI agents (Sierra, Glean) or the upcoming SEC climate disclosure rules' impact on data center operators (Cerebras). These regulatory risks are 12-24 months away and should be flagged.

### 5.7 MISSING: Customer Reference Depth

Every dossier lists customer logos. No dossier includes reference call notes or quotes from actual customers (beyond review platforms). A VC would require 3-5 direct customer reference calls per company before committing capital. The dossiers should flag: "Customer references not conducted. Logo lists verified but depth of relationship unknown."

This is particularly important for Vercel, where the executive summary notes that enterprise "customers" may be individual teams using a $20-25K/year plan, not wall-to-wall enterprise deployments.

---

## 6. Summary of Recommended Adjustments

### Score Changes

| Company | Metric | Current | Recommended | Rationale |
|---------|--------|:-------:|:-----------:|-----------|
| Glean | AI Reality Score | 4.0 | **3.5** | Zero publications, unverifiable "proprietary" graph, comparable depth to Sierra |
| Glean | Build vs Buy | 2.7 | **2.85-2.95** | Connector moat underweighted relative to Vercel's community moat treatment |
| All others | All scores | -- | **No change** | Correctly calibrated |

### Verdict Changes

| Company | Current Verdict | Recommended | Rationale |
|---------|----------------|:-----------:|-----------|
| Sierra | PROCEED WITH CAUTION | **No change** | Highest multiple, least disclosed metrics, "LLM wrapper" risk |
| Vercel | PROCEED WITH CAUTION | **No change** | Cloudflare threat, pricing friction, culture issues |
| Glean | PROCEED WITH CAUTION | **No change** | Microsoft threat, culture deterioration, despite best risk-adjusted entry |
| Cerebras | STRONG CANDIDATE | **No change** | Irreplicable moat, transformative deal, but time-sensitive |

### Critical Gaps to Address

1. **Add a cross-dossier comparable table to each P6 valuation report.** The four companies should be compared against each other, not just external peers, to surface valuation inconsistencies.

2. **Standardize the treatment of "no proprietary model" risk.** Either penalize all three software companies equally for LLM dependence, or explicitly justify why Glean's model-agnostic positioning is a strength while Sierra's is a vulnerability.

3. **Create a systemic risk section.** All four companies depend on continued enterprise AI spending momentum. An "AI winter" scenario or enterprise budget rationalization would hit all four simultaneously. No dossier models this correlated risk.

4. **Flag NRR as a blocking data gap, not just a notable gap.** For any company at 36x+ ARR multiple, NRR is the difference between "durable growth" and "front-loaded logos that churn." Make it a gating requirement for any "PROCEED" or "STRONG CANDIDATE" verdict.

5. **Model the path to profitability for each company.** Current dossiers estimate burn rates but do not project when each company reaches cash flow breakeven. This is a standard VC diligence item that is missing from all four reports.

---

## 7. Relative Ranking (Risk-Adjusted)

If forced to rank these five as investment opportunities today:

| Rank | Company | Rationale |
|:----:|---------|-----------|
| 1 | **Cerebras** | Irreplicable moat, transformative anchor deal, favorable competitive consolidation. Highest risk/reward but the moat is physical, not narrational. Time-sensitive. |
| 2 | **Glean** | Best risk-adjusted entry (lowest multiple at 36x), most defensible operational moat (connectors), clearest enterprise PMF. Culture risk is the key monitor. |
| 3 | **Okta** | Only profitable company in the set. $730M FCF, 7,000+ integration moat, 5.5x EV/Rev. Lowest upside but lowest risk. Portfolio anchor and calibration benchmark. Growth deceleration (11%) and NRR decline (106%) cap the ceiling. |
| 4 | **Vercel** | Real community moat (Next.js), validated AI pivot (v0), reasonable multiple (46.5x). But Cloudflare threat is structural and pricing friction is self-inflicted. |
| 5 | **Sierra** | Fastest revenue ramp is genuinely impressive. But highest multiple (67-100x), zero disclosed health metrics, "LLM wrapper" vulnerability, and configuration-dependent safety. The bet is entirely on trajectory and founder brand. |

---

*Validation report generated by Dossier v0.1.0 -- cross-dossier consistency analysis.*
*All findings based on data collected 2026-02-18 to 2026-02-19 across 5 completed due diligence pipelines (Okta added 2026-03-16).*
