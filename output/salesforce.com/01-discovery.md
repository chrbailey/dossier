# Discovery: salesforce.com

## Company Identity

| Field | Value | Source |
|-------|-------|--------|
| **Legal Name** | Salesforce, Inc. (formerly Salesforce.com, Inc.) | WHOIS registrant org |
| **Domain** | salesforce.com | Target |
| **Founded** | March 8, 1999 | Salesforce company page, Wikipedia |
| **Founders** | Marc Benioff, Parker Harris, Dave Moellenhoff, Frank Dominguez | Wikipedia, Salesforce newsroom |
| **CEO** | Marc Benioff (Chair, CEO & Co-Founder) | Salesforce.com/company |
| **HQ** | Salesforce Tower, 415 Mission Street, 3rd Floor, San Francisco, CA 94105 | WHOIS record |
| **Employees** | ~76,453 (as of Jan 2026) | LinkedIn / Tracxn |
| **Public Company** | NYSE: CRM (IPO June 23, 2004 at $11/share) | Wikipedia, Yahoo Finance |
| **Market Cap** | ~$185.83B (March 2026) | CompaniesMarketCap |
| **FY2026 Revenue** | $41.53B (+9.58% YoY) | Stock Analysis, Salesforce earnings |
| **FY2025 Revenue** | $37.9B (record year) | Salesforce earnings |
| **CRM Market Share** | 23.9% — #1 globally for 12 consecutive years (IDC) | IDC via Salesforce newsroom |
| **Customers** | 150,000+ companies worldwide | Salesforce company page |
| **Primary Product** | Cloud-based CRM platform (Sales, Service, Marketing, Commerce, Platform) | Homepage |
| **Positioning** | "The #1 AI CRM" — enabling "Agentic Enterprises" where humans and AI agents collaborate | Homepage meta description |
| **Target Market** | Enterprise and mid-market B2B across all industries; expanding to SMB via Starter Suite | Pricing pages, product portfolio |
| **Key Differentiators** | Platform breadth (CRM + Data + AI + Slack), Agentforce AI agents, AppExchange ecosystem, Trust/compliance posture, 1-1-1 philanthropy model | Homepage, company page |
| **Core Values** | Trust, Customer Success, Innovation, Equality, Sustainability | Company page |

## Domain & Infrastructure

### WHOIS Summary

| Field | Value |
|-------|-------|
| Registrar | MarkMonitor, Inc. |
| Created | 1998-12-02 |
| Expires | 2026-10-21 |
| Updated | 2024-09-19 |
| Registrant Org | Salesforce.com, Inc. |
| Registrant Contact | Domain Adminstrator |
| DNSSEC | signedDelegation |
| Status | Full lock (clientDeleteProhibited, clientTransferProhibited, clientUpdateProhibited + server-side equivalents) |

**Analysis:** Domain registered December 1998, three months before the company's March 1999 founding. MarkMonitor is an enterprise-grade registrar used by Fortune 500 companies. Full client+server lock status and DNSSEC indicate mature domain security posture. Expiration in October 2026 — within 8 months — is notable but typical for large enterprises that renew annually.

### Nameservers

- `udns1.salesforce.com` through `udns4.salesforce.com` — self-hosted authoritative DNS (UltraDNS)
- `pch1.salesforce-dns.com`, `pch2.salesforce-dns.com` — Packet Clearing House anycast DNS

**Analysis:** Salesforce operates its own authoritative nameservers (via Neustar/UltraDNS) plus PCH anycast for resilience. This is enterprise-grade DNS infrastructure consistent with a company running critical SaaS services globally.

### A Records

Multiple IPs across Akamai CDN ranges:
- `23.1.35.132`, `23.1.99.130`, `23.1.106.133`
- `104.109.10.129`, `104.109.11.129`
- `184.25.179.132`, `184.31.3.130`, `184.31.10.133`

**Analysis:** All IPs resolve to Akamai's CDN network. Salesforce uses Akamai as its primary CDN and web acceleration layer for the marketing site. Salesforce help documentation confirms Akamai is their included CDN provider.

### MX Records

- `10 mxa-00177002.gslb.pphosted.com.`
- `10 mxb-00177002.gslb.pphosted.com.`

**Analysis:** Proofpoint-hosted email (pphosted.com). Proofpoint is an enterprise email security gateway — consistent with a security-conscious large enterprise. Equal priority (10) indicates active-active mail routing.

### TXT Records (Notable)

