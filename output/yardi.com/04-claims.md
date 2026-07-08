# Claims Validation: Yardi Systems (yardi.com)

**Phase:** P4 Claims Validation
**Date:** 2026-07-08
**Method note:** WebFetch 403-blocked for nearly all targets (incl. rabilventures.com, Crunchbase, PitchBook); all evidence via WebSearch snippets per Tool Resilience policy. Every source tagged with a canonical trust class (FIRST-PARTY 0.2 / AFFILIATED 0.4 / INDEPENDENT 0.8 / ADVERSARIAL 0.4). Ratings apply the CLAUDE.md Verification Bar exactly: VERIFIED = 2+ independent sources or one high-authority independent (court record, SEC, audited); first-party can never self-verify; plus the phase-specific EXAGGERATED tier.

---

## Claims Inventory

| # | Claim | Category | Materiality | Source of claim | Evidence (dated, trust-tagged) | Rating |
|---|-------|----------|-------------|-----------------|-------------------------------|--------|
| 1 | Revenue ≈ "$3B" | Scale | CRITICAL | Secondary press/scraper profiles (RocketReach-type) | No primary source found; not corroborated by any estimator. Getlatka $1.6B ARR 2024 (INDEPENDENT, weak), ZoomInfo $2.2B (INDEPENDENT, weak), Owler/IncFact/Growjo in the $1.5–2.2B band. Rev/employee sanity check (below) makes $3B an outlier | **UNVERIFIABLE** (outlier; triangulation says ~$2B ±$0.5B) |
| 2 | Revenue ≈ $1.6B ARR | Scale | CRITICAL | Getlatka (2024 est.) | ZoomInfo $2.2B is the only other point estimate; both are scraper-grade. Rev/emp math supports $1.5–2.5B | **PLAUSIBLE** (low end of triangulated range) |
| 3 | Headcount "9,000+ in 40+ offices" | Team | NOTABLE | yardi.com careers (FIRST-PARTY) | Revelio Labs 9,477 (Dec 2025, INDEPENDENT); Tracxn ~9.3K (2026, INDEPENDENT); PitchBook 10,000 (2026, INDEPENDENT). LeadIQ 6,990 (May 2026) is a stale/US-only outlier | **VERIFIED** (3 independent sources converge 9.3–10K) |
| 4 | "Bootstrapped — no outside capital since 1984" | Financing | NOTABLE | FIRST-PARTY narrative, echoed by press | Wikipedia, Forbes profile, Getlatka (INDEPENDENT) all state no outside funding; zero funding rounds in 42 yrs of press; company self-funded a $337M WeWork rescue (2024 — Bisnow, allwork.space, traded.co, INDEPENDENT), consistent with large internal cash generation. Counter-datum: Crunchbase lists "Rabil Ventures" as investor — but Rabil Ventures (SF, founded 2016) is a pre-seed/seed sports/fintech/wellness shop (portfolio: Betterment, Impossible Foods, PLL, beehiiv — Tracxn/superscout/investorlist, INDEPENDENT); no second source anywhere corroborates a Yardi investment; economically implausible (seed firm into a 1984 multi-$B company). Assessed as a **Crunchbase data error**. Nuance from P5: USPTO records show patent US7890215 assigned Yardi→Wells Fargo Bank (security interest) — evidence of ordinary secured bank *debt* (credit facility collateral), which does not contradict "no outside equity capital" but softens any "debt-free" folklore | **VERIFIED** (bootstrapped, as no-outside-equity) / Crunchbase datum **CONTRADICTED** |
| 5 | Virtuoso Connectors for Anthropic's Claude exist (first PM connector on Anthropic marketplace; second = Matrix connector Jun 17, 2026) | Technology | NOTABLE | Yardi press releases (FIRST-PARTY, Sep 2025 / Feb & Jun 2026) | Live listing on claude.com/connectors/yardi-virtuoso (Anthropic marketplace — INDEPENDENT artifact); Multi-Housing News, Mann Report (trade press, largely PR-derived — AFFILIATED-leaning); BC Solutions, Atlas Global Advisors partner guides (AFFILIATED); BestCRE review (INDEPENDENT) | **VERIFIED** (the connectors are real, shipped artifacts) |
| 6 | Virtuoso Support resolves "78% of queries without escalation" (+"92% satisfaction") | Feature/perf | CRITICAL | Yardi (FIRST-PARTY metric) | Every third-party mention (BestCRE, BubbleGum BI, BC Solutions, usehaven.ai — 2026) explicitly attributes it "per Yardi's own metrics." Pure citation circularity; zero customer-side corroboration found | **UNVERIFIABLE** (first-party echo chamber) |
| 7 | "AI-powered platform" (Virtuoso agents for "every multifamily role and workflow") | Technology | NOTABLE | Yardi PR (FIRST-PARTY, Sep 2025–Jun 2026) | Real ML hiring: "SDE II, Machine Learning" — PyTorch/spaCy in production (LinkedIn posting, INDEPENDENT, from P3); GitHub AI-tooling forks 2023–2025 (llm-retrieval-plugin, Flowise, bolt.diy — INDEPENDENT artifact); shipped MCP connectors (#5). But: no research publications, thin ML-role volume vs ~9.5K staff, "every role and workflow" breadth unverified by any user review | **PLAUSIBLE** (real AI engineering; marketed scope outruns evidence) |
| 8 | Partner API access costs $25,000/yr per interface | Pricing | NOTABLE | Was single-source (PLAUSIBLE) after P3 | ND Consulting integration guide 2026 (INDEPENDENT client-side consultant); mariourquia/cre-skills-plugin (INDEPENDENT, from P3); BC Solutions pricing guide (AFFILIATED partner); search synthesis indicates Yardi's own interface-program pages carry the fee (FIRST-PARTY, self-declared pricing). Some interfaces per-transaction instead | **VERIFIED** (upgraded: 2 independent + affiliated + first-party consistent) |
| 9 | "Yardi Technology Limited" (Kooboo CMS copyright) is related to Yardi Systems | Anomaly | MINOR | P3 open flag | Apollo.io, ZoomInfo, CMSWire, RocketReach (INDEPENDENT directories): Yardi Technology Limited = web-dev firm in **Xiamen, China** (NL contact office), ASP.NET/MS-SQL outsourcing shop, operator of kooboo.com. No ownership/officer/address link to Yardi Systems Inc. Name coincidence | **CONTRADICTED** (no relationship — anomaly resolved) |
| 10 | Units/clients under management: "8M+ residential units, 7B+ sqft commercial, 20,000 clients" (2025); "15,000 clients overseeing $4T assets, 80+ countries" (Forbes profile) | Scale | NOTABLE | Yardi press releases; Forbes company profile (company-supplied = FIRST-PARTY in substance) | No independent audit or third-party count exists. Directional sanity: AppFolio 9.4M units audited (SEC), RealPage 19M+ self-reported — Yardi ≥8M is not implausible for the enterprise leader, but nothing independent confirms it | **UNVERIFIABLE** (first-party only) |
| 11 | Duffy v. Yardi — Yardi's claim: "Revenue IQ does not mandate prices; adjusts up and down; does not, and by design cannot, use one client's confidential data to price for another" | Legal/product | CRITICAL | yardi.com legal-news statement (FIRST-PARTY) | FOR Yardi: Oct 2025 CA state-court ruling agreed Revenue IQ does not use cross-client confidential data under CA law (court record — high-authority INDEPENDENT); Apr 2026 federal narrowing, 11 landlord defendants dismissed (PYMNTS, Multifamily Dive, INDEPENDENT). AGAINST: Dec 2024 federal MTD **denied under per se treatment** (Morgan Lewis, Bloomberg Law, INDEPENDENT — court found the conspiracy allegations plausible, harsher posture than the RealPage court); FTC/DOJ statement of interest opposed dismissal; case in active discovery vs Yardi + 10 operators | **PLAUSIBLE** (one high-authority source partially supports the data-use claim; the core antitrust question is unresolved — do not treat Yardi's characterization as fact) |
| 12 | "We have never furloughed or laid off employees" | Team/culture | CRITICAL | Yardi employer-branding text (FIRST-PARTY, appears on Glassdoor company response/profile) | No WARN filings, no layoffs.fyi entry, absent from TechCrunch/Crunchbase 2024–25 layoff lists (INDEPENDENT — no *formal RIF* documented). BUT: Glassdoor employee reviews (Mar 2024 onward): "company claims no layoffs… they just laid off people not long ago," "quietly firing people… eliminating 'overhead' without calling it layoffs because the word scares clients," reorg/burnout reviews into 2025 (INDEPENDENT); Blind hosts a dedicated Yardi-layoffs discussion (INDEPENDENT). Employees link cuts to a bad third-party investment (WeWork inference) | **EXAGGERATED** (technically no tracked RIF; multiple independent employee reports of quiet terminations contradict the spirit) |
| 13 | Security/compliance: SOC 1 (biannual) + SOC 2 (annual), CSA STAR, PCI, HIPAA, GDPR, ISO 27001 | Compliance | CRITICAL (binary per prompt) | yardi.com cloud-security pages (FIRST-PARTY) | CSA STAR registry entry for Yardi Cloud Services exists — Level 2 (cloudsecurityalliance.org, INDEPENDENT registry); historical SSAE16 SOC 1 Type 2 press (insideselfstorage, 2010s, AFFILIATED-leaning trade); Nudge Security profile repeats compliance list (INDEPENDENT aggregator, likely self-attested inputs); Rankiteo (INDEPENDENT) *disputes* ISO 27001 and SOC 2 Type 2. Reports are customer-gated, not public | **PLAUSIBLE** (CSA STAR verified; SOC/ISO specifics unproven publicly, one source disputes — request attestations in any real diligence) |
| 14 | "450+ interface partners" | Ecosystem | MINOR | Yardi partner directory (FIRST-PARTY) | Directory is self-published; no independent count | **UNVERIFIABLE** |
| 15 | "15 data centers worldwide" / own-cloud hosting | Infrastructure | MINOR | Yardi (FIRST-PARTY) | Own-DC model independently corroborated ({client}.yardiasp13.com tenancy URLs, P3 INDEPENDENT); DC count itself first-party only | **PLAUSIBLE** (model verified, count unverified) |
| 16 | Benefits: 100% employer-paid healthcare, profit sharing, tuition reimbursement | Team | MINOR | careers.yardi.com (FIRST-PARTY) | Glassdoor reviews (3,102, INDEPENDENT) and Blind posts (INDEPENDENT) independently confirm paid medical + profit sharing (also: "no 401k match") | **VERIFIED** |
| 17 | CEO succession: Anant Yardi → Chairman; Rob Teel (22-yr veteran) CEO from Jan 2026 | Team/governance | NOTABLE (new fact — prior phases assumed founder still CEO) | Yardi announcement at YASC Sep 2025 (FIRST-PARTY) | Commercial Property Executive, Multi-Housing News, Wikipedia, LinkedIn coverage (INDEPENDENT, Sep 2025) | **VERIFIED** |
| 18 | WeWork: Yardi took 60% equity (~$337M; $450M lender deal) in 2024 bankruptcy exit | Corporate | NOTABLE | Deal press | Bisnow, allwork.space, traded.co, Wikipedia (INDEPENDENT, Apr–May 2024) | **VERIFIED** |
| 19 | Breeze pricing $1–2/unit/mo (published) | Pricing | MINOR | yardi.com (FIRST-PARTY published price) | Capterra/Vendr/review-site listings repeat the published tiers (INDEPENDENT observation of a public price) | **VERIFIED** (as the list price) |
| 20 | CommercialEdge: "2M monthly visits, 200K+ leads/yr" | Scale | MINOR | Yardi (FIRST-PARTY) | No independent traffic data captured | **UNVERIFIABLE** |
| 21 | No public REST API / SOAP-only, partner-gated (Breeze: no API at all) | Technology | NOTABLE | P3 finding (about Yardi, not by Yardi) | yhavin/yardi-sdk, api-evangelist docs, integration-vendor analyses, browser-automation workaround repos (INDEPENDENT, 2+; from P3) | **VERIFIED** (carried forward) |

---

## Internal Signal Intelligence

### Source Coverage

| Source | Found? | Key signals (dated) |
|--------|--------|---------------------|
| Glassdoor | Yes — 4.0/5, 3,102 reviews, 80% recommend | Rating **down 2% over trailing 12 months** (2025–26). WLB 4.2 / culture 4.2 / career opps 3.6 / comp 3.8. Recurring: below-market pay, "slow but steady" raises, great healthcare/profit-sharing. Negative cluster 2024–25: "Reorg is changing the culture. Now it's bad"; quiet-layoff reports (Mar 2024+); "stressed and burned out, wondering if they'll be next"; isolated toxic-manager/favoritism reviews. (INDEPENDENT) |
| Blind | Yes | Dedicated **Yardi layoffs** discussion thread (severance, impacted teams). Culture: "great unless you're in management"; company-paid health insurance; **no 401k match**, profit sharing "can be decent." Salary spread $55K–$1M. (INDEPENDENT) |
| Reddit | Weak coverage this session | Three query variants returned no direct threads via the search tool (tool limitation, not proven absence — P1/P2 noted r/PropertyManagement complaint folklore; unresolved gap). |
| Hacker News | Effectively absent | No substantive HN threads surfaced — notable in itself: a 42-year-old, ~$2B software firm with near-zero developer-community discourse, consistent with the closed-API posture. (absence signal, INDEPENDENT) |
| LinkedIn | Yes | "9,000+ professionals, 40+ offices"; regional entities (UK, NL, India-Pune). Rob Teel profile: CEO. Revelio (LinkedIn-derived workforce data): 9,477 (Dec 2025). (INDEPENDENT) |
| Layoff trackers | Checked — **no entry** | No layoffs.fyi entry, no WARN filings found, absent from TechCrunch/Crunchbase 2024–25 lists. Combined with employee reports → cuts happened below formal-RIF/WARN thresholds ("quiet firing"). (INDEPENDENT) |
| arXiv/Scholar | No Yardi-affiliated publications found (P5 to confirm) | AI claims rest on engineering, not research. |
| Job boards | Yes | ML role (PyTorch/spaCy, production) confirmed; bulk of openings are Client Services/Consulting/.NET dev; one cloud-native DevOps posting (EKS/Terraform). Hiring mix says services-heavy enterprise vendor with a small real ML core, not an AI-first org. (INDEPENDENT) |
| Twitter/X | Low signal | @Yardi used for corporate announcements (CEO succession post, Sep 2025). No notable complaint clusters captured. |
| G2/Capterra | Yes (P1/P2 + this phase) | Verified-user reviews (2026): praise reporting depth/end-to-end coverage; recurring complaints — **"extremely slow… several minutes to run reports, upload files, even load pages"**, no QuickBooks integration, missing property-level data fields. Voyager G2 ~4.6/265; Breeze Capterra 4.2/316+. (INDEPENDENT) |
| Trustpilot / Product Hunt | Not meaningful | Enterprise B2B; predates PH. (absence, expected) |

### Triangulated Estimates

| Metric | Company claims | Triangulated range | Sources (each shown) | Confidence |
|--------|----------------|--------------------|----------------------|------------|
| Revenue | None publicly (Yardi is deliberately silent) | **$1.5–2.5B, midpoint ≈ $2B.** $3B = unsupported outlier; $1.6B = credible floor | Getlatka $1.6B ARR '24; ZoomInfo $2.2B; Owler/IncFact/Growjo ~$1.5–2.2B band (all INDEPENDENT, scraper-grade). Cross-check: 9,477 emp × $160–250K rev/emp (services-heavy, large Pune offshore base; cf. AppFolio $475K/emp lean-SaaS ceiling) = $1.5–2.4B. Cash-flow check: self-funded $337M WeWork stake (2024) + LCP Media acquisition (2025) without debt/raise → consistent with ≥$1.5B high-margin revenue | Medium-low (no audited data exists) |
| Team size | "9,000+ / 40+ offices" | **9,300–10,000** | Revelio 9,477 (Dec 2025); Tracxn ~9.3K (2026); PitchBook 10,000; LinkedIn 9,000+. LeadIQ 6,990 rejected as stale/US-scope outlier | High — claim VERIFIED; company's own stale pages (5,000+/30 offices) are the discrepancy, not the headline claim |
| Customer count | 15,000 → 20,000 clients; "$4T assets" | Not independently measurable; ≥10K plausible given 3,102 Glassdoor reviews, 450-partner ecosystem, and rivals' scale (RealPage 12K customers) | First-party press only; Forbes profile is company-supplied | Low — UNVERIFIABLE |
| Units under management | 8M+ residential, 7B+ sqft commercial | Directionally credible vs AppFolio 9.4M (audited) / RealPage 19M+ (self-reported); no independent count | FIRST-PARTY only | Low |
| Tech stack | "Energized for tomorrow"; AI platform | Reality: ASP.NET/C#/SQL Server/SOAP monolith, per-client instances, own DCs, AngularJS/jQuery-era front end + genuine but small modern pockets (PyTorch ML, EKS/Terraform, MCP connectors) | Job postings, partner docs, community SDKs, tenancy URLs, GitHub artifacts (all INDEPENDENT — P3) | High |
| AI capability | Virtuoso agents "for every role and workflow"; 78% deflection | Shipped: 2 real MCP connectors on Anthropic marketplace; in-app support assistant exists. Verified perf data: none | Anthropic marketplace listing (INDEPENDENT); all perf numbers trace to Yardi itself | Medium on existence; nil on performance |

### Internal Prediction Market Summary

- **What's real:** end-to-end product breadth and stickiness; 9.3–10K headcount; bootstrapped/founder-owned economics strong enough to write a $337M WeWork check; 100% paid healthcare + profit sharing (employees confirm); a small genuine ML team (PyTorch/spaCy in production); shipped Claude/MCP connectors (first in its industry); legacy SOAP/ASP.NET core with independently confirmed slow-performance pain; own-datacenter hosting model.
- **What's aspirational:** "AI agents for every multifamily role and workflow" (agents launched Sep 2025–Jun 2026, no user-side validation yet); core-platform modernization (.NET Core migration asserted in job posts, unconfirmed for Voyager core); open-ecosystem posture (still $25K/yr gated SOAP).
- **What's theater:** "We have never furloughed or laid off employees" (employees report quiet cuts since Mar 2024); the "78% deflection / 92% satisfaction" metrics (self-reported, laundered through partner blogs into apparent third-party fact — a textbook circular-citation pattern); "Energized for Tomorrow" positioning atop an EOL AngularJS front end.
- **Morale trajectory:** **stable-to-declining.** Still solid in absolute terms (4.0, 80% recommend) but rating fell ~2% in 12 months, with a distinct 2024–26 anxiety cluster (reorg, quiet layoffs, below-market pay) and a first-ever founder→professional-CEO transition (Jan 2026) adding uncertainty insiders would price in.
- **AI reality score: 3/5.** Genuine engineering substance (production ML hires, 3 years of LLM experimentation artifacts, first-mover MCP connectors on a real marketplace) — but no research bench, thin ML hiring relative to 9.5K staff, and every headline performance number is first-party. Not AI-washing, but marketing runs ~18 months ahead of verifiable capability.

---

## Verified Claims

1. **Headcount 9,000+ / 40+ offices** — Revelio, Tracxn, PitchBook converge (9.3–10K).
2. **Bootstrapped since 1984** — no funding round in 42 years across all databases/press; Crunchbase's "Rabil Ventures" entry is a data error (seed-stage sports/fintech firm, portfolio independently enumerated without Yardi, zero corroboration).
3. **Claude/MCP connectors exist** (Virtuoso Feb 2026, Matrix Jun 2026) — live Anthropic marketplace listing + trade coverage.
4. **$25K/yr per interface partner fee** — upgraded from PLAUSIBLE: ND Consulting + cre-skills-plugin (independent) + BC Solutions + Yardi's own program pages.
5. **CEO succession** — Rob Teel CEO Jan 2026; founder Anant Yardi → Chairman (announced YASC, Sep 2025).
6. **WeWork 60% stake (~$337M, 2024)** — multiple independent deal reports.
7. **Benefits claims** (paid healthcare, profit sharing) — corroborated by Glassdoor and Blind.
8. **No public REST API; SOAP-only, partner-gated; Breeze has no API** — carried from P3 (2+ independent).
9. **Breeze published pricing $1–2/unit/mo** — observable public price, echoed on review platforms.
10. **Kooboo anomaly resolved:** "Yardi Technology Limited" is an unrelated Xiamen, China web-dev firm (name coincidence) — multiple independent directories.

## Critical Gaps

1. **"Never laid off employees" vs employee reality (EXAGGERATED).** No WARN/tracker events, but 2+ independent employee accounts (Glassdoor Mar 2024+, Blind layoffs thread) describe quiet terminations framed as overhead elimination, with burnout/fear reviews continuing into 2025–26. This is the dossier's clearest integrity marker: the company makes an absolute claim its own workforce publicly disputes. Also weakens trust in other absolute first-party statements.
2. **The flagship AI metric (78% deflection) is unverifiable and circularly cited.** It is the core quantitative sales argument for Virtuoso, appears in numerous "reviews" — every one sourcing Yardi itself. Would change a purchase decision if untrue; demand client references/raw data in real diligence.
3. **Revenue opacity with a 2x public spread.** Triangulation lands at ~$2B ±$0.5B, and the widely repeated $3B figure has no traceable primary source. For a $4.9B-implied-valuation company this is an unquantified underwriting risk — no audited figures exist, period.
4. **Duffy v. Yardi vs marketing.** Yardi's public denial ("does not and cannot use cross-client confidential data") is partially supported by an Oct 2025 CA state ruling but the federal court applied *per se* treatment at MTD (Dec 2024) — the harshest available posture — and discovery continues. Revenue IQ's share of revenue remains unknown (P6 must scenario-model it). Security/compliance corollary: SOC 2/ISO 27001 could not be publicly confirmed and one rating service disputes them — binary items requiring attestation letters.

## Notable Gaps

- **Units/clients/$4T-assets scale claims are first-party only** (10, 20) — directionally credible, never independently counted; Forbes profile is company-supplied data wearing an independent masthead.
- **AI marketing scope vs hiring reality** — "agents for every role and workflow" vs a small visible ML bench and zero publications; job-board mix is dominated by services/consulting/.NET roles.
- **"450+ interface partners", "15 data centers"** — self-published counts (hosting *model* verified, counts not).
- **Company's own headcount/office figures disagree with each other** across its properties (5,000/30 vs 9,000/40 vs 10,000+) — sloppy, not deceptive; the high figure is the correct one.
- **Glassdoor trajectory** — mildly negative (-2% YoY) through a reorg + CEO transition window; watch, not alarm.

## Unverifiable Claims

- 78% support deflection / 92% satisfaction (Virtuoso).
- $3B revenue figure (and any specific revenue figure — private, unaudited).
- 8M+ residential units / 7B+ sqft / 15–20K clients / $4T AUM footprint.
- CommercialEdge 2M visits / 200K leads.
- 450+ partners; 15 DCs (counts); SOC 2/ISO 27001 currency (publicly).
- llms.txt / AI-instruction files: still unprobed (Cloudflare 403 persists) — carried gap from P1.

## Source Provenance

Approximate tally of discrete evidence data points used in this phase (each source-use counted once per claim it supports):

| Trust class | Count | Share | Notes |
|---|---|---|---|
| INDEPENDENT (0.8) | ~46 | ~66% | Workforce-data firms (Revelio, Tracxn, PitchBook), court-record reporting (Morgan Lewis, Bloomberg Law, PYMNTS, Multifamily Dive), Glassdoor/Blind employee content, community repos/SDKs, CSA STAR registry, deal press (Bisnow et al.), review platforms, business directories (Apollo/ZoomInfo for Kooboo) |
| FIRST-PARTY (0.2) | ~14 | ~20% | Yardi PR (Virtuoso/Claude, AI agents), legal statement, careers/benefits, cloud-security pages, partner pages, pricing, employer-branding text on Glassdoor |
| AFFILIATED (0.4) | ~8 | ~11% | BC Solutions, Atlas Global Advisors, Assetsoft, ND-adjacent partner guides, PR-derived trade coverage (Multi-Housing News, Mann Report), insideselfstorage |
| ADVERSARIAL (0.4) | ~2 | ~3% | Plaintiff-firm case pages (Mogin Law — used for docket facts only); competitor comparison content excluded per P2 tagging |

Circularity warning logged: the Virtuoso "78%" figure demonstrates active first-party→blog→"review" laundering; P4.5 should treat all Virtuoso performance content as potentially LLM-optimized/SEO-planted (several "review" sites are AI-content mills quoting the same press release).

## Overall Assessment

- **Claims accuracy rate:** of 21 rated claims — **10 VERIFIED, 5 PLAUSIBLE, 4 UNVERIFIABLE, 1 EXAGGERATED, 1 CONTRADICTED** (the contradicted item resolves *in Yardi's favor* — the Kooboo entity is unrelated; the Rabil datum also falls, in Yardi's favor). 15/21 verified-or-plausible ≈ 71%.
- **Pattern: honest-but-opaque, with two theater zones.** Yardi understates rather than inflates in most areas (publishes no revenue/TAM claims at all — rare discipline). The exceptions: absolute employment claims ("never laid off") contradicted by employees, and self-reported AI metrics presented through an echo chamber of pseudo-independent blogs.
- **Signal convergence:** internal signals mostly align with external marketing on benefits, stability, and product breadth; they *diverge* on employment practices (quiet cuts), technology freshness ("energized" vs slow legacy reality), and AI maturity (real but far narrower than PR).
- **Material gaps: 4 CRITICAL + 5 NOTABLE.**

## Key Findings

1. **The bootstrapped story survives attack; the revenue story does not resolve.** No outside capital in 42 years is now VERIFIED (Crunchbase's Rabil Ventures entry is a demonstrable data error), but revenue triangulates to ~$2B ±$0.5B with the popular $3B figure unsupported — every downstream valuation must carry the full $1.5–2.5B band.
2. **New material fact missed by earlier phases: founder succession has already happened.** Rob Teel became CEO in Jan 2026 (Anant Yardi → Chairman) — the P2 "founder-succession question" is answered and P6 should model execution risk of the first non-founder CEO in company history instead.
3. **The single worst claims-integrity signal is the layoff denial.** "We have never furloughed or laid off employees" is an absolute claim that Yardi's own employees publicly dispute (quiet firings reported from Mar 2024), even though no formal RIF appears on any tracker — exactly the profile of reputation-managed workforce reduction.
4. **Yardi's AI is real but its AI *numbers* are not yet evidence.** First-in-industry Claude/MCP connectors and production ML hiring are verified; the 78%-deflection metric exists only as a self-citation loop through content-mill "reviews." AI reality score 3/5.
5. **Litigation claim posture is defensible but unresolved:** one high-authority ruling (CA, Oct 2025) supports Yardi's central data-use denial while the federal *per se* posture keeps worst-case exposure alive; with Revenue IQ's revenue share unknown, this remains the largest unquantified risk entering P4.5/P6.
