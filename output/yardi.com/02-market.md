# Market Research: Yardi Systems (yardi.com)

**Phase:** P2 Market
**Date:** 2026-07-08
**Method note:** WebFetch to most analyst/vendor sites is blocked in this environment (Cloudflare/egress-proxy 403), so all data below comes from WebSearch snippets per the Tool Resilience policy. Every data point is tagged with a canonical trust class (FIRST-PARTY 0.2 / AFFILIATED 0.4 / INDEPENDENT 0.8 / ADVERSARIAL 0.4). Competitor marketing about Yardi or the category (AppFolio blog, MRI blogs, Buildium blog, DoorLoop, Re-Leased comparison pages) is tagged ADVERSARIAL, not INDEPENDENT. Gaps flagged inline.

---

## Problem Statement

**Problem:** Real estate owners/operators/managers run complex, regulated, money-moving operations — leasing, rent collection, maintenance, vendor payments, GL accounting, compliance (affordable/HUD/tax credit), investor reporting — historically across spreadsheets, generic accounting tools (QuickBooks), and point solutions. Property management ERP consolidates this into one system of record.

**Who has it:**
- SMB landlords/managers (1–1,000 units) — served by Breeze, AppFolio, Buildium, Rent Manager, TenantCloud.
- Mid-market/enterprise operators and fee managers (1,000–100,000+ units) — served by Voyager, RealPage, Entrata, MRI, ResMan.
- Institutional owners/asset managers (REITs, pension funds, PE real estate) — Voyager/MRI + investment-management modules; Yardi claims clients overseeing ~$4T in assets (FIRST-PARTY figure repeated by Forbes profile — treat as claim).

**How solved without the product:** QuickBooks + Excel + point tools (payments, screening, listing syndication) — viable below ~100 units, painful above. For professional managers the software is the operating system of the business.

**Vitamin or painkiller:** Painkiller. Trust accounting, rent collection, and compliance are legally mandatory functions; switching costs are high (accounting data migration, staff retraining — Voyager implementations reportedly run 6–18 months, $50K–$500K+; INDEPENDENT: BC Solutions/agorareal pricing guides — note these are Yardi consulting/implementation partners, so arguably AFFILIATED; flagged). This stickiness is why category churn is low and why incumbents can carry dated UX for years.

---

## Market Size

### Top-down (analyst estimates — wide scope variance, documented)

Global "property management software" 2025–26 estimates by independent research firms (all INDEPENDENT, but low-cost syndicated research — treat as order-of-magnitude, not point estimates):

| Firm | 2025–26 estimate (global) | Notes |
|---|---|---|
| Grand View Research | $3.6B (2025) → $5.9B (2033), 6.4% CAGR | Narrowest scope |
| SkyQuest | $6.4B (2025) | |
| Mordor Intelligence | $6.5B (2026) | |
| Research Nester | $7.1B (2025) → $7.7B (2026) | |
| Fortune Business Insights | $26.6B (2025) → $29.2B (2026), 9.7% CAGR | Broad scope (likely incl. services/adjacent) |
| Coherent Market Insights | $30.8B (2026) | Broad scope |

