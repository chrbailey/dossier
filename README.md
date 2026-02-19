# Dossier — Automated SaaS Due Diligence

**What it does:** Given a domain name, produces a full due diligence report on the SaaS company — market position, technical reality, claims validation, academic footprint, replication cost — in 5-8 autonomous iterations.

**When to use it:** You're evaluating a SaaS company for acquisition, investment, partnership, or competitive intelligence. You need more than a landing page review but less than a $200K consulting engagement.

**How it works:** 7 analysis phases run as Claude Code sub-agents, orchestrated by Ralph Loop. No API keys, no external services beyond what Claude Code already provides. Just `target.env` → run → read the report.

---

## Quick Start

```bash
cd "/Volumes/OWC drive/Dev/dossier"

# 1. Set target
echo "DOMAIN=example.com" > target.env

# 2. Install helper dependencies (one-time)
python3 -m venv scripts/.venv
scripts/.venv/bin/pip install -r scripts/requirements.txt

# 3. Run the pipeline
# /ralph-loop --max-iterations 20 --completion-promise "DOSSIER_COMPLETE"
# (paste contents of ralph-prompt.md when prompted)

# 4. Read results
cat output/example.com/executive-summary.md
cat output/example.com/07-report.md
```

---

## What You Get

A complete dossier in `output/{domain}/`:

| File | Contents |
|------|----------|
| `executive-summary.md` | 2-page overview: strengths, risks, recommendation |
| `07-report.md` | Full PRD-format report with all sections |
| `01-discovery.md` | Company identity, digital footprint, tech signals |
| `02-market.md` | TAM/SAM/SOM, competitors, SWOT, positioning matrix |
| `03-technical.md` | GitHub analysis, architecture, code quality, dependencies |
| `04-claims.md` | Marketing vs reality — with shadow prediction market |
| `05-academic.md` | Papers, patents, open-source alternatives |
| `06-valuation.md` | SaaS metrics, replication cost, agent swarm build plan |
| `raw/*.json` | WHOIS, website content, GitHub repos, arXiv papers |

---

## The 7 Phases

```
P1 Discovery ──┬──→ P2 Market ────────┐
               ├──→ P3 Technical ──┐  │
               └──→ P5 Academic    │  │
                                   ▼  │
               P4 Claims (P1+P3) ──┤  │
                                   ▼  ▼
               P6 Valuation (all) ────┤
                                      ▼
               P7 Report (all) → DONE
```

| Phase | What It Does | Tools Used |
|-------|-------------|------------|
| **P1 Discovery** | Domain → company identity, digital footprint | WebSearch, WebFetch, WHOIS script, dig |
| **P2 Market** | Market size, competitors, SWOT, Gartner-style positioning | WebSearch, WebFetch |
| **P3 Technical** | GitHub org analysis, architecture, dependencies, quality signals | `gh` CLI, WebFetch |
| **P4 Claims** | Marketing claims vs evidence + shadow prediction market from internal signals | WebSearch (11 source types), prior phase outputs |
| **P5 Academic** | arXiv papers, patents, open-source alternatives | arXiv script, `gh search`, WebSearch |
| **P6 Valuation** | SaaS metrics, replication assessment, agent swarm build plan | All prior phases |
| **P7 Report** | Unified PRD + executive summary + confidence matrix | All prior phases |

### Phase 4: The Shadow Prediction Market

The most differentiated phase. Instead of taking marketing claims at face value, P4 triangulates **internal signals** from 11 source types — Glassdoor, Blind, Reddit, HN, LinkedIn, layoff trackers, arXiv, Twitter/X, job boards, Product Hunt, and review sites.

The core method: collect 3+ independent data points for each quantitative claim. The **spread** across sources becomes the confidence interval. When the company's claim falls outside the triangulated range, that's a material gap. When employee signals contradict marketing, the employee signals get higher weight.

Output includes an "AI Reality Score" (1-5): is their AI genuine research-grade ML, or a rules engine with a marketing department?

---

## Architecture

### Why Claude Code Native?

Traditional approach: build a Python CLI that wraps Claude API → manage keys, handle rate limits, parse responses, maintain code.

This approach: Claude Code **is** the execution engine. Sub-agents have direct access to WebSearch, WebFetch, `gh` CLI, file I/O. The "program" is 7 prompt files + 1 orchestration prompt. The "database" is `PROGRESS.md`. The "scheduler" is Ralph Loop.

