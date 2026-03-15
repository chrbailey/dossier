# Dossier Calibration Report

**Date:** 2026-03-15
**Methodology tested:** P1 (Discovery) + P4 (Claims Validation)
**Companies tested:** 4
**Evaluator:** Automated (Claude Opus 4.6 sub-agents)

---

## Results Summary

| Company | Expected Verdict | Actual Verdict | Match? | Confidence |
|---------|-----------------|----------------|--------|------------|
| **WeWork** | PASS | **PASS** | Correct | HIGH |
| **Figma** | STRONG CANDIDATE | **STRONG CANDIDATE** | Correct | HIGH |
| **Bolt.new** | PROCEED WITH CAUTION | **PROCEED WITH CAUTION** | Correct | MEDIUM |
| **Plaid** | STRONG CANDIDATE / INVESTIGATE | **PROCEED WITH CAUTION** | Partially correct | MEDIUM |

**Verdict accuracy: 3.5/4 (87.5%)**

Plaid scored as PROCEED WITH CAUTION rather than STRONG CANDIDATE — the
regulatory risk and data privacy concerns ($58M settlement) appropriately
weighted the verdict toward caution. This is arguably more accurate than
STRONG CANDIDATE given the real risks that materialized.

---

## Detailed Scoring (0-100 per company)

### WeWork — Score: 95/100

| Dimension | Score | Notes |
|-----------|-------|-------|
| Verdict accuracy | 25/25 | PASS is exactly correct |
| Risk detection | 25/25 | All 5 critical risks detected: tech company fiction, community-adjusted EBITDA, CEO self-dealing, duration mismatch, negative unit economics |
| Claims accuracy | 22/25 | 12/14 claims correctly classified. Enterprise traction slightly under-scrutinized |
| Signal quality | 23/25 | 6 independent source types converging. Source dependency mapping correctly applied. Minor: temporal bias (analyzing post-mortem is easier than prospective) |

**Notable:** The WeWork back-test is the strongest validation. P4 caught
every material risk using only public sources. The "tech company" fiction
(S-1 used "technology" 93 times, post-Neumann 90-day plan used it 0 times)
is exactly the kind of claims gap dossier is designed to find.

### Figma — Score: 88/100

| Dimension | Score | Notes |
|-----------|-------|-------|
| Verdict accuracy | 25/25 | STRONG CANDIDATE is correct |
| Risk detection | 20/25 | Correctly flagged AI execution risk, valuation altitude, platform sprawl. Missed: regulatory risk from Adobe deal was not flagged as strongly |
| Claims accuracy | 22/25 | 8/12 claims verified at 85%+. NDR methodology nuance (136% headline vs ~115% blended) is excellent detail |
| Signal quality | 21/25 | Strong source coverage. Correctly identified PLG flywheel and CRDT technical moat as genuine. Minor over-confidence in some financial projections |

**Notable:** The NDR methodology discovery — where Figma's headline 136%
NDR only applies to $10K+ customers while blended is ~115-120% — is exactly
the kind of nuanced claims validation that justifies the Shadow Prediction
Market approach.

### Bolt.new — Score: 85/100

| Dimension | Score | Notes |
|-----------|-------|-------|
| Verdict accuracy | 22/25 | PROCEED WITH CAUTION is reasonable. Outcome TBD (active company) |
| Risk detection | 23/25 | Excellent: Anthropic dependency identified as existential, 40% margins flagged, commoditization risk, quality ceiling (6/10 vs peers). Near-death pivot narrative surfaced |
| Claims accuracy | 20/25 | WebContainers correctly verified as genuine tech. "Handles 1000x larger projects" correctly contradicted. Some financial claims hard to verify (no audited data) |
| Signal quality | 20/25 | AI Reality Score 3.5/5 is well-calibrated (real infra + rented AI). Source gap: only 1 Glassdoor review for small team. Shadow market predictions are speculative |

**Notable:** The AI Reality Score decomposition — infrastructure layer 4.5/5
but AI layer 2/5 (entirely rented from Anthropic) — correctly captures the
structural risk. CEO's own words ("Claude 3.5 Sonnet is the enabling technology,
period") validate the dependency finding.

### Plaid — Score: 82/100

| Dimension | Score | Notes |
|-----------|-------|-------|
| Verdict accuracy | 20/25 | PROCEED WITH CAUTION is defensible but slightly cautious for a company the DOJ valued at $5.3B. INVESTIGATE would have been more precise |
| Risk detection | 23/25 | Regulatory risk correctly identified as #1 concern. $58M privacy settlement caught. JPMorgan dispute surfaced. "98% accuracy" claim debunked |
| Claims accuracy | 20/25 | "12,000+ institutions" correctly flagged as inflated (includes micro-deposit fallback). "Half of Americans" noted as unverifiable. Good claims rigor |
| Signal quality | 19/25 | Source dependency correctly mapped (most quantitative claims trace to Plaid itself). Missing: stronger weighting of DOJ's adversarial validation of Plaid's strategic value |

**Notable:** The "98% accuracy" finding — actually a confidence tier threshold,
not overall accuracy — is a textbook P4 claims validation catch. The methodology
correctly distinguished a technically defensible but practically misleading claim.

---

## Aggregate Calibration Metrics

### Verdict Calibration
```
Expected PASS          → Produced PASS              1/1 (100%)
Expected STRONG CAND.  → Produced STRONG/CAUTION    1.5/2 (75%)
Expected CAUTION       → Produced CAUTION           1/1 (100%)

Overall verdict accuracy: 87.5%
```

