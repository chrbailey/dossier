# Discovery: okta.com

**Analysis Date:** 2026-02-18
**Analyst:** Automated SaaS Due Diligence (Phase 1)

---

## Company Identity

| Field | Value | Source |
|-------|-------|--------|
| **Legal Name** | Okta, Inc. | [SEC S-1 Filing](https://www.sec.gov/Archives/edgar/data/1660134/000119312517080301/d289173ds1.htm) |
| **Domain** | okta.com | Direct |
| **Founded** | 2009 (as Saasure Inc., CA); reincorporated 2010 as Okta, Inc. (DE) | [SEC Filing](https://www.sec.gov/Archives/edgar/data/1660134/000119312517080301/d289173ds1.htm), [Wikipedia](https://en.wikipedia.org/wiki/Okta,_Inc.) |
| **HQ Location** | San Francisco, California, USA | [Okta Company Page](https://www.okta.com/company/), [LinkedIn](https://www.linkedin.com/company/okta-inc-) |
| **Global Offices** | 15 countries (London, Sydney, Amsterdam, San Jose, Washington DC, Bellevue, others) | [Okta Company Page](https://www.okta.com/company/) |
| **Team Size** | 5,900-7,100 employees (sources vary: PitchBook reports 5,914; other sources report up to 7,064 as of Jan 31, 2026; LinkedIn range: 5,001-10,000) | [LinkedIn](https://www.linkedin.com/company/okta-inc-), [Tracxn](https://tracxn.com/d/companies/okta), [PitchBook](https://pitchbook.com/profiles/company/52633-18) |
| **Funding Status** | Public: NASDAQ: OKTA (IPO April 7, 2017 at $17/share, raised $187M) | [CNBC](https://www.cnbc.com/2017/04/07/okta-ipo-share-price-nasdaq-trading.html), [Crunchbase](https://www.crunchbase.com/organization/okta) |
| **Market Cap** | ~$15.1-15.5 billion (Feb 2026) | [companiesmarketcap.com](https://companiesmarketcap.com/okta/marketcap/), [StockAnalysis](https://stockanalysis.com/stocks/okta/market-cap/) |
| **Stock Price** | ~$82-87 (Feb 17-18, 2026) | [Yahoo Finance](https://finance.yahoo.com/quote/OKTA/), [Benzinga](https://www.benzinga.com/quote/OKTA) |
| **Revenue (FY2025)** | $2.61 billion total (98% subscription); 15% YoY growth | [Okta Investor Relations](https://investor.okta.com/news-and-events/news-releases/news-details/2025/Okta-Announces-Fourth-Quarter-And-Fiscal-Year-2025-Financial-Results/default.aspx) |
| **Revenue Guidance (FY2026)** | $2.875-2.885 billion (10-11% YoY growth); non-GAAP operating margin 25-26% | [Okta Investor Relations](https://investor.okta.com/news-and-events/news-releases/news-details/2025/Okta-Announces-First-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx) |
| **Co-Founders** | Todd McKinnon (CEO, Chairman), Frederic Kerrest (Exec Vice Chairman) | [Okta Leadership](https://www.okta.com/company/leadership/) |
| **Key Executives** | Brett Tighe (CFO), Eric Kelleher (President & COO) | [Okta Leadership](https://www.okta.com/company/leadership/) |
| **Pre-IPO Funding** | $228M total over 8 rounds from 15 investors | [Crunchbase](https://www.crunchbase.com/organization/okta) |
| **Key Investors** | Sequoia Capital (19%), Andreessen Horowitz (17%), Greylock Partners (15%) — at-IPO stakes | [Crunchbase](https://www.crunchbase.com/organization/okta/company_financials) |
| **Key Acquisition** | Auth0 — $6.5B stock deal, closed May 2021 (Customer Identity / developer-first) | [Auth0 Blog](https://auth0.com/blog/okta-acquisition-announcement/), [Fortune](https://fortune.com/2021/05/03/okta-auth0-deal-stock-login-acquisition/) |

### Primary Product Description

Okta is a cloud-native identity and access management (IAM) platform that secures connections between people and technology. It provides two core clouds: **Workforce Identity Cloud** (SSO, MFA, lifecycle management, identity governance for employees) and **Customer Identity Cloud** (Auth0-powered authentication and authorization for consumer-facing applications). Okta serves as a neutral identity layer that integrates with 7,000+ applications across any technology stack.

### Target Market / ICP

- **Primary buyers:** CISOs, CIOs, IT Directors at mid-market to enterprise organizations
- **Segments:** Enterprise (Fortune 500), mid-market, and developer teams (via Auth0)
- **Industries:** Technology, financial services, healthcare, government, retail, media
- **Notable customers:** Box, JetBlue, PGA of America, LinkedIn, and thousands of enterprise organizations
- **Geographic reach:** Global, with offices in 15 countries

### Key Differentiators

1. **Neutral identity platform** — Works across any cloud, any application, any device (not tied to a specific ecosystem like Microsoft Entra)
2. **Dual identity clouds** — Workforce Identity (top-down enterprise sales) + Customer Identity via Auth0 (developer-first, bottom-up adoption)
3. **Scale and reliability** — 99.99% uptime SLA, processes billions of authentications, cell-based multi-tenant architecture
4. **Integration breadth** — 7,000+ pre-built integrations in the Okta Integration Network (OIN)
5. **AI-native security** — Identity Threat Protection with AI, Identity Security Posture Management (ISPM)

---

## Domain & Infrastructure

> WHOIS and DNS data are being collected in parallel and will be merged separately. See `raw/whois.json` for DNS/WHOIS data when available.

**Known infrastructure signals from web research:**
- Primary cloud: **AWS** (multiple availability zones, ECS, Kubernetes)
- Edge infrastructure: Application Load Balancer + Apache (SSL termination) + Nginx (routing/business logic)
- Cell-based architecture: Each "cell" is a self-contained instance of the entire Okta service for tenant isolation
- CDN usage: Yes (edge caching for performance)
- Developer portal: Hosted at `developer.okta.com` (subdomain)

---

## Digital Footprint

### Social Media & Community Presence

| Platform | Handle/URL | Details | Source |
|----------|-----------|---------|--------|
| **LinkedIn** | [Okta, Inc.](https://www.linkedin.com/company/okta-inc-) | 5,001-10,000 employees listed; active company page with Life, Jobs sections | WebSearch |
| **X (Twitter)** | [@okta](https://x.com/okta) | ~42,500 followers; active posting on identity security, AI, enterprise | WebSearch |
| **X (Developer)** | [@oktadev](https://x.com/oktadev) | ~8,873 followers; developer-focused content | WebSearch |
| **X (Support)** | [@OktaSupport](https://twitter.com/oktasupport) | Customer support channel | WebSearch |
| **GitHub (Corp)** | [github.com/okta](https://github.com/okta) | 87 repositories; SDKs in Java, Go, .NET, Python, Kotlin, Swift, JavaScript | [GitHub](https://github.com/okta) |
| **GitHub (Dev)** | [github.com/oktadev](https://github.com/oktadev) | Developer advocacy org; blog code samples | [GitHub](https://github.com/oktadev) |
| **GitHub (Samples)** | [github.com/okta-samples](https://github.com/okta-samples) | 25 sample app repositories | [GitHub](https://github.com/okta-samples) |

### Review Sites

| Platform | Rating | Reviews | Source |
|----------|--------|---------|--------|
| **Capterra** | 4.7/5.0 | ~905-927 reviews | [Capterra](https://www.capterra.com/p/119653/Okta/reviews/) |
| **Gartner Peer Insights** | N/A (aggregated) | 908 ratings across markets | [Gartner](https://www.gartner.com/reviews/market/identity-governance-administration/vendor/okta) |
| **G2** | Referenced in multiple sources but exact score not confirmed via search | Significant review volume (referenced widely) | WebSearch |

**Review sentiment summary** (across platforms):
- **Strengths:** Intuitive SSO, broad app integrations, robust MFA, centralized identity management, strong compliance capabilities
- **Weaknesses:** High cost at scale for large teams, steep learning curve for admin configuration (SAML/SCIM/OAuth setup), occasional MFA friction, intermittent performance issues
- Sources: [Capterra](https://www.capterra.com/p/119653/Okta/reviews/), [Gartner Peer Insights](https://www.gartner.com/reviews/market/identity-governance-administration/vendor/okta)

### Analyst Recognition

| Report | Position | Source |
|--------|----------|--------|
| **Gartner MQ (Access Management, 2024)** | Leader — #2 in Execution (behind Microsoft), #2 in Vision (behind Ping) | [BankInfoSecurity](https://www.bankinfosecurity.com/microsoft-ping-okta-dominate-access-management-gartner-mq-a-27214) |
| **Forrester Wave (Workforce Identity, 2024)** | Leader — #1 in Current Offering strength | [BankInfoSecurity](https://www.bankinfosecurity.com/microsoft-okta-cyberark-lead-workforce-identity-rankings-a-24783) |
| **Access Management Market** | Market grew 17.6% to $5.85B in 2023; Okta among top 3 vendors | [BankInfoSecurity](https://www.bankinfosecurity.com/microsoft-ping-okta-dominate-access-management-gartner-mq-a-27214) |

### Competitive Landscape

| Competitor | Positioning | Notes |
|-----------|-------------|-------|
| **Microsoft Entra ID** | Primary rival; deep Microsoft ecosystem integration; bundled with M365/Azure | Biggest threat due to bundling advantage |
| **Ping Identity** (+ ForgeRock) | Strong on-prem + cloud hybrid; top vision score in Gartner MQ | Merged by Thoma Bravo (2023) |
| **CyberArk** | PAM specialist expanding into workforce identity | Pure-play public competitor |
| **IBM Security Verify** | Enterprise IAM for IBM ecosystem | Lower market share |
| **OneLogin** | Mid-market alternative | Acquired by One Identity |

---

## Website Analysis

### Homepage Messaging

- **Title:** "Okta | The Identity Standard"
- **Mission statement:** "To enable any organization to use any technology"
- **Vision:** "The World's Identity Company"
- **Primary CTA:** Free trial + contact sales
- **Positioning:** Neutral identity platform (not tied to any single vendor ecosystem)
- **2025-2026 messaging emphasis:** AI agents, identity as the frontline of AI security, ISPM, Identity Threat Protection
- Source: WebSearch on okta.com homepage content

### Pricing Model

**Workforce Identity Cloud:**
| Plan | Price | Target |
|------|-------|--------|
| Starter Suite | $6/user/month | Getting started with identity |
| Essentials Suite | $17/user/month | Scaling identity security |
| Professional Suite | Contact sales | Unified identity at scale |
| Enterprise Suite | Contact sales | Identity-core organizations |

- Billed annually; $1,500 minimum annual contract
- Free trial available

**Customer Identity Cloud (Auth0):**
- Starting at $3,000/month
- Separate product line and pricing from Workforce Identity

Sources: [Okta Pricing](https://www.okta.com/pricing/), [UnderDefense](https://underdefense.com/industry-pricings/okta-pricing-ultimate-guide-for-security-products/), [Spendflo](https://www.spendflo.com/blog/okta-pricing-the-ultimate-guide), [Okta Blog on Simplified Pricing](https://www.okta.com/blog/2025/03/a-new-way-to-buy-okta-simplified-solution-pricing-to-unlock-workforce-identity/)

### Content Strategy (Blog)

- **Two blogs:** Corporate blog (okta.com/blog/) and Developer blog (developer.okta.com/blog/)
- **Frequency:** Multiple posts per week across both blogs
- **Categories:** Threat Intelligence, Product Innovation, Customers & Partners, AI, Engineering, Company & Culture, Industry Insights
- **Current themes (2025-2026):** AI agents and identity security, Auth0 for AI Agents, ISPM, Zero Trust, launch weeks
- **Technical depth:** Mixed — thought leadership, product announcements, and deep engineering posts
- **Developer blog:** Tutorials, SDK guides, protocol deep-dives (OIDC, OAuth, SAML)
- Sources: [Okta Blog](https://www.okta.com/blog/), [Okta Developer Blog](https://developer.okta.com/blog/)

### Developer Documentation

- **Developer portal:** [developer.okta.com](https://developer.okta.com) — comprehensive, well-maintained
- **API reference:** [developer.okta.com/docs/api/](https://developer.okta.com/docs/api/) — Core Okta API + OIDC/OAuth API
- **SDKs:** JavaScript (+ React/Angular/Vue wrappers), Java, .NET, Go, Python, Kotlin (Android), Swift (iOS)
- **Protocols:** OAuth 2.0, OpenID Connect, SAML 2.0, SCIM
- **Quick starts:** Yes
- **Community:** Active developer community, forum presence
- Source: [developer.okta.com](https://developer.okta.com/code/)

---

## Tech Stack Signals

| Technology | Confidence | Signal Source |
|-----------|------------|---------------|
| **AWS (primary cloud)** | HIGH | [Architecture blog](https://www.okta.com/blog/2024/08/evolving-oktas-edge-infrastructure/), [whitepaper](https://www.okta.com/resources/whitepaper/how-okta-builds-and-runs-scalable-infrastructure/), job postings |
| **Kubernetes** | HIGH | Job postings, [architecture interview](https://platocommunity.substack.com/p/unpacking-oktas-tech-architecture), edge infra blog |
| **Docker / ECS** | HIGH | Architecture documentation, job postings |
| **Java** | HIGH | Primary SDK language, GitHub repos, job postings |
| **Kotlin** | HIGH | Android SDK (okta-mobile-kotlin), job postings |
| **Go (Golang)** | HIGH | Management SDK, job postings |
| **Python** | MEDIUM | SDK available, job postings for some roles |
| **JavaScript / TypeScript** | HIGH | Auth.js SDK, React/Angular/Vue wrappers, front-end roles |
| **C# / .NET** | HIGH | .NET SDK, ASP.NET middleware |
| **Nginx** | HIGH | Edge routing/business logic layer ([blog](https://www.okta.com/blog/2024/08/evolving-oktas-edge-infrastructure/)) |
| **Apache** | HIGH | SSL termination at edge ([blog](https://www.okta.com/blog/2024/08/evolving-oktas-edge-infrastructure/)) |
| **Elasticsearch** | HIGH | Architecture documentation |
| **Redis** | HIGH | Caching layer, architecture documentation |
| **Amazon Kinesis** | MEDIUM | Data pipeline, architecture documentation |
| **ProxySQL** | MEDIUM | Database layer scaling ([architecture eBook](https://www.okta.com/sites/default/files/2021-04/Okta's%20Architecture-eBook-042020.pdf)) |
| **ReactJS** | MEDIUM | Job postings mention ReactJS for front-end |
| **Node.js** | MEDIUM | Job postings mention NodeJS |
| **Terraform** | HIGH | Official Okta Terraform provider on GitHub |
| **CI/CD (unspecified)** | HIGH | Job postings require CI/CD experience |
| **Microservices architecture** | HIGH | Job postings, architecture blog, cell-based design |

### Architecture Highlights

- **Cell-based multi-tenancy:** Each cell is a self-contained instance of the full Okta service for isolation and scale
- **Edge infrastructure:** 3-layer edge — ALB -> Apache (SSL termination) -> Nginx (routing + business logic)
- **Horizontal scaling:** Read scaling at database layer, auto-scaling groups, efficient caching
- **99.99% uptime SLA:** Achieved 99.9978% in 2020; zero planned downtime policy
- **Tech radar approach:** Internal technology radar governs Principles, Technologies, and Practices
- Sources: [Architecture blog](https://www.okta.com/blog/2024/08/evolving-oktas-edge-infrastructure/), [Architecture interview](https://platocommunity.substack.com/p/unpacking-oktas-tech-architecture), [Architecture eBook](https://www.okta.com/sites/default/files/2021-04/Okta's%20Architecture-eBook-042020.pdf)

---

## Notable Security History

**October 2023 Support System Breach:**
- Threat actor accessed Okta's customer support case management system (Sept 28 - Oct 17, 2023)
- Extracted HAR files containing session tokens; hijacked sessions of 5 customers
- Initially reported as affecting 134 customers; later expanded to include names/emails of all support users
- Independent investigation by Stroz Friedberg confirmed no further malicious activity
- Response: Enhanced monitoring, stricter access controls, admin session timeouts, transparent disclosure
- This is a material risk factor — identity providers are high-value targets
- Sources: [Okta Security](https://sec.okta.com/articles/harfiles/), [BeyondTrust](https://www.beyondtrust.com/blog/entry/okta-support-unit-breach-update), [Nightfall AI](https://www.nightfall.ai/blog/okta-data-breach-what-happened-impact-and-security-lessons-learned)

---

## Key Findings

1. **Okta is the dominant pure-play public identity company** — $2.6B revenue, ~$15B market cap, NASDAQ-listed since 2017. The Auth0 acquisition ($6.5B, 2021) gave them both enterprise (top-down) and developer (bottom-up) go-to-market motions. Only CyberArk remains as a comparable pure-play public IAM vendor.

2. **Microsoft Entra is the existential competitive threat** — Microsoft's bundling of Entra ID with M365/Azure creates significant price pressure. Okta's counter-strategy is platform neutrality (works with any vendor) and depth of identity-specific features. Revenue growth is decelerating (15% in FY2025, guided to 10-11% in FY2026).

3. **AI is the current strategic bet** — Okta is positioning identity as the critical control point for AI agents, with "Auth0 for AI Agents" and Identity Threat Protection with AI. This aligns with the industry trend of AI agents needing managed identity and authorization.

4. **The 2023 security breach is a trust liability** — As an identity provider, a support system breach that exposed session tokens is particularly damaging to brand credibility. Okta's subsequent "Secure Identity Commitment" and enhanced security posture are direct responses, but the incident remains a talking point in competitive deals.

5. **Strong technical moat via integration network** — The Okta Integration Network (OIN) with 7,000+ pre-built connectors, combined with comprehensive SDKs across 7+ languages and support for all major identity protocols (OAuth, OIDC, SAML, SCIM), creates significant switching costs.

---

## Open Questions

- **Exact current employee count:** Sources range from 5,914 to 7,064 — unclear if recent layoffs or restructuring have occurred in FY2026. SEC 10-K filing would provide authoritative number.
- **Customer count:** Total number of paying customers not confirmed through web search. Okta previously reported 19,300+ customers (FY2024); current number needs investor relations data.
- **G2 exact rating and review count:** Unable to confirm specific G2 score through web search; direct G2 page access needed.
- **Net revenue retention rate:** Critical SaaS metric not found in web search results; available in earnings reports.
- **Auth0 revenue contribution:** Breakdown between Workforce Identity and Customer Identity revenue not publicly disclosed at granular level.
- **Churn/competitive loss data:** Market share trends vs. Microsoft Entra not quantified.
- **DNS/WHOIS details:** Being collected in parallel — see raw/whois.json.
- **Security posture post-2023:** Extent of security investments and whether any additional incidents have occurred since the Oct 2023 breach.
