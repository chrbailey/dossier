# Architecture — Dossier

## Design Philosophy

**Prompt-as-program.** The intelligence layer (Claude Code) already exists. Instead of wrapping it in Python, we let the prompts be the program. Each phase prompt fully specifies a sub-agent's behavior. The orchestration prompt (`ralph-prompt.md`) is the scheduler. `PROGRESS.md` is the database. Python only appears where Claude Code genuinely can't do the work (WHOIS parsing, arXiv API).

**Result:** ~120 LOC of Python. ~1,300 lines of structured prompts. Full SaaS due diligence pipeline.

---

## System Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Claude Code                       │
│                                                      │
│  ┌───────────────────────────────────────────────┐  │
│  │              Ralph Loop                        │  │
│  │  (reads PROGRESS.md → dispatches agents →      │  │
│  │   updates state → repeats until done)          │  │
│  └──────────┬────────────────────────────┬───────┘  │
│             │                            │           │
│    ┌────────▼────────┐         ┌─────────▼───────┐  │
│    │   Sub-Agent P1   │         │  Sub-Agent P2  │  │
│    │   (discovery)    │         │  (market)      │  │
│    │                  │         │                │  │
│    │  WebSearch       │         │  WebSearch     │  │
│    │  WebFetch        │         │  WebFetch      │  │
│    │  Bash (scripts)  │         │  Read (P1)     │  │
│    └────────┬─────────┘         └───────┬────────┘  │
│             │                           │            │
│             ▼                           ▼            │
│    output/{domain}/            output/{domain}/      │
│    01-discovery.md             02-market.md          │
│    raw/whois.json                                    │
│                                                      │
│    ... (P3-P7 similar pattern) ...                   │
│                                                      │
└─────────────────────────────────────────────────────┘

External:
  ├── Web (via WebSearch/WebFetch)
  ├── GitHub API (via gh CLI)
  ├── WHOIS servers (via python-whois)
  └── arXiv API (via arxiv library)
```

---

## Data Flow

### Input → Output Pipeline

```
target.env (DOMAIN=example.com)
    │
    ▼
P1 Discovery ─── WebSearch, WebFetch, WHOIS, DNS
    │               └── 01-discovery.md + raw/whois.json + raw/website-content.json
    │
    ├──→ P2 Market ─── WebSearch, WebFetch, reads P1
    │       └── 02-market.md
    │
    ├──→ P3 Technical ─── gh CLI, WebFetch, reads P1
    │       └── 03-technical.md + raw/github-repos.json
    │
    ├──→ P5 Academic ─── arXiv script, gh search, WebSearch, reads P1
    │       └── 05-academic.md + raw/arxiv-papers.json
    │
    └──→ P4 Claims ─── WebSearch (11 sources), reads P1 + P3
            └── 04-claims.md
                │
                ├──→ P6 Valuation ─── reads ALL P1-P5
                │       └── 06-valuation.md
                │
                └──→ P7 Report ─── reads ALL P1-P6
                        └── 07-report.md + executive-summary.md
```

### State Management

All state lives in `output/{domain}/PROGRESS.md`:

```markdown
# Dossier: example.com
Started: 2026-02-18T14:00:00Z
Iteration: 3

## Phases
- [x] P1 Discovery — completed 2026-02-18T14:05:00Z
- [x] P2 Market — completed 2026-02-18T14:12:00Z
- [ ] P3 Technical — IN PROGRESS
- [ ] P4 Claims — blocked (needs P1, P3)
...
```

Ralph Loop reads this file at the start of every iteration. Sub-agents update it after completing their phase. No external state store.

**Why markdown for state?**
- Human-readable (you can check progress by opening the file)
- Agent-readable (structured enough for LLMs to parse reliably)
- Version-controlled (git tracks every state change)
- Zero dependencies (no database, no Redis, no API)

---

## Phase Dependency DAG

```
        P1 (Discovery)
       /    |    \
      /     |     \
    P2    P3     P5
  (Market) (Tech) (Academic)
      \     |     /
       \    |    /
        P4 (Claims)     ← needs P1 + P3
          |
        P6 (Valuation)  ← needs P1-P5
          |
        P7 (Report)     ← needs P1-P6
