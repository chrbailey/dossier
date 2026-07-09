# Product Requirements Document: Yardi Systems, Inc.

**Dossier — SaaS Due Diligence Report**
**Target:** yardi.com | **Date:** 2026-07-09 | **Pipeline:** P1–P7 complete (incl. mandatory P4.5 Red Team)

> **Reading rule for this report:** wherever P4 (Claims Validation) and P4.5 (Red Team) disagreed, the red team's downgraded rating is authoritative and is what appears in the body text; both assessments are shown side-by-side in §6.3. The red team's verdicts — source manipulation risk **MEDIUM**, LLM-content influence **UNKNOWN (limited indirect absorption detected)**, overall dossier bias **BALANCED with offsetting local skews** — condition every section below.

---

## 1. Executive Summary

Yardi Systems is a 42-year-old, private, founder-built property-management ERP vendor at a genuine inflection point. It is dominant and durable: the widest asset-class coverage in its category (residential, commercial, affordable/HUD, senior living, military housing, coworking, plus investment management, the Matrix market-data business, and the RentCafe/CommercialEdge marketplaces), an estimated 20–40% of a ~$7B core market, ~9,300–10,000 employees, structural sub-5% enterprise churn built on trust-accounting data gravity and 6–18-month migrations, and a balance sheet that self-funded a $337M purchase of 60% of WeWork out of bankruptcy (VERIFIED, P4). It is also honest in an unusual way: the company publishes no revenue or TAM claims at all, and 15 of 21 material claims tested rated verified-or-plausible (~71%).

But three deferred bills are landing simultaneously. **First**, succession: Rob Teel became the first non-founder CEO in company history in January 2026 (founder Anant Yardi → Chairman), taking over amid a reorg, employee-reported quiet layoffs the company categorically denies (its "never laid off" claim rated EXAGGERATED), and a mildly declining Glassdoor trend. **Second**, modernization: the core is an ASP-era hosted monolith — ASP.NET/SQL Server per-client instances in Yardi's own data centers, an EOL AngularJS/jQuery front end that verified users say takes minutes to run reports, and a SOAP-only, $25K/yr-per-interface-gated API surface so hostile that integrators ship browser-automation scrapers — precisely the surfaces the AI-agent era punishes. **Third**, litigation: *Duffy v. Yardi*, a federal antitrust class action over algorithmic rent pricing, survived dismissal under the **per se** standard (harsher than rival RealPage faced before its DOJ settlement) and remains in active discovery, un-de-risked; the pipeline's best exculpatory fact (an Oct 2025 California ruling) was never read in original text and gets no weight.

Nothing financial is auditable: revenue is a LOW-confidence $1.5–2.5B estimate cluster (tails $1.2–3.0B), and the widely repeated "$3B" has no traceable primary source. On that base, P6 estimates EV at ~$3.5–5B bear / **$8–11B base** / $16–22B bull. Because Yardi is private with no outside capital and no exit clock, the practical recommendation is posture-specific — partner/integrate, compete on the SMB flank (which is genuinely replicable), or monitor the Duffy docket and CEO transition. **Overall: PROCEED WITH CAUTION.**

Key scores (traceable to phases noted):
- AI Reality Score: 3/5 (P4 — real ML engineering and shipped Claude/MCP connectors; headline metrics unverifiable and laundered)
- Revenue Quality: 2/10 (P4/P4.5/P6 — likely durable and profitable, but zero auditability, 2x public spread, single-methodology estimate cluster)
- Claims accuracy rate: 15/21 verified or plausible (P4; ratings as adjusted by P4.5)
- Build vs Buy: 3/4 overall — hard to replicate, buy over build; bimodal (SMB flank ~2, enterprise core 4) (P6)
- Overall: PROCEED WITH CAUTION

---

## 2. Company Profile

