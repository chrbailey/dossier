---
description: People due diligence on one company — headcount, hiring, retention, leadership, key-person risk. One shippable page, every claim independently sourced.
argument-hint: <domain> <BUYER|BUILDER|INVESTOR>
---

# HR Dossier

One company in, one people-risk read out. Read time: 5 minutes. This is the
companion to `dossier.md`: same discipline, aimed at the org instead of the
product.

## Input

Two required fields (read from `$ARGUMENTS` if present):

- **Domain** (e.g. `stripe.com`).
- **Audience** — one of `BUYER` (adopting the product; you care about vendor
  viability and support staffing), `BUILDER` (competing with it; you care about
  who you'll be poaching from and bidding against for talent), or `INVESTOR`
  (evaluating equity; you care about org health, burn, and key-person risk). The
  audience changes which people signals matter and what the verdict means.

If either is missing, ask the user once, then stop asking.

## Method

Do these five steps in order. Stop after step five. Do not add steps.

1. **Shape.** Search the company. Establish the org shape: total headcount,
   primary location(s), and growth trajectory over the last 12–24 months. Write
   one sentence: how big, where, growing or shrinking.
2. **Hiring signal.** Find ONE independent source for current hiring posture —
   open-role count and which functions dominate (eng / sales / G&A / support).
   Job-board aggregators, LinkedIn, press on hiring or layoffs. The company's own
   careers page can STATE open roles but cannot VERIFY velocity or trend — that
   needs a second, dated reference point.
3. **Retention & culture.** List the people-health claims you can find —
   Glassdoor/Comparably rating, attrition or tenure signals, layoff events,
   notable executive or founder departures. For each, find ONE independent
   source. Mark each VERIFIED, DISPUTED, or UNVERIFIED. Verification is about the
   signal itself, not which page surfaced it. If there is genuinely nothing
   public, write "none" and move on — do not invent rows.
4. **Key-person risk.** Find ONE independent source for the most material
   people risk *for this audience*: founder/CEO flight risk, a thin or recently
   reshuffled leadership bench, single-point-of-failure dependence, visa/location
   concentration, or a hiring freeze masking distress. Tag the time-frame: `NEAR`
   (0–12mo), `MEDIUM` (1–3yr), or `STRUCTURAL` (3yr+).
5. **People verdict.** Choose one of: `HEALTHY`, `STABLE`, `STRAINED`,
   `DISTRESSED`. Write one sentence of rationale tied explicitly to the declared
   audience.

## Rules

- Every factual claim has an inline `[source](url)` next to it. No exceptions.
- A first-party source (company site, careers page, company blog, exec's own
  post) can STATE a fact, never VERIFY it. Verification requires an independent
  source. Headcount and culture self-reports are the most-inflated numbers in
  this whole exercise — treat them as claims, not facts.
- If you cannot find an independent source for a claim, mark it `[UNVERIFIED]`
  and move on. Do not pad.
- If `WebFetch` is denied, fall back to `WebSearch`. Search snippets are
  acceptable evidence — LinkedIn and Glassdoor snippets in particular often carry
  richer headcount/rating metadata than the gated pages themselves.
- **Headcount is a range, not a point.** LinkedIn "employees on LinkedIn",
  SEC filings, and press estimates rarely agree. Report the range and name the
  sources; do not average them into a false-precision single number.
- Hard stop at five steps. No phase 6, no scoring index, no calibration pass.
- Show the user the full draft in chat. Ask: **"ship as
  `output/<domain>-hr.md`?"** Wait for an explicit yes before writing the file.

## Output skeleton

```markdown
# {Company} — HR Dossier

**Audience:** BUYER | BUILDER | INVESTOR
**Verdict:** HEALTHY | STABLE | STRAINED | DISTRESSED
**Rationale:** {one sentence, tied to audience}
**Risk time-frame:** NEAR | MEDIUM | STRUCTURAL
**Generated:** {ISO date}

## Org shape
{One paragraph: headcount range, locations, 12–24mo trajectory.} [source]({url})

## Hiring signal
{One paragraph: open-role count, function mix, velocity vs. prior period.} [source]({url})

## Retention & culture, checked

| Signal | Independent source | Status |
|---|---|---|
| {signal} | [{source}]({url}) | VERIFIED / DISPUTED / UNVERIFIED |

## Key-person risk for {audience}
{One paragraph.} [source]({url})

## What this dossier cannot see
- {gap 1}
- {gap 2}
```

## Ship criteria

An HR dossier is shippable when:

- Every section has at least one inline `[source](url)`, OR an explicit
  `[UNVERIFIED]` marker.
- The verdict is one of the four constants — not a hedge, not a paragraph.
- Audience is one of `BUYER` / `BUILDER` / `INVESTOR`; risk time-frame is one of
  `NEAR` / `MEDIUM` / `STRUCTURAL`.
- Headcount is reported as a sourced range, not an unsourced point estimate.
- The "cannot see" section names at least two real gaps. Not boilerplate.

If those are not all true, do not ship. Tell the user what is missing and stop.