Cluster analysis: estimates split into a **core-software cluster ($3.6–7.7B)** and a **broad-scope cluster ($27–31B)** that appears to include property management *services*/adjacent revenue. No first-party (Yardi) market-size figure was found or used — Yardi publishes no TAM claims on its own site (consistent with P1's finding that Yardi is press-shy about numbers).

### Bottom-up (assumptions shown)

- **US rental stock:** ~34.9% of US households rent (JCHS State of the Nation's Housing 2025 — INDEPENDENT, high authority) → ~45–46M renter households; apartment sector (5+ unit buildings) houses 40M+ Americans (NMHC/JCHS — INDEPENDENT). Assume **~46M US rental units**, of which roughly **~30M are professionally/third-party managed** (5+ unit professionally managed apartments plus professionally managed SFR; assumption — the precise professionally-managed count was not recoverable this session, gap flagged).
- **Software spend per unit (realized, incl. attached payments/screening/ancillary):** AppFolio, the only pure-play public comp, realized **$951M revenue on 9.4M units in FY2025 ≈ $101/unit/yr** (SEC 10-K + earnings release — INDEPENDENT, highest authority in this section). Core-software-only list prices are far lower: Breeze $12–24/unit/yr (FIRST-PARTY published pricing), Rent Manager $12–30/unit/yr (FIRST-PARTY-of-competitor pricing page), Voyager reported effective $30–75K/yr for 500–2,000 units ≈ $30–60/unit/yr (partner/consultant pricing guides — AFFILIATED).
- **Bottom-up US TAM:** 30M professionally managed units × $60–100/unit/yr blended (software + realistic ancillary attach) ≈ **$1.8–3.0B core software / $3.0B+ with full fintech attach**; extending to all 46M units at maturity and adding commercial/CRE modules (Yardi, MRI, RealPage all monetize office/retail/industrial portfolios by sqft) plus international (UK/EU/ANZ/Asia) plausibly **1.7–2.2× the US residential figure**.
- **Reconciliation:** bottom-up lands at **$5–8B global core** — consistent with the analyst core-software cluster ($6.5–7.7B for 2026). The $27–31B figures are only defensible if property-adjacent fintech (payments float, screening, insurance) and services are included.

### TAM / SAM / SOM

| Metric | Estimate | Approach | Confidence | Source (trust class) |
|--------|----------|----------|------------|--------|
| TAM (core PM software, global, 2026) | **~$7B** (range $6.5–7.7B) | Top-down cluster of Mordor/SkyQuest/Research Nester, corroborated by bottom-up units×spend | Medium | INDEPENDENT (3 analyst firms) + INDEPENDENT bottom-up (JCHS units, AppFolio 10-K ARPU) |
| TAM (broad: PM software + attached fintech/marketing/data, global) | **$25–30B** | Top-down (Fortune BI, Coherent); scope includes ancillary revenue streams that Yardi/AppFolio actually monetize | Low (scope ambiguity) | INDEPENDENT (2 analyst firms, unverified methodology) |
| SAM (Yardi-addressable: professional operators NA + UK/EU/ANZ, residential + commercial + affordable/senior/coworking, incl. ancillary attach) | **~$9–12B** | Bottom-up: ~30M US professionally managed units × ~$100 realized/unit ($3B) + US commercial/CRE software ($2–3B est.) + international + data/marketplace (Matrix, CommercialEdge) | Low-Medium | Derived; anchored on INDEPENDENT inputs (AppFolio ARPU, JCHS stock) — commercial-side split is an assumption (gap) |
| SOM (Yardi current capture) | **$1.6–3B revenue today** (~20–40% of core TAM); realistic 3-yr obtainable ~$2–3.5B | Yardi's own estimated revenue IS the empirical SOM; growth constrained by mature share + litigation overhang | Low (2× revenue-estimate spread from P1, unresolved) | INDEPENDENT but weak estimators (Getlatka $1.6B vs ~$3B press) — flagged for P4/P6 |

**No market-size figure above rests on first-party sources** (Yardi publishes none). The weakest link is the analyst-firm scope ambiguity and the unresolved 2× spread in Yardi's own revenue.

---

## Competitive Landscape

| Competitor | Domain | Founded | Ownership / financials | Scale signals | Differentiator | Pricing model | Overlap with Yardi | Key source (class) |
|---|---|---|---|---|---|---|---|---|
| **RealPage** | realpage.com | 1998 | Thoma Bravo (PE), took private 2021 for **$10.2B**; ~$1B+ run-rate at take-private; earnings growing on AI push (Bloomberg 2026) | **19M+ units served**, 12,000+ customers | Revenue mgmt/analytics (AIRM/YieldStar), full multifamily suite; owns Buildium | Enterprise quote + per-unit modules | HIGH — closest full-suite rival, esp. mid/large multifamily | INDEPENDENT (TechCrunch, SEC 8-K, Bloomberg); unit count from RealPage = FIRST-PARTY-of-competitor |
| **MRI Software** | mrisoftware.com | 1971 | PE-owned (GI Partners 2015, TA 2017, Harvest 2020); **approaching $1B revenue, ~$400M EBITDA**; owners exploring sale/IPO at **up to $10B** (Reuters via Yahoo, Oct 2025) | 1,450+ employees (likely understated post-acquisitions) | Open/flexible ecosystem ("Partner Connect") vs Yardi's closed stack; strong in commercial + international (UK) | Enterprise quote, modular | HIGH — commercial + enterprise residential; the "open vs closed" foil to Yardi | INDEPENDENT (Reuters/Yahoo, PE Hub, Markets Group) |
| **AppFolio** | appfolio.com | 2006 | **Public (NASDAQ: APPF)** — FY2025 revenue **$950.8M (+20% YoY)**, 9.4M units, 22,096 customers, GAAP op income $153M; 2026 guide $1.10–1.12B | 9.4M units — fastest-growing at scale | Modern UX, AI (Realm-X agents), payments attach; SMB→mid-market residential only, no real commercial offering | Per-unit SaaS, published tiers | MEDIUM-HIGH vs Breeze and low-end Voyager; limited enterprise/commercial overlap | INDEPENDENT (SEC 10-K, GlobeNewswire) — best-quality financials in the category |
| **Entrata** | entrata.com | 2003 | Silver Lake majority (2021, $507M); **Blackstone $200M minority at $4.3B valuation (2025)** | "12M+ residents, 35,000 communities" (self-reported) | AI-first positioning (Layered Intelligence/ELI+), single-stack multifamily OS; Blackstone real-estate ecosystem access | Enterprise quote | HIGH in multifamily; none in commercial | INDEPENDENT (deal coverage: AOL/Reuters, PE Wire); scale metrics FIRST-PARTY-of-competitor |
| **Buildium** (RealPage) | buildium.com | 2004 | Acquired by RealPage 2019 (~$580M) | SMB base; G2 score ~60 in category reports | SMB/community-association management | Published per-unit/tiered | MEDIUM vs Breeze (SMB) | INDEPENDENT (G2 learn page); comparisons from Buildium's own blog = ADVERSARIAL |
| **Rent Manager** (London Computer Systems) | rentmanager.com | 1987 | Private, bootstrapped (no PE/VC found — gap: no revenue figures) | Long-lived loyal SMB/mid base | Flexibility/customization, published cheap pricing ($1–2.50/unit/mo, $200–500 min) | Published per-unit tiers | MEDIUM vs Breeze/low Voyager | Pricing from rentmanager.com = FIRST-PARTY-of-competitor; analyst-rating snippets (SelectHub 85/100) INDEPENDENT |
| **ResMan** | myresman.com | 2000s | Owned by Inhabit (PE roll-up) — financials not public (gap) | Mid-market multifamily + affordable | Affordable-housing compliance focus, BI | Quote | MEDIUM — mid-market multifamily/affordable | INDEPENDENT (Software Advice alternatives listings) — thin data, flagged |
| **DoorLoop / TenantCloud / Innago (fringe)** | — | 2019– | VC-backed SMB long tail | Small | Cheap modern SMB tools | Freemium/low per-unit | LOW today; pipeline threat to Breeze | Their "vs Yardi" comparison content = ADVERSARIAL (used only for feature claims, not facts about Yardi) |

**Landscape reading:** This is a consolidated oligopoly at the top (Yardi, RealPage, MRI, Entrata, AppFolio — every one now valued or estimated between ~$4B and ~$12B) with a fragmented SMB tail. Three of the five majors are PE-owned (RealPage, MRI, Entrata majority), one public (AppFolio), and Yardi alone is founder-owned with no exit pressure — a structural strategic difference. Market-share snippets (6sense-type trackers: Yardi ~10.6% of "real estate software," RealPage 13.4%, Yardi Voyager 1.53% of some US slice) are methodologically opaque web-tracker data — INDEPENDENT but low quality; used only directionally.

**ADVERSARIAL-content note:** The 2026 "best property management software" content surfaced in search is dominated by the vendors themselves reviewing each other (AppFolio's blog ranking itself #1 via G2 citations; MRI-owned blogs publishing "G2 shortlists"; Buildium ranking Buildium; DoorLoop/Re-Leased "Yardi alternatives" listicles). All such claims about Yardi (e.g., "dated UI," "expensive," "slow support") are tagged ADVERSARIAL here — but note they **corroborate** the genuinely INDEPENDENT G2/Capterra user-review complaints from P1 (slow reports, dated UI, no open API), so the direction is credible even if the framing is self-serving.

---

## SWOT Analysis: Yardi Systems

### Strengths (Internal, Positive)
- **End-to-end breadth no rival matches:** residential + commercial + affordable + senior + coworking + investment management + market data (Matrix) + listing marketplace (CommercialEdge/RentCafe). AppFolio and Entrata are residential-only; MRI is closest but assembled via acquisitions. (Convergent INDEPENDENT reviews + ADVERSARIAL comparisons agreeing)
- **Founder-owned, debt-free-by-reputation, no exit clock:** can price patiently and fund R&D through cycles while RealPage/MRI/Entrata owners seek exits at $4–10B marks. (INDEPENDENT: Forbes, deal press)
- **Extreme switching costs / accounting lock-in:** 6–18-month implementations and trust-accounting data gravity make Voyager churn structurally low. (AFFILIATED implementation guides + INDEPENDENT review complaints about migrations)
- **Two-tier land-and-expand:** Breeze at $1–2/unit/mo feeds the funnel; ancillary services (payments, screening, insurance) monetize the base — the same model AppFolio proves at $101/unit/yr realized. (FIRST-PARTY pricing + INDEPENDENT comp math)

### Weaknesses (Internal, Negative)
- **Aging core technology & UX:** ASP.NET/SOAP-era stack; consistent independent user complaints — slow report runs, dated UI, steep learning curve (P1: G2/Capterra, INDEPENDENT; echoed by ADVERSARIAL comparisons).
- **Closed ecosystem:** gated SOAP/WSDL partner program, no open API (Breeze confirmed no API — INDEPENDENT). MRI actively markets openness against this; modern buyers increasingly demand API-first.
- **Weak AI narrative vs. peers:** RealPage touts AI-driven earnings growth (Bloomberg), Entrata raised $200M explicitly for AI agents, AppFolio ships Realm-X; Yardi's public AI evidence is thin (archived GitHub LLM-plugin fork, blog posts — INDEPENDENT, weak signal).
- **Opacity:** no audited financials, conflicting headcount/revenue — harder for enterprise buyers/partners to underwrite than public AppFolio or DOJ-monitored RealPage. (P1 finding)

### Opportunities (External, Positive)
- **RealPage's DOJ handcuffs:** the Nov 2025 consent decree bans RealPage's revenue-management tools from using non-public competitor data, <12-month-old data, and sub-state geographic modeling for 7 years, with a court monitor (DOJ press release, Wilson Sonsini, Paul Weiss — INDEPENDENT). Its flagship differentiator is structurally degraded; Yardi can take share in core PM — *if* its own case resolves tolerably.
- **AI-agent replatforming wave:** 90%+ of large RE firms call AI strategic; 30–50% of proptech VC now AI-directed; agentic leasing/maintenance projected mainstream 2026–27 (PwC/ULI, Commercial Observer, CRETI figures — INDEPENDENT; MRI/Buildium trend posts ADVERSARIAL-tinged). Incumbent with the deepest data (Matrix + Voyager GL) is well-positioned if it executes.
- **Distressed-competitor M&A:** PE owners of MRI seeking exit at up to $10B (Reuters — INDEPENDENT) may create portfolio-carve-out or client-defection opportunities during ownership transition.
- **Multifamily supply wave = operator margin squeeze:** record 2024–25 completions and negative rent growth in professionally managed apartments (JCHS/Cushman — INDEPENDENT) push operators toward efficiency software and ancillary-revenue tools — a tailwind for ops platforms even in a soft rent market.

### Threats (External, Negative)
- **Duffy v. Yardi (existential-adjacent):** W.D. Wash. class action over RENTmaximizer/Revenue IQ; Dec 2024 motion to dismiss DENIED with **per se** treatment (harsher standard than the RealPage court applied — Hogan Lovells, Morgan Lewis, INDEPENDENT); case narrowed (11 landlord defendants dismissed, Apr 2026) and co-defendant FPI settled ($2.8M, Sep 2025), plus a favorable Oct 2025 CA state ruling — but Yardi remains lead defendant in active discovery. The DOJ/RealPage settlement is now a template plaintiffs will demand of Yardi. (INDEPENDENT: Multifamily Dive, law-firm analyses; plaintiff-firm posts ADVERSARIAL-adjacent, used only for docket facts)
- **Regulatory contagion beyond the lawsuit:** state/city algorithmic-pricing bans (a spreading legislative trend post-RealPage) can shrink the revenue-management product category for everyone, and taint bundled suites by association.
- **AppFolio moving upmarket:** +20% growth at $951M, 9.4M units, publicly funded R&D, top G2 satisfaction — directly pressuring Breeze and the low end of Voyager. (INDEPENDENT: 10-K; its self-ranked #1 blogs ADVERSARIAL)
- **Entrata + Blackstone alignment:** Blackstone is one of the world's largest apartment owners; its investment in Entrata (INDEPENDENT deal coverage) risks steering flagship institutional portfolios away from Yardi.
- **Interest-rate cycle:** high-rate environment froze CRE transactions and stressed office owners 2023–25, dampening commercial-module demand and new-logo formation; a rate-cut cycle would reverse this but timing is uncertain. (INDEPENDENT: Fed Minneapolis, Cushman & Wakefield market beats)

### Strategic Implications
| Quadrant | Priority Action |
|----------|----------------|
| S+O (Leverage) | Use founder-owned patience + full-suite breadth to win share while RealPage operates under DOJ monitor and MRI is distracted by exit process; ship credible AI agents on top of Matrix data advantage |
| S+T (Defend) | Wall off institutional accounts from Entrata/Blackstone with investment-management + commercial breadth AppFolio/Entrata lack; settle or win Duffy before it reaches a jury |
| W+O (Improve) | Open the API/ecosystem (neutralize MRI's best attack line) and modernize UX before the AI-replatforming wave gives customers a natural switching moment |
| W+T (Avoid/Mitigate) | Do not let Revenue IQ litigation contaminate the core ERP franchise — structurally separate/retire the pricing product if needed; publish more verifiable numbers to keep enterprise-buyer trust vs public/monitored rivals |

---

## Competitive Positioning: Property Management Software (ERP-class)

### Positioning Matrix

```
                    COMPLETENESS OF VISION →
                    Low                    High
    ┌──────────────────┬──────────────────┐
    │                  │   YARDI (7,9)    │
  H │   CHALLENGERS    │   APPFOLIO (8,8) │
  i │                  │   REALPAGE (7,7) │
  g │                  │   MRI (7,7)      │
  h │                  │   ENTRATA (8,7)  │
    ├──────────────────┼──────────────────┤
A   │  BUILDIUM (5,6)  │                  │
B   │  RENT MGR (4,6)  │                  │
I   │  RESMAN (4,5)    │   VISIONARIES    │
L   │                  │                  │
I   │  NICHE PLAYERS   │                  │
T   └──────────────────┴──────────────────┘
Y
↑
```

### Company Positions

| Company | Quadrant | Vision Score (1-10) | Execution Score (1-10) | Rationale |
|---------|----------|--------------------|-----------------------|-----------|
| **Yardi** | **Leader** | **7** | **9** | Execution: unmatched breadth (all asset classes + data + marketplace), ~$1.6–3B revenue, 40+ yrs of profitable operation, dominant enterprise share, high ratings (4.0–4.6) despite scale (INDEPENDENT). Vision docked: closed ecosystem, dated stack/UX, thin public AI story, and its own revenue-management product is now a legal liability rather than a vision asset. |
| AppFolio | Leader | 8 | 8 | Vision: category-best UX, real shipped AI (Realm-X), fintech-attach model proven at $101/unit/yr. Execution: $951M +20% YoY, 9.4M units, public audited numbers (SEC — INDEPENDENT, strongest evidence in table). Docked on execution scope: residential SMB/mid only, no commercial, no institutional investment mgmt. |
| RealPage | Leader (weakening) | 7 | 7 | Execution: 19M+ units, 12K customers, ~$10.2B take-private, earnings growing (Bloomberg — INDEPENDENT). Docked: DOJ consent decree neuters flagship revenue-mgmt differentiation for 7 yrs with court monitor; PE leverage; reputational damage from ProPublica saga. Vision: broad suite + AI investment, but strategy now partly dictated by settlement terms. |
| MRI Software | Leader (borderline Challenger) | 7 | 7 | Vision: open-ecosystem strategy is the clearest counter-position to Yardi; strong commercial + international. Execution: ~$1B revenue, ~$400M EBITDA (Reuters — INDEPENDENT), but acquisition-assembled product sprawl and a distracting owner exit process at up to $10B. |
| Entrata | Leader (Visionary lean) | 8 | 7 | Vision: most aggressive AI-native repositioning (ELI+), $200M Blackstone capital earmarked for AI, single-stack pitch (INDEPENDENT deal coverage; product claims FIRST-PARTY-of-competitor). Execution: $4.3B valuation, 12M residents claimed, but multifamily-only, private financials unverified, smaller than the big three. |
| Buildium (RealPage) | Niche Player | 5 | 6 | Solid SMB/HOA product with published pricing and decent reviews, but innovation cadence slowed under RealPage ownership and G2 momentum scores lag (G2 learn page — INDEPENDENT). No enterprise or commercial path. |
| Rent Manager (LCS) | Niche Player | 4 | 6 | 35+ years, bootstrapped, loyal SMB base, flexible/customizable, transparent pricing. Vision limited: no discernible AI/platform strategy, minimal marketing presence, US-centric. Analyst-rating parity with Buildium (~85/86 SelectHub — INDEPENDENT). |
| ResMan | Niche Player | 4 | 5 | Mid-market multifamily + affordable-compliance niche under Inhabit (PE roll-up); thin public evidence of scale or roadmap (gap — lowest-confidence row). |

**Scoring criteria** per template: Vision = market understanding/strategy, innovation, pricing strategy, vertical & geographic reach. Execution = product quality, responsiveness, customer experience, operations, revenue/growth. Scores are this analyst's synthesis of the tagged evidence above; the table feeds the P7 quadrant chart.

---

## Market Dynamics

**1. The algorithmic-pricing legal storm (category-defining regulatory threat).**
The DOJ's Nov 24, 2025 proposed settlement with RealPage (7-year term, no fine, no admission) rewrites the rules for the whole category: no pooling of non-public competitor data for pricing recommendations, only ≥12-month-old data, no sub-state geographic modeling, court-appointed monitor, and RealPage must cooperate against co-defendant landlords (DOJ OPA, Wilson Sonsini, Paul Weiss, Fenwick — all INDEPENDENT). *Duffy v. Yardi* applies the same theory to Yardi under a **per se** standard (more plaintiff-friendly than the rule-of-reason posture in the RealPage matter — Hogan Lovells, INDEPENDENT), creating a live circuit-level split. Net effect on the market: revenue-management modules — a major upsell profit pool for RealPage and Yardi — are shrinking/being defanged industry-wide, while compliance-safe "own-data-only" pricing tools become the new spec. Every vendor's marketing now leads with data-governance language. Watch item for P4/P6: what share of Yardi revenue is Revenue IQ-linked (unknown — gap).

**2. Interest-rate cycle and the multifamily supply wave.**
Record multifamily completions (608K units in 2024, 488K in 2025, ~940K under construction at 2025 peak — JCHS/Census via search, INDEPENDENT) plus flat-to-negative rents in professionally managed apartments (−0.6% YoY in Q4 2025) squeeze operator margins — historically *good* for ops-efficiency software demand but bad for new community formation and for landlords' appetite for price increases on software itself. High rates froze CRE transactions 2023–25, muting the commercial modules; multifamily operators describe a "precarious position" (Minneapolis Fed — INDEPENDENT). A rate-cutting cycle would be a demand tailwind for the whole category, especially transaction/investment-management modules.

**3. AI feature race → replatforming risk for incumbents.**
Proptech VC is now 30–50% AI-directed; global proptech investment hit $16.7B in 2025 (+68% YoY); agentic AI (autonomous leasing agents, maintenance triage) is projected mainstream 2026–27 (PwC/ULI Emerging Trends, Commercial Observer — INDEPENDENT; MRI/Buildium trend blogs — ADVERSARIAL-tinged, used only as sentiment confirmation). AI is the first genuine UX-reset event in this category since cloud migration — it temporarily lowers switching costs by giving buyers a reason to re-evaluate. Yardi is the least publicly visible of the top five on AI (INDEPENDENT signal, weak), which is either a disclosure-style artifact (Yardi is press-shy generally) or a real gap — P3 Technical should probe.

**4. Consolidation & capital dynamics.**
Category majors are all mega-cap private assets: RealPage ($10.2B, 2021), MRI (up to $10B sale/IPO explored, Oct 2025), Entrata ($4.3B, 2025), AppFolio (~$8–9B-class public company at typical multiples on $1.1B 2026 guided revenue). PE ownership on three of five majors implies price discipline erosion (need to hit growth cases) and eventual ownership churn. Yardi is the only major with no capital-markets clock — and simultaneously the only one whose founder is 79+ (succession is a P6 diligence item; founder age from public profiles, INDEPENDENT).

**5. Fintech-attach is the real revenue model.**
AppFolio's audited $101/unit/yr (vs $12–24 core list price) proves the category monetizes payments, screening, and insurance more than seat licenses. Yardi's Breeze pricing + ancillary strategy mirrors this (P1). Market-size analyses that ignore this (the $3.6–7.7B core cluster) understate the effective profit pool; this is why SAM above is presented with the attach layer included.

---

## Key Findings

1. **TAM ~$7B core / $25–30B broad, and Yardi may already hold 20–40% of core.** Triangulated top-down (3 analyst firms, INDEPENDENT) and bottom-up (JCHS unit stock × AppFolio's audited $101/unit realized ARPU). Yardi's growth story is therefore share-defense + ancillary attach + international/commercial expansion, not greenfield TAM capture. No first-party market-size numbers exist or were used.
2. **The algorithmic-pricing storm is the single biggest market risk — and it is asymmetric against Yardi.** RealPage has *settled* with the DOJ (certainty, no fine); Yardi is still the lead defendant in a per se-standard class action (*Duffy*). Until resolved, Yardi carries the category's worst legal overhang while its main rival's is capped. Favorable signs exist (case narrowed Apr 2026; Oct 2025 CA ruling on data-use; FPI's modest $2.8M co-defendant settlement suggests plaintiff pragmatism), but discovery continues.
3. **Competitive set has bifurcated: AI-forward challengers (AppFolio, Entrata) vs. scale incumbents (Yardi, RealPage, MRI).** Yardi scores highest on execution (9/10 — breadth + scale + longevity) but only 7/10 on vision (closed ecosystem, dated stack, thin AI evidence). The AI wave is the first event in a decade that could unfreeze this category's notoriously low churn.
4. **Yardi's structural advantage is patience: the only founder-owned major.** Three of five top competitors are PE-owned with exit clocks (MRI actively for sale at up to $10B), one is public. Yardi can absorb a soft-rent, high-rate cycle and fund modernization without external pressure — but faces a founder-succession question no rival has.
5. **Rate cycle + supply wave = near-term demand for efficiency, not expansion.** Record apartment supply and negative professionally-managed rent growth (JCHS, INDEPENDENT) squeeze the customers who pay for this software; positive for ops/AI-efficiency modules, negative for new-logo growth and commercial modules until rates turn.

## Gaps / carried-forward questions
- Yardi revenue ($1.6B vs $3B, 2× spread) unresolved — bounds the SOM row; P4/P6 must triangulate.
- Share of Yardi revenue tied to Revenue IQ/RENTmaximizer — unknown, critical for litigation exposure sizing (P6).
- Precise US professionally-managed unit count (assumed ~30M) — replace with NMHC/RealPage figure if directly fetchable later.
- Yardi units-under-management figure not recoverable (only "millions of units, $4T assets, 15,000 clients" — FIRST-PARTY via Forbes profile).
- ResMan and Rent Manager financials — no independent data (private, no PE disclosures).
- Market-share tracker percentages (6sense-type) are methodologically opaque — do not promote them to VERIFIED anywhere downstream.