**Result:** ~120 LOC of Python (two helper scripts) instead of 5K-20K LOC. The intelligence layer was already there.

### State Machine

```
target.env → PROGRESS.md (state) → ralph-prompt.md (scheduler)
                ↕                        ↕
        output/{domain}/          prompts/p{N}-*.md
        (phase outputs)           (sub-agent instructions)
```

Ralph Loop reads `PROGRESS.md` each iteration, identifies unblocked phases, dispatches sub-agents, updates state, and repeats until all phases complete or max iterations reached.

### Helper Scripts

Only two Python scripts exist — for tasks Claude Code can't do natively:

| Script | Purpose | Input → Output |
|--------|---------|---------------|
| `scripts/whois_lookup.py` | WHOIS records | domain → JSON |
| `scripts/arxiv_search.py` | Academic papers | query → JSON array |

Both output JSON to stdout. Called via `scripts/.venv/bin/python scripts/{name}.py`.

---

## For Agent Builders

### Patterns You Can Reuse

1. **Prompt-as-program:** Each phase is a markdown file that fully specifies a sub-agent's behavior. No code generation framework needed — the prompts ARE the code.

2. **PROGRESS.md as state machine:** A human-readable markdown file tracks completion state. Any agent can read it, any agent can update it. No database, no API.

3. **DAG via dependency rules:** Phase dependencies are declared in `ralph-prompt.md` as simple rules (`P1 + P3 → unlocks P4`). Ralph Loop interprets these each iteration. Adding a phase means adding one rule.

4. **Signal triangulation:** The Phase 4 methodology — collect 3+ independent sources, derive confidence from convergence — is reusable for any verification task.

5. **Materiality tiers:** CRITICAL / NOTABLE / MINOR classification with explicit trigger conditions. Prevents false alarms from minor discrepancies.

### Extending Dossier

**Add a new phase:**
1. Create `prompts/p{N}-{name}.md` with goal, steps, output format
2. Add dependency rule to `ralph-prompt.md`
3. Add to `templates/progress-template.md`

**Add a new data source:**
1. If it needs a library: add script to `scripts/`, update `requirements.txt`
2. If WebSearch/WebFetch suffices: just add instructions to the relevant phase prompt

**Run against a different domain:**
1. Edit `target.env`
2. Run Ralph Loop — each domain gets its own `output/{domain}/` directory

---

## Project Structure

```
dossier/
├── CLAUDE.md                    # Project rules for Claude Code
├── README.md                    # This file
├── ARCHITECTURE.md              # Technical architecture details
├── llm.md                       # LLM/agent integration guide
├── target.env                   # DOMAIN=example.com
├── ralph-prompt.md              # Ralph Loop orchestration prompt
├── pyproject.toml
├── .gitignore
│
├── scripts/                     # Python helpers (JSON stdout)
│   ├── whois_lookup.py
│   ├── arxiv_search.py
│   └── requirements.txt
│
├── prompts/                     # Sub-agent phase instructions
│   ├── p1-discovery.md
│   ├── p2-market.md
│   ├── p3-technical.md
│   ├── p4-claims.md             # Shadow prediction market
│   ├── p5-academic.md
│   ├── p6-valuation.md
│   └── p7-report.md
│
├── templates/                   # Report structure templates
│   ├── progress-template.md
│   ├── prd-template.md
│   ├── swot-template.md
│   └── magic-quadrant-template.md
│
└── output/                      # Generated reports (gitignored)
    └── {domain}/
        ├── PROGRESS.md
        ├── 01-discovery.md ... 07-report.md
        ├── executive-summary.md
        └── raw/*.json
```

---

## Limitations (V1)

- **No browser automation** — WebSearch/WebFetch only. Some sites (LinkedIn, Glassdoor) may limit what's accessible.
- **No financial APIs** — SaaS metrics are estimated from public signals, not Crunchbase/PitchBook data.
- **No deep code analysis** — GitHub repos are analyzed via `gh` CLI and file inspection, not cloned + run through static analysis.
- **Single domain** — no side-by-side comparison mode yet.

See the V2 roadmap in `ARCHITECTURE.md`.

---

## License

MIT
