# Executive Summary: Yardi Systems, Inc.
Date: 2026-07-09

## Company at a Glance

| Field | Value | Confidence |
|-------|-------|------------|
| Domain | yardi.com | — |
| Company | Yardi Systems, Inc. — Santa Barbara, CA | High |
| Founded | 1984 by Anant Yardi (42 years founder-run) | High |
| Leadership | **Rob Teel, CEO since Jan 2026** (first non-founder CEO ever); Anant Yardi → Chairman | VERIFIED (P4) |
| Ownership | Private; no outside equity in 42 years — **PLAUSIBLE, not verified** (red-team downgrade: echo-chamber sourcing; a Wells Fargo security interest on a patent proves ordinary secured debt exists) | Medium |
| Headcount | ~9,300–10,000 (LinkedIn-derived family of sources; PLAUSIBLE per red team) | Medium-High |
| Revenue (est.) | **$1.5–2.5B band, tails $1.2–3.0B — LOW confidence.** Scraper-grade estimate cluster sharing one methodology; the popular "$3B" figure has no traceable primary source. No audited figures exist, period | LOW |
| Products | Voyager (enterprise ERP), Breeze (SMB, $1–2/unit/mo), RentCafe, CommercialEdge, Matrix (data), Revenue IQ (pricing — in litigation) | High |
| EV estimate | Bear ~$3.5–5B / **Base ~$8–11B** / Bull ~$16–22B (P6; keyed to an unauditable revenue base) | LOW-Medium |
| Litigation | *Duffy v. Yardi* (W.D. Wash.) — antitrust class action over algorithmic rent pricing; MTD denied Dec 2024 under **per se** treatment; active discovery; **un-de-risked** | High (docket facts) |

**Red Team notice (read first):** LLM-optimized content influence is **UNKNOWN, not none** — the llms.txt/.well-known probe was 403-blocked and never completed, and **limited indirect first-party-phrasing absorption was detected** in four places in the dossier's own analysis (since corrected). Source manipulation risk: **MEDIUM** — one demonstrated laundering loop (Yardi's "78% support deflection" metric propagating through AI-content-mill "review" sites all citing one press release) actively targets exactly the research surface this pipeline uses. All figures below use the red team's downgraded ratings where P4 and P4.5 disagreed.

## Key Strengths

1. **A genuinely durable, dominant franchise.** Widest asset-class coverage in category (residential, commercial, affordable/HUD, senior, military, coworking + investment management + Matrix data + marketplaces), an estimated 20–40% of the ~$7B core market, 42 years of profitable operation, and enough balance-sheet firepower to write a $337M check for 60% of WeWork out of bankruptcy (VERIFIED). The only major in the category with no PE exit clock.
2. **A moat money can't quickly buy: compliance corpus + data network + switching costs.** Trust accounting across 50 states, decades of HUD/LIHTC/TRACS edge cases, the Matrix surveyed dataset, and 6–18-month migrations create structural sub-5% enterprise churn. No OSS substitute exists (verified absence); full replication is estimated at 300–600 people, 7–10+ years, $500M–1.5B — and still improbable. Build vs Buy: 3/4 (hard to replicate — buy over build).
3. **Real (if modest) AI substance and honest financial discipline.** Shipped Claude/MCP connectors on Anthropic's marketplace (VERIFIED artifacts), production ML hiring (PyTorch/spaCy), 3 years of visible LLM experimentation — and, unusually, the company publishes no revenue or TAM claims at all.

## Key Risks

1. **Un-de-risked antitrust overhang.** *Duffy v. Yardi* proceeds under the **per se** standard — harsher than RealPage received — with treble-damage exposure, the DOJ/RealPage consent decree as plaintiffs' template, and Revenue IQ's revenue share unknown. The best exculpatory fact (an Oct 2025 CA state ruling) **was never read by this pipeline** and its characterization may be laundered through Yardi's own PR; it carries no weight here. Scenario swing: roughly –$0.2B (settlement) to –$1.5B+ (adverse) plus suite contagion.
2. **Everything financial is unauditable.** Revenue is a LOW-confidence estimate cluster with a 2x spread; units/clients/$4T-AUM claims are first-party-only; SOC 2/ISO 27001 could not be publicly confirmed (one service disputes them). Revenue Quality: 2/10 — the revenue is likely durable and profitable, but nothing can be verified without a data room.
3. **Succession and a deferred modernization bill land simultaneously.** The first non-founder CEO in company history takes over amid a reorg, employee-reported quiet layoffs the company denies ("never laid off" rated EXAGGERATED), a −2% Glassdoor trend, an EOL AngularJS/jQuery front end, SOAP-only $25K/yr-gated APIs in the AI-agent era, and own-DC single-tenant hosting — while rivals raise hundreds of millions explicitly for AI.

## Technical Assessment

The core is a ~2000s Microsoft monolith: ASP.NET/C#/SQL Server, per-client instances at `{client}.yardiasp13.com` in Yardi's own ~15 (claimed) data centers, SOAP/WSDL-only partner-gated APIs, no public REST/SDK/portal (the dossier's strongest verification — multiple unrelated builders ship Playwright screen-scrapers to route around it), and Breeze has no API at all. Verified users report minutes-long report runs. Zero original open source ever; the GitHub org (all forks) was archived Sep 2025. Against this: genuine modern pockets — production ML hires, EKS/Terraform postings, and shipped MCP connectors. AI Reality Score: 3/5 — real engineering, but every headline AI performance number (78% deflection / 92% satisfaction) is a first-party metric laundered through content mills, and marketing runs ~18 months ahead of verifiable capability.

## Market Position

Leader in a consolidated oligopoly (Yardi, RealPage, MRI, Entrata, AppFolio — all ~$4–12B assets). Execution 7–8 / Vision 7 per the red-team-corrected quadrant (P2's original 9 was not evidence-supported). Tailwinds: RealPage's flagship pricing product is defanged for 7 years under a DOJ monitor; MRI is distracted by a sale process. Headwinds: AppFolio (+20% at $951M audited, category-best UX) attacks the SMB flank; Entrata+Blackstone courts institutional accounts; the AI wave is the first genuine churn-unfreezing event in a decade — aimed at Yardi's weakest surfaces (UX, APIs).

## Valuation Signal

Base-case EV ~$8–11B (working central ~$9–10B) anchored on AppFolio's live ~5.5x EV/revenue, RealPage's 2021 $10.2B print, and MRI's $10B ask — which would make Yardi the category's most valuable asset. Honesty caveat: this all rests on the LOW-confidence revenue base; at $1.5B true revenue the base is ~$7B, at $2.5B ~$12B. Claims accuracy rate: 15/21 verified or plausible (~71%) — pattern "honest-but-opaque," carried with both proven exceptions attached (the layoff denial and the laundered AI metrics).

## Recommendation

**Overall: PROCEED WITH CAUTION**

Yardi is not conventionally investable or acquirable — private, founder-family-controlled, no outside capital wanted — so the recommendation is posture-specific: **partner/integrate** (the moat is real; ride it, but budget for the $25K/yr SOAP gate), **compete on the SMB flank** (Breeze-class functionality is genuinely replicable — ~$1.5–3M and 3–6 months to a better-UX MVP — while Voyager-class is not), or **monitor** (Duffy docket + CEO-transition execution are the two swing variables). Do not underwrite anything financial without audited statements, and do not treat the litigation as de-risked until the actual record is read.

---
*Generated by Dossier v0.1.0 — automated SaaS due diligence*
*Data collected: 2026-07-08/09. Confidence levels noted per section in full report (07-report.md). Red-team-adjusted ratings are authoritative throughout.*
