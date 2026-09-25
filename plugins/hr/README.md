# hr — People Due Diligence Plugin

A Claude Code plugin that adds one slash command: an HR/people read on a target
company. It is the companion to [`dossier.md`](../../dossier.md) — same
discipline (five steps, hard stop, every claim independently sourced, human
ship-gate), aimed at the org instead of the product.

The product dossier tells you whether to trust the *software*. This one tells you
whether to trust the *organization behind it*: is it growing or bleeding, who
holds it together, and what breaks if a key person leaves.

## Install

This repo doubles as a plugin marketplace. From a Claude Code session:

```
/plugin marketplace add chrbailey/dossier
/plugin install hr@dossier-plugins
```

Or point at a local checkout:

```
/plugin marketplace add /path/to/dossier
/plugin install hr@dossier-plugins
```

## Use

```
/hr:dossier stripe.com INVESTOR
```

- **Domain** — e.g. `stripe.com`.
- **Audience** — `BUYER`, `BUILDER`, or `INVESTOR`. Changes which people signals
  matter and what the verdict means.

The command shows the full draft in chat and asks before writing
`output/<domain>-hr.md`. Nothing is written without an explicit yes.

## The five steps

1. **Shape** — headcount range, locations, 12–24mo trajectory.
2. **Hiring signal** — open-role count, function mix, velocity vs. prior period.
3. **Retention & culture** — Glassdoor/attrition/departures, each marked
   VERIFIED / DISPUTED / UNVERIFIED.
4. **Key-person risk** — most material people risk for the audience, time-framed
   NEAR / MEDIUM / STRUCTURAL.
5. **People verdict** — `HEALTHY` | `STABLE` | `STRAINED` | `DISTRESSED`.

## Rules that make it trustworthy

- Every factual claim carries an inline `[source](url)`, or an explicit
  `[UNVERIFIED]` marker.
- First-party sources (careers page, exec posts) can *state*, never *verify*.
- Headcount is reported as a sourced range, never a false-precision point.
- `WebFetch` denied? Fall back to `WebSearch` — snippets are acceptable evidence.
- Hard stop at five steps. No scoring index, no calibration pass.

See [`commands/dossier.md`](commands/dossier.md) for the full program.
