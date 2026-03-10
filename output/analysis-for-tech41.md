# Deep Dive Analysis: Dossier Repo — Stanford TECH 41 Suitability Assessment

## What This Repo Actually Is

**Dossier** is an automated SaaS company due diligence engine built *entirely inside Claude Code*. You give it a domain name, and it runs 7 analysis phases via AI sub-agents orchestrated by a "Ralph Loop" scheduler, producing a full investment-grade(ish) dossier on the target company.

The key architectural insight: **the prompts ARE the program**. There are only ~120 lines of Python (two helper scripts for WHOIS and arXiv). Everything else — the orchestration, analysis, data collection, report generation — is structured markdown prompts that Claude Code sub-agents execute autonomously.

### What's In The Repo

| Component | Files | Purpose |
|-----------|-------|---------|
| **Orchestration** | `ralph-prompt.md`, `CLAUDE.md` | The "scheduler" — reads state, dispatches agents, loops |
| **Phase Prompts** | `prompts/p1-p7*.md` (7 files) | Each is a full sub-agent program (~1,300 lines total) |
| **Helper Scripts** | `scripts/whois_lookup.py`, `scripts/arxiv_search.py` | Only Python — for APIs Claude can't call natively |
| **Templates** | `templates/*.md` (4 files) | Output structure definitions (SWOT, Magic Quadrant, PRD) |
| **Generated Output** | `output/{domain}/*.md` | Full dossiers for 5 companies |
| **Validation** | `output/validation/*.md` (8 files) | Bias audits, fact-checks, calibration corrections |
| **Docs** | `README.md`, `ARCHITECTURE.md`, `llm.md` | Architecture, agent integration guide |

### Companies Analyzed (with completed dossiers)

1. **Okta** — $2.61B revenue, identity/security SaaS
2. **Glean** — $200M ARR, enterprise AI search
3. **Vercel** — $200M ARR, developer platform (Next.js)
4. **Sierra AI** — $150M ARR, enterprise AI agents
5. **Cerebras** — $950M-$1.2B revenue, wafer-scale AI chips

### The 7-Phase Pipeline

```
P1 Discovery → P2 Market + P3 Technical + P5 Academic (parallel)
             → P4 Claims Validation (needs P1+P3)
             → P6 Valuation (needs all)
             → P7 Final Report → DONE
```

**Phase 4 (Claims Validation)** is the standout — it implements a "Shadow Prediction Market" that triangulates 11 source types (Glassdoor, Blind, Reddit, HN, LinkedIn, job boards, arXiv, review sites) to independently verify company marketing claims. Each claim gets a verdict: VERIFIED / PLAUSIBLE / EXAGGERATED / CONTRADICTED / UNVERIFIABLE.

---

## Hardcore Hot Take

### What's Genuinely Impressive

1. **The architecture is elegant.** Prompt-as-program is a real pattern. Using PROGRESS.md as a state machine, markdown prompts as agent programs, and Ralph Loop as a DAG scheduler — with zero framework code — is a legitimate architectural contribution. This is how people will build agent systems in 2026-2027.

2. **The output quality is surprisingly high.** The 5 completed dossiers contain real analysis — market sizing with TAM/SAM/SOM, competitive positioning matrices, SaaS metrics estimation, replication cost assessment. The Okta report alone runs ~15,000+ words with SEC-filing-verified revenue data.

3. **The self-audit is what makes it credible.** The `output/validation/` directory contains 8 validation reports that identify 6 systematic LLM biases (hardware worship, publication proxy, culture catastrophizing, FAANG-wins prior, description-as-construction fallacy, post-ZIRP skepticism) and apply 63 documented corrections. This level of methodological honesty is rare.

4. **Phase 4's Shadow Prediction Market** is a genuinely novel methodology for AI-assisted due diligence — reconstructing what an internal prediction market would say by triangulating employee/community/product signals against marketing claims.

5. **The V2 roadmap is realistic.** Next.js dashboard, Wappalyzer integration, SEC EDGAR, MCP browser automation — these are achievable extensions, not pie-in-the-sky fantasies.

### What's Weak

1. **Non-reproducibility is the fatal flaw.** Run it twice, get different scores. No inter-rater reliability. No confidence intervals that mean anything. The validation files call this out honestly, but it's still unresolved.

2. **"120 LOC of Python" undersells the actual complexity.** The 1,300 lines of prompt engineering ARE the code. Saying "no code" is like saying a spreadsheet with 500 formulas is "no code" — technically true, architecturally misleading.

3. **No tests.** Zero test coverage. No way to validate that prompt changes don't break output quality. No regression suite. For a tool that claims to produce "due diligence," this is ironic.

