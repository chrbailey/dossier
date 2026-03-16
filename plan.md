# Plan: Cross-Portfolio Analysis (2-Day Sprint)

## Current State

You have 5 completed dossiers (Okta, Glean, Vercel, Sierra AI, Cerebras) with all 7 phases done, plus 8 validation reports. The existing `cross-dossier-consistency.md` covers only 4 companies (excludes Okta) and identifies several gaps. The `ai-claims-reality-index.html` is a visualization but needs updating.

## What Needs to Be Done

### Day 1: Analysis & New Deliverables

#### 1. Update cross-dossier consistency report to include Okta (2-3 hours)
- Add Okta to all comparison tables (AI Reality Score, Build vs Buy, Verdict calibration)
- Okta changes the portfolio dynamics: it's the only public company, the only mature/profitable one, and the only one with SEC-verified financials
- Re-calibrate scoring frameworks with Okta as an anchor (its metrics are verifiable)
- **File:** Update `output/validation/cross-dossier-consistency.md`

#### 2. Create portfolio-level comparison dashboard (3-4 hours)
A single markdown file with unified comparison tables across all 5 companies:

- **Company scorecard matrix** — side-by-side: revenue, growth, margins, valuation multiple, AI Reality Score, Build vs Buy, verdict
- **Financial comparison** — ARR, growth rate, capital raised, revenue per $1 raised, gross margin, FCF margin
- **Moat comparison** — type of moat (hardware/community/connectors/data/brand), depth score, time-to-replicate
- **Risk heat map** — competitive, technical, culture/team, regulatory, customer concentration
- **Stack position map** — where each company sits in the AI infrastructure stack (from the cross-dossier report's Layer 1-4 framework)
- **File:** Create `output/cross-portfolio-analysis.md`

#### 3. Fill the 7 gaps identified in cross-dossier-consistency.md (2-3 hours)
The existing report flags these as missing. Research and write sections for:

1. **Cross-dossier valuation comparable table** — compare the 5 companies against each other, not just external peers
2. **Standardized "no proprietary model" treatment** — consistent framework for penalizing/crediting LLM dependence
3. **Systemic risk section** — correlated risk if AI spending cools; all 5 companies' exposure
4. **NRR as blocking gap** — unified statement across all dossiers
5. **Path-to-profitability models** — when each company reaches cash flow breakeven (Okta already there)
6. **Founder/CEO risk matrix** — key-person risk, succession, attention fragmentation for all 5
7. **Regulatory/compliance comparison** — EU AI Act, CFIUS, data governance exposure per company
- **File:** Add to `output/cross-portfolio-analysis.md`

### Day 2: Synthesis & Polish

#### 4. Portfolio investment thesis document (2-3 hours)
Synthesize everything into an investor-facing portfolio view:

- **Thesis:** What is the investment thesis for this 5-company portfolio?
- **Correlation analysis:** Which companies rise/fall together? Which are hedges?
- **Portfolio construction:** If you had $100M, how would you allocate across these 5?
- **Scenario analysis:** Bull case, base case, bear case for the portfolio
- **12-month watchlist:** Key events/metrics to monitor per company
- **File:** Create `output/portfolio-thesis.md`

#### 5. Update the HTML visualization (2-3 hours)
Update `output/ai-claims-reality-index.html` to include:
- Okta data points
- Portfolio-level charts (radar chart comparing all 5, scatter plot of growth vs. multiple)
- Risk heat map visualization

#### 6. Apply pending corrections from cross-dossier analysis (1-2 hours)
The cross-dossier consistency report recommends:
- Glean AI Reality Score: 4.0 → 3.5
- Glean Build vs Buy: 2.7 → 2.85-2.95
- Apply these to the actual dossier files (04-claims.md, 06-valuation.md, executive-summary.md for Glean)
- Add cross-reference valuation tables to each company's P6 report

#### 7. Commit and push (30 min)
- Commit all new/updated files
- Push to `claude/analyze-github-dossier-eRzAL`

## Execution Approach

- Steps 1-3 can be partially parallelized using sub-agents
- Step 4 depends on steps 1-3 being complete
- Steps 5 and 6 are independent and can run in parallel
- Total estimated effort: ~14-18 hours of active Claude Code work across 2 days

## Files Created/Modified

| File | Action |
|------|--------|
| `output/validation/cross-dossier-consistency.md` | Update (add Okta) |
| `output/cross-portfolio-analysis.md` | Create (new) |
| `output/portfolio-thesis.md` | Create (new) |
| `output/ai-claims-reality-index.html` | Update (add Okta, new charts) |
| `output/glean.com/04-claims.md` | Update (score corrections) |
| `output/glean.com/06-valuation.md` | Update (score corrections) |
| `output/glean.com/executive-summary.md` | Update (score corrections) |
| Each company's `06-valuation.md` | Update (add cross-reference table) |
