# Contributing

Thanks for looking.

## Before opening a PR

1. **Open an issue first** for anything larger than a typo.
2. **All changes need tests.** If tests don't exist yet, at minimum add a test alongside your change.
3. **Match the existing code style.** Match language version, imports, naming.
4. **Run the full test suite locally** before submitting.

## What this project will not accept

Dossier is a Claude Code native research pipeline (7 analysis phases orchestrated by Ralph Loop). Keep it that way.

- PRs that replace the Claude Code sub-agent architecture with an API-wrapping CLI (defeats the reason this project exists — intelligence lives in the Claude Code harness, not in a Python layer).
- PRs that add paid external data services as required dependencies. Optional enrichment is fine; required paid APIs are not.
- PRs that bypass or alter the shadow prediction market methodology in Phase 4 to produce softer outputs. The spread across independent sources IS the confidence interval.
- PRs to the helper scripts (`scripts/`) that drop Python 3.9 compatibility.
- PRs that add scoring/ranking to the raw evidence captures in `output/{domain}/raw/` — that data is deliberately unprocessed.

## Reporting security issues

See [SECURITY.md](SECURITY.md). Do not file security issues in the public tracker.

## Author

[Christopher Bailey](https://github.com/chrbailey).
