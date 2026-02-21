# Dossier Corrections Log — Calibrated v1

**Date:** 2026-02-19
**Branch:** `corrections/calibrated-v1`
**Source of truth:** `validation/final-calibrated-output.md`
**Methodology:** Post-validation calibration pass applying 63 corrections from multi-layer validation pipeline

---

## Already Applied (Pre-Pass)
- Cerebras: SambaNova "acquired" → "term sheet stalled" (executive-summary, 02-market, 07-report, PROGRESS)
- Vercel: "High school dropout" → "Self-taught engineer" (05-academic, 07-report)

---

## Corrections Applied

### CEREBRAS (COR-001 through COR-017)

| ID | Description | Files | Before | After |
|----|-------------|-------|--------|-------|
| COR-001/002 | AI Reality split score | 07-report, exec-summary | 5/5 | 5.0/5 (tech) / 3.5/5 (business) |
| COR-003/004/005 | Build vs Buy downgrade | 07-report, exec-summary, 06-valuation | 3.5/4 | 3.0/4 |
| COR-006/007 | Verdict downgrade | 07-report (×3), exec-summary, PROGRESS | STRONG CANDIDATE | QUALIFIED CANDIDATE |
| COR-008–012 | NVIDIA-Groq date/structure | 01-discovery, 02-market, 05-academic, 06-valuation, 07-report | "Jan 2026 acquisition" | "Dec 24, 2025 licensing + asset deal; Groq independent" |
| COR-013/014 | Gordon Bell attribution | 05-academic, 07-report | "won" | "awarded to Argonne team; Cerebras contributed hardware" |
| COR-015 | FY2024 revenue range | 06-valuation, 07-report | "$272M" or "$500M" single figures | "$272-500M" range with uncertainty note |
| COR-016 | Gross margin caution | 02-market | 45-50% stated as projection | Added caution: unproven at scale |
| COR-017 | TSMC risk context | 07-report | TSMC as Cerebras-specific risk | Contextualized as industry-wide (Apple/NVIDIA/AMD) |

### GLEAN (COR-018 through COR-032)

| ID | Description | Files | Before | After |
|----|-------------|-------|--------|-------|
| COR-018 | AI Reality downgrade | 04-claims, 07-report | 4.0/5 | 3.7/5 |
| COR-019/020 | Build vs Buy upgrade | 06-valuation, exec-summary | 2.7/4 | 3.1/4 |
| COR-021/022/023 | Verdict upgrade | exec-summary, 07-report, PROGRESS | PROCEED WITH CAUTION | PROCEED (standard diligence) |
| COR-024/025 | Culture reframe | exec-summary, 04-claims | "deteriorating" | "strain requiring monitoring" + peer comparables |
| COR-026/027/028 | Microsoft reframe | exec-summary, 02-market, 07-report | "existential threat" | "significant competitive pressure" + coexistence evidence |
| COR-029 | Knowledge Graph reframe | 07-report | "commodity GraphRAG" | Removed dismissal |
| COR-030 | Valuation context | 06-valuation | 36x noted | Added: lowest despite equal growth |
| COR-031 | Dell partnership elevation | 07-report, exec-summary | Mentioned | Elevated as on-prem differentiator |
| COR-032 | $1M+ segment elevation | exec-summary | Mentioned | Elevated as strongest NRR proxy |

### SIERRA (COR-033 through COR-046)

| ID | Description | Files | Before | After |
|----|-------------|-------|--------|-------|
| COR-033 | AI Reality upgrade | 04-claims, 07-report | 3.5/5 | 3.8/5 |
| COR-034 | Build vs Buy upgrade | 06-valuation, 07-report | 2.82/4 | 3.1/4 |
| COR-035 | Founder Network downgrade | 06-valuation, 07-report | 4.0/4 | 3.5/4 (Taylor attention-split) |
| COR-036/037/038 | Verdict upgrade | exec-summary, 07-report, PROGRESS | PROCEED WITH CAUTION | LEAN PROCEED |
| COR-039–042 | LLM wrapper reframe | 04-claims, 06-valuation, 07-report, exec-summary | "LLM wrapper" | "model provider dependency" |
| COR-043/044 | Gap.com severity | 04-claims, exec-summary, 07-report | CRITICAL | MEDIUM (1 of 12+ deployments) |
| COR-045 | Compliance elevation | 07-report | Mentioned | Elevated SOC2+HIPAA+GDPR+ISO as execution signal |
| COR-046 | Taylor attention-split | 07-report, exec-summary | Mentioned | Strengthened OpenAI board chair risk |

### VERCEL (COR-047 through COR-056)

| ID | Description | Files | Before | After |
|----|-------------|-------|--------|-------|
| COR-047 | AI Reality dual score | 04-claims, 07-report | 3.2/5 | 3.2/5 (depth) / 4.2/5 (leverage) |
| COR-048 | Next.js moat downgrade | exec-summary, 06-valuation, 07-report | 4.0/4 | 3.6/4 |
| COR-049/050 | Verdict rationale rebalance | exec-summary, PROGRESS | Original rationale | Rebalanced per calibration |
| COR-051/052 | Cloudflare reframe | exec-summary, 02-market | "existential convergence" | "coexistence more likely" |
| COR-053 | Netanyahu demote | exec-summary, 07-report | Key Risk #3 | Contributing factor |
| COR-054 | v0 $42M ARR reframe | exec-summary, 02-market | Negative anchoring | Top 1% time-to-revenue |
| COR-055 | v0 $100M probability | 04-claims | 45% | 55-60% |
| COR-056 | Heroku migration wave | 07-report | Not mentioned | Added as near-term catalyst |

### CROSS-DOSSIER (COR-057 through COR-060)

| ID | Description | Files | Before | After |
|----|-------------|-------|--------|-------|
| COR-057 | Model provider dependency for Glean | glean 04-claims, 07-report, exec-summary | Inconsistent framing | Consistent "model provider dependency" |
| COR-058 | Employee sentiment for Cerebras | cerebras 07-report | Inconsistent weighting | Consistent with cross-dossier methodology |
| COR-059 | NRR as BLOCKING DATA GAP | all 4 exec-summaries | Not flagged | Added BLOCKING DATA GAP flag |
| COR-060 | Customer reference calls MANDATORY | sierra + cerebras 07-report | Not mentioned | Added as mandatory next step |

### HTML DASHBOARD (COR-061 through COR-063)

| ID | Description | File | Before | After |
|----|-------------|------|--------|-------|
| COR-061 | Sierra valuation | ai-claims-reality-index.html | $4.5B | $10B |
| COR-062 | Vercel valuation | ai-claims-reality-index.html | $3.17B | $9.3B |
| COR-063 | Version annotation | ai-claims-reality-index.html | None | "corrections applied 2026-02-19" |

---

## Verification Status

- [x] Grep checks passed (orphaned old values) — all old verdicts/scores only appear in calibration notes or correction logs
- [x] "LLM wrapper" removed from Sierra and Glean — replaced with "model provider dependency"
- [x] Groq "Jan 2026" references in cerebras are about HN post (different event), not NVIDIA deal — correct
- [x] "existential" in Glean only in corrected framing or unrelated contexts — clean
- [x] All 4 PROGRESS.md files have Corrections Pass sections
- [x] All 4 exec-summaries have BLOCKING DATA GAP flags
- [x] HTML dashboard: Sierra $10B, Vercel $9.3B, version annotation present
- [x] Cross-file score consistency verified
- [x] Git committed — `0b9b31d` on branch `corrections/calibrated-v1`
