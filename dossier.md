# Dossier

One company in, one decision out. Read time: 5 minutes.

## How to run

Open this file in Claude Code and pass a domain. Example:

    claude -p "$(cat dossier.md)" stripe.com

Or paste the contents of this file into a Claude Code session and give it a domain when asked.

## Input

A single company domain (e.g. `stripe.com`). If none was given, ask the user once, then stop asking.

## Method

Do these five steps in order. Stop after step five. Do not add steps.

1. **Pitch.** Search the company. Read the homepage once. Write one sentence: what they do, who pays.
2. **Money.** Find ONE independent source for revenue scale, customer count, or pricing model. Press, S-1, Pitchbook, Crunchbase, analyst report. The company's own blog does not count.
3. **AI claims.** List every AI/ML claim on their landing page or pricing page. For each, find ONE independent source. Mark each VERIFIED, DISPUTED, or UNVERIFIED.
4. **Top risk.** Find ONE independent source for the most material risk in their space right now: lawsuit, layoffs, customer loss, regulation, security incident, competitor move.
5. **Verdict.** Choose one of: `PASS`, `PROCEED`, `CAUTION`, `AVOID`. Write one sentence of rationale.

## Rules

- Every factual claim has an inline `[source](url)` next to it. No exceptions.
- A first-party source (company site, company blog, company SEC filing comms) cannot VERIFY — only STATE. Verification requires an independent source.
- If you cannot find an independent source for a claim, mark it `[UNVERIFIED]` and move on. Do not pad.
- If `WebFetch` is denied, fall back to `WebSearch`. Search snippets are acceptable evidence.
- Hard stop at five steps. No phase 6, no red team, no calibration pass. If a future reader needs more, they can run this again with a sharper question.
- Show the user the full draft in chat. Ask: **"ship as `output/<domain>.md`?"** Wait for an explicit yes before writing the file.

## Output skeleton

```markdown
# {Company} — Dossier

**Verdict:** PASS | PROCEED | CAUTION | AVOID
**Rationale:** {one sentence}
**Generated:** {ISO date}

## What they do
{One paragraph.} [source]({url})

## How they make money
{One paragraph: pricing model, segment, revenue scale.} [source]({url})

## AI claims, checked

| Claim | Independent source | Status |
|---|---|---|
| {claim} | [{source}]({url}) | VERIFIED / DISPUTED / UNVERIFIED |

## Top risk
{One paragraph.} [source]({url})

## What this dossier cannot see
- {gap 1}
- {gap 2}
```

## Ship criteria

A dossier is shippable when:

- Every section has at least one inline `[source](url)`, OR an explicit `[UNVERIFIED]` marker.
- The verdict is one of the four constants — not a hedge, not a paragraph.
- The "cannot see" section names at least two real gaps. Not boilerplate.

If those three are not true, do not ship. Tell the user what is missing and stop.
