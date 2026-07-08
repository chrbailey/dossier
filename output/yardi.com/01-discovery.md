# Discovery: yardi.com

**Phase:** P1 Discovery
**Date:** 2026-07-08
**Method note:** Direct access to the target's website was blocked in this environment (Cloudflare/egress-proxy 403 on WebFetch and curl), so all first-party content was captured via WebSearch snippets per the Tool Resilience policy. WHOIS port 43 and RDAP were also blocked; registration data comes from an independent WHOIS aggregator snippet. Gaps are flagged inline.

Per the Source Trust Policy, independent sources were gathered FIRST (sections below are ordered that way); the company's self-description was processed LAST.

---

## Company Identity

| Field | Value | Source (trust class) |
|---|---|---|
| Legal name | Yardi Systems, Inc. | D&B, GlobalData, Wikipedia (INDEPENDENT) |
| Domain | yardi.com (+ yardibreeze.com, rentcafe.com, careers.yardi.com, commercialedge.com) | DNS + search results (INDEPENDENT) |
| Founded | 1984 (founder reportedly conceived product ~1982, built on an Apple IIe) | Wikipedia, Forbes profile, Tracxn (INDEPENDENT); matches first-party claim |
| Founder / CEO | Anant Yardi (founder; still leads the company) | Wikipedia, Forbes (INDEPENDENT) |
| HQ | 430 South Fairview Avenue, Santa Barbara, CA 93117, USA | LeadIQ/D&B profiles (INDEPENDENT) |
| Team size | **Conflicting:** ~6,990 (LeadIQ, May 2026) vs ~9,300 (Tracxn, 2026, up from 5.6K in 2023) vs "9,000+ in 40+ offices" (company claim) vs "5,000+ / 30+ offices" (stale careers page) vs "10,000+" (job posting). Best estimate: **7,000–10,000** | Mixed INDEPENDENT + FIRST-PARTY — discrepancy flagged |
| Funding status | **Private, founder-owned, bootstrapped** — grew without VC/outside institutional capital. NOTE: Crunchbase lists "Rabil Ventures" as an investor, which conflicts with the widely repeated "no outside capital" narrative — verify in P4 | Multiple INDEPENDENT (Getlatka, Forbes, Wikipedia); Crunchbase (INDEPENDENT) for the conflicting datum |
| Revenue (est.) | **Conflicting:** ~$1.6B ARR / $4.9B implied valuation (Getlatka, 2024 est.) vs "annual revenues reported to be ~$3B" (secondary press). Private company — no audited public figures exist. Treat all figures as estimates | INDEPENDENT but low-quality estimators — flagged for P4/P6 |
| Product | End-to-end investment, asset and property management software for real estate (residential, commercial, affordable, senior, coworking, military housing) | Convergent INDEPENDENT + FIRST-PARTY |
| Target market / ICP | Real estate owners/operators/managers of all sizes: Voyager = mid/large portfolios & institutions; Breeze = SMB landlords/managers | Review sites (INDEPENDENT) + FIRST-PARTY |
| Key claimed differentiators | Single connected platform ("frictionless… customer acquisition to resident retention"), breadth across asset classes, "Energized for Tomorrow" | FIRST-PARTY — claims to verify |
| GitHub org | `YardiSystems` — 13 repos, **archived by an administrator Sep 15, 2025**; effectively no open-source presence | github.com (INDEPENDENT) |
| Primary tech stack | Microsoft stack: C#/ASP.NET/.NET Core, SQL Server, Angular/jQuery front end; SOAP/WSDL integration APIs; Cloudflare CDN; AWS Route 53 DNS; Proofpoint email | Job postings + DNS + partner docs (INDEPENDENT) |

---

## Domain & Infrastructure

WHOIS (via whois.com snippet — INDEPENDENT, single-source; direct WHOIS/RDAP blocked in this environment):
- **Created:** 1996-02-01 (30-year-old domain — consistent with a company founded 1984)
- **Expires:** 2030-02-02 (long renewal horizon — signals institutional domain management)
- **Registrar:** GoDaddy Corporate Domains, LLC (corporate-tier registrar)
- **Registrant org:** not recovered (gap)

