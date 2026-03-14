# Research Program — Dossier Autoresearch Configuration

## Purpose

This file is the dossier equivalent of Karpathy's `program.md` in autoresearch.
The human edits this file to steer research strategy. The agent reads it before
each research sprint. You stop writing research. You start writing instructions
for how an agent should think about doing research.

## Research Loop Rules

### Sprint Budget
Each research sprint (one attempt at a phase) runs until the phase output is written.
There is no time limit, but there IS a quality gate: the Evidence Density Score (EDS).

### Iteration Protocol
```
1. RUN the phase with current strategy
2. EVALUATE the output → compute EDS via scripts/evaluate_phase.py
3. COMPARE to previous best
   ├── Improvement? → SAVE as new best, log in PROGRESS.md
   └── Regression?  → DISCARD, revert to previous best
4. REFLECT → which sources yielded weak results?
5. ADJUST → select next strategy variant
6. REPEAT until EDS ≥ threshold OR max_attempts reached
```

### Quality Thresholds (EDS)
| Phase | Min EDS | Max Attempts |
|-------|---------|-------------|
| P1 Discovery | 0.40 | 2 |
| P2 Market | 0.45 | 2 |
| P3 Technical | 0.50 | 2 |
| P4 Claims | 0.55 | 4 |
| P5 Academic | 0.40 | 2 |
| P6 Valuation | 0.45 | 3 |
| P7 Report | 0.50 | 2 |

P4 gets the most attempts because it's the analytical core and benefits most from
iteration. P1/P5 get fewer because their data sources are more deterministic.

### Never Stop Rules
- If a sprint produces EDS = 0 (total failure), still count it and move on
- If EDS is improving on each attempt, keep going up to max_attempts
- If EDS plateaus (same score twice), stop early — diminishing returns

---

## Research Strategy Variants

### Phase 4: Claims Validation (most iteration-sensitive)

**Attempt 1: Broad sweep**
- Search all 11 source types with standard queries
- Establish baseline coverage
- Expected EDS: 0.35-0.45

**Attempt 2: Deep dive on weak sources**
- Re-examine sources that returned no results in attempt 1
- Try alternative search queries (company aliases, founder names, product names)
- Add date-bounded searches for temporal freshness
- Expected EDS improvement: +0.05-0.10

**Attempt 3: Triangulation focus**
- For each claim with <3 sources, actively seek corroboration
- Search for contrarian viewpoints (if all sources agree, search for disagreement)
- Cross-reference employee signals with product signals
- Expected EDS improvement: +0.03-0.08

**Attempt 4: Adversarial pass**
- Assume every claim is false. Search for disconfirming evidence
- Check if cited URLs actually support the claims attributed to them
- Look for signs of gaming (review campaigns, SEO manipulation, phantom repos)
- Expected EDS improvement: +0.02-0.05

### Phase 1: Discovery

**Attempt 1:** Standard discovery (WHOIS, homepage, social, GitHub)
**Attempt 2:** If key data missing, try archived versions, alternative domains, subsidiary names

### Phase 2: Market

**Attempt 1:** Standard market research (TAM, competitors, SWOT)
**Attempt 2:** If competitor list thin, search industry reports, analyst coverage, G2 categories

### Phase 3: Technical

**Attempt 1:** Standard GitHub analysis (org repos, code quality, architecture)
**Attempt 2:** If GitHub org missed or thin, search npm/PyPI packages, Docker Hub, contributor profiles

### Phase 6: Valuation

**Attempt 1:** Standard SaaS metrics + replication cost
**Attempt 2:** If financial data sparse, search SEC filings, Sacra, PitchBook mentions, press funding rounds
**Attempt 3:** Cross-reference P4 findings with valuation assumptions — are we valuing capabilities that P4 flagged as exaggerated?

---

## Source Weighting (for Phase 4)

Weight signals inversely by controllability:

| Source | Controllability | Weight |
|--------|----------------|--------|
| SEC filings | Very low | STRONG |
| Court records | Very low | STRONG |
| GitHub commit history | Low | STRONG |
| arXiv publications | Low | MODERATE |
| Glassdoor/Blind reviews | Medium | WEAK (require corroboration) |
| Customer reviews (G2, Capterra) | Medium | MODERATE |
| Reddit/HN discussions | Medium | MODERATE |
| Job postings | Medium-High | MODERATE (easy to manipulate) |
| Company website | Very high | BASELINE (this IS the claim) |
| Press releases | Very high | BASELINE |
| LinkedIn | High | WEAK |

When triangulating, require at least one STRONG-weight source per claim.

---

## Source Independence Rules

Before claiming "3+ independent sources converge," verify independence:

```
INDEPENDENT:
  SEC filing + Glassdoor review + customer G2 review
  → Three structurally different viewpoints (regulatory, employee, customer)

NOT INDEPENDENT:
  Glassdoor review + Blind review + Reddit r/cscareerquestions
  → Same population (current/former employees) in three venues
  → Count as ONE source type: "employee sentiment"

NOT INDEPENDENT:
  TechCrunch article + HN discussion of that article + Reddit thread about that article
  → One primary source (TechCrunch) with two derivative echoes
  → Count as ONE source
```

---

## Multi-Run Variance Protocol

For scoring phases (P4, P6), run the scoring section 3 times and report variance:

```markdown
AI Reality Score: 4/5 (range: 3-4, 2/3 agreement)
Build vs Buy: 2.8/4 (range: 2.5-3.1, spread: 0.6)
```

If the range spans more than 1 point on a 5-point scale, flag as LOW CONFIDENCE.

---

## Mandatory Blind Spots Disclosure

Every Phase 7 report MUST include this section (non-removable):

```markdown
## What This Analysis Cannot See

This analysis is based entirely on publicly available data. It cannot access:

- **Financial internals:** Revenue breakdown, gross margins, burn rate, runway, cash position
- **Customer data:** Actual churn rate, NRR, LTV/CAC, pipeline, contract terms
- **Legal exposure:** Pending litigation, regulatory investigations, IP disputes in discovery
- **Cap table:** Dilution, preference stacks, liquidation waterfalls, secondary prices
- **Board dynamics:** Investor pressure, founder-board conflicts, governance issues
- **Internal roadmap:** Actual priorities vs. marketing roadmap, killed projects

This report is a screening tool, not a substitute for traditional due diligence
with data room access, management interviews, and customer calls.
```

---

## Editing This File

**For humans:** Modify the strategy variants, thresholds, and source weightings to
steer how the agent researches. You are the experimental designer. The agent is
the experimenter.

**For agents:** Read this file before each research sprint. Follow the iteration
protocol. Select the strategy variant matching your attempt number. Report EDS
after each sprint.