4. **The data access problem is fundamental.** NRR, gross margins, burn rate, cap table — the metrics that actually determine investment decisions — are inaccessible to web search. The tool produces a screening report, not due diligence. The README somewhat oversells this.

5. **Hardcoded Mac paths.** `"/Volumes/OWC drive/Dev/dossier"` appears in ralph-prompt.md and README — this only runs on one person's machine. Not portable.

---

## Stanford TECH 41 Suitability Assessment

### What TECH 41 Expects

Based on the [course description](https://continuingstudies.stanford.edu/courses/detail/20252_TECH-41), TECH 41 ("AI Prototyping") at Stanford Continuing Studies teaches professionals to:

- Identify high-impact AI use cases
- Scope minimum viable products
- Prototype AI solutions using prompt engineering, no-code platforms, open-source models
- Apply rapid validation techniques and ethical guardrails
- Build a **repeatable AI prototyping framework** and a **working prototype**

The course targets product managers, entrepreneurs, business leaders, and technical professionals. Instructor is Ata Tahiroglu (ex-Apple, ex-Salesforce AI/ML).

### Fit Score: 8.5/10 — STRONG SUBMIT

**Why this works for TECH 41:**

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| **High-impact use case** | 9/10 | SaaS due diligence is a real $200K+ consulting engagement compressed to 25 minutes |
| **MVP scoping** | 9/10 | Clean 7-phase pipeline, clear V1 boundaries, honest limitations section |
| **Prompt engineering depth** | 10/10 | 1,300 lines of structured prompts across 7 phases — this IS prompt engineering at scale |
| **Working prototype** | 9/10 | 5 completed company analyses with real output. Not a demo, not a mockup — actual artifacts |
| **Repeatable framework** | 8/10 | Change `target.env`, run again. Demonstrated on 5 different companies |
| **Rapid validation** | 8/10 | Self-audit pipeline with bias identification and 63 corrections |
| **Ethical guardrails** | 7/10 | Materiality tiers prevent false alarms, but no discussion of ethical implications of automated company assessment |
| **Technical sophistication** | 9/10 | DAG scheduling, parallel agent dispatch, graceful degradation, state machine — all via prompts |
| **Documentation quality** | 9/10 | README, ARCHITECTURE.md, llm.md are publication-quality |
| **Originality** | 9/10 | Shadow Prediction Market, prompt-as-program architecture, LLM bias self-audit — all novel |

### What to Fix Before Submission (10-day punch list)

1. **Remove hardcoded paths.** Replace `/Volumes/OWC drive/Dev/dossier` with relative paths or `$PROJECT_ROOT`. Takes 30 minutes.

2. **Add an ethics section.** TECH 41 emphasizes ethical guardrails. Add a section on: risks of automated company assessment, potential for LLM hallucination in financial analysis, disclosure requirements if used for actual investment decisions.

3. **Add a "How to Run" video or GIF.** Show the Ralph Loop in action. A 2-minute screen recording of it analyzing a company would be the single most impactful addition.

4. **Write a 1-page reflection.** What you learned about prompt engineering at scale, what surprised you, what failed. TECH 41 is a continuing education course — they want to see learning, not just output.

5. **Clean up the output directory.** Either gitignore it properly (it's supposed to be gitignored but it's committed) or curate one exemplary dossier (Okta is the strongest) as a showcase.

6. **Add a cost/time table.** How much did each run cost in Claude Code credits? How long did each company take? This is the kind of practical data a TECH 41 instructor wants to see.

### What NOT to Do

- Don't add tests or CI/CD — it's a prototype, not production software. TECH 41 explicitly values rapid prototyping over engineering polish.
- Don't build the V2 Next.js dashboard — scope creep will kill you in 10 days.
- Don't rewrite the prompts — they work. Ship what you have.
- Don't pretend it's more than it is. Call it a "screening tool," not "due diligence." The honesty will resonate with a Stanford audience.

---

## Bottom Line

**This is one of the best TECH 41 submissions I could imagine.** It demonstrates exactly what the course teaches — taking an AI idea (automated SaaS due diligence), scoping it to an MVP (7-phase prompt pipeline), prototyping it with prompt engineering (zero framework code), validating it (5 real companies + bias self-audit), and producing a repeatable framework (change domain, run again).

The Shadow Prediction Market methodology alone would make a strong paper. The prompt-as-program architecture is a genuine contribution to how people think about building agent systems. And the self-audit pipeline (identifying 6 LLM biases, applying 63 corrections) shows the kind of critical thinking that separates an A from a B+.

**Ship it. Fix the paths, add the ethics section, write the reflection. You have 10 days and you need 2.**