DNS (live queries via dnspython — INDEPENDENT; raw in `raw/dns.json`):
- **A:** 104.18.102.99 → **Cloudflare** (site fronted by Cloudflare; explains the 403 bot-blocking we hit)
- **www:** 172.66.1.254 / 162.159.142.5 → Cloudflare
- **NS:** ns-114.awsdns-14.com, ns-783.awsdns-33.net, ns-1336.awsdns-39.org, ns-1678.awsdns-17.co.uk → **AWS Route 53**
- **MX:** mxa/mxb-0005a801.gslb.pphosted.com → **Proofpoint** (enterprise email security)
- **TXT:** lookup timed out repeatedly over UDP and TCP in this container (gap — SPF/verification records not captured)

Inference (medium confidence): enterprise-grade, security-conscious infrastructure mix (Cloudflare + Route 53 + Proofpoint) rather than a single-cloud startup profile.

---

## Digital Footprint

Independent presence, gathered before reading the company's own site:

- **LinkedIn:** Main page `linkedin.com/company/yardi` plus regional entities (Yardi Systems Limited UK, Yardi Systems B.V. NL, Yardi Software India Pvt Ltd — Pune). Confirms multinational legal structure. (INDEPENDENT)
- **Crunchbase:** Profile exists; **19 acquisitions** listed (Tracxn says 24), incl. Point2 Technologies (2010), WUN Systems (coworking), CommissionTrac (Dec 2020), 42Floors (2021), Planimetron, CloudVO, Immobilien-Management-Systeme (DE), Forge, most recently **LCP Media (Feb 2025)**. Growth-by-acquisition pattern in adjacent real-estate tech. (INDEPENDENT)
- **PitchBook:** Profile exists (details paywalled — gap). (INDEPENDENT)
- **G2 / Capterra:**
  - Yardi Voyager: **G2 ~4.6/5 (265 reviews)**; Capterra ~4.5/5 (601 reviews) — another comparison snippet cites ~4.0 G2 / 4.1 Capterra; exact current figures need direct-site confirmation (flagged)
  - Yardi Breeze: **Capterra 4.2/5 (316+ reviews)**; ~4.0 on G2
  - Recurring praise: reporting depth, end-to-end coverage, support
  - Recurring complaints: **slow performance** (minutes to run reports), **dated UI**, steep learning curve, **Breeze has no open API**
  - (INDEPENDENT — watch for vendor-managed review programs in P4)
- **Glassdoor:** **4.0/5 from 3,102 reviews; 78% recommend**; work-life balance 4.2, culture 4.2, career opportunities 3.6. Pros: 100% employer-paid medical, profit sharing, collaborative culture. Cons: below-market pay, career-growth complaints, some toxic-manager reports. (INDEPENDENT)
- **Twitter/X:** @yardi exists; follower count not captured (gap). Product-level accounts (@RentCafeapts) also exist. Low signal.
- **Product Hunt:** No meaningful listing found — expected; company predates PH and sells enterprise B2B. (absence noted, INDEPENDENT)
- **GitHub:** `github.com/YardiSystems` — 13 repos (AngularJS xlsx export, JMeter tooling, Teams apps, an LLM retrieval plugin fork, PDF.js viewer), **entire org archived Sep 15, 2025**. Minimal open-source engagement; the archived LLM-retrieval-plugin fork hints at internal AI experimentation. (INDEPENDENT)
- **Litigation footprint (material):** Consolidated antitrust class action in W.D. Washington (*Duffy v. Yardi*) alleging Yardi's revenue-management software (RENTmaximizer/Revenue IQ) facilitated rent price-fixing among dozens of landlord co-defendants. Developments: co-defendant FPI Management settled for $2.8M (Sep 26, 2025); an **October 2025 California state-court ruling agreed with Yardi that Revenue IQ does not use one client's confidential data to price for another**; the federal case was narrowed by the judge. Context: DOJ settled the parallel RealPage case (Nov 2025) with conduct remedies. This is a live risk item for P2/P4/P6. (INDEPENDENT: Multifamily Dive, ProPublica, NPR, law-firm analyses — note plaintiff-firm posts lean ADVERSARIAL-adjacent)

