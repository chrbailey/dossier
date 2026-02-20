# Phase 2: Market Research — Glean Technologies (glean.com)

**Target:** glean.com
**Date:** 2026-02-19
**Analyst:** Claude (Phase 2 sub-agent)
**Status:** COMPLETE
**Depends on:** `01-discovery.md`

---

## 1. Problem Statement

### What problem does Glean solve?

Enterprise knowledge is fragmented across dozens of SaaS applications (Slack, Google Drive, Jira, Salesforce, Confluence, GitHub, etc.). The average enterprise uses 130+ SaaS tools. Employees spend **3.6 hours per day** searching for information, and 44% of the time they cannot find what they need. This results in duplicated work, slow onboarding, delayed decisions, and institutional knowledge loss when employees leave.

### Who has this problem?

- **Primary persona:** Knowledge workers in mid-market and enterprise organizations (500+ employees)
- **Sweet spot:** Fortune 500 / Global 2000 with complex, multi-tool environments
- **Buyer:** CIO/IT (platform deployment), line-of-business leaders (assistant/agent use cases)
- **Verticals:** 50+ industries — telecom, banking, retail, travel, manufacturing, semiconductors, technology

### How are they solving it today without Glean?

1. **Manual search:** Employees open each app separately and search within it (Slack search, Google Drive search, Jira search) — slow and fragmented
2. **Microsoft 365 Copilot / Microsoft Search:** For Microsoft-ecosystem-heavy shops, bundled search and AI assistant — limited to Microsoft data sources
3. **Google Cloud Search:** For Google Workspace shops — limited to Google ecosystem
4. **Custom solutions:** Elasticsearch/OpenSearch deployments requiring significant engineering investment
5. **Knowledge wikis:** Confluence, Notion, Guru — requires manual curation, goes stale
6. **Asking colleagues:** Slack messages, meetings, "who knows about X?" — unscalable, interrupts others

### Vitamin or painkiller?

**Painkiller** — and increasingly a **strategic platform**. Enterprise search was historically a "vitamin" (nice-to-have productivity boost). The AI agent layer transforms it into a painkiller: Glean's Knowledge Graph and permissions-aware retrieval become the **foundational infrastructure** for enterprise AI deployment. As enterprises deploy AI agents that need to access organizational data safely, Glean becomes the context and governance layer that makes this possible. The shift from "search tool" to "enterprise AI platform" is the critical reframing.

---

## 2. Market Size

### 2.1 Top-Down Approach

