# Dossier Calibration Framework

## Purpose

Back-test the dossier methodology against companies with **known outcomes**.
Compare what dossier would have predicted to what actually happened.
Compute hit rates, false positive rates, and calibration scores.

## Company Selection

### Criteria
- Outcome is publicly known and unambiguous
- Sufficient public data exists for dossier to analyze
- Mix of outcomes: success, failure, mixed, fraud
- Mix of stages: pre-IPO, public, acquired, bankrupt

### Selected Companies

| Company | Domain | Known Outcome | Expected Verdict | Why Selected |
|---------|--------|--------------|-------------------|-------------|
| **WeWork** | wework.com | Catastrophic failure — $47B → bankrupt Nov 2023 | PASS | Governance fraud, unit economics, founder issues. P4 should catch massive claims gaps |
| **Figma** | figma.com | Strong product — $20B Adobe bid (blocked), $12.5B standalone | STRONG CANDIDATE | Genuine product-market fit, strong technical moat, regulatory risk only |
| **Bolt** | bolt.new | Rapid growth with sustainability questions — raised $240M, AI code gen | PROCEED WITH CAUTION | Hot AI startup, unclear moat, competitive market. Tests current-era AI hype detection |
| **Plaid** | plaid.com | Near-acquisition by Visa ($5.3B, blocked by DOJ), pivoted, strong | STRONG CANDIDATE / INVESTIGATE | Proved value through acquisition interest, regulatory risk, API moat |

### Evaluation Method

Run abbreviated dossier (P1 Discovery + P4 Claims Validation) per company.
P4 is the analytical core — if the methodology works, P4 should detect the
signals that foreshadowed each company's outcome.

### Scoring Rubric

For each company, score the dossier output on:

**1. Verdict Accuracy (0-25 points)**
- Did the recommended verdict match the actual outcome?
- PASS for WeWork = 25 points. STRONG CANDIDATE for WeWork = 0.

**2. Risk Detection (0-25 points)**
- Did P4 identify the risks that actually materialized?
- WeWork: governance, unit economics, founder issues
- Figma: regulatory risk (but strength otherwise)
- For each key risk: detected = 5 pts, missed = 0 pts

**3. Claims Accuracy (0-25 points)**
- How well did P4 classify claims?
- Claims later proven true → VERIFIED should be correct
- Claims later proven false → should be EXAGGERATED or CONTRADICTED

**4. Signal Quality (0-25 points)**
- Were the most important signals identified?
- Were false signals flagged that didn't matter? (false positives)
- Was the overall narrative directionally correct?

**Total: 0-100 per company. Methodology is calibrated if average ≥ 60.**

## Timeline

This calibration is a one-time exercise that should be repeated quarterly
with new companies as outcomes become known.
