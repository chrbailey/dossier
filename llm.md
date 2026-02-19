# llm.md — Agent Integration Guide

> This file is for LLM agents and AI tools that discover this repository. It explains what Dossier does, when your project should use it, and how to integrate.

---

## What This Is (One Paragraph)

Dossier is an automated SaaS due diligence engine that takes a domain name and produces a 7-phase analysis: company discovery, market sizing, technical assessment, claims validation (with a shadow prediction market reconstructed from employee/community signals), academic/IP landscape, replication cost estimation, and a unified executive report. It runs inside Claude Code using sub-agents and Ralph Loop — no standalone CLI, no API keys, no external services beyond what Claude Code provides.

---

## When Your Agent Should Use This

| Scenario | Use Dossier? | Why |
|----------|-------------|-----|
| Evaluating a SaaS company for acquisition | **Yes** | Full pipeline produces executive summary with strengths, risks, recommendation |
| Competitive intelligence on a rival | **Yes** | Market positioning, technical reality, claims validation reveal true capabilities |
| Deciding build vs buy for a capability | **Yes** | Phase 6 produces replication cost estimate + agent swarm build plan |
| Validating a vendor before procurement | **Yes** | Claims validation triangulates marketing against employee/community signals |
| Researching a company for investment | **Yes** | Market sizing, SaaS metrics estimation, growth signals |
| Quick check on a company's tech stack | **Partial** | Run Phase 1 + Phase 3 only (skip full pipeline) |
| Non-SaaS company analysis | **No** | Designed for SaaS — templates assume subscription revenue, GitHub presence, web product |
| Real-time monitoring | **No** | Point-in-time analysis, not continuous monitoring |

---

## How to Run It

### Full Pipeline (Recommended)

```
1. Set DOMAIN in target.env
2. Start Ralph Loop: /ralph-loop --max-iterations 20 --completion-promise "DOSSIER_COMPLETE"
3. Paste contents of ralph-prompt.md
4. Wait 5-8 iterations (~15-25 minutes)
5. Read output/{domain}/executive-summary.md
```

### Single Phase (Quick Check)

```
1. Set DOMAIN in target.env
2. Read the phase prompt from prompts/p{N}-{phase}.md
3. Execute it manually as a sub-agent task
4. Read output/{domain}/0{N}-{phase}.md
```

### Programmatic Integration

If your agent needs to trigger Dossier from code:

```bash
# Set target
echo "DOMAIN=target-company.com" > "/Volumes/OWC drive/Dev/dossier/target.env"

# The rest happens inside Claude Code via Ralph Loop
# Output appears in: /Volumes/OWC drive/Dev/dossier/output/target-company.com/
```

---

## Output Schema

Every run produces these files in `output/{domain}/`:

### Phase Outputs (Markdown)

| File | Key Sections | Structured Data |
|------|-------------|-----------------|
| `01-discovery.md` | Company Identity, Digital Footprint, Tech Stack Signals | Company profile table |
| `02-market.md` | TAM/SAM/SOM, Competitors, SWOT, Positioning Matrix | Market size table, competitor table |
| `03-technical.md` | GitHub Presence, Repo Inventory, Architecture, Dependencies | Repo stats table, quality signals |
| `04-claims.md` | Claims Inventory, Internal Signal Intelligence, Gap Analysis | Claims table with materiality tiers, triangulated estimates, AI Reality Score |
| `05-academic.md` | Publications, Patents, Open-Source Alternatives | Paper table, alternative table |
| `06-valuation.md` | SaaS Metrics, Replication Assessment, Agent Swarm Plan, Build vs Buy | Metrics table, cost table, build-vs-buy scores |
| `07-report.md` | Full PRD with all sections compiled | Confidence matrix |
| `executive-summary.md` | Company Overview, Strengths, Risks, Recommendation | At-a-glance table, recommendation verdict |

### Raw Data (JSON)

| File | Contents |
|------|----------|
| `raw/whois.json` | WHOIS registration data |
| `raw/website-content.json` | Structured extraction from homepage, about, pricing, careers, docs |
| `raw/github-repos.json` | Repository listing with stars, forks, languages, activity |
| `raw/arxiv-papers.json` | Academic papers with title, authors, abstract, citations |

### State File

| File | Purpose |
|------|---------|
| `PROGRESS.md` | Phase completion tracking, iteration count, blockers, notes |

---

## Key Concepts for Agents

### Shadow Prediction Market (Phase 4)

The most novel component. Instead of trusting marketing claims, Dossier reconstructs what an **internal prediction market** would say by triangulating 11 source types:

