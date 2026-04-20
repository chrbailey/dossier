# Security

## Responsible Disclosure

If you find a security issue, please do **not** file a public GitHub issue.

Email: chris.bailey@erp-access.com — include "SECURITY: dossier" in the subject line.

Expect an acknowledgment within 72 hours.

## What this tool does

Dossier runs Claude Code sub-agents that perform read-only research on a target domain. It queries public sources (WebSearch, WebFetch), reads the public GitHub API via the `gh` CLI, queries WHOIS and DNS via local utilities, and writes report files to `output/{domain}/`. The target is specified in `target.env`.

## What this tool does NOT do

- It does not make authenticated requests with write permissions against any third-party service.
- It does not send the target's data anywhere other than the public APIs it queries (WebSearch/WebFetch endpoints, GitHub public API, arXiv, WHOIS).
- It does not bypass robots.txt, paywalls, or authentication to access non-public information about the target.
- It does not perform any action against the target other than reading public information.
- It does not call the Claude API directly — all LLM calls go through the Claude Code harness the user is already running.

## Known Considerations

- `target.env` lives in the repository working directory. If you fork a local copy with your own targets, be careful about committing that file. Verify your `.gitignore` covers it.
- `output/{domain}/` contains everything the pipeline scraped about the target, including raw JSON captures. Treat those artifacts accordingly — some data (employee sentiment, layoff signals) may be sensitive to the target even if individually public.
- The pipeline uses whatever credentials your local `gh` CLI has authenticated with to call the GitHub API. If you run Dossier against a competitor and your `gh` token is tied to a corporate identity, the target can see that identity in their API logs.

If you see evidence of any of the "does NOT do" items, that is a security issue — please report.