---

## Website Analysis

FIRST-PARTY (trust 0.2) — captured via search snippets because direct fetch was blocked. These are claims, not facts. Raw capture in `raw/website-content.json`.

- **Homepage title:** "Yardi: Real Estate Software Energized For Tomorrow, Today"; self-description: "develops and supports industry-leading investment and property management software for all types and sizes of real estate companies."
- **Mission (claimed):** "frictionless customer experience… connected property management workflow from customer acquisition to resident retention."
- **Product architecture (claimed):** Two platforms — **Voyager** (enterprise, web-based end-to-end) and **Breeze/Breeze Premier** (SMB) — plus suites: RentCafe (marketing/leasing/resident, launched 2011), CommercialEdge marketplace network (claims 2M monthly visits, 200K+ leads/yr — unverified first-party metrics), Yardi Matrix (market data), Yardi Kube (coworking).
- **Pricing model:** Enterprise quote-based for Voyager (no public pricing — typical enterprise opacity). Breeze publishes pricing: **$1/unit/mo residential ($100 min), $2/unit/mo commercial ($200 min), Premier $2/unit/mo ($400 min)**, with bundling discounts. Land-and-expand: cheap SMB entry, ancillary services (screening, insurance, payments) attached.
- **Careers page:** Openings across Client Services, Cloud & IT, Operations, Professional Services, Sales, Software Development; Remote US + Santa Barbara + global. Benefits claims: 100% healthcare premiums paid, profit sharing, tuition reimbursement (consistent with Glassdoor reviews — one of the few first-party claims independently corroborated).
- **Docs:** No open developer portal. Integration via SOAP/WSDL "Standard Interfaces" gated behind a partner program (requires 2+ years in business and 3+ active Voyager clients) — a deliberate ecosystem moat. Independent sources confirm Breeze lacks an open API.
- **Content strategy:** Corporate blog + press-release stream heavy on client wins and philanthropy (Yardi Foundation / yardi.org); "Energized for Tomorrow" positioning. Notably press-shy about financials — no revenue or ARR claims found on the company's own pages.
- **Discrepancy flags:** employee/office counts differ across the company's own properties (5,000+/30 offices vs 9,000+/40 offices vs 10,000+/40+); CommercialEdge traffic/lead metrics are unverified first-party numbers.

### LLM-Optimized Content Check