| Field | Value | Source / rating |
|-------|-------|-----------------|
| Domain | yardi.com (+ yardibreeze.com, rentcafe.com, commercialedge.com) | P1, INDEPENDENT (DNS) |
| Company Name | Yardi Systems, Inc. | P1, INDEPENDENT |
| Founded | 1984 (Anant Yardi; domain registered 1996, expires 2030) | P1, INDEPENDENT |
| HQ Location | 430 South Fairview Ave, Santa Barbara, CA; 40+ offices claimed; entities in UK, NL, India (Pune) | P1/P4 |
| Leadership | **Rob Teel, CEO since Jan 2026** (22-year insider); Anant Yardi → Chairman — first non-founder CEO in 42 years | P4 **VERIFIED** (survived red team) |
| Team Size | ~9,300–10,000 (Revelio 9,477 Dec 2025; Tracxn; PitchBook) — **PLAUSIBLE** per P4.5 (P4 said VERIFIED; sources are one LinkedIn-derived family — pseudo-replication) | P4 → P4.5 downgrade |
| Funding | No outside equity in 42 years — **PLAUSIBLE** per P4.5 (P4 said VERIFIED; positive assertions all repeat the first-party narrative). Crunchbase "Rabil Ventures" entry: probable data error. Wells Fargo security interest on patent US7890215 shows ordinary secured bank debt exists | P4 → P4.5 downgrade; P5 |
| Revenue (est.) | **$1.5–2.5B central band; tails $1.2–3.0B; confidence LOW.** Single-methodology scraper cluster (Getlatka $1.6B, ZoomInfo $2.2B, Owler/IncFact/Growjo), NOT triangulation per P4.5. "$3B" = unsupported outlier | P4 → P4.5 → P6 |
| Primary Products | Voyager (enterprise ERP, quote-priced), Breeze/Breeze Premier (SMB, published $1–2/unit/mo — VERIFIED), RentCafe, CommercialEdge, Yardi Matrix, Yardi Kube, Revenue IQ | P1/P4 |
| Scale claims | "8M+ residential units, 7B+ sqft commercial, 15–20K clients, $4T AUM" — **UNVERIFIABLE** (first-party only; directionally credible vs audited AppFolio 9.4M units) | P4 |
| Litigation | *Duffy v. Yardi* (W.D. Wash., consolidated antitrust class action) — live, discovery ongoing | P1/P2/P4 |

---

## 3. Problem Statement

(P2.) Real estate operators run complex, regulated, money-moving businesses — leasing, rent collection, maintenance, vendor payments, GL/trust accounting, affordable-housing compliance, investor reporting. Property-management ERP is the system of record for all of it; below ~100 units QuickBooks-plus-spreadsheets suffices, above it the software is the operating system of the business. This is a **painkiller** category: trust accounting and compliance are legally mandatory, switching costs are extreme (Voyager implementations reportedly 6–18 months, $50K–500K+ — AFFILIATED partner sources), and category churn is structurally low — which is also why incumbents can carry dated UX for years. Customer tiers: SMB landlords (Breeze vs AppFolio/Buildium), mid-market/enterprise fee managers (Voyager vs RealPage/Entrata/MRI), and institutional owners/REITs (Voyager + investment management + Matrix).

---

## 4. Market Analysis

### 4.1 Market Size

(P2 — no first-party market-size figures exist or were used.)