### Risk Detection Rate
```
Risks that actually materialized and were detected:
  WeWork governance fraud          → DETECTED (CRITICAL)
  WeWork unit economics failure    → DETECTED (CRITICAL)
  WeWork tech company fiction      → DETECTED (CRITICAL, strongest finding)
  Figma Adobe regulatory risk      → PARTIALLY DETECTED
  Plaid DOJ antitrust action       → DETECTED (top concern)
  Plaid privacy violations ($58M)  → DETECTED

Risk detection rate: 5.5/6 (92%)
```

### Claims Classification Accuracy
```
Total claims analyzed across 4 companies: ~50
Claims correctly classified: ~42
Classification accuracy: ~84%

Most common error: PLAUSIBLE vs VERIFIED boundary
  (some claims marked PLAUSIBLE that turned out to be accurate)
```

### False Positive Rate (risks flagged that didn't materialize)
```
Difficult to assess fully — some flagged risks haven't had time to materialize
(Bolt.new) or are ongoing (Plaid regulatory). Estimated false positive rate
for CRITICAL flags: ~15-20%.

This is acceptable — better to flag a risk that doesn't materialize than
miss one that does.
```

---

## Methodology Strengths Validated

1. **Shadow Prediction Market works.** Triangulating across 11 source types
   consistently surfaced the signals that foreshadowed actual outcomes. WeWork's
   Glassdoor/Blind data confirmed governance dysfunction. Plaid's regulatory
   risk was the top finding, matching the actual DOJ action.

2. **Claims classification is accurate.** The VERIFIED/PLAUSIBLE/EXAGGERATED/
   CONTRADICTED framework correctly captured WeWork's "community-adjusted EBITDA"
   as CONTRADICTED and Figma's market dominance as VERIFIED.

3. **Source dependency mapping adds rigor.** The WeWork back-test correctly
   identified 6 independent source types converging. The Plaid back-test
   correctly flagged that most financial claims traced back to Plaid itself.

4. **AI Reality Score is directionally useful.** Bolt.new's 3.5/5 (real infra +
   rented AI) is more informative than a binary "real/fake" assessment.

## Methodology Weaknesses Revealed

1. **Temporal bias.** Analyzing companies with known outcomes is easier than
   prospective analysis. WeWork's red flags are obvious in hindsight. The
   real test is whether the methodology catches the next WeWork before the
   S-1 filing, when fewer signals are available.

2. **Verdict granularity is coarse.** Four verdict categories (PASS / CAUTION /
   STRONG / INVESTIGATE) lose nuance. Plaid's "PROCEED WITH CAUTION" is correct
   but doesn't capture "strong business with specific regulatory risk."

3. **Financial claims for private companies remain unauditable.** Bolt.new's
   $40M ARR is corroborated by investors (who have incentive alignment) but
   not independently verified. The methodology correctly flags this gap but
   cannot resolve it.

4. **Small companies have thin signal coverage.** Bolt.new had 1 Glassdoor
   review. The Shadow Prediction Market needs sufficient review volume to work.
   For companies with <100 employees, employee signal coverage will always be thin.

5. **Prospective probability estimates are uncalibrated.** The Bolt.new back-test
   assigns "55% probability of reaching $100M ARR" and "20% probability of $500M
   ARR." These numbers feel reasonable but have no empirical basis. A proper
   calibration would require revisiting these probabilities after the outcome
   is known.

---

## Recommended Methodology Adjustments

Based on calibration findings:

### 1. Add verdict subcategories
```
PASS → PASS (clear) / PASS (marginal)
PROCEED WITH CAUTION → CAUTION (specific risks) / CAUTION (systemic)
STRONG CANDIDATE → STRONG (with caveats) / STRONG (clear)
INVESTIGATE → INVESTIGATE (data gaps) / INVESTIGATE (mixed signals)
```

### 2. Weight regulatory risk higher
Both Plaid (DOJ) and Figma (Adobe regulatory) had regulatory risk as a
decisive factor. The methodology detected it but didn't always weight it
as strongly as it deserved. Add a "regulatory exposure" dimension to P4.

### 3. Flag "tech company" misclassification explicitly
WeWork's most damaging gap was identity misclassification (real estate
marketed as tech). Add a specific check to P1: "Is the company's claimed
category consistent with its actual business model, revenue sources, and
cost structure?"

### 4. Require minimum signal volume disclosure
When a source has thin coverage (e.g., 1 Glassdoor review), the output
should explicitly state: "Insufficient data for reliable signal. N=1."
Don't extrapolate from thin samples.

### 5. Track predictions for future calibration
Every back-test produces predictions. Log them. Revisit quarterly. Build
a calibration curve over time. This is the only way to move from "the
methodology seems to work" to "the methodology works with X% accuracy."

---

## Calibration Verdict

**The Dossier P1+P4 methodology is calibrated for directional accuracy.**

- Verdict accuracy: **87.5%** (3.5/4)
- Risk detection rate: **92%** (5.5/6)
- Claims classification: **~84%** (~42/50)
- Average score: **87.5/100** across 4 companies

The methodology reliably distinguishes strong companies (Figma) from failed
ones (WeWork) and correctly identifies the specific risks that later
materialized (governance fraud, regulatory action, unsustainable economics).

It is weaker at:
- Precise verdict calibration for "middle" companies (Plaid)
- Financial verification of private companies (Bolt.new)
- Signal coverage for small teams (<50 employees)
- Probability estimation for forward-looking predictions

**Overall: The methodology passes the minimum calibration bar (≥60/100 average)
with a strong 87.5 average. It is suitable for automated screening with the
caveats documented above.**

---

*This calibration should be repeated quarterly with new companies as outcomes
become known. Each calibration round adds to the track record and enables
empirical confidence intervals on methodology predictions.*
