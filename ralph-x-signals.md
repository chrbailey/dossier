# Ralph Loop — X Social Signal Discovery

## Goal

Iteratively discover and rank the **100 most relevant X (Twitter) accounts** for
the target company. Same Ralph Loop pattern as the main pipeline, but applied to
social graph discovery instead of due diligence phases.

**Done when:** `social-signals-x.md` contains ≥100 ranked accounts with SSCS ≥ 0.50
→ output `<promise>X_SIGNALS_COMPLETE</promise>`

## Setup

```bash
DOSSIER_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$DOSSIER_ROOT"
source target.env
echo "Target: $DOMAIN"
```

Read `output/${DOMAIN}/01-discovery.md` to extract:
- Company name, product name(s)
- CEO, CTO, founders (names)
- Key competitors
- GitHub org name

If P1 hasn't run yet, this phase cannot start. P1 is a prerequisite.

## Iteration Logic

This is a **4-attempt discovery loop** inspired by autoresearch. Each attempt uses
a different search strategy. The loop narrows from broad discovery to a validated Top 100.

### Attempt 1: SEED

**Goal:** Find the obvious, high-profile accounts.

Launch a sub-agent with `prompts/px-social-signals.md` (Attempt 1 section).
The agent should:
1. Search for official company accounts, CEO/founder accounts, DevRel accounts
2. Write initial candidates to `output/{DOMAIN}/social-signals-x.md`
3. Log all search queries used

After completion:
```bash
python3 scripts/score_x_accounts.py "output/${DOMAIN}/social-signals-x.md"
```

Log SSCS in PROGRESS.md: `PX attempt 1: SSCS = {score}, accounts = {N}`

### Attempt 2: EXPAND

**Goal:** Follow the social graph outward from seed accounts.

Launch a sub-agent with:
- `prompts/px-social-signals.md` (Attempt 2 section)
- The current `social-signals-x.md` as context (so it doesn't re-discover known accounts)

The agent should:
1. Search for employees, former employees, customers, critics, investors
2. **Append** new accounts to the existing table (don't overwrite seeds)
3. Update relevance scores if new information changes an existing account's score

After completion, evaluate SSCS again.

If SSCS improved → keep. If regressed → revert to previous version.

### Attempt 3: DEEPEN

**Goal:** Find hidden/niche voices that don't appear in obvious searches.

Launch a sub-agent with:
- `prompts/px-social-signals.md` (Attempt 3 section)
- Current `social-signals-x.md` as context
- Category gap analysis from SSCS evaluation (which categories are underrepresented?)

The agent should:
1. Target underrepresented categories specifically
2. Search for layoff signals, security researchers, competitor employees, migration voices
3. Search for accounts that *reply to* high-relevance accounts (graph expansion)
4. **Append** new accounts, update scores

Evaluate SSCS. Keep or revert.

### Attempt 4: VALIDATE

**Goal:** No new discovery. Verify, de-duplicate, score, rank, cut to 100.

Launch a sub-agent with:
- `prompts/px-social-signals.md` (Attempt 4 section)
- Full `social-signals-x.md` candidate pool

The agent should:
1. Verify each account handle exists (WebSearch for exact handle)
2. Remove duplicates (same person, different handles)
3. Remove inactive accounts (no posts about {COMPANY} in 6+ months)
4. Re-score all accounts with full context
5. Rank by relevance score descending
6. Cut to top 100
7. Write the 10 deep profiles (Top 10 section)
8. Fill in Signal Gaps and Monitoring Recommendations sections

Final SSCS evaluation:
```bash
python3 scripts/score_x_accounts.py "output/${DOMAIN}/social-signals-x.md"
```

### Completion Criteria

| Condition | Action |
|-----------|--------|
| SSCS ≥ 0.50 AND accounts ≥ 100 | Complete → `<promise>X_SIGNALS_COMPLETE</promise>` |
| SSCS < 0.50 after 4 attempts | Accept best version, note quality gap in PROGRESS.md |
| Fewer than 50 accounts found after 4 attempts | Company may have thin X presence — note as finding |

## Integration with Main Pipeline

### Option A: Pre-pipeline (recommended for first run)
```
Set target.env → Run PX → Run P1-P7 main pipeline
                    ↓
              P4 reads social-signals-x.md for targeted account searches
```

### Option B: Parallel with P2/P3/P5
```
P1 completes → Launch PX alongside P2, P3, P5
                    ↓
              P4 reads social-signals-x.md (if PX is done by then)
```

### Option C: Standalone monitoring
```
Run PX periodically (weekly/monthly) for ongoing social signal tracking
Compare current social-signals-x.md to previous version → detect drift
```

## PROGRESS.md Updates

After each attempt:
```markdown
## PX Social Signals
- Attempt 1 (SEED): SSCS = 0.25, accounts = 18
- Attempt 2 (EXPAND): SSCS = 0.38, accounts = 67
- Attempt 3 (DEEPEN): SSCS = 0.45, accounts = 112
- Attempt 4 (VALIDATE): SSCS = 0.55, accounts = 100 ✓
```

## Sub-Agent Dispatch Template

```
Task tool parameters:
  subagent_type: "general-purpose"
  description: "Dossier PX Social Signals Attempt {N}"
  prompt: |
    You are executing Attempt {N} of X Social Signal Discovery.

    Target domain: {DOMAIN}
    Company name: {COMPANY_NAME}
    Key people: {CEO}, {CTO}, {FOUNDERS}
    Competitors: {COMPETITORS}

    {PX_PROMPT_CONTENT_FOR_THIS_ATTEMPT}

    Current account pool (if attempt > 1):
    {CURRENT_SOCIAL_SIGNALS_X_MD}

    Category gaps to fill (if attempt 3+):
    {SSCS_GAPS}

    Write output to: output/{DOMAIN}/social-signals-x.md

    IMPORTANT: Include the handle, name, category, relevance score,
    follower count, and signal summary for EVERY account in the
    ranked table. WebFetch may be unavailable — use WebSearch as fallback.
```

## Important Notes
- X/Twitter data is gathered via WebSearch — no API access required
- Account handles must be verified via search, not guessed
- Former employees are the highest-value category — invest extra search effort
- Distinguish personal opinions from company-sanctioned messaging
- Note accounts that may be bots or astroturf (check for patterns)
- This phase produces a WATCHLIST, not a sentiment analysis — Phase 4 does the analysis
