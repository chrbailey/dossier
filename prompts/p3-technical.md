# Phase 3: Technical Analysis

## Goal
Assess the target company's technical capabilities through their open-source presence, GitHub activity, and publicly observable architecture.

## Inputs
- `output/{DOMAIN}/01-discovery.md` — GitHub org, tech stack claims, product description

## Steps

### 3.1 GitHub Organization Discovery
Find the company's GitHub presence:
```bash
source "/Volumes/OWC drive/Dev/dossier/target.env"
# Search for repos by org (if found in Phase 1)
gh search repos --owner={ORG_NAME} --limit=50 --json name,description,language,stargazersCount,forksCount,updatedAt,isArchived
# Also search by company name
gh search repos "{COMPANY_NAME}" --limit=20 --json fullName,description,language,stargazersCount
```

### 3.2 Repository Analysis
For each significant repo (non-archived, with activity):
- Stars, forks, open issues, open PRs
- Primary language and framework
- Last commit date and commit frequency
- Contributor count (`gh api repos/{owner}/{repo}/contributors --jq 'length'`)
- License type

Save to `output/{DOMAIN}/raw/github-repos.json`.

### 3.3 Code Quality Signals
For the top 3-5 repos by stars/activity, check (via WebFetch on the GitHub pages, or gh CLI):
- README quality (presence, completeness, examples)
- CI/CD configuration (`.github/workflows/`, `.circleci/`, etc.)
- Test directory presence (`tests/`, `test/`, `__tests__/`, `spec/`)
- Package manifest (`package.json`, `requirements.txt`, `go.mod`, `Cargo.toml`)
- Documentation (`docs/`, wiki, API docs)
- Security policy (`SECURITY.md`, `.github/security.yml`)
- Changelog or release history

### 3.4 Dependency Analysis
For repos with package manifests:
- List key dependencies (frameworks, databases, cloud SDKs)
- Note any outdated or deprecated dependencies
- Check for dependency on the company's own packages (internal ecosystem)
- Look for security-sensitive dependencies (auth, crypto, payments)

### 3.5 Architecture Assessment
Based on all findings, assess:
- **Architecture style**: Monolith, microservices, serverless, or hybrid
- **Language diversity**: Single-language or polyglot
- **Infrastructure signals**: Cloud provider, container usage, IaC presence
- **API design**: REST, GraphQL, gRPC (from docs or repo structure)
- **Data layer**: Database type signals (ORM usage, migration files)

### 3.6 Open Source Health
Evaluate the company's open-source practice:
- Do they actively maintain their repos?
- Response time on issues and PRs
- Community engagement (external contributors)
- Documentation quality
- Versioning discipline (semantic versioning, changelogs)

## Output

Write `output/{DOMAIN}/03-technical.md`:
```markdown
# Technical Analysis: {COMPANY_NAME}

## GitHub Presence
| Metric | Value |
|--------|-------|
| GitHub Org | |
| Total Repos | |
| Total Stars | |
| Primary Languages | |
| Active Contributors | |

## Repository Inventory
| Repo | Stars | Language | Last Commit | CI | Tests | License |
|------|-------|----------|-------------|-----|-------|---------|
| | | | | | | |

## Architecture Assessment
(architecture style, language choices, infrastructure signals)

## Code Quality Signals
(CI/CD, testing, documentation, security practices)

## Dependency Analysis
(key dependencies, risks, ecosystem)

## Open Source Health
(maintenance activity, community engagement, versioning)

## Technical Strengths
- (what they do well technically)

## Technical Concerns
- (red flags, gaps, risks)

## Key Findings
- (3-5 most important technical insights)
```

## Source Trust Rules

Apply the source trust classification from CLAUDE.md. A crucial nuance for this
phase: **the target's own repos are still FIRST-PARTY (trust 0.2)** — the company
controls them and can delete failing tests, vendor green CI badges, or curate what
is public. Code is more *observable* than marketing copy, but observing the
company's own artifact is not independent corroboration.

- README files, docs, self-authored code, the company's own CI configs and test
  suites = FIRST-PARTY. Use them to check the company's claims for *internal
  consistency* (does the code do what the marketing says?), not as INDEPENDENT
  evidence that verifies a claim.
- Genuinely INDEPENDENT (trust 0.8) technical signals: external contributors and
  forks, other projects that depend on their packages, third-party security
  audits, and bug reports/issues filed by outside users.
- Star counts can be gamed. Weight external contributor count and downstream
  dependents higher than stars.
- If the company's website or llms.txt claims specific technical capabilities,
  check them against actual repo contents and log discrepancies.

Tag each technical finding as **CODE-OBSERVED** (seen in the company's own repo —
first-party, good for consistency checks) or **CLAIMED** (asserted with no repo
artifact at all). Neither tag alone VERIFIES a claim under P4's bar — that still
requires an independent source.

## Quality Criteria
- Repository data should be current (use gh CLI for live data)
- Distinguish between public repos and likely private infrastructure
- Note what you CAN'T see — a company with 3 public repos may have 300 private ones
- Architecture assessment should be clearly labeled as inference where appropriate
- Every technical claim must be tagged CODE-OBSERVED (first-party) or CLAIMED, and neither substitutes for independent corroboration
