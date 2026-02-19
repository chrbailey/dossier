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

## Quality Criteria
- Repository data should be current (use gh CLI for live data)
- Distinguish between public repos and likely private infrastructure
- Note what you CAN'T see — a company with 3 public repos may have 300 private ones
- Architecture assessment should be clearly labeled as inference where appropriate
