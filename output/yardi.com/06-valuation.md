# Valuation & Replication: Yardi Systems

**Phase:** P6 Valuation & Replication
**Date:** 2026-07-08
**Method note:** Desk synthesis of P1–P5 plus three WebSearch calls for public-comp multiples (AppFolio market data, MRI sale-process reporting, 2026 SaaS multiple surveys — all INDEPENDENT). No first-party Yardi figure is used as evidence anywhere in this phase; company numbers appear only as "claims" rows.

**Red-team adjustments applied (per P4.5 directives — this phase uses the downgraded ratings, not P4's originals):**
1. Revenue treated as a **single-methodology estimate cluster, NOT triangulation** — confidence LOW; scenario tails widened beyond the $1.5–2.5B band (modeled $1.2–3.0B).
2. **Execution score 7–8** used for competitive-position inputs, not P2's original 9.
3. G2 Voyager rating carried as **4.0–4.6 (unresolved range)** everywhere.
4. **Bootstrapped** (no outside equity) and **headcount 9.3–10K** treated as **PLAUSIBLE**, not VERIFIED (echo-chamber / pseudo-replication findings).
5. **Duffy v. Yardi:** the Oct 2025 CA state ruling is treated as **unread/snippet-grade** (possible laundering of Yardi's own framing) — it carries no exculpatory weight here; legal scenarios explicitly include the harsher **federal per se track** (MTD denied Dec 2024, active discovery).
6. No "first-mover / first PM connector" superlatives (firstness = FIRST-PARTY framing, UNVERIFIABLE); Virtuoso 78%/92% metrics excluded from all value math (UNVERIFIABLE, laundered).
7. Founder succession modeled as a **completed event with execution risk** (first non-founder CEO, Rob Teel, Jan 2026), not an open question.

---

## Business Model

**Revenue model — hybrid enterprise SaaS with a fintech-attach engine (facts vs inference separated):**

- **Voyager (enterprise core):** quote-priced, hosted single-tenant instances (`{client}.yardiasp13.com`, own data centers — INDEPENDENT, P3). Effective pricing reported at ~$30–75K/yr for 500–2,000-unit operators (AFFILIATED implementation-partner guides — treat as indicative only). Contract structure is subscription/hosted ASP; legacy perpetual-license customers exist but the hosted "Yardi Cloud" tiers (SaaS / SaaS Select / Private Cloud — CLAIMED) are the delivery model. This is a sales-led, services-heavy motion: 6–18-month implementations at $50K–500K+ create the switching-cost moat and a large professional-services revenue layer (consistent with the P4 hiring-mix finding: job postings dominated by Client Services/Consulting roles).
- **Breeze / Breeze Premier (SMB land-and-expand):** published $1–2/unit/mo ($100–400 minimums) — VERIFIED list price. Deliberately cheap entry; real monetization is downstream.
- **Ancillary fintech attach — where the margin actually is (inference anchored on the audited comp):** AppFolio's SEC-audited FY2025 economics prove the category realizes **~$101/unit/yr against $12–24 core list price** — i.e., payments processing, tenant screening, and renters insurance generate 4–8x the seat-license revenue. Yardi runs the same playbook (screening, insurance, payments bundled into Breeze/RentCafe; P1). For Yardi the attach layer plus RentCafe (leasing/marketing), Matrix (market-data subscriptions), and CommercialEdge (listing marketplace) mean the "software company" is substantially a **payments + data + services company wearing an ERP shell**. No Yardi-specific attach figures exist (private) — the AppFolio anchor is the best available proxy, and Yardi's enterprise mix likely attaches at a lower *rate* but far higher *ACV*.
- **Revenue IQ (revenue management):** the one product with algorithmic pricing power — and the one under antitrust attack (Duffy). Its revenue share is **unknown** (gap carried from P2/P4); scenarios below treat it as 1–5% of revenue directly, with contagion risk to the suite priced separately.

**Customer segments:** SMB landlords (Breeze) → mid-market/enterprise operators and fee managers (Voyager) → institutional owners/REITs (Voyager + investment management + Matrix). Breadth across asset classes (residential, commercial, affordable/HUD/LIHTC, senior, military, coworking) is the widest in category (directionally INDEPENDENT via reviews; "end-to-end" phrasing avoided per P4.5 — it is Yardi's own language).

**GTM:** enterprise sales-led with a partner/consultant ecosystem; SMB self-serve-ish with published pricing; ecosystem deliberately gated ($25K/yr/interface SOAP partner program — VERIFIED, survived red team). No PLG in any modern sense; effectively zero developer-community presence (P3/P4 absence signals).

**Estimated revenue range:** see table below — **$1.5–2.5B central band, $1.2–3.0B modeled tails, confidence LOW** (scraper-grade estimate cluster sharing one methodology; no audited data exists, period).

---

## SaaS Metrics (Estimated)

| Metric | Estimate | Confidence | Basis |
|--------|----------|------------|-------|
| ARR Range | **$1.5–2.5B central; tails $1.2–3.0B; working midpoint ~$2B (do not anchor)** | **LOW** (red-team: single-methodology estimate cluster, not triangulation) | Getlatka $1.6B / ZoomInfo $2.2B / Owler-IncFact-Growjo $1.5–2.2B — all scraper-grade, likely shared methodology (headcount × benchmark). Rev/employee sanity: 9,477 est. staff × $160–250K (services-heavy, large Pune offshore base) = $1.5–2.4B — same method, not corroboration. "$3B" press figure has no traceable primary source (P4: UNVERIFIABLE outlier) but the widened bull tail acknowledges it could be partially right |
| Customer Count | 10,000–20,000 clients | LOW | First-party only (15K→20K claimed; UNVERIFIABLE). Floor inferred from ecosystem scale: 3,102 Glassdoor reviews, ~450-partner claim, RealPage's 12K customers at smaller revenue |
| Units Under Management | ≥8M residential units directionally credible; unverified | LOW | First-party (8M+ res, 7B+ sqft commercial). Sanity: AppFolio 9.4M audited units at ~$1B revenue makes ≥8M enterprise-priced units consistent with a $1.5–2.5B Yardi |
| Growth Rate | ~5–12%/yr (est.) | LOW-MEDIUM | Headcount ~5.6K (2023) → ~9.5K (Dec 2025) is a strong expansion signal (PLAUSIBLE per red team — LinkedIn-derived family), but partly offshore/services buildout; category grows 6–10%; mature 20–40% share-holder cannot far outgrow its market. No direct revenue time series exists |
| ACV | Blended ~$100–170K/client if 12–20K clients on $2B; Voyager $30–75K+ core (higher with modules/attach); Breeze $1.2–5K | LOW | Arithmetic on two low-confidence inputs; Voyager figure from AFFILIATED partner pricing guides |
| Gross Margin | est. 60–75% (below pure-SaaS peers) | LOW | Inference: own 15-DC hosting (capital in the margin stack), heavy professional services, per-client single-tenant instances — structurally below AppFolio-style pooled multi-tenancy |
| Churn / Retention | Very low enterprise churn (est. gross churn <5%/yr Voyager) | MEDIUM (directional) | Structural: trust-accounting data gravity, 6–18-month implementations, migration pain in reviews (INDEPENDENT). Category-wide low churn is well documented |
| NRR Signals | Positive: module/attach expansion, per-unit pricing scales with portfolios, ancillary fintech | MEDIUM (directional, no number) | Model mirrors AppFolio's audited attach economics; Yardi-specific NRR unknowable from outside |
| Profitability | Decades profitable; funded $337M WeWork stake + serial acquisitions from balance sheet | MEDIUM | WeWork 60% stake VERIFIED (survived red team); no P&L visible. Wells Fargo security interest (P5) shows ordinary secured debt exists — "debt-free" folklore not assumed |

---

## Valuation Scenarios

**Comp anchors (INDEPENDENT, July 2026):**

| Comp | Metric | Multiple | Quality of anchor |
|---|---|---|---|
| AppFolio (NASDAQ: APPF) | EV ~$5.4B / TTM revenue ~$0.99B, +20% growth, GAAP-profitable | **~5.5x EV/rev** | Best anchor — audited, same category, traded today |
| RealPage take-private (Thoma Bravo, 2021) | $10.2B on ~$1.17B revenue | **~8.7x EV/rev** | Real print, but 2021 peak-multiple vintage — treat as ceiling-era |
| MRI Software sale process (2025–26) | Up to $10B sought on ~$1B rev / ~$400M EBITDA | **~10x rev / ~25x EBITDA — an ASK, not a print** | Reuters-reported; aspiration, not clearing price |
| Entrata (Blackstone minority, 2025) | $4.3B valuation, revenue undisclosed | n/m | Directional only |
| Public SaaS median (Mar–Jun 2026) | — | ~3.3x median; premium vertical SaaS 7–9x | Floor/ceiling context |

**Yardi-specific adjustments:** (+) category-best breadth, structurally low churn, fintech attach, decades of profitability, no leverage pressure; (−) growth likely below AppFolio's 20%, dated stack/UX with modernization debt (EOL front end, SOAP-only APIs, own-DC single-tenant hosting), **Duffy overhang un-de-risked** (per red team: the exculpatory CA ruling is unread and gets no weight; the federal per se track — the harshest posture available — is live in discovery, with treble-damage exposure and the DOJ/RealPage consent decree as plaintiffs' template), **first non-founder CEO in 42 years** (Jan 2026, during a reorg with declining Glassdoor trend), revenue unauditable (any buyer prices in an information-risk discount), and G2 satisfaction only bracketable at 4.0–4.6.

| Scenario | Revenue assumption | Multiple | Litigation/succession treatment | **EV** |
|---|---|---|---|---|
| **Bear** | $1.2–1.5B (low tail — estimators overstated; services revenue larger than assumed) | 3.0–3.5x (public median; legacy discount; information-risk discount) | Duffy goes badly on the per se track: adverse verdict or coercive settlement ($0.5–2B after trebling dynamics — speculative, damages theory untested against Yardi's architecture), Revenue IQ retired, conduct remedies taint suite pricing; CEO transition stumbles into modernization crunch | **~$3.5–5B** (≈ multiple × revenue minus $0.5–1.5B litigation/discount load) |
| **Base** | $1.8–2.2B (center of cluster) | 4.5–5.5x (AppFolio anchor, discounted for slower growth/legacy stack, credited for breadth/moat/profitability) | Duffy settles RealPage-style: conduct remedies + a manageable cash settlement (~$100–400M); Revenue IQ defanged but core ERP unharmed; succession orderly (22-yr insider) — apply a ~10% combined overhang discount | **~$8–11B** |
| **Bull** | $2.5–3.0B (high tail — the $3B folklore proves partially right; attach economics richer than modeled) | 6.5–8x (premium-vertical band; RealPage-print territory; justified only if growth >12% and AI/modernization narrative lands) | Duffy resolved cheaply or won; Yardi takes share from DOJ-constrained RealPage and distracted-MRI; fintech attach + Matrix data monetization rerate the asset | **~$16–22B** |

**Working central estimate: EV ~$9–10B** — which would make Yardi the most valuable asset in the category (consistent with MRI's $10B *ask* on half the revenue, and RealPage's $10.2B 2021 print). Honesty note: this rests on a LOW-confidence revenue base; if true revenue is $1.5B the base case is ~$7B, if $2.5B it is ~$12B. The single highest-value diligence item remains audited financials; the second is reading the actual Duffy record (per red team, the best exculpatory fact in the file is currently snippet-grade).

**Getlatka's "$4.9B implied valuation" (P1) is rejected** as an anchor — it applies ~3x to the lowest revenue estimate; even the bear case here only reaches that zone with a litigation shock included.

---

## Replication Assessment

Grounded in CODE-OBSERVED/INDEPENDENT findings (P3/P5), not claimed capabilities. Core constraint: **zero Yardi source code is public** (all-forks GitHub org, archived Sep 2025), so LOC figures are inferences from product surface, age, and acquisition count (19–24 acquisitions).

### Scope

| Component | Estimated LOC | Complexity | Notes |
|-----------|--------------|------------|-------|
| Voyager core ERP (GL/trust accounting, leases, AP/AR, reporting engine) | 8–20M (inference: 40 yrs accretion, ASP.NET/SQL monolith) | Very High | The GL + trust-accounting engine is the hard kernel — legally load-bearing (state trust-account rules), 40 years of client-driven edge cases |
| Asset-class modules (commercial CAM/recoveries, affordable HUD/LIHTC/TRACS/Section 8, senior living, military, coworking) | 5–15M combined | Very High | The compliance corpus is the deepest moat: HUD 50059/TRACS file formats, LIHTC certifications, state-by-state rules — encoded over decades, no OSS equivalent exists (P5: category OSS ≈ 6 repos >100 stars, none with GL/compliance) |
| RentCafe (marketing/leasing/resident portals, call-center CRM) | 2–5M | Medium | Conventional web CRM/portal surface; AngularJS/jQuery-era front end (CODE-OBSERVED fork cluster) |
| Breeze (SMB SaaS) | 0.5–2M | Low-Medium | Newer, simpler; microrealestate (1.1K-star OSS) already approximates its CRUD core |
| Payments/screening/insurance rails | 1–3M + partnerships | High (regulatory, not technical) | Money-transmitter licensing, FCRA screening compliance, insurance agency licensure, bank/bureau integrations — legal artifacts, not code |
| Revenue IQ | 0.1–0.5M | Medium code / toxic context | Trade secret, no patent (P5); rebuilding it now means rebuilding the defendant's product mid-antitrust-storm |
| Matrix + CommercialEdge (data network, marketplace) | 1–3M + data ops | High (data, not code) | Claims 92K+ properties/18M+ units tracked — a surveyed proprietary dataset with a human collection operation; unpurchasable |
| Integration layer (SOAP interfaces, ~450-partner claimed ecosystem) | 0.5–1M | Medium code / High ecosystem | The WSDLs are replicable; the partner network and per-tenant field mappings are not |
| Hosting/ops (claimed 15 DCs, per-client instances) | n/a (infra) | High capital | A replicator would use hyperscalers — one of the few places the clone is *structurally better* than the original |
| **Total portfolio** | **~20–50M LOC (inference, wide)** | — | Directly comparable to a mid-size ERP vendor; the number matters less than the compliance/data content embedded in it |

### Team & Timeline

| Scenario | Team Size | Timeline | Cost |
|----------|-----------|----------|------|
| **MVP** (Breeze-class SMB PM: properties/leases/rent/maintenance, basic double-entry accounting, tenant portal, payments via Stripe-class PSP) | 8–15 eng + 1–2 PM/domain + design | 9–15 months | **$3–6M** (fully loaded ~$250K/head/yr) — agent-swarm-accelerated: potentially 4–8 months / $1.5–3M (see below) |
| **Feature Parity — Breeze+attach** (screening, insurance, marketing syndication, owner reporting; SMB competitive with Buildium/low-end AppFolio) | 30–50 (incl. compliance counsel, payment-ops) | 2–3 years | **$20–40M** + licensing/partnership costs (money-transmitter or PSP-agent model, FCRA program, insurance agency) |
| **Full Platform** (Voyager-class: multi-asset-class ERP + affordable/HUD compliance + investment mgmt + data network + ecosystem) | 300–600 eng/domain/compliance | 7–10+ years | **$500M–1.5B**, and success is still improbable — AppFolio, the best-funded modern attacker, is 20 years in at ~$1B revenue with **no** commercial, affordable-compliance, or institutional investment-management offering. The binding constraints are compliance corpus, data network, enterprise trust, and migration friction — none of which money converts to time efficiently |

**Cost estimation basis:** engineering at $200–300K fully loaded US-blend (offshore mix reduces ~30%); infrastructure for a cloud-native clone is trivial relative to payroll ($1–5M/yr at scale); data acquisition for a Matrix equivalent is effectively a standing survey company (~$10–30M/yr operating cost, years to reach coverage credibility). GTM excluded per prompt.

---

## Agent Swarm Plan

What a Claude Code agent swarm could actually build, honestly bounded. Overall judgment: **a swarm compresses the MVP tier dramatically, helps modestly at parity tier, and is nearly irrelevant to the full-platform moat** — because the moat is regulatory knowledge, licenses, data, and trust, not code volume.

### Component Breakdown

| Component | Agent Type | Tools Needed | Agent-Hours | Automatable? |
|-----------|-----------|--------------|-------------|-------------|
| Data model + double-entry accounting core (SMB-grade) | Code-gen + test-gen agents (TDD loop) | Bash, git, Postgres MCP, property-based testing harness | 300–600 | **Yes** — well-documented domain (accounting primitives); property-based tests catch invariant violations |
| Property/lease/tenant CRUD + workflows | Code-gen swarm (parallel per-module) | Same + schema-migration tooling | 200–400 | **Yes** — commodity; microrealestate is an existence proof |
| Tenant/owner portals + leasing site | Frontend agents + design-system agent | Playwright MCP (visual verification), component library | 200–400 | **Yes** — and would exceed Yardi's dated UX (its weakest verified surface: 4.0–4.6 reviews citing "minutes to run reports," EOL AngularJS) |
| Reporting engine (rent roll, delinquency, owner statements, T-12) | Code-gen + domain-research agents | WebSearch (report-format research), SQL, PDF generation | 150–300 | **Mostly** — formats are industry-standard; validation needs practitioner review |
| Payments integration (PSP-agent model, not own rails) | Integration agents | Stripe/Adyen APIs, sandbox accounts | 100–200 | **Partially** — code yes; money-transmission licensing, sponsor-bank relationships, risk/compliance ops **no** |
| Screening integration | Integration + compliance-research agents | Bureau sandbox APIs (TransUnion et al.) | 80–150 | **Partially** — code yes; FCRA permissible-purpose program, bureau credentialing (onsite audits) **no** |
| Affordable-housing compliance (HUD 50059, TRACS, LIHTC) | Research agents mining public HUD/IRS specs + code-gen | WebFetch/WebSearch on HUD handbooks, TRACS specs (public!) | 500–1,500 | **Surprisingly partially** — the *specs* are public documents; agents can encode them. But certification against TRACS, edge-case correctness (audit exposure for clients), and credibility with agencies require humans and years. Highest-risk module to ship wrong |
| Commercial (CAM reconciliation, recoveries, % rent) | Domain-research + code-gen | Lease-abstraction test corpus (must be acquired) | 400–800 | **Partially** — logic encodable; the test corpus of real leases is the bottleneck |
| Yardi/competitor data migration tooling | Integration agents | The community's own artifacts: yhavin/yardi-sdk (SOAP), Playwright scraping repos (P3) | 150–300 | **Yes, ironically** — the independent workaround ecosystem is a ready-made extraction toolkit; this is the attacker's wedge into Yardi's base |
| Market-data network (Matrix clone) | Research/scraping agents | WebSearch, listing-site APIs | n/m | **No** — public scraping yields listing-grade data; Matrix's surveyed ground-truth (rents actually achieved, concessions) needs a human survey operation |
| Revenue management | — | — | 0 | **Do not build** — the category is under DOJ/court-imposed constraint (RealPage consent decree terms, Duffy per se track); a 2026 entrant building pooled-data pricing is buying a lawsuit |
| **Total (Breeze-class MVP)** | ~10–20 concurrent agents + 3–5 human staff (domain expert, compliance counsel, payments ops, QA lead) | | **~2,100–4,650 agent-hours** (≈ 3–6 calendar months wall-clock with parallelism) | MVP: largely yes. Parity: half. Voyager: no |

**Dependencies:** accounting core → everything; schema/data model → CRUD modules (parallelizable after); portals and reporting parallel; integrations last (need live sandbox credentials — human-gated); compliance modules independent but human-verification-gated.

### What Can't Be Automated

- **The compliance corpus as *validated* knowledge:** agents can read HUD handbooks and TRACS specs, but 40 years of "what the auditor actually accepts," state trust-accounting quirks, and client-driven edge cases live in Yardi's code and its consultants' heads. Shipping affordable-housing software that's 98% right creates audit liability for customers — the last 2% is the product.
- **Licenses and regulated partnerships:** money-transmitter licensing (or sponsor-PSP agreements), FCRA screening credentialing, insurance agency licensure, bank relationships, SOC 1/SOC 2 attestation history. Calendar time + lawyers + audits; zero agent leverage.
- **The Matrix data network:** a proprietary surveyed dataset (claimed 92K properties) with a standing human collection operation and 15+ years of history. Scraping does not reproduce ground-truth rent/concession data.
- **The 450-partner (claimed) integration ecosystem and per-tenant field mappings** — network effects accreted over decades; partners integrate where the customers are.
- **Enterprise trust and switching costs:** REITs and fee managers do not move their general ledger to a startup; Voyager migrations run 6–18 months *toward* Yardi — the same gravity works against any replicator. 42 years of operational track record is not compressible.
- **Customer data gravity:** decades of client financial history inside per-client Yardi databases, exportable only via gated SOAP or screen-scraping.

---

## Build vs Buy Score

Scale: 1 = easy to replicate … 4 = near-impossible.

| Factor | Score (1-4) | Rationale |
|--------|------------|-----------|
| Core Technology | **2** | The stack is dated commodity (ASP.NET/SQL monolith, SOAP, EOL front end — INDEPENDENT, P3); nothing technically exotic anywhere. A competent team (or agent swarm) rebuilds the *SMB* functionality readily; the enterprise GL kernel is a 3 on effort but still conventional engineering. No patents protect any of it (P5: ~9 peripheral patents, none on Voyager/Breeze/Revenue IQ) |
| Data/Content | **4** | Matrix surveyed dataset + decades of client financial data + the encoded compliance corpus. No OSS equivalent exists (VERIFIED absence, P5); not purchasable; survey network takes years to gain credibility |
| Integrations | **3** | SOAP interfaces themselves are replicable (community SDKs prove it), but the claimed ~450-partner ecosystem, bank/bureau/payment partnerships, and regulatory credentialing are multi-year, human-gated. Scored 3 not 4 because modern open APIs let an attacker build a *different, better* ecosystem — as MRI markets and AppFolio demonstrates |
| UX/Design | **1** | Yardi's weakest surface: "minutes to run reports," dated UI, steep learning curve (INDEPENDENT verified-user reviews; G2 carried at 4.0–4.6 unresolved). Any modern rebuild beats it; AppFolio already does |
| Domain Expertise | **4** | Trust accounting across 50 states, HUD/LIHTC/Section 8/military/senior-living rules, CAM reconciliation practice — 40 years of regulatory accretion. This, not IP, is the moat (P5 conclusion, red-team-affirmed). Hireable only in small quantities; Yardi/RealPage/MRI employ most of it |
| **Overall** | **3 — Hard to replicate (buy over build)** | Bimodal: the *SMB flank scores ~2* (Breeze is genuinely attackable — by agent swarms, by AppFolio, by OSS-plus), but the *enterprise core scores 4* on the two factors that gate revenue (data, domain). No legal exclusivity protects Yardi (no patents, no OSS threat either) — the moat is depth + switching costs + ecosystem, which money cannot rapidly convert into. An acquirer has no credible build-BATNA for Voyager-class capability |

---

## Key Findings

1. **EV range $3.5–5B bear / $8–11B base / $16–22B bull; working central ~$9–10B — on a LOW-confidence revenue base.** Anchored to AppFolio's live ~5.5x EV/revenue (audited), RealPage's $10.2B/8.7x 2021 print, and MRI's $10B ask on ~$1B revenue. The base case would make Yardi the category's most valuable asset. Everything keys off an unaudited $1.5–2.5B revenue cluster (tails widened to $1.2–3.0B per red team — these estimators share one methodology; this is an estimate cluster, not triangulation). Audited financials are diligence item #1.

2. **Duffy v. Yardi is the swing factor between bear and base, and it is currently *un-de-risked*.** Per the red team, the best exculpatory fact (Oct 2025 CA ruling) was never read and its characterization may be laundered through Yardi's own PR — it gets no weight here. The live federal track applies *per se* treatment (harsher than RealPage received), with treble-damage exposure, the DOJ/RealPage consent decree as plaintiffs' template, and Revenue IQ's revenue share unknown. Scenario spread from this one item: roughly –$1.5B (adverse) to –$0.2B (RealPage-style settlement) plus a suite-contagion discount until resolved. Reading the actual docket is diligence item #2.

3. **The moat is real but it isn't IP — it's domain depth, data, and switching costs.** No patents on core products, no OSS substitute (verified absences, P5). Build-vs-Buy overall: **3 (Hard)** — but bimodal: Breeze-class SMB functionality scores ~2 and is genuinely swarm-replicable (~2,100–4,650 agent-hours, ~$1.5–3M, 3–6 months to a *better-UX* MVP), while Voyager-class enterprise capability scores 4 on Data and Domain Expertise, where agents provide almost no leverage (licenses, audits, surveyed data, 40 years of compliance edge cases, enterprise trust).

4. **The margin engine is the attach layer, not seats.** The only audited comp (AppFolio, SEC) realizes ~$101/unit/yr vs $12–24 list — payments/screening/insurance are 4–8x the software revenue. Yardi's business should be read as fintech + data + services on an ERP chassis; any valuation model priced on "property management software TAM" alone understates the profit pool, and any replication plan without licensed payment rails misses the business.

5. **Succession and modernization risk now coincide.** The first non-founder CEO in 42 years (Rob Teel, Jan 2026 — VERIFIED, survived red team) takes over amid a reorg, quiet-cut reports, a −2% Glassdoor trend, an EOL front end, SOAP-only APIs in an AI-agent era, and competitors raising hundreds of millions explicitly for AI (execution score carried at **7–8 per red team, not 9**; G2 carried at **4.0–4.6 unresolved**; bootstrapped and headcount carried as **PLAUSIBLE**). The bull case requires this transition to fund and land a decade-deferred modernization; the bear case is the transition fumbling it while Duffy runs. Both are live — which is precisely why the scenario spread is wide.