| Record | Significance |
|--------|-------------|
| `v=spf1 include:_spf.google.com include:_spf.salesforce.com ...` | SPF: Google Workspace + Salesforce's own mail infrastructure |
| `DirectFedAuthUrl=https://salesforce.okta.com/...` | Okta for SSO/federation |
| `pardot1=...`, `pardot220122=...` | Pardot (Salesforce's own B2B marketing automation) |
| `stripe-verification=...` (4 records) | Stripe payment integration — multiple verification entries suggest complex billing setup |
| `hubspot-developer-verification=...` | HubSpot developer integration (likely AppExchange connector) |
| `atlassian-domain-verification=...` | Atlassian (Jira/Confluence) integration |
| `docker-verification=...` | Docker Hub organization verification |
| `google-site-verification=...` (8 records) | Extensive Google property verification (Search Console, multiple properties) |
| `zoom-domain-verification=...` (2 records) | Zoom integration |
| `tiktok-developers-site-verification=...` | TikTok developer integration |
| `cloudhealth=...` | CloudHealth (VMware) cloud cost management |
| `vmware-cloud-verification=...` | VMware Cloud integration |
| `jamf-site-verification=...` | Jamf (Apple device management) |
| `mixpanel-domain-verify=...` | Mixpanel analytics |
| `canva-site-verification=...` | Canva integration |
| `liveramp-site-verification=...` | LiveRamp data connectivity |
| `remarkable-domain-verification=...` | reMarkable integration |
| `neat-pulse-domain-verification=...` | Neat (video conferencing hardware) |
| `SFMC-...` | Salesforce Marketing Cloud verification |

**Analysis:** The TXT record footprint reveals an enormous internal toolchain: Google Workspace for email, Okta for SSO, Stripe for payments, Atlassian for project management, Docker for containers, Jamf for device management, Mixpanel for analytics, CloudHealth/VMware for cloud ops, and integrations with TikTok, Zoom, Canva, LiveRamp, and more. The 4 separate Stripe verification records suggest multiple Stripe accounts or complex billing entities. 8 Google site verifications indicate numerous web properties under the same domain.

## Digital Footprint

### Social Media Presence

| Platform | Handle/URL | Key Metrics | Source |
|----------|-----------|-------------|--------|
| **LinkedIn** | [linkedin.com/company/salesforce](https://www.linkedin.com/company/salesforce) | 10,001+ employees listed; global offices (SF, Zurich, Singapore, Tokyo, Munich, Milan) | LinkedIn |
| **X (Twitter)** | [@salesforce](https://x.com/salesforce) | ~585.2K followers; active posting about Agentforce, Dreamforce | WebSearch |
| **GitHub** | [github.com/salesforce](https://github.com/salesforce) | 404 repositories; notable: LWC (1.7K stars), Cloudsplaining (2.2K stars) | GitHub |
| **GitHub (additional)** | [github.com/developerforce](https://github.com/developerforce) | 31 repos — developer-focused samples and tools | GitHub |
| **GitHub (additional)** | [github.com/SalesforceFoundation](https://github.com/SalesforceFoundation) | 37 repos — Salesforce.org open source | GitHub |

### Review Sites

| Platform | Rating | Details | Source |
|----------|--------|---------|--------|
| **G2** | #1 vendor (2026 Best Software Awards) | 6 separate #1 rankings; #1 in Winter 2026 reports | G2 via Yahoo Finance |
| **G2 (Sales Cloud)** | High ratings | Praised for automation, customization; criticized for learning curve | G2 |
| **G2 (Service Cloud)** | High ratings | Praised for case management, macros; licensing cost concerns | G2 |
| **Capterra (Sales Cloud)** | 4.4/5 stars | Value for money: 4.29/5; strong on tracking and integration | Capterra |
| **Capterra (Marketing Cloud)** | 524 verified reviews | Detailed review corpus available | Capterra |

### Community Presence

- **Trailhead** — proprietary learning platform with gamified training, certifications, and community (Trailblazers)
- **AppExchange** — marketplace for third-party apps and integrations
- **Dreamforce** — annual conference (one of the largest tech conferences globally)
- **Developer community** — developer.salesforce.com with 400+ YouTube technical sessions, monthly newsletters, Agentforce NOW events

## Website Analysis

### Homepage Messaging (salesforce.com)

- **Title:** "Salesforce: The #1 AI CRM"
- **Primary H1:** "Welcome to the Agentic Enterprise."
- **Sub-headline:** "Where humans and agents drive customer success together."
- **Social proof:** "3M+ conversations handled by Agentforce and counting"
- **Product pillars (main nav):** Slack, Agentforce, Customer 360, Data 360

The homepage is entirely oriented around the "Agentic Enterprise" concept — positioning AI agents (Agentforce) as the next evolution of CRM. The language has shifted from traditional CRM terminology to agent-centric framing.

### Pricing Model

Salesforce uses a **per-user, per-month** pricing model, billed annually:

| Tier | Price (USD/user/month) | Target |
|------|----------------------|--------|
| **Starter Suite** | $25 | SMB, bundled CRM |
| **Enterprise** | $175 | Mid-market / Enterprise |
| **Unlimited** | $350 | Large enterprise |
| **Agentforce 1** | $550 | AI-forward enterprise |

- **August 2025 update:** 6% price increase across Enterprise and Unlimited editions (Sales Cloud, Service Cloud, Field Service, Industry Clouds)
- Contracts are primarily annual; Starter allows monthly
- Free trial available (non-production only)
- Specific pricing requires contacting sales for many products

**Analysis:** The pricing ladder is designed to upsell from SMB ($25) through enterprise ($175-$350) to AI-premium ($550). The Agentforce tier at $550/user/month represents a significant AI premium. The 6% 2025 price increase signals pricing power and confidence in retention.

### Content Strategy (Blog)

- **Frequency:** Daily to near-daily publication
- **Dominant theme:** Agentic AI (AI agents, enterprise AI adoption, workforce transformation)
- **Content types:** Thought leadership, product education, industry-specific guides, trend analysis
- **Recent titles include:** "We've Reached Peak LLM," "Beyond the AI Hype: Five Trends That Will Transform Business in 2026," "Why CRM Is the Trusted Foundation of the Agentic Enterprise"
- **Positioning:** Salesforce as the authoritative voice on enterprise AI transformation

### Developer Portal (developer.salesforce.com)

- **9 developer centers:** Agentforce, Platform, Data Cloud, Marketing Cloud, Service Cloud, Commerce Cloud, MuleSoft, Tableau, Slack
- **Key new offerings:** Agentforce Vibes ("enterprise vibe coding"), Agent Script framework, Python SDK for agents
- **APIs:** REST API, B2C Commerce API, Marketing Cloud APIs (REST + SOAP), Metadata API
- **Community resources:** 400+ YouTube technical sessions, monthly newsletters, Agentforce NOW events

## Tech Stack Signals

### Confirmed Technologies (High Confidence)

| Technology | Evidence | Confidence |
|-----------|----------|------------|
| **Java** | Job postings explicitly require Java; Salesforce's core platform is Java-based (confirmed by multiple sources) | Very High |
| **Apex** | Salesforce's proprietary strongly-typed language for platform development; referenced across developer docs | Very High |
| **Lightning Web Components (LWC)** | 1,755 GitHub stars; core UI framework for Salesforce platform | Very High |
| **Python** | New Agentforce SDK; job postings for DevOps/SRE roles | Very High |
| **Kubernetes** | Job postings require K8s experience; production engineering roles building K8s environments | Very High |
| **AWS** | Job postings: "Senior Software Engineer - Java, AWS"; production infrastructure on AWS/GCP/Azure | Very High |
| **GCP / Azure** | Production engineering roles mention multi-cloud (AWS/GCP/Azure) | High |
| **Docker** | Docker Hub domain verification in DNS TXT; job postings mention containerization | High |
| **Terraform** | Job postings for DevOps require Terraform / Infrastructure-as-Code | High |
| **Akamai CDN** | DNS A records resolve to Akamai; Salesforce docs confirm Akamai as CDN provider | Very High |
| **Proofpoint** | MX records point to pphosted.com (Proofpoint) | Very High |
| **Google Workspace** | SPF record includes `_spf.google.com` | Very High |
| **Okta** | TXT record: `DirectFedAuthUrl=https://salesforce.okta.com/...` | Very High |
| **Stripe** | 4 Stripe verification TXT records | Very High |
| **Heroku** | Salesforce-owned PaaS; AppLink GA in 2025; polyglot container-based platform | Very High |
| **PostgreSQL** | Heroku Postgres is the database for Heroku-based services; Heroku Connect syncs to Postgres | High |
| **Splunk** | Job postings for DevOps require Splunk | High |
| **HashiCorp Vault** | Job postings mention Vault for secrets management | High |
| **React.js** | Job postings for "Fullstack (Java + React.JS)" roles | High |
| **Node.js** | Heroku AppLink SDK supports Node.js; developer tooling | High |

### Inferred Technologies (Medium Confidence)

| Technology | Evidence | Confidence |
|-----------|----------|------------|
| **Oracle Database** | Legacy core platform likely still uses Oracle; Marc Benioff came from Oracle | Medium |
| **Elasticsearch** | Common at Salesforce's scale for search; not directly confirmed | Medium |
| **Kafka / Event Streaming** | Platform Events and Change Data Capture features suggest event streaming infrastructure | Medium |
| **Redis / Caching** | Scale of operations implies distributed caching layer | Medium |
| **Go/Golang** | Job postings mention Python/Golang/Node.js for infrastructure roles | Medium |

### Platform Products (Acquired)

| Product | Acquisition Year | Price | Technology |
|---------|-----------------|-------|------------|
| **Slack** | 2021 | $27.7B | Messaging/collaboration platform |
| **Tableau** | 2019 | $15.3B | Data visualization / analytics |
| **MuleSoft** | 2018 | $6.5B | API integration platform |
| **Informatica** | 2025 (announced) | ~$8B | Data management / governance |
| **Heroku** | 2010 | $212M | PaaS (polyglot cloud hosting) |

## Key Findings

1. **Salesforce is the undisputed CRM market leader** — 23.9% global market share (IDC #1 for 12 consecutive years), $41.53B FY2026 revenue, ~$186B market cap. Their nearest competitor (Microsoft Dynamics) earns roughly 4x less CRM revenue.

2. **The company is executing a full strategic pivot to "Agentic AI"** — every customer-facing property (homepage, blog, developer portal, pricing) has been reoriented around Agentforce and the "Agentic Enterprise" concept. The $550/user/month Agentforce tier represents a massive AI premium. Agentforce ARR grew 82% in 6 months to $800M.

3. **Infrastructure maturity is enterprise-grade** — self-hosted DNS (UltraDNS + PCH anycast), Akamai CDN, Proofpoint email security, Okta SSO, full DNSSEC and domain lock. The TXT record footprint reveals integration with 20+ enterprise tools (Stripe, Atlassian, Docker, Jamf, Mixpanel, etc.).

4. **The tech stack is Java-centric with aggressive modernization** — core platform is Java/Apex/Oracle, but job postings show heavy investment in Kubernetes, AWS/GCP multi-cloud, Python (Agentforce SDK), React, and Infrastructure-as-Code. The Heroku AppLink expansion (Node.js, Python) signals a push toward polyglot development.

5. **Acquisition strategy drives platform breadth** — $50B+ in major acquisitions (Slack, Tableau, MuleSoft, Informatica) have built a comprehensive data + collaboration + integration + AI platform. This breadth is both a competitive moat and a complexity risk.

## Open Questions

- **Agentforce adoption trajectory** — $800M ARR is strong but what is the net-new vs. upsell mix? Are customers actually deploying agents or just buying licenses?
- **Multi-cloud infrastructure split** — job postings mention AWS/GCP/Azure but the actual distribution and migration trajectory is unclear. What percentage runs on Salesforce's own data centers vs. hyperscalers?
- **Technical debt** — how much of the core platform still runs on legacy Java/Oracle architecture vs. modernized microservices? The Heroku AppLink push suggests they are trying to break free of Apex-only constraints.
- **Pricing pressure** — the 6% price increase in August 2025 and $550 Agentforce tier may face pushback. What is the churn rate at the Enterprise/Unlimited tiers?
- **Informatica integration risk** — the ~$8B Informatica acquisition (announced June 2025) is a major integration challenge on top of still-digesting Slack and Tableau.
- **Competitor AI responses** — Microsoft Copilot in Dynamics 365, HubSpot's AI features, and Oracle's AI initiatives are all targeting the same "AI CRM" positioning. How defensible is Salesforce's Agentforce moat?
- **Employee headcount trajectory** — ~76K employees after significant layoffs in 2023. Is the current headcount stable, growing, or still being optimized?
- **Data Cloud adoption** — Data 360 / Data Cloud is positioned as a major product pillar alongside Agentforce. What is the actual adoption and revenue contribution?

---

*Phase 1 Discovery completed 2026-03-05. All facts sourced from WHOIS records, DNS queries, Salesforce.com web properties, and public web search results.*
