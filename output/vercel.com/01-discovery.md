# Vercel — Phase 1: Discovery Report

**Date:** 2026-02-18
**Domain:** vercel.com
**Analyst method:** WebSearch only (Bash and WebFetch denied in this environment; WHOIS script and DNS dig commands could not be executed)

---

## Company Identity

| Field | Value | Source |
|-------|-------|--------|
| Legal name | Vercel Inc. | [Vercel DPA](https://vercel.com/legal/dpa), [Justia Trademark](https://trademarks.justia.com/901/49/vercel-90149383.html) |
| Former name | ZEIT (rebranded April 2020) | [Vercel blog](https://vercel.com/blog/zeit-is-now-vercel) |
| Incorporation | Delaware corporation | [Vercel legal](https://vercel.com/legal/dpa) |
| Founded | 2015 | [Wikipedia](https://en.wikipedia.org/wiki/Vercel), [Crunchbase](https://www.crunchbase.com/organization/vercel) |
| Headquarters | San Francisco, California | [LinkedIn](https://www.linkedin.com/company/vercel), [Tracxn](https://tracxn.com/d/companies/vercel/__uPuJfXzfvAQs0wmUuqRiXFxW4uGbcaKUHjHks8VPbrI) |
| CEO | Guillermo Rauch (founder) | [Crunchbase](https://www.crunchbase.com/person/guillermo-rauch) |
| CTO | Malte Ubl | [The Org](https://theorg.com/org/vercel/teams/leadership-team) |
| Employees | ~823-874 (late 2025 estimates) | [Getlatka](https://getlatka.com/companies/vercel), [Tracxn](https://tracxn.com/d/companies/vercel/__uPuJfXzfvAQs0wmUuqRiXFxW4uGbcaKUHjHks8VPbrI) |
| Industry | Cloud Infrastructure / Developer Tools / AI | [LinkedIn](https://www.linkedin.com/company/vercel) |
| Primary product | Frontend Cloud platform (deploy, scale, secure web apps) | [Vercel homepage](https://vercel.com) |
| Secondary product | v0 — AI-powered full-stack development agent | [Vercel v0](https://v0.app) |
| Key OSS projects | Next.js, Turborepo, SWR, AI SDK | [GitHub](https://github.com/vercel) |
| Target market | Frontend developers (individual to enterprise), AI application builders | [Vercel pricing](https://vercel.com/pricing), [Vercel enterprise](https://vercel.com/enterprise) |
| Key differentiators | Next.js creator advantage, AI-first pivot (v0), Rust-powered serverless, global edge network, developer experience | [Contrary Research](https://research.contrary.com/company/vercel) |

### Funding History

| Round | Date | Amount | Valuation | Lead Investors |
|-------|------|--------|-----------|---------------|
| Series F | Sep 2025 | $300M | $9.3B | Accel, GIC |
| Series E | May 2024 | $250M | $3.25B | Accel |
| Earlier rounds | 2016-2021 | ~$313M total | Various | Various (CRV, GV, Tiger Global, 8VC, SV Angel, Notable Capital) |
| **Total raised** | | **~$863M** | | **31 investors** |

Sources: [BusinessWire Series F](https://www.businesswire.com/news/home/20250930898216/en/), [Crunchbase Nasdaq](https://www.nasdaq.com/articles/vercels-valuation-jumps-325b-after-250m-series-e), [Tracxn](https://tracxn.com/d/companies/vercel/__uPuJfXzfvAQs0wmUuqRiXFxW4uGbcaKUHjHks8VPbrI/funding-and-investors)

### Revenue Trajectory

| Year | ARR (estimated) | YoY Growth |
|------|-----------------|------------|
| 2019 | $1M | - |
| 2020 | $5M | 400% |
| 2021 | $21M | 320% |
| 2022 | $51M | 143% |
| 2023 | $86M | 69% |
| 2024 | $100M | 16% |
| 2025 (May) | $200M | 100% |

v0 contribution: ~$42M ARR as of Feb 2025 (~21% of total), with 3.5M+ unique users and Teams/Enterprise representing >50% of v0 revenue.

Sources: [Sacra](https://sacra.com/c/vercel/), [Getlatka](https://getlatka.com/companies/vercel), [Shipper](https://shipper.now/vercel-v0-stats/)

---

## Domain & Infrastructure

### WHOIS Summary

| Field | Value |
|-------|-------|
| Domain | vercel.com |
| Registrar | Amazon Registrar, Inc. |
| WHOIS server | whois.registrar.amazon |
| Created | 1999-10-04 |
| Expires | 2029-10-04 |
| Last updated | 2022-12-01 |
| Registrant | Redacted (WHOIS privacy) |
| DNSSEC | Unknown (dig unavailable) |

Source: [Who.is](https://who.is/whois/vercel.com), [infowebstats](https://infowebstats.com/whois/vercel.com)

**Note:** The domain was registered in 1999, well before Vercel/ZEIT was founded in 2015. This suggests the domain was acquired secondhand. The domain is secured through 2029.

### DNS & Nameservers (Inferred)

| Record | Value | Source |
|--------|-------|--------|
| Nameservers | ns1.vercel-dns.com, ns2.vercel-dns.com (inferred — Vercel operates its own DNS) | [Vercel docs](https://vercel.com/docs/domains/working-with-nameservers) |
| MX records | Unknown (dig unavailable; Vercel does not provide mail services for domains) | [Vercel KB](https://vercel.com/kb/guide/why-has-email-stopped-working) |
| Hosting | Vercel's own global edge network (self-hosted) | [Vercel blog](https://vercel.com/blog/new-edge-dev-infrastructure) |

**Limitation:** Bash tool was denied, so `dig` commands for MX, TXT, and NS records could not be executed. The WHOIS Python script also could not be run. Nameserver information is inferred from documentation and community posts.

---

## Digital Footprint

### Social & External Presence

| Platform | Presence | Details | Source |
|----------|----------|---------|--------|
| GitHub | [github.com/vercel](https://github.com/vercel) | 216 repos + 149 labs repos. Next.js: 138K stars. Turborepo: 29.8K. SWR: 32.3K. AI SDK: 21.9K. | [GitHub](https://github.com/vercel) |
| Twitter/X | [@vercel](https://twitter.com/vercel) | Active account. CEO @rauchg has 303K+ followers. | [X](https://x.com/rauchg) |
| LinkedIn | [linkedin.com/company/vercel](https://www.linkedin.com/company/vercel) | Listed as 201-500 (outdated range); actual ~823-874 employees. | [LinkedIn](https://www.linkedin.com/company/vercel) |
| Product Hunt | [producthunt.com/products/vercel](https://www.producthunt.com/products/vercel) | Launched June 2020 ("Develop. Preview. Ship."). v0 launched Sep 2023. Multiple launches. | [Product Hunt](https://www.producthunt.com/products/vercel) |
| Crunchbase | [crunchbase.com/organization/vercel](https://www.crunchbase.com/organization/vercel) | Full profile with 6+ funding rounds, 31 investors. | [Crunchbase](https://www.crunchbase.com/organization/vercel) |
| Glassdoor | 4.1/5 (115 reviews), 74% recommend | Positives: talent density, fast pace, intellectually stimulating. Negatives: culture shift concerns, overwork reports. | [Glassdoor](https://www.glassdoor.com/Reviews/Vercel-Reviews-E6510369.htm) |
| PeerSpot | 8.2/10 | Customer reviews praising speed and DX. | [PeerSpot](https://www.peerspot.com/products/vercel-reviews) |
| Trustpilot | Present | Customer service reviews. | [Trustpilot](https://www.trustpilot.com/review/vercel.com) |
| Capterra | Present | Reviews available. | [Capterra](https://www.capterra.com/p/203626/Vercel/reviews/) |
| Gartner Peer Insights | Present | Cloud Application Platforms category. | [Gartner](https://www.gartner.com/reviews/market/cloud-application-platforms/vendor/vercel/product/vercel-platform) |
| AWS Marketplace | Present | Listed with reviews. | [AWS](https://aws.amazon.com/marketplace/reviews/reviews-list/prodview-oemsykos6jbty) |

### Notable Enterprise Customers (Confirmed)

OpenAI, The Washington Post, McDonald's, IBM, Ticketmaster, Marvel, Staples, eBay, GitHub, PayPal, Ramp, Supreme, Under Armour, Unity, Nintendo, Notion, MotorTrend, Tray.ai

Next.js framework users (broader than Vercel platform): Walmart, Apple, Nike, Netflix

Source: [Vercel Customers](https://vercel.com/customers), [Vercel ROI](https://vercel.com/roi)

---

## Website Analysis

### Homepage
- **Positioning:** "The Frontend Cloud" for building, scaling, and securing web experiences
- **Tagline:** "Develop. Preview. Ship."
- **Key value props:** Speed, developer experience, global edge network, AI-first tools (v0, AI SDK)
- **Self-description:** "Vercel provides developer tools, frameworks, and cloud infrastructure to build and maintain websites"

### Pricing Page
- **Model:** Hybrid — fixed monthly fee per seat + usage-based overages
- **Hobby:** Free (non-commercial only)
- **Pro:** $20/developer/month (includes $20 credit, 1TB data transfer, 10M edge requests)
- **Enterprise:** Custom (~$20-25K/year minimum per community reports)
- **Key insight:** The Hobby plan restriction to non-commercial use is aggressive — competitors like Netlify allow limited commercial use on free tiers

### Blog
- **URL:** https://vercel.com/blog
- **Frequency:** Multiple posts per month, consistently active
- **Topics:** AI/agents (v0, AI SDK), infrastructure engineering (Rust, Fluid compute), product launches, enterprise case studies, open source programs, Next.js updates
- **Technical depth:** High — detailed engineering posts (Rust migration, performance benchmarks, architecture decisions)
- **Notable recent posts:** "We removed 80% of our agent's tools" (Dec 2025), AI SDK 6 launch, BFCM 2025 performance analysis

### Documentation
- **Main docs:** https://vercel.com/docs — comprehensive coverage of all platform features
- **REST API:** https://vercel.com/docs/rest-api — full API reference
- **AI SDK:** https://ai-sdk.dev/docs/introduction — standalone docs site for AI toolkit
- **Changelog:** https://vercel.com/changelog — regular updates
- **Quality:** Enterprise-grade documentation with tutorials, API reference, and guides

### Careers
- **Open positions:** ~67-69 roles (as of Feb 2026)
- **Role types:** Fullstack Engineer, Backend Systems (v0 team), Developer Success Engineer, Sales, Product Design, HR, Finance, Marketing
- **Tech stack hints from jobs:** Python, JavaScript, TypeScript, AI/ML
- **Internship program:** Active (Spring 2026 part-time internship available)

Source: [Vercel Careers](https://vercel.com/careers), [Glassdoor Jobs](https://www.glassdoor.com/Jobs/Vercel-Jobs-E6510369.htm)

---

## Tech Stack Signals

### Internal Infrastructure (Confirmed)

| Layer | Technology | Evidence |
|-------|-----------|----------|
| Serverless runtime | Rust | [Blog: Functions powered by Rust](https://vercel.com/blog/vercel-functions-are-now-faster-and-powered-by-rust) — 47% faster connections, 77% faster p99 |
| Build system | Turborepo (Rust) | [Blog: Go-to-Rust migration](https://vercel.com/blog/finishing-turborepos-migration-from-go-to-rust) |
| Edge Functions | JavaScript, TypeScript, WebAssembly | [Vercel docs](https://vercel.com/docs/functions) |
| Compute model | Fluid (hybrid servers + serverless) | [The New Stack](https://thenewstack.io/vercel-rolls-out-more-cost-effective-infrastructure-model/) |
| DNS | Self-operated (vercel-dns.com) | [Vercel docs](https://vercel.com/docs/domains/working-with-nameservers) |
| Domain registration | Amazon Registrar (corporate), Name.com/Tucows (customer domains) | [Who.is WHOIS](https://who.is/whois/vercel.com), [Vercel legal](https://vercel.com/legal/domain-name-registration-and-services-terms) |
| CDN/Edge | Vercel Edge Network (proprietary global) | [Vercel blog](https://vercel.com/blog/new-edge-dev-infrastructure) |

### Developer-Facing Stack

| Technology | Context |
|-----------|---------|
| Next.js (React) | Primary framework, 138K GitHub stars |
| TypeScript | Primary language for SDK and tools |
| AI SDK | TypeScript toolkit for LLM integration (21.9K stars) |
| Node.js | Serverless function runtime |
| Python | Serverless function runtime (supported alongside Node.js) |

### Architecture Evolution

Vercel has undergone a strategic migration from Go to Rust for performance-critical components. Turborepo was fully ported from Go to Rust, and the serverless function runtime was rewritten in Rust, yielding measurable performance gains. This signals a commitment to systems-level performance optimization while maintaining TypeScript/JavaScript as the developer-facing interface.

### GitHub Organization Summary

- **Total repos:** 216 (main org) + 149 (vercel-labs)
- **Primary languages:** TypeScript, JavaScript, Rust
- **Combined star count (top 5 repos):** ~235K+
- **Open source strategy:** Core frameworks (Next.js, Turborepo, SWR, AI SDK) are fully open source; platform/infrastructure is proprietary

---

## Key Findings

1. **AI pivot is driving the growth inflection.** Vercel's revenue doubled from $100M to $200M ARR in 15 months (2024-2025), largely driven by v0 which generated ~$42M ARR within its first year. The Series F at $9.3B (3x the prior round's $3.25B) validates this bet. The company's own language has shifted from "Frontend Cloud" to "AI Cloud."

2. **Open source moat is massive and unique.** Next.js (138K stars) is the dominant React framework. Vercel created it, maintains it, and optimizes their platform for it. This creates a flywheel where Next.js adoption drives Vercel platform adoption. Competitors cannot easily replicate this.

3. **Rapid infrastructure modernization signals engineering depth.** The Go-to-Rust migration across Turborepo and serverless functions, plus the "Fluid" compute model, demonstrate investment in systems-level performance. The 47% connection time improvement and 77% p99 improvement from Rust are concrete, published benchmarks.

4. **Enterprise traction is real but customer concentration risk is unclear.** Marquee logos (OpenAI, McDonald's, The Washington Post, PayPal) and 264% ROI claims suggest enterprise product-market fit. However, revenue breakdowns by segment (SMB vs. enterprise) are not publicly available, and Enterprise pricing starts at only ~$20-25K/year, which is low for enterprise SaaS.

5. **Culture signals are mixed.** Glassdoor at 4.1/5 with 74% recommending is solid but not exceptional. Recent reviews cite culture shift concerns, "bro culture" allegations in senior management, and overwork. With ~823-874 employees supporting $200M ARR, revenue per employee is ~$230K — moderate for a cloud infrastructure company.

---

## Open Questions

1. **What are the actual DNS records (MX, TXT, NS) for vercel.com?** Bash was denied; these should be captured via `dig` when available.
2. **What is the enterprise vs. SMB revenue split?** v0 Teams/Enterprise is >50% of v0 revenue, but the overall platform breakdown is unknown.
3. **What is Vercel's net revenue retention rate?** Critical for SaaS valuation but not publicly disclosed.
4. **How does the Hobby plan restriction enforcement work?** Non-commercial-only free tier is unusual; enforcement mechanism and churn impact are unclear.
5. **What is the v0 competitive position vs. Cursor, Replit, Bolt, and other AI coding tools?** v0 is positioned as a "full-stack vibe coding platform" but the market is crowded and evolving rapidly.
6. **What is the burn rate and path to profitability?** $863M+ raised with $200M ARR — the company could be burning significantly, especially with 800+ employees and AI infrastructure costs.
7. **Domain acquisition history:** vercel.com was registered in 1999, 16 years before the company was founded. What was the acquisition price and from whom?
8. **What is the actual Twitter/X follower count for @vercel?** Could not be extracted from search results.
9. **What is Vercel's SOC 2 / ISO 27001 / security certification status?** Critical for enterprise due diligence.
10. **What percentage of Next.js users actually deploy on Vercel vs. competitors (Netlify, Cloudflare, self-hosted)?** This determines how well the OSS flywheel converts.

---

## Methodology Notes

- **Tools used:** WebSearch exclusively. Bash (for WHOIS script, dig commands) and WebFetch were both denied by the environment.
- **Data freshness:** All searches conducted 2026-02-18. Financial data is a mix of confirmed press releases and third-party estimates.
- **Confidence levels:**
  - **High confidence:** Funding amounts, key dates, product descriptions, GitHub stats (from press releases and GitHub)
  - **Medium confidence:** Revenue figures (from third-party estimates like Sacra, Getlatka), employee counts (varying by source)
  - **Low confidence:** Enterprise pricing minimums (from community reports), Glassdoor rating trends (snapshot in time)
- **Raw data:** Structured JSON saved to `output/vercel.com/raw/website-content.json`
