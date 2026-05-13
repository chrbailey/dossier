# Dossier

One company in, one decision out. Read time: 5 minutes.

## How to run

Open this file in Claude Code and pass a domain plus an audience. Example:

    claude -p "$(cat dossier.md)" stripe.com BUYER

Or paste the contents of this file into a Claude Code session and give it a domain and audience when asked.

## Input

Two required fields:

- **Domain** (e.g. `stripe.com`).
- **Audience** — one of `BUYER` (adopting the product), `BUILDER` (deciding to compete with it), or `INVESTOR` (evaluating equity). The audience changes which risks matter and what the verdict means.

If either is missing, ask the user once, then stop asking.

## Method

Do these five steps in order. Stop after step five. Do not add steps.

1. **Pitch.** Search the company. Read the homepage once. Write one sentence: what they do, who pays.
2. **Money.** Find ONE independent source for revenue scale, customer count, or pricing model. Press, S-1, Pitchbook, Crunchbase, analyst report. The company's own blog does not count.
3. **AI claims.** List every AI/ML claim the company makes publicly — landing page, pricing page, product changelog, or recent press coverage. For each, find ONE independent source. Mark each VERIFIED, DISPUTED, or UNVERIFIED. Verification status is about the claim itself, not about which page sourced it. If the company has no AI claims, write "none" and move on — do not invent rows.
4. **Top risk.** Find ONE independent source for the most material risk *for this audience*. Tag the time-frame: `NEAR` (0–12mo), `MEDIUM` (1–3yr), or `STRUCTURAL` (3yr+).
5. **Verdict.** Choose one of: `PASS`, `PROCEED`, `CAUTION`, `AVOID`. Write one sentence of rationale tied explicitly to the declared audience.

## Rules

- Every factual claim has an inline `[source](url)` next to it. No exceptions.
- A first-party source (company site, company blog, company SEC filing comms) cannot VERIFY — only STATE. Verification requires an independent source.
- If you cannot find an independent source for a claim, mark it `[UNVERIFIED]` and move on. Do not pad.
- If `WebFetch` is denied, fall back to `WebSearch`. Search snippets are acceptable evidence.
- **Homepage unreachable.** If the homepage returns 403/404 or is fully JS-rendered, retry once via `https://web.archive.org/web/2026/<url>` (the harness may block `web.archive.org` itself — if so, do not retry further). When neither succeeds, populate step 3 from press, the company's own changelog, or analyst coverage instead of the landing page. Add `homepage unreachable — claims sourced from press/changelog` to the "cannot see" section. Do not skip step 3.
- Hard stop at five steps. No phase 6, no red team, no calibration pass. If a future reader needs more, they can run this again with a sharper question.
- Show the user the full draft in chat. Ask: **"ship as `output/<domain>.md`?"** Wait for an explicit yes before writing the file.

## Output skeleton

```markdown
# {Company} — Dossier

**Audience:** BUYER | BUILDER | INVESTOR
**Verdict:** PASS | PROCEED | CAUTION | AVOID
**Rationale:** {one sentence, tied to audience}
**Risk time-frame:** NEAR | MEDIUM | STRUCTURAL
**Generated:** {ISO date}

## What they do
{One paragraph.} [source]({url})

## How they make money
{One paragraph: pricing model, segment, revenue scale.} [source]({url})

## AI claims, checked

| Claim | Independent source | Status |
|---|---|---|
| {claim} | [{source}]({url}) | VERIFIED / DISPUTED / UNVERIFIED |

## Top risk for {audience}
{One paragraph.} [source]({url})

## What this dossier cannot see
- {gap 1}
- {gap 2}
```

## Ship criteria

A dossier is shippable when:

- Every section has at least one inline `[source](url)`, OR an explicit `[UNVERIFIED]` marker.
- The verdict is one of the four constants — not a hedge, not a paragraph.
- Audience is one of `BUYER` / `BUILDER` / `INVESTOR`; risk time-frame is one of `NEAR` / `MEDIUM` / `STRUCTURAL`.
- The "cannot see" section names at least two real gaps. Not boilerplate.

If those four are not true, do not ship. Tell the user what is missing and stop.