```

**Parallelism opportunities:**
- P2, P3, P5 run simultaneously after P1
- P4 starts as soon as P1 + P3 are done (doesn't wait for P2 or P5)
- P6 is the convergence point — waits for everything

**Typical execution: 5 iterations, ~15-25 minutes.**

---

## Claims Validation Architecture (Phase 4)

Phase 4 is the most complex phase. It implements a **shadow prediction market** by triangulating signals across 11 source types.

### Signal Collection Layer

```
┌────────────────────────────────────────────────┐
│              Source Matrix (11 types)            │
├────────────────────────────────────────────────┤
│ Employee signals:                               │
│   Glassdoor, Blind, LinkedIn, Layoff trackers   │
│                                                 │
│ Community signals:                              │
│   Reddit, Hacker News, Twitter/X                │
│                                                 │
│ Product signals:                                │
│   G2/Capterra/Trustpilot, Product Hunt          │
│                                                 │
│ Technical signals:                              │
│   Job boards, arXiv/Google Scholar              │
└───────────────────┬────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────────┐
│           Triangulation Engine                  │
│                                                 │
│  For each quantitative claim:                   │
│    1. Collect 3+ independent data points        │
│    2. Compute spread (= confidence interval)    │
│    3. Compare company claim against range       │
│    4. If claim is outlier → flag as gap          │
│                                                 │
│  Bayesian update:                               │
│    Prior = company's claim                      │
│    Evidence = each independent signal           │
│    3+ agreeing signals = high confidence        │
│    Contradictory signals = investigation flag   │
└───────────────────┬────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────────┐
│          Materiality Classification             │
│                                                 │
│  CRITICAL: core value prop, security/compliance,│
│    internal signals contradict marketing,       │
│    triangulated estimate diverges significantly │
│                                                 │
│  NOTABLE: less capable than marketed, hiring    │
│    for claimed capabilities, AI claims w/o      │
│    ML hiring or publications                    │
│                                                 │
│  MINOR: aspirational language, rounding,        │
│    beta-as-GA, mild positioning spin            │
└───────────────────┬────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────────┐
│       Internal Prediction Market Summary        │
│                                                 │
│  What's real / aspirational / theater           │
│  Morale trajectory                              │
│  AI Reality Score (1-5)                         │
└────────────────────────────────────────────────┘
```

---

## Error Handling

```
Phase fails?
    │
    ├── Log error in PROGRESS.md → ## Blockers
    ├── Mark phase as FAILED
    ├── Continue with unblocked phases
    │
    └── Next iteration:
        ├── Retry failed phase (up to 3 attempts)
        └── After 3 failures → SKIPPED
            └── P7 Report runs anyway, notes gaps
```

No phase failure blocks the entire pipeline. P7 (Report) is designed to work with incomplete data — it notes which sections have low confidence and recommends follow-up investigation.

---

## File Organization Rationale

| Directory | Purpose | Git-tracked? |
|-----------|---------|-------------|
| `prompts/` | Sub-agent instructions — the "program" | Yes |
| `templates/` | Output structure definitions | Yes |
| `scripts/` | Python helpers for external APIs | Yes |
| `output/` | Generated reports per domain | No (gitignored) |
| `output/{domain}/raw/` | Raw JSON from data collection | No |

**Why gitignore output?** Each run generates domain-specific data that may contain sensitive competitive intelligence. Keep the tool generic; keep the results private.

---

## V2 Roadmap

| Feature | V1 (Current) | V2 (Planned) |
|---------|-------------|-------------|
| Web data | WebSearch + WebFetch | MCP_DOCKER browser automation (Playwright) |
| GitHub | `gh` CLI (metadata only) | Clone repos, run `scc`, `radon`, `bandit` |
| Tech detection | DNS + job posting inference | Wappalyzer script (`scripts/tech_detect.py`) |
| Market data | LLM synthesis from web | Crunchbase API, PitchBook |
| Financial | Web search for funding rounds | SEC EDGAR, annual reports |
| Claims sources | 11 web-searchable sources | + SEC filings, press releases, court records |
| Report format | Markdown files | Next.js interactive dashboard (`viewer/`) |
| Comparison | Single domain per run | Side-by-side multi-domain comparison |
| Integration | Ralph Loop prompt paste | `/dossier example.com` Claude Code skill |
| Scheduling | Manual trigger | Periodic re-evaluation with diff report |

### V2 Data Collection Additions

```python
# scripts/tech_detect.py — Wappalyzer integration
# Input: URL → Output: JSON (detected technologies, confidence)
# Requires: python-Wappalyzer

# scripts/sec_search.py — SEC EDGAR filings
# Input: company name → Output: JSON (10-K, 10-Q, 8-K filings)
# Requires: sec-edgar-downloader
```

### V2 Viewer Architecture

```
viewer/                          # Next.js 16 app
├── app/
│   ├── page.tsx                 # Domain selector
│   ├── [domain]/
│   │   ├── page.tsx             # Executive summary dashboard
│   │   ├── market/page.tsx      # Interactive SWOT + positioning
│   │   ├── technical/page.tsx   # GitHub stats + architecture viz
│   │   ├── claims/page.tsx      # Claims table with evidence drill-down
│   │   └── compare/page.tsx     # Side-by-side domain comparison
│   └── api/
│       └── dossier/route.ts     # Read output/ dir, serve as JSON
├── components/
│   ├── confidence-badge.tsx     # HIGH/MEDIUM/LOW visual indicator
│   ├── claims-table.tsx         # Sortable/filterable claims grid
│   └── positioning-chart.tsx    # Interactive magic quadrant
└── lib/
    └── parse-dossier.ts         # Markdown → structured data
```