| Metric | Estimate | Approach | Confidence | Source |
|--------|----------|----------|------------|--------|
| **TAM** | **$32–55B by 2030** | Enterprise search ($8.9–11.2B) + AI knowledge management ($32.2B) + enterprise agentic AI ($24.5B). Significant overlap between categories; de-duplicated TAM reflects the converging market for AI-powered enterprise knowledge and work platforms. | Medium | [Grand View Research](https://www.grandviewresearch.com/industry-analysis/enterprise-search-market), [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/enterprise-search-market), [Grand View Research Agentic AI](https://www.grandviewresearch.com/industry-analysis/enterprise-agentic-ai-market-report) |
| **SAM** | **$8–12B by 2030** | AI-powered enterprise search specifically: $6.25B (2024) growing to ~$14.75B (2033) at 10.3% CAGR. Glean's SAM is the subset of enterprise search buyers who (a) have 500+ employees, (b) use multiple SaaS tools, (c) budget for AI-powered solutions. Estimated at ~55-65% of total enterprise search market. | Medium | [Verified Market Reports](https://www.verifiedmarketreports.com/product/ai-enterprise-search-market/), [IMARC Group](https://www.imarcgroup.com/enterprise-search-market) |
| **SOM** | **$1.5–3B by 2030** | Glean's realistic capture: ~15-25% of the AI enterprise search SAM. At $200M ARR (Dec 2025) with ~100% YoY growth, Glean would reach $800M–$1.6B ARR by 2028 if growth decelerates to 50-60% annually (typical for post-$200M scaling). | Medium-Low | Bottom-up projection from current ARR trajectory |

### 2.2 Bottom-Up Approach

**Assumptions:**
- Global 2000 enterprises: ~2,000 companies (primary target)
- Broader enterprise market (500+ employees): ~50,000 companies globally
- Average contract value for Fortune 500: $1–5M/year (confirmed from P1)
- Average contract value for mid-market: $100–500K/year (confirmed from P1)
- Glean currently serves ~200+ enterprise customers (confirmed from P1)

**Calculation:**

| Segment | # Companies | Avg ACV | Segment TAM | Glean Penetration |
|---------|------------|---------|-------------|-------------------|
| Fortune 500 | 500 | $3M/yr | $1.5B | ~2-5% (10-25 customers) |
| Global 2000 (ex-Fortune 500) | 1,500 | $750K/yr | $1.1B | ~1-3% |
| Mid-market (500-2000 employees) | ~25,000 | $150K/yr | $3.75B | <0.5% |
| Upper mid-market (2000-5000 employees) | ~10,000 | $300K/yr | $3.0B | <0.5% |
| **Total bottom-up SAM** | | | **$9.35B** | |

**Cross-check:** Bottom-up SAM of ~$9.35B aligns with top-down SAM estimate of $8–12B. Glean's current $200M ARR represents ~2.1% of this SAM — substantial room for growth, but also indicates the market is early-stage.

---

## 3. Competitive Landscape

### 3.1 Competitor Profiles

| Competitor | Domain | Founded | Funding / Revenue | Key Differentiator | Pricing | Target Overlap with Glean |
|------------|--------|---------|-------------------|-------------------|---------|--------------------------|
| **Microsoft Copilot / M365 Search** | microsoft.com | 1975 | ~$8.6B projected Copilot revenue (FY2026). 400M+ M365 seats. 90% of Fortune 500 using Copilot. | Bundled with existing M365 licenses. Native integration with Microsoft ecosystem. Massive distribution. | $21-30/user/month add-on to M365 | **HIGH** — Direct competitor for M365-heavy enterprises. Biggest distribution advantage of any competitor. |
| **Google Vertex AI Search** | cloud.google.com | 1998 | Google Cloud: $43B+ revenue (FY2025), 28% YoY growth. | Google-quality search applied to enterprise data. Deep Gemini integration. Native for Google Workspace shops. | Consumption-based (per query/document) | **MEDIUM** — Strongest in Google Workspace shops. Less cross-platform than Glean. |
| **Coveo** | coveo.com | 2005 (public: TSX:CVO) | SaaS ARR: ~$142M (FY2026 guidance). 13-15% YoY growth. $172M raised pre-IPO. | ML-driven relevance platform. Strongest in customer-facing search (ecommerce, support). GenAI driving 25-35% of new bookings. | Per-user, enterprise contracts | **MEDIUM** — More customer-facing focus vs. Glean's internal enterprise focus. Overlap in enterprise search infrastructure. |
| **Elastic** | elastic.co | 2012 (public: NYSE:ESTC) | Revenue: $1.68B (FY2026 guidance). Cloud revenue growing 22-24% YoY. | Open-source foundation (Elasticsearch). Infrastructure-level search. RAG/vector search capabilities. Observability + security + search. | Consumption-based (cloud) + self-managed licenses | **MEDIUM-LOW** — Infrastructure layer, not end-user product. Complementary more than competitive. Some enterprises build DIY on Elastic instead of buying Glean. |
| **Algolia** | algolia.com | 2012 | $335M raised. $2.25B valuation (2021). Revenue estimated $100-250M. 18,000+ customers. | API-first search. Developer-focused. Fastest implementation. Strong in ecommerce/consumer search. | Usage-based (search requests) | **LOW-MEDIUM** — Developer/ecommerce focus vs. Glean's enterprise knowledge focus. Moving toward agentic AI retrieval in 2026. |
| **Lucidworks** | lucidworks.com | 2007 | $178M raised. Revenue estimated $25-100M. | Apache Solr/Fusion-based. Commerce and workplace search. Retail/ecommerce strength. | Enterprise licenses | **LOW-MEDIUM** — More commerce-focused. Less AI-native. Shrinking competitive overlap. |
| **Guru (by Getguru)** | getguru.com | 2015 | $90M+ raised. Acquired by Bonterra (2023). | Knowledge base + verification workflows. Browser extension delivery. Knowledge accuracy focus. | Per-user ($5-20/user/month) | **MEDIUM** — Competes for knowledge management budget. Simpler product, lower price point, smaller scale. |
| **Dust** | dust.tt | 2023 | $21.5M raised (Sequoia). $7.3M ARR (mid-2025). 66 employees. | Open-source AI assistant + agent builder. Enterprise data connections. Focuses on AI agents, not just search. | Pro: $19/user/month, Enterprise: custom | **MEDIUM** — Emerging competitor in AI assistant/agent space. Much earlier stage. Sequoia-backed like Glean. |
| **GoSearch** | gosearch.ai | 2022 | Limited funding data available. | Lower TCO, faster deployment (<1 week). Hybrid search. Pre-built connectors. | Per-user, lower than Glean | **MEDIUM** — Positioned specifically as Glean alternative. Competes on price and deployment speed. |

### 3.2 Competitive Analysis

**Tier 1 Threats (significant competitive pressure):**
- **Microsoft Copilot** — The 800-lb gorilla. 400M+ M365 seats, 90% Fortune 500 adoption, bundled pricing. Microsoft's strategy is "good enough AI for free (or cheap)" — CIOs may not justify a separate Glean license when Copilot comes with their existing M365 contract. However, Copilot is Microsoft-ecosystem-only; Glean's cross-platform (100+ connectors) story is the primary defense.
- **Google Vertex AI Search** — For Google Workspace enterprises, Vertex AI Search with Gemini offers similar RAG capabilities. Less of a threat than Microsoft because Google Workspace has lower enterprise market share than M365.

**Tier 2 Threats (competitive pressure):**
- **Coveo** — Public company, profitable trajectory, strong in regulated industries. Different focus (customer-facing vs. internal), but converging toward the same "AI-powered enterprise relevance" market.
- **Elastic** — At $1.68B revenue, Elastic is 8x Glean's size. Primarily infrastructure, but increasingly building end-user-facing search experiences. The "build vs. buy" decision with Elastic is a real competitor to Glean deals.

**Tier 3 Threats (emerging/niche):**
- **Dust, GoSearch, Guru** — Smaller players attacking from below. Lower price points, faster deployment. Could erode Glean's mid-market opportunity before it gets there.

---

## 4. SWOT Analysis

### Strengths

| Strength | Evidence | Impact |
|----------|----------|--------|
| **Explosive revenue growth** | $100M to $200M ARR in 9 months (100%+ growth). $1M+ contracts tripled. | Demonstrates strong product-market fit and enterprise demand. Approaching IPO-ready scale. |
| **Elite founding team** | Four ex-Google engineers. CEO Arvind Jain = Google Distinguished Engineer + Rubrik co-founder (public company). | Deep search expertise + proven ability to scale enterprise companies. Investor confidence signal. |
| **Proprietary Knowledge Graph** | Maps people, content, activity, and permissions across 100+ connectors. | Core moat — network effects improve with usage. Extremely difficult to replicate. |
| **Model-agnostic architecture** | Supports Claude, Gemini, GPT — no LLM lock-in. | Reduces vendor risk for enterprise buyers. Strategic advantage as LLM market shifts. |
| **Permissions-aware retrieval** | Respects source-system ACLs (access control lists). | Critical for enterprise security/compliance. Key differentiator vs. simpler RAG solutions. |
| **Tier-1 investor syndicate** | Sequoia, Lightspeed, Kleiner Perkins, General Catalyst, Wellington, Altimeter, DST Global. | Access to capital, strategic advice, and customer introductions. $765M+ war chest. |
| **Platform expansion (search -> assistant -> agents)** | Three product pillars with increasing TAM. On pace for 1B agent actions by end of 2025. | Expands addressable market beyond search into the $7-24B agentic AI market. |
| **High engagement** | 40% wDAU/wMAU (2x SaaS industry benchmark). 5 queries/day per employee. | Indicates genuine utility, not shelfware. Strong foundation for land-and-expand. |

### Weaknesses

| Weakness | Evidence | Impact |
|----------|----------|--------|
| **No public pricing** | Enterprise-only pricing model. Minimum ~$50-60K/year. | Excludes SMB market entirely. Creates friction in sales cycle. Allows competitors to undercut on transparency. |
| **Complex deployment** | IT departments face challenges with data access requirements, connector setup, and rollout. 4-5 month sales cycles. | Slows growth compared to product-led growth competitors. Limits ability to scale downmarket. |
| **GCP dependency** | Hosted entirely on Google Cloud Platform. | Single-cloud concentration risk. May concern AWS/Azure-first enterprises. |
| **Burn rate concerns** | ~1,400 employees at $200M ARR = ~$140K revenue per employee. Likely spending $250-350M annually. | Cash burn is sustainable with $765M raised, but path to profitability unclear. Pre-IPO investors need a clear unit economics story. |
| **No public NRR data** | Churn already emerging from "experimental AI budgets." | If NRR is below 120%, it signals expansion challenges. Lack of disclosure is a yellow flag. |
| **Late to international markets** | India office (2024), but no Europe/EMEA office announced. | European enterprises have data residency requirements (GDPR). Missing EU presence limits SAM capture. |
| **In-house model strategy creates tension** | Moving toward proprietary models while claiming model-agnostic positioning. | May concern LLM vendors (Anthropic, OpenAI, Google) who are also partners. Mixed messaging. |

### Opportunities

| Opportunity | Rationale | Potential Impact |
|-------------|-----------|------------------|
| **Agentic AI platform play** | Enterprise agentic AI market: $2.6B (2024) to $24.5B (2030) at 46% CAGR. Glean already has 100+ built-in agent actions. Gartner predicts 40% of enterprise apps will have AI agents by 2026, up from <5% in 2025. | Could 3-5x Glean's TAM from search alone. Agents require the context + governance layer that Glean already provides. |
| **On-premises / hybrid deployment** | Dell partnership (May 2025) enables regulated industries (government, healthcare, financial services). | Opens sovereign/regulated market segments that were previously inaccessible. |
| **IPO window (2026-2027)** | $200M+ ARR, 100%+ growth, $7.2B valuation, secondary market trading. | IPO would provide growth capital, public currency for acquisitions, and employee retention. |
| **European expansion** | No EU office yet. EU enterprises have strong demand for data-sovereign AI solutions. | Could add $1-2B to SAM if Glean establishes EU data residency. |
| **Vertical-specific solutions** | 50+ industries served generically. Vertical AI agents (legal, healthcare, financial) command premium pricing. | Vertical specialization increases ACV and reduces competitive substitution. |
| **MCP protocol / interoperability** | Remote MCP Server already launched. Positions Glean as enterprise context provider for any AI system. | Becomes the "enterprise memory layer" for third-party AI tools. Platform lock-in via integration rather than product. |

### Threats

| Threat | Severity | Likelihood | Rationale |
|--------|----------|------------|-----------|
| **Microsoft Copilot bundling** | **Critical** | **High** | 90% Fortune 500 already using Copilot. Microsoft can subsidize AI search at $0 marginal cost. "Good enough" for many enterprises. Glean must prove 100+ connector cross-platform value exceeds switching cost. |
| **LLM commoditization** | **High** | **Medium-High** | As LLMs become commodity, the AI assistant layer loses differentiation. Glean's moat depends on the Knowledge Graph and connectors, not the AI model itself. |
| **Enterprise AI budget rationalization** | **High** | **Medium** | CEO Arvind Jain acknowledged churn from "experimental AI budgets." As AI hype normalizes, enterprises will demand concrete ROI. Only 19% of executives report >5% revenue increase from GenAI investments. |
| **Google Workspace + Gemini convergence** | **Medium** | **Medium** | Google could integrate Vertex AI Search natively into Workspace, making it "free" for Google shops. Lower threat than Microsoft (smaller enterprise footprint). |
| **Elastic moving upstack** | **Medium** | **Medium** | At $1.68B revenue, Elastic has resources to build end-user search experiences. Their RAG/vector capabilities are mature. "Build on Elastic" vs. "buy Glean" is a live decision. |
| **Economic downturn** | **Medium** | **Medium** | Enterprise software budgets are cyclically sensitive. $50K+ minimum contracts are discretionary spend in a downturn. |
| **Data privacy / regulatory risk** | **Medium** | **Low-Medium** | Glean ingests data from 100+ enterprise tools. A data breach or compliance failure would be catastrophic to trust. EU AI Act and data residency requirements add compliance burden. |
| **Emerging low-cost competitors** | **Low-Medium** | **Medium** | GoSearch, Dust, and others attack from below with faster deployment and lower TCO. Could capture mid-market before Glean scales down. |

---

## 5. Competitive Positioning

### Positioning Matrix

Axes:
- **X-axis: Completeness of Vision** (strategy, innovation, market understanding, platform breadth)
- **Y-axis: Ability to Execute** (product quality, revenue scale, growth rate, operations)

| Company | Vision (1-10) | Execution (1-10) | Rationale |
|---------|---------------|-------------------|-----------|
| **Glean** | **9** | **8** | Strongest vision: search + assistant + agents + enterprise graph + MCP. Execution: $200M ARR, 100% growth, 1,400 employees. Loses 1 point on vision for unclear in-house model strategy. Loses 2 on execution for no profitability path shown and limited international presence. |
| **Microsoft Copilot** | **8** | **9** | Vision: Full enterprise AI across M365, but Microsoft-ecosystem-only limits completeness. Execution: 400M+ M365 seats, 90% Fortune 500 adoption, massive engineering resources. Loses 2 on vision for ecosystem lock-in limitation. |
| **Google Vertex AI Search** | **7** | **7** | Vision: Google-quality search for enterprise, Gemini integration, RAG Engine. Execution: Google Cloud growing 28% YoY, but Vertex AI Search is one product among many — not Google's primary focus. Enterprise search is a feature, not a company. |
| **Coveo** | **6** | **7** | Vision: AI-powered relevance platform expanding from customer-facing to internal search. Limited agent/assistant story. Execution: Public company, $142M SaaS ARR, profitable trajectory, steady 13-15% growth. Solid but unspectacular. |
| **Elastic** | **6** | **8** | Vision: "Search AI Company" positioning, but still fundamentally infrastructure. Agent/assistant vision is emerging. Execution: $1.68B revenue, public company, dominant in infrastructure search. Massive installed base. |
| **Algolia** | **5** | **6** | Vision: API-first search expanding to agentic retrieval. Still primarily developer/ecommerce focused. Execution: $100-250M revenue estimate, 18K customers, but growth has slowed since 2021 peak valuation. |
| **Dust** | **8** | **3** | Vision: Open-source AI assistant + agent builder with enterprise data. Strong vision but very early. Execution: $7.3M ARR, 66 employees. Impressive efficiency but orders of magnitude behind Glean. |
| **GoSearch** | **5** | **3** | Vision: Faster, cheaper Glean alternative. Narrow vision. Execution: Early stage, limited public data on scale. |

### Quadrant Summary

```
                        HIGH EXECUTION
                              |
           Microsoft Copilot  |
                    (8,9)     |
                              |
              Elastic (6,8)   |  Glean (9,8)
                              |
          Coveo (6,7)         |
    Google Vertex (7,7)       |
                              |
LIMITED ──────────────────────+────────────────────── COMPLETE
VISION        Algolia (5,6)   |                       VISION
                              |
                              |
              GoSearch (5,3)  |  Dust (8,3)
                              |
                              |
                        LOW EXECUTION
```

**Glean occupies the "Leader" quadrant** — highest completeness of vision with strong (but not highest) execution. Microsoft leads on execution but is constrained by ecosystem vision. Dust has strong vision but lacks execution scale.

---

## 6. Market Dynamics

### Key Trends

1. **Enterprise AI search is converging with AI agents.** The market is shifting from "find information" to "take action on information." Glean's search -> assistant -> agent evolution tracks this trend. Gartner predicts 40% of enterprise apps will feature AI agents by 2026, up from <5% in 2025. ([Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025))

2. **The "enterprise AI context layer" is becoming a recognized category.** Glean's Feb 2026 TechCrunch positioning as "the layer beneath the interface" signals market recognition of a new platform category — not just search, but the data/governance/permissions infrastructure that makes enterprise AI work. ([TechCrunch](https://techcrunch.com/2026/02/15/the-enterprise-ai-land-grab-is-on-glean-is-building-the-layer-beneath-the-interface/))

3. **Platform bundling is the primary competitive dynamic.** Microsoft and Google can offer "free" or bundled AI search with existing enterprise subscriptions. The key question: is cross-platform, permission-aware, knowledge-graph-powered search valuable enough to justify a separate $50/user/month license? For the Fortune 500 with 130+ SaaS tools, the answer appears to be yes. For smaller enterprises, unclear.

4. **LLM commoditization favors the data/context layer.** As LLMs become interchangeable commodities, the differentiating value shifts to (a) the data/context layer (Glean's Knowledge Graph), (b) the permissions/governance layer, and (c) the connector ecosystem. This is structurally favorable for Glean's positioning.

5. **Enterprise AI ROI scrutiny is intensifying.** Only 19% of executives report >5% revenue increase from GenAI investments. "Experimental AI budgets" are being rationalized. Glean's 40% wDAU/wMAU and 5 queries/day/employee engagement metrics are important defensive evidence, but the bar for proving ROI will rise.

### Regulatory Considerations

- **EU AI Act (2025-2026 enforcement):** Glean's enterprise AI tools may fall under "limited risk" classification requiring transparency obligations. On-premises deployment (Dell partnership) helps address data sovereignty concerns.
- **GDPR / Data Residency:** Glean ingests data from 100+ enterprise tools. EU enterprises require data to remain within EU borders. No EU data center or office announced — a gap.
- **SOC 2 / ISO 27001:** Enterprise-grade compliance is table stakes. Glean has these (verified in P1 security architecture docs).
- **Sector-specific regulation:** Financial services (SEC, FINRA), healthcare (HIPAA), and government (FedRAMP) each have AI-specific compliance requirements that Glean must address for vertical expansion.

### Technology Shifts

- **RAG (Retrieval-Augmented Generation)** has become the standard architecture for enterprise AI — structural tailwind for Glean.
- **MCP (Model Context Protocol)** is emerging as the standard for connecting AI models to enterprise data. Glean's Remote MCP Server is a forward-looking bet.
- **Multi-model / model-agnostic** architecture is becoming the enterprise default. Glean's support for Claude, Gemini, and GPT aligns with this trend.
- **Agentic AI frameworks** (LangChain, CrewAI, AutoGen) are proliferating. Glean's agent builder and 100+ built-in actions compete with (and complement) these open frameworks.

---

## 7. Key Findings

### 1. Glean is at an inflection point between "enterprise search vendor" and "enterprise AI platform."

The $200M ARR milestone and three-pillar product strategy (search + assistant + agents) position Glean to capture a much larger market than enterprise search alone. The enterprise agentic AI market is growing at 46% CAGR to $24.5B by 2030. If Glean succeeds in the platform play, the TAM expands 3-5x. If it remains primarily a search tool, it competes in an $8-11B market against Microsoft's bundling strategy.

### 2. Microsoft Copilot represents significant competitive pressure — but Glean has a defensible counter-position and empirical evidence of coexistence.

90% of Fortune 500 enterprises are using Microsoft Copilot. The bundling risk is real. However, Glean's cross-platform story (100+ connectors vs. Microsoft-only) and superior engagement metrics (40% wDAU/wMAU) suggest the products address different needs. The enterprises that need Glean are those with complex multi-tool environments — which is most large enterprises. The key risk is Microsoft expanding its connector ecosystem or acquiring a cross-platform solution.

### 3. Revenue growth is exceptional, but sustainability is unproven at scale.

Doubling from $100M to $200M ARR in 9 months is elite-tier growth (comparable to early Snowflake, Datadog). However, Glean acknowledged churn from "experimental AI budgets," and with ~1,400 employees the burn rate is likely $250-350M annually. The path to profitability is not yet visible. NRR is not publicly disclosed, which is a notable omission for a company approaching IPO.

### 4. The Knowledge Graph is the real moat — not the AI models.

As LLMs commoditize, Glean's proprietary Knowledge Graph (mapping people, content, activity, and permissions across 100+ data sources) becomes the defensible asset. It improves with usage (network effects), requires deep enterprise integration to replicate, and is foundational for both search and agent use cases. Competitors can swap models; they cannot easily replicate years of connector development and graph construction.

### 5. International expansion and downmarket motion are the untapped growth levers.

Glean is currently North America-focused with an India engineering center but no European office or data center. EU data residency requirements and the EU AI Act create urgency for European expansion. Additionally, the $50K/year minimum contract excludes the vast mid-market opportunity (~25,000 companies globally). Competitors like GoSearch and Dust are positioning for this gap.

---

## Sources

- [Grand View Research — Enterprise Search Market](https://www.grandviewresearch.com/industry-analysis/enterprise-search-market)
- [Mordor Intelligence — Enterprise Search Market](https://www.mordorintelligence.com/industry-reports/enterprise-search-market)
- [Verified Market Reports — AI Enterprise Search Market](https://www.verifiedmarketreports.com/product/ai-enterprise-search-market/)
- [Grand View Research — Enterprise Agentic AI Market](https://www.grandviewresearch.com/industry-analysis/enterprise-agentic-ai-market-report)
- [Gartner — AI Agents Prediction](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025)
- [Fortune — Glean $200M ARR](https://fortune.com/2025/12/08/exclusive-glean-hits-200-million-arr-up-from-100-million-nine-months-back/)
- [BusinessWire — Glean $200M ARR](https://www.businesswire.com/news/home/20251208127913/en/Glean-Surpasses-$200M-in-ARR-for-Enterprise-AI-Doubling-Revenue-in-Nine-Months)
- [TechCrunch — Glean Enterprise AI Land Grab](https://techcrunch.com/2026/02/15/the-enterprise-ai-land-grab-is-on-glean-is-building-the-layer-beneath-the-interface/)
- [CNBC — Glean Series F](https://www.cnbc.com/2025/06/10/glean-gen-ai-search-startup-raises-150-million-at-7-billion-value.html)
- [Business of Apps — Microsoft Copilot Statistics](https://www.businessofapps.com/data/microsoft-copilot-statistics/)
- [Coveo IR — Q3 FY2026 Results](https://ir.coveo.com/en/news-events/press-releases/detail/472/coveo-reports-third-quarter-fiscal-2026-financial-results)
- [Elastic IR — FY2026 Results](https://ir.elastic.co/news/news-details/2025/Elastic-Reports-Second-Quarter-Fiscal-2026-Financial-Results/)
- [Sacra — Glean Revenue & Valuation](https://sacra.com/c/glean/)
- [Mordor Intelligence — Knowledge Management Software Market](https://www.mordorintelligence.com/industry-reports/knowledge-management-software-market)
- [MarketsandMarkets — Agentic AI Market](https://www.marketsandmarkets.com/Market-Reports/agentic-ai-market-208190735.html)