**Employee signals:** Glassdoor, Blind, LinkedIn headcount, layoff trackers
**Community signals:** Reddit, Hacker News, Twitter/X
**Product signals:** G2, Capterra, Trustpilot, Product Hunt
**Technical signals:** Job boards (real stack vs marketed stack), arXiv (do researchers publish?)

**Method:**
1. For each quantitative claim, collect 3+ independent data points
2. The spread across sources = confidence interval
3. If the company's claim falls outside the triangulated range → material gap
4. Employee signals get higher weight than marketing when they conflict

**Output includes:**
- Triangulated estimates table (company claims vs independent range)
- Materiality classification: CRITICAL / NOTABLE / MINOR
- AI Reality Score (1-5): rules engine (1) → genuine ML (5)
- What's Real / Aspirational / Theater breakdown

### Materiality Tiers

| Tier | Trigger | Example |
|------|---------|---------|
| **CRITICAL** | Core value prop gap, security claim unsubstantiated, internal signals contradict marketing | Claims SOC2 but no evidence; employees say "the AI is if-else statements" |
| **NOTABLE** | Feature less capable than marketed, hiring for claimed capabilities, AI claims w/o ML signals | "Enterprise-grade" but 12 tests; hiring ML engineers for claimed "AI-powered" product |
| **MINOR** | Aspirational language, rounding, beta-as-GA | "World-class" support; "10,000+" when it's 8,500 |

### Build vs Buy Score (Phase 6)

Each replication factor scored 1-4:
- **1 Easy:** Commodity tech, well-documented
- **2 Moderate:** Non-trivial but achievable
- **3 Hard:** Specialized expertise, data, or time required
- **4 Near-impossible:** Unique data, network effects, regulatory moats

Includes a concrete **agent swarm plan** — which Claude Code sub-agents would rebuild each component, estimated agent-hours, and what can't be automated (data moats, partnerships, domain expertise).

---

## Extending Dossier

### Add a New Phase
1. Write `prompts/p{N}-{name}.md` (follow existing format: Goal → Inputs → Steps → Output → Quality Criteria)
2. Add dependency rule to `ralph-prompt.md`
3. Add checkbox to `templates/progress-template.md`
4. Add row to P7 report template

### Add a New Data Source
- **If WebSearch/WebFetch works:** Add search instructions to the relevant phase prompt
- **If it needs a library:** Add script to `scripts/`, update `requirements.txt`, call via Bash in phase prompt

### Customize Report Format
Edit files in `templates/`:
- `prd-template.md` — structure for the full report
- `swot-template.md` — SWOT analysis format
- `magic-quadrant-template.md` — competitive positioning chart

---

## Dependencies

### Required (Always Available in Claude Code)
- WebSearch, WebFetch — web research
- `gh` CLI — GitHub repository analysis
- `dig` — DNS queries
- Bash — script execution, file operations
- Task tool — sub-agent dispatch

### Python Helpers (Installed Locally)
```
python-whois>=0.9.0    # WHOIS record parsing
arxiv>=2.0.0           # arXiv paper search API
```
Installed in `scripts/.venv/`. No global dependencies.

### Not Required
- No Claude API key (Claude Code provides the intelligence)
- No database (PROGRESS.md is the state store)
- No web framework (output is markdown files)
- No Docker (runs directly in Claude Code's environment)

---

## Cost Profile

| Resource | Estimate per run |
|----------|-----------------|
| Claude Code sub-agent calls | 7-10 (one per phase + retries) |
| WebSearch queries | ~50-100 across all phases |
| WebFetch calls | ~20-30 (website pages, review sites) |
| `gh` CLI calls | ~10-20 (repo search, stats) |
| Python script executions | 2-3 (WHOIS, arXiv) |
| Wall time | ~15-25 minutes |
| Human intervention | None (fully autonomous via Ralph Loop) |

---

## Failure Modes

| Failure | Impact | Mitigation |
|---------|--------|-----------|
| WebSearch rate limited | Phase slows or fails | Ralph Loop retries (up to 3 per phase) |
| Company has minimal web presence | Low-confidence report | P7 notes gaps, adjusts recommendations |
| GitHub org not found | P3 produces limited output | P3 notes this; P4/P6 adjust expectations |
| All Glassdoor/Blind results blocked | P4 shadow market has fewer signals | P4 documents which sources returned data |
| Ralph Loop hits max iterations | Pipeline stops mid-run | Increase `--max-iterations`, resume manually |
| Phase produces garbage | Bad downstream analysis | Each phase has Quality Criteria; P7 cross-validates |