| Metric | Estimate | Confidence | Source |
|--------|----------|------------|--------|
| TAM (core PM software, global, 2026) | **~$7B** (cluster $6.5–7.7B) | Medium | INDEPENDENT: 3 analyst firms + bottom-up (JCHS unit stock × AppFolio's SEC-audited ~$101/unit/yr realized ARPU) |
| TAM (broad: + attached fintech/marketing/data) | $25–30B | Low (scope ambiguity) | INDEPENDENT: 2 analyst firms, unverified methodology |
| SAM (Yardi-addressable, incl. commercial + international + attach) | ~$9–12B | Low-Medium | Derived from independent inputs; commercial split assumed |
| SOM (Yardi current capture) | $1.5–2.5B (its own est. revenue ≈ 20–40% of core TAM) | LOW | Estimate cluster (see §2); growth constrained by mature share + litigation overhang |

The margin engine is the **fintech attach layer**, not seats: AppFolio (the only audited comp) realizes ~$101/unit/yr against $12–24 core list — payments/screening/insurance are 4–8x seat revenue. Yardi runs the same playbook; models priced on "software TAM" alone understate the profit pool (P2/P6).

### 4.2 Competitive Landscape

(P2; scores red-team-corrected.) A consolidated oligopoly at the top — every major is a ~$4–12B asset — over a fragmented SMB tail:

| Competitor | Ownership / scale | Overlap | Key fact (trust class) |
|---|---|---|---|
| **RealPage** | Thoma Bravo, $10.2B take-private 2021; 19M+ units (self-reported) | HIGH | Under 7-year DOJ consent decree (Nov 2025): pricing product defanged, court monitor (INDEPENDENT) |
| **MRI Software** | PE-owned; ~$1B rev / ~$400M EBITDA; owners exploring sale/IPO up to $10B | HIGH | The "open ecosystem" foil to Yardi's closed stack (INDEPENDENT: Reuters) |
| **AppFolio** | Public (APPF); FY2025 $950.8M +20%, 9.4M units — audited | MED-HIGH (SMB flank) | Best financials in category (SEC); category-best UX; moving upmarket |
| **Entrata** | Silver Lake + Blackstone ($4.3B val., 2025); $200M raised explicitly for AI | HIGH (multifamily) | Blackstone alignment threatens Yardi's institutional accounts (INDEPENDENT) |
| Buildium, Rent Manager, ResMan, DoorLoop et al. | SMB tail | LOW-MED | Pipeline threat to Breeze only |

**Positioning (red-team-corrected):** Yardi is a Leader at **Vision 7 / Execution 7–8** — *not* the 9 P2 originally assigned. P4.5 found the 9 contradicted by the dossier's own independent evidence (minutes-long report runs, EOL front end, screen-scraping integrators, no Breeze API, unaudited revenue, G2 rating only bracketable at 4.0–4.6 unresolved, declining Glassdoor). AppFolio 8/8, Entrata 8/7, RealPage 7/7 (weakening), MRI 7/7.

**Market dynamics:** (1) The algorithmic-pricing legal storm is category-defining and currently asymmetric **against** Yardi — RealPage settled and capped its exposure; Yardi is still lead defendant on the harsher per se track. (2) The AI wave is the first churn-unfreezing event in a decade, aimed at Yardi's weakest surfaces. (3) Record multifamily supply + soft rents squeeze customers — good for efficiency modules, bad for new-logo growth. (4) Yardi is the only major with no capital-markets clock — its structural advantage is patience.

### 4.3 SWOT (condensed from P2, red-team-adjusted)

- **Strengths:** widest product breadth in category (independent reviews corroborate; note "end-to-end" is Yardi's own phrasing — avoided per P4.5); founder-owned patience; extreme switching costs; two-tier land-and-expand with fintech attach.
- **Weaknesses:** aging stack/UX (EOL front end, slow reports — INDEPENDENT); closed $25K/yr SOAP ecosystem; weakest public AI narrative among majors; financial opacity.
- **Opportunities:** RealPage's DOJ handcuffs; MRI's exit distraction; AI-replatforming wave (deepest data in category if it executes); operator margin squeeze drives efficiency spend.
- **Threats:** *Duffy* (per se track, treble damages, DOJ template); spreading state/city algorithmic-pricing bans; AppFolio upmarket; Entrata+Blackstone; rate cycle suppressing commercial modules.

---

## 5. Technical Assessment

### 5.1 Architecture

(P3 — inference from independent artifacts; zero Yardi source code is public.) **Conclusion: a modern edge wrapped around an ASP-era core.** Voyager runs as per-client single-tenant instances at `{client}.yardiasp13.com` (INDEPENDENT) in Yardi's own claimed ~15 data centers (own-DC model independently corroborated; the count is first-party) — not pooled cloud multi-tenancy. Stack: C#/ASP.NET/SQL Server monolith; AngularJS/jQuery-era front end (EOL frameworks, corroborated by the fork cluster and job postings); SOAP/WSDL-only official APIs, partner-gated (2+ years in business, 3+ Voyager clients, **$25K/yr per interface — VERIFIED**, survived red team); no public REST/SDK/portal — **the dossier's single strongest verification** (structurally diverse independent artifacts: community SDKs, third-party OpenAPI docs, integration-vendor audits, and Playwright screen-scraping repos built to route around the API). Breeze has no API at all. Modern pockets exist: production ML hiring (PyTorch/spaCy — INDEPENDENT), an EKS/Terraform/GitHub Actions DevOps posting (attribution uncertain), Cloudflare/Route 53/Proofpoint edge. AI: shipped Virtuoso and Matrix connectors on Anthropic's Claude marketplace (VERIFIED as artifacts; the "first in industry" framing is first-party-only and stripped per P4.5); the "78% deflection / 92% satisfaction" metrics are UNVERIFIABLE first-party numbers laundered through content mills.

### 5.2 Open Source Presence

**None, ever — by design.** GitHub org `YardiSystems`: 13 repos, 100% forks, zero original code, 2 stars total, entire org archived ~Sep 15, 2025 — days after fresh pushes to AI-tooling forks (Flowise, bolt.diy), suggesting a deliberate move private rather than an engineering halt (inference, medium confidence). Effectively zero Hacker News footprint — a ~$2B software firm invisible to the developer ecosystem (absence signal, INDEPENDENT). Meanwhile a community shadow ecosystem (yhavin/yardi-sdk, browser-automation tools, PHP/Python clients) grew *despite* Yardi.

### 5.3 Dependency Analysis

Only the fork set is visible: front-end libraries vendored as forks (2010s practice), several at/past EOL (AngularJS ecosystem). Server-side dependency posture and .NET version currency are invisible; a ".NET Core migration" is asserted in scattered job posts but unconfirmed for the Voyager core (P3 gap).

### 5.4 Test & Quality Signals

Essentially unobservable — no public CI/CD, tests, or security policy. Weak proxies: JMeter fork (load-testing practice), Teams call-record tooling. Compliance: CSA STAR Level 2 registry-verified (INDEPENDENT); SOC 1/SOC 2/ISO 27001 claims **PLAUSIBLE only** — publicly unproven, one rating service actively disputes them; a CRITICAL binary item requiring attestation letters (P4, red-team-emphasized). Independent user telemetry is the loudest quality signal: verified reviews report minutes-long report runs and page loads.

---

## 6. Claims Validation

### 6.1 Summary (P4, as adjusted by P4.5)

**21 material claims rated: 10 VERIFIED, 5 PLAUSIBLE, 4 UNVERIFIABLE, 1 EXAGGERATED, 1 CONTRADICTED under P4; after red-team downgrades the split shifts (bootstrapped and headcount VERIFIED→PLAUSIBLE) but the verified-or-plausible total is unchanged at 15/21 (~71%).** Pattern: **honest-but-opaque** — a phrase the red team permits only with both proven exceptions attached: (1) the absolute "we have never furloughed or laid off employees" claim, which Yardi's own employees publicly dispute (EXAGGERATED); (2) self-reported AI metrics presented through an echo chamber of pseudo-independent blogs. Notably, Yardi understates rather than inflates in most areas and publishes no revenue/TAM claims at all — rare discipline.

### 6.2 Key claims table (condensed; full detail in 04-claims.md)

| Claim | Evidence | Final rating (P4.5-adjusted) | Gap? |
|-------|----------|------------------------------|------|
| Revenue ~$3B | No traceable primary source; estimator cluster says $1.5–2.5B | UNVERIFIABLE (outlier) | CRITICAL |
| Headcount 9,000+/40+ offices | Revelio/Tracxn/PitchBook — one LinkedIn-derived family | PLAUSIBLE (high practical confidence) | — |
| Bootstrapped, no outside capital since 1984 | Assertions repeat first-party narrative; only structural evidence is absence of funding records; Wells Fargo lien proves secured debt exists | PLAUSIBLE | Request cap-table rep |
| Claude/MCP connectors exist | Live Anthropic marketplace listing (artifact) | VERIFIED — existence only; "first in industry" UNVERIFIABLE (PR framing) | — |
| Virtuoso "78% deflection / 92% satisfaction" | Every citation traces to one Yardi press release via content mills | UNVERIFIABLE — laundered | CRITICAL |
| $25K/yr per API interface | 2 independent + affiliated + Yardi's own program pages | VERIFIED | — |
| No public REST API; SOAP-only; Breeze no API | Multiple unrelated builders' artifacts | VERIFIED (strongest in dossier) | — |
| "Never furloughed or laid off" | No WARN/tracker entry, but Glassdoor (Mar 2024+) and Blind report quiet cuts | EXAGGERATED (rating upheld; rhetoric reduced per P4.5) | Integrity flag |
| Duffy: "Revenue IQ cannot use cross-client data" | Oct 2025 CA ruling reportedly agrees — **ruling never read; high-authority label withdrawn** | PLAUSIBLE (snippet-grade support) | CRITICAL |
| CEO succession (Teel, Jan 2026) | Multiple independent reports + LinkedIn state | VERIFIED | — |
| WeWork 60% stake ~$337M (2024) | Court-supervised deal, widely reported | VERIFIED | — |
| Benefits (paid healthcare, profit sharing) | Glassdoor + Blind, incl. anti-astroturf negative detail ("no 401k match") | VERIFIED (model verification) | — |
| Units/clients/$4T AUM; CommercialEdge traffic; "450+ partners"; 15 DCs | First-party only | UNVERIFIABLE | NOTABLE |
| SOC 2 / ISO 27001 etc. | CSA STAR verified; rest disputed/unproven | PLAUSIBLE | CRITICAL (binary) |

### 6.3 Where P4 and P4.5 disagree (both shown; red team authoritative)

| Item | P4 said | P4.5 ruled | Why |
|------|---------|-----------|-----|
| Bootstrapped | VERIFIED | **PLAUSIBLE** | Echo chamber: Wikipedia/Forbes/Getlatka repeat the first-party narrative; Forbes profile is company-supplied per P4's own claim-10 ruling; nobody can see a private cap table |
| Headcount 9.3–10K | VERIFIED | **PLAUSIBLE** (high practical confidence) | Pseudo-replication — three vendors, one LinkedIn upstream; number probably right, label unearned |
| Revenue "~$2B triangulated, Medium-low" | PLAUSIBLE band | **Band retained; confidence LOW; "triangulation" withdrawn** | Estimators share one methodology (headcount × benchmark); the rev/employee "cross-check" is the same model re-run |
| "First PM connector on Anthropic marketplace" | VERIFIED (bundled) | **Existence VERIFIED / firstness UNVERIFIABLE** | Firstness exists only in Yardi PR; superlative absorbed into a verified conclusion |
| Oct 2025 CA ruling | "high-authority INDEPENDENT" | **High-authority descriptor WITHDRAWN** | Ruling text never read; dossier phrasing matches Yardi's PR ("does not, and by design cannot") — laundering risk |
| Rabil Ventures = "demonstrable data error" | CONTRADICTED (demonstrable) | **CONTRADICTED (softened: "probable")** | Refutation rests on shared-upstream scraper directories + inference; an SPV sliver can't be excluded |
| Execution score (P2: 9/10) | carried | **7–8** | Contradicted by the dossier's own independent evidence on product quality/UX/APIs |
| G2 Voyager ~4.6 | carried as fact | **4.0–4.6 unresolved range** | P1's conflict was never resolved; the higher figure silently propagated |
| Layoff denial = "textbook reputation-managed workforce reduction" | Key Finding rhetoric | **EXAGGERATED rating upheld; rhetoric cut** | A handful of anonymous reviews out of 3,102 (80% recommend) can't carry that certainty — the one place dossier bias ran *anti*-company |

**What survived the red team fully:** SOAP-only/no-REST/Breeze-no-API; connector existence; Breeze list pricing; benefits; CEO succession; WeWork stake; $25K/yr fee; Kooboo anomaly resolution (unrelated Xiamen firm); the verified absences (zero publications, zero OSS); and P4's quarantine of the 78%/92% metrics.

---

## 7. Academic & IP Landscape

### 7.1 Company Publications
**Zero in 42 years** — no arXiv/SSRN/Scholar output by the company, founder, or any executive (verified absence, INDEPENDENT). Yardi makes no research claims, so there is no discrepancy — but the AI story rests entirely on engineering, not research. Academic ties are philanthropic (IIT Delhi AI school donor, UC Berkeley "Yardi Scholars"), buying goodwill and talent adjacency, not output. Yardi Matrix is a commercial data product, not research — and a conflict-of-interest surface given Duffy (Yardi sells both the pricing software and the market data).

### 7.2 Related Research
The literature that matters is hostile to the product category but **does not study Yardi**: Calder-Wang & Kim (Wharton, FTC-presented) find coordination effects (+$34/mo/unit) among **RealPage/LRO** users; Calvano et al. (AER 2020) supply collusion-without-communication theory — which matters because the enforcement theory does not require data pooling, so Yardi's "no pooling" defense, even if true, is not a complete shield. No peer-reviewed study of Revenue IQ exists. P5's firewall held: RealPage findings were never silently attributed to Yardi (red-team-confirmed).

### 7.3 Patent Landscape
Thin, defensive, peripheral: ~9 identifiable patents/apps in 40 years — building-energy/HVAC optimization and business-name-categorization ML. **No patent covers Voyager, Breeze, or Revenue IQ.** The pricing algorithm is a trade secret; the Duffy courtroom is its only forced-disclosure channel. USPTO shows US7890215 assigned to Wells Fargo Bank (security-interest pattern) — evidence of ordinary secured debt, feeding the bootstrapped-claim downgrade. Snippet-derived data (patent DBs were proxy-blocked); claims unread.

### 7.4 Open-Source Alternatives
A non-factor: 6 repos >100 stars in the entire category; the best (microrealestate, 1.1K stars) approximates only Breeze's CRUD core. No OSS general ledger, affordable-housing compliance, or revenue management exists anywhere. Consequence: no displacement threat, and no build-from-OSS BATNA for an acquirer — but also no legal exclusivity protecting Yardi. The moat is domain depth + data + switching costs, not IP.

---

## 8. Valuation Signals

### 8.1 Business Model
(P6.) Hybrid enterprise SaaS with a fintech-attach engine: quote-priced hosted Voyager (services-heavy, 6–18-month implementations that *are* the moat), published cheap Breeze entry ($1–2/unit/mo — VERIFIED), and the real margin downstream in payments/screening/insurance plus Matrix data and marketplace revenue. Read it as **fintech + data + services on an ERP chassis**. Revenue IQ — the one product with algorithmic pricing power — is the one under antitrust attack; its revenue share is unknown (persistent gap, modeled at 1–5% direct with contagion priced separately).

### 8.2 SaaS Metrics (Estimated)

| Metric | Estimate | Confidence |
|--------|----------|------------|
| ARR | $1.5–2.5B central; tails $1.2–3.0B; working midpoint ~$2B (do not anchor) | **LOW** |
| Customers | 10,000–20,000 clients | LOW (first-party) |
| Growth | ~5–12%/yr | LOW-MEDIUM |
| Gross margin | est. 60–75% (own DCs + heavy services < pure SaaS) | LOW |
| Churn | <5%/yr gross (Voyager, structural) | MEDIUM (directional) |
| Profitability | Decades profitable; self-funded WeWork + serial M&A | MEDIUM |

### 8.3 Valuation Scenarios
Comp anchors (INDEPENDENT, Jul 2026): AppFolio live ~5.5x EV/rev (audited, best anchor); RealPage $10.2B/8.7x (2021 peak vintage); MRI ~$10B **ask** on ~$1B rev; public SaaS median ~3.3x, premium vertical 7–9x.

| Scenario | Revenue | Multiple | Litigation/succession | **EV** |
|---|---|---|---|---|
| Bear | $1.2–1.5B | 3.0–3.5x + discounts | Duffy adverse on per se track ($0.5–2B exposure w/ trebling dynamics); transition stumbles | **~$3.5–5B** |
| **Base** | $1.8–2.2B | 4.5–5.5x | RealPage-style settlement (~$100–400M) + ~10% overhang discount; orderly succession | **~$8–11B** |
| Bull | $2.5–3.0B | 6.5–8x | Duffy cheap/won; share taken from constrained RealPage/distracted MRI; attach rerates | **~$16–22B** |

Working central **~$9–10B** — would make Yardi the category's most valuable asset. Honesty note: at $1.5B true revenue the base is ~$7B; at $2.5B, ~$12B. Getlatka's "$4.9B implied valuation" is rejected as an anchor.

### 8.4 Replication Assessment

| Factor | Assessment |
|--------|-----------|
| Estimated LOC | ~20–50M across the portfolio (inference; zero public code) |
| Team to Rebuild | MVP (Breeze-class): 8–15 eng, 9–15 mo — **agent-swarm-accelerated: ~2,100–4,650 agent-hours, 3–6 months, $1.5–3M, with better UX than the original**. Parity+attach: 30–50 people, 2–3 yrs, $20–40M. Full platform: 300–600 people |
| Timeline (full) | 7–10+ years |
| Cost (full) | $500M–1.5B — and success still improbable (AppFolio is 20 years in at ~$1B with no commercial/affordable/institutional coverage) |

**Build vs Buy: 3/4 overall (hard — buy over build), bimodal.** Core Technology 2, UX/Design 1 (Yardi's weakest surface — any modern rebuild beats it), Integrations 3, **Data/Content 4, Domain Expertise 4**. What can't be automated or bought: the validated compliance corpus (HUD/TRACS/LIHTC edge cases — "the last 2% is the product"), money-transmitter/FCRA/insurance licensing, the Matrix surveyed data network, the partner ecosystem, enterprise trust and data gravity. Do-not-build: revenue management (buying a lawsuit in 2026). Strategic implication: **the SMB flank (Breeze) is genuinely attackable; the enterprise core (Voyager) is not.**

---

## 9. Confidence Matrix

Honesty note up front: **the single most load-bearing number in this dossier — revenue — is LOW confidence on both dimensions**, and every valuation figure inherits that. Ratings below apply red-team adjustments.

| Section | Data Quality | Analysis Confidence | Notes |
|---------|-------------|---------------------|-------|
| Company Profile | MEDIUM | MEDIUM-HIGH | Identity/leadership/succession solid (VERIFIED); headcount PLAUSIBLE (one LinkedIn-derived family); ownership PLAUSIBLE (echo-chamber downgrade) |
| Market Analysis | MEDIUM | MEDIUM | TAM well-bracketed (3 firms + audited bottom-up anchor); SOM bounded by the LOW-confidence revenue; quadrant scores corrected post-red-team |
| Technical Assessment | MEDIUM-HIGH (perimeter) / **LOW (interior)** | HIGH (perimeter) | API/hosting/stack findings artifact-verified (strongest in dossier); but zero code visibility — quality, security, modernization progress unobservable |
| Claims Validation | HIGH | HIGH | 21 claims, canonical bar applied, then red-team audited; label errors found and corrected — residual risk is what snippets can't see |
| Red Team (P4.5) | — | HIGH | Manipulation risk MEDIUM (Virtuoso laundering loop demonstrated); LLM influence UNKNOWN (probe 403-blocked) — dossier is *unaudited*, not *clean*, on this axis |
| Academic/IP | MEDIUM | MEDIUM-HIGH | Verified absences are robust; patent detail snippet-grade (claims unread; DBs proxy-blocked) |
| **Revenue base** | **LOW** | **LOW** | Single-methodology estimate cluster, 2x public spread, no audited data exists, period |
| Valuation | LOW-MEDIUM | MEDIUM | Comp anchors strong (one audited, one print, one ask); output bounded by revenue LOW + un-de-risked Duffy (spread −$0.2B to −$1.5B+ on that item alone) |
| Litigation read | MEDIUM (docket facts) | **LOW-MEDIUM (outcome)** | Key exculpatory ruling never read in original text; per se track live; Revenue IQ revenue share unknown |

---

## 10. Source Provenance Summary

Per P4's tally (~70 discrete evidence data points), adjusted by the red-team audit:

| Trust class | Count | Share | Red-team adjustment |
|---|---|---|---|
| INDEPENDENT (0.8) | ~46 | **~66%** | Effective independence somewhat lower: two pseudo-replication clusters identified (the LinkedIn-derived headcount trio and the scraper-revenue quintet each count as ~one source family, not 3–5 independents), and one content mill (BestCRE) was mis-tagged INDEPENDENT. Adjusted effective ratio ≈ **60%** |
| FIRST-PARTY (0.2) | ~14 | ~20% | Plus four detected leaks of first-party *framing* into analyst voice (firstness superlative, "end-to-end," CA-ruling language, Virtuoso echo) — corrected in this report |
| AFFILIATED (0.4) | ~8 | ~11% | Partner guides, PR-derived trade press — used as indicative only |
| ADVERSARIAL (0.4) | ~2 | ~3% | Quarantine held: plaintiff/competitor content used for docket facts/feature claims only |

**Conclusions resting on INDEPENDENT sources only** include everything rated VERIFIED post-red-team (API architecture, connectors' existence, succession, WeWork, benefits, pricing, verified absences). **First-party influence that survived to this report:** none knowingly — but the LLM-influence surface is **UNKNOWN**: the llms.txt/.well-known probe was 403-blocked in every phase and never completed, and the demonstrated Virtuoso laundering loop proves Yardi's PR successfully colonizes third-party-looking surfaces aimed at snippet-driven research. Treat every blog-tier source repeating Yardi AI metrics as potentially planted.

---

## 11. Recommended Next Steps

**Recommendation: PROCEED WITH CAUTION** — posture-specific, since Yardi is private, family-controlled, and takes no outside capital (no conventional investment or acquisition path exists):

- **Partner/integrate posture:** the moat and stability are real; budget the $25K/yr/interface SOAP gate and 6-month integration timelines; watch for any API-openness shift under the new CEO (it would be the single clearest modernization signal).
- **Compete posture:** attack the SMB flank, not the core. Breeze-class functionality is replicable in ~3–6 months / $1.5–3M with better UX (P6 agent-swarm plan); Voyager-class is a 4/4 on data + domain and is not. Do not build revenue management.
- **Monitor posture:** the two swing variables are the *Duffy* docket and CEO-transition execution (modernization funding, API strategy, retention through the reorg).

**If direct engagement with the company is possible, the diligence list in priority order:**
1. **Audited financials** (item #1 by value) — resolves the 2x revenue spread that moves EV by ±$4B+; plus cap-table representation and any credit-facility covenants (Wells Fargo lien).
2. **Read the actual Duffy record** — especially the Oct 2025 CA ruling text (currently snippet-grade and possibly Yardi-framed) and discovery posture; obtain Revenue IQ's revenue share and contract count.
3. **SOC 2 Type 2 / ISO 27001 attestation letters** — binary item, publicly disputed by one service.
4. **Client references on Virtuoso** — raw deflection/satisfaction data to replace the laundered 78%/92% metrics.
5. **Modernization roadmap** — .NET migration status for the Voyager core, front-end replacement plan, REST/API roadmap, DC-vs-cloud strategy.
6. **Workforce facts** — attrition/termination data 2024–26 vs the "never laid off" claim; retention terms for key compliance/domain staff.
7. **Re-probe llms.txt/.well-known from an unblocked environment** — the LLM-influence surface must be tested before this dossier's evidence base is declared clean.

**Estimated timeline/cost for the above (with company cooperation):** 4–6 weeks, primarily legal review of the Duffy docket (~$25–50K outside counsel) and a standard financial/security data-room pass. Without cooperation: items 2 and 7 are still executable independently (PACER pull + direct probes) at nominal cost and are recommended regardless.

---

## Scorecard (machine-readable)

- AI Reality Score: 3/5
- Revenue Quality: 2/10
- Claims accuracy rate: 15/21 verified or plausible
- Build vs Buy: 3/4 (hard to replicate — buy over build)
- Source independence ratio: ~66% nominal / ~60% red-team-adjusted
- LLM-influence verdict: UNKNOWN (limited indirect absorption detected); manipulation risk MEDIUM
- Overall: PROCEED WITH CAUTION

---
*Generated by Dossier v0.1.0 — automated SaaS due diligence. Phases P1–P7 (incl. P4.5 Red Team), 2026-07-08/09. Every claim above traces to a phase output (01-discovery.md … 06-valuation.md); red-team-adjusted ratings are authoritative where P4 and P4.5 disagreed, and both are shown in §6.3.*