- `llms.txt`, `llms-full.txt`, `llms.md`, `/.well-known/ai-plugin.json`, `/.well-known/ai-instructions.txt` **could not be probed directly** — every direct request to yardi.com returned 403 (Cloudflare bot protection / egress-proxy policy).
- Web search shows **no indexed llms.txt for yardi.com** (other companies' llms.txt files surfaced; none for the target).
- **Status: none found, but UNCONFIRMED.** Downstream phases with working direct fetch must re-check before treating this as clean. (No "LLM-Optimized Content Detected" section is included because none was verified to exist.)

---

## Tech Stack Signals

| Signal | Evidence | Trust class | Confidence |
|---|---|---|---|
| C#, ASP.NET, MVC, .NET Core, Entity Framework, WCF | Yardi job postings (.NET Developer, SDE I: "C# and MS-SQL preferred"); Glassdoor interview reports (".NET and C# MCQs, SQL query tests") | INDEPENDENT | High |
| Microsoft SQL Server | Same job postings + a whole third-party job market for "Yardi SQL" skills | INDEPENDENT | High |
| JavaScript, jQuery, HTML5/CSS3/Bootstrap, AngularJS/Angular | Job postings; archived GitHub repos (AngularJS xlsx export, PDF.js viewer) | INDEPENDENT | High |
| SOAP/WSDL web services (not REST-first) | Partner integration docs (BC Solutions, Latchel, IMS, unitmap.com), community Python SDK (yhavin/yardi-sdk); OSCRE-standard commercial data export | INDEPENDENT | High |
| Cloudflare (CDN/WAF) | A records 104.18.x / 172.66.x / 162.159.x; aggressive bot 403s | INDEPENDENT (DNS) | High |
| AWS Route 53 (DNS) | awsdns nameservers | INDEPENDENT (DNS) | High |
| Proofpoint (email security) | MX → pphosted.com | INDEPENDENT (DNS) | High |
| Own "Yardi Cloud" / private hosting for Voyager SaaS | Job department "Cloud & IT"; legacy of self-hosted Voyager | INDEPENDENT | Medium — hosting provider for the app itself not confirmed |
| Internal AI experimentation | Archived fork of an LLM retrieval plugin in GitHub org; company blog posts about AI | INDEPENDENT (weak) | Low |

Overall read: a mature ~2000s-era Microsoft enterprise stack (ASP.NET + SQL Server + SOAP) behind modern edge infrastructure. Consistent with independent user complaints about dated UI and slow reports.

---

## Key Findings

1. **Genuinely large, private, founder-controlled incumbent:** ~42 years old (founded 1984, Anant Yardi still in charge), 7,000–10,000 employees, 40+ offices, grown reportedly without outside capital — but headline revenue figures ($1.6B vs $3B) are third-party estimates that conflict by ~2x, and no audited numbers exist. All size claims need P4 verification.
2. **Two-tier product strategy with an ecosystem moat:** quote-priced enterprise Voyager plus published cheap per-unit Breeze for SMBs, monetized further through ancillary services; integration locked behind a gated SOAP/WSDL partner program (no open API — confirmed independently for Breeze).
3. **Material live legal risk:** Yardi is lead defendant in a federal antitrust class action over algorithmic rent pricing (Duffy v. Yardi, W.D. Wash.), directly analogous to the DOJ/RealPage case — partially narrowed and with a favorable Oct 2025 CA state ruling, but unresolved. Must be central to P2 (market), P4 (claims) and P6 (valuation).
4. **Aging core technology:** independent job postings and partner docs show an ASP.NET/SQL Server/SOAP stack, and review sites consistently report slow performance and dated UI — a modernization-debt signal despite strong (4.0–4.6) aggregate ratings.
5. **Environment-driven evidence gaps:** the target's site and WHOIS/RDAP were unreachable from this container (Cloudflare + egress-proxy 403s), so all first-party content is via search snippets and the LLM-optimized-file check is unconfirmed.

## Open Questions

- Actual revenue/ARR and growth rate — $1.6B (Getlatka) vs ~$3B (press) is a 2x spread; can P4/P6 triangulate via headcount, job-posting volume, or court filings?
- True current headcount — 6,990 vs 9,300 vs 10,000+; which independent measure (LinkedIn employee count trend) is most reliable?
- Who/what is "Rabil Ventures" (listed by Crunchbase as an investor) — does it contradict the "no outside capital ever" narrative, or is it a data error/minor SPV?
- Does yardi.com serve `llms.txt` or `.well-known` AI files? Unconfirmed — re-probe from an environment with direct access.
- TXT/SPF records and Voyager production hosting (own datacenters vs public cloud) — not captured.
- Registrant organization on the domain and the full corporate entity map (US Inc. + UK Ltd + B.V. + India Pvt Ltd).
- Exposure and expected outcome of *Duffy v. Yardi*; how much revenue depends on the challenged revenue-management module?
- Current exact G2/Voyager rating (snippets conflicted: ~4.6 vs ~4.0) — pull directly in P2.
- Churn/competitive dynamics vs RealPage, AppFolio, MRI, Entrata, Buildium (P2).
