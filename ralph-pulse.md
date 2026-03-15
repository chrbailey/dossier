# Ralph Loop — Dossier Pulse (Continuous Social Signal Monitor)

## Goal

Continuously monitor the Top 100 X accounts for a target company. Detect
sentiment changes, validate account relevance, and publish updated results.
This is an always-running loop — like autoresearch, it never stops until
the human interrupts.

**Done when:** Human interrupts. This loop runs indefinitely.

## Core Principle

**The database IS the memory.** Every scan compares new findings against
what's already stored. The agent doesn't start fresh each iteration — it
reads the DB, knows what was said before, and detects CHANGES.

Pattern detection comes from delta analysis:
- Account was bullish 2 weeks ago → now bearish → FLAG
- Account posted 3x/week about {COMPANY} → went silent → FLAG
- 5 employee accounts shifted negative in same week → CLUSTER ALERT
- Top 10 account hasn't provided signal in 30 days → DEMOTE
- New voice appeared 3 times with high relevance → PROMOTE into Top 100

## Setup

```bash
DOSSIER_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$DOSSIER_ROOT"
source target.env

# Initialize DB if first run
python3 scripts/signal_db.py init "$DOMAIN"

# Import accounts if social-signals-x.md exists
if [ -f "output/${DOMAIN}/social-signals-x.md" ]; then
    python3 scripts/signal_db.py import-accounts "$DOMAIN" "output/${DOMAIN}/social-signals-x.md"
fi
```

## Iteration Logic (Infinite Loop)

Each iteration is a **scan cycle**. The agent runs one cycle, publishes
results, then immediately starts the next.

### Step 1: READ STATE (What do we already know?)

```bash
python3 scripts/signal_db.py summary "$DOMAIN"
```

Read the current pulse metrics. Note:
- Current sentiment (bullish/bearish/neutral)
- Which accounts were last active and when
- Any accounts flagged for demotion (no signal in 30+ days)
- Total signal count and recent trend

### Step 2: SCAN (What's new?)

For each of the Top 20 accounts (prioritized by relevance score):

```
WebSearch: from:@{HANDLE} {COMPANY_NAME} OR {PRODUCT_NAME}
WebSearch: "@{HANDLE}" {COMPANY_NAME} site:x.com
```

For the next 30 accounts (ranks 21-50):
```
WebSearch: "@{HANDLE}" {COMPANY_NAME}
```

For accounts 51-100, scan only every 3rd cycle.

**For each new post/signal found:**

1. **Is it relevant?** Does it mention or relate to {COMPANY}? (Claude analysis)
2. **What's the sentiment?** Score -1.0 (bearish) to +1.0 (bullish)
   - -1.0: "This product is terrible, we're migrating away"
   - -0.5: "Disappointed with recent changes"
   - 0.0: Neutral mention, factual statement
   - +0.5: "Impressed with new feature"
   - +1.0: "This is the best product in the category"
3. **How relevant is it?** Score 0.0 (noise) to 1.0 (critical signal)
   - 1.0: CEO announces pivot, layoffs, or acquisition
   - 0.7: Former employee criticizes core product
   - 0.4: Customer shares positive experience
   - 0.1: Tangential mention, retweet without commentary
4. **Compare to previous signals from this account:**
   - Was this account previously bullish/bearish? Has stance changed?
   - Is this account posting more or less frequently about {COMPANY}?
   - Flag any stance reversals as HIGH-PRIORITY signals

### Step 3: UPDATE DATABASE

For each new signal found:
```bash
python3 scripts/signal_db.py add-signal "$DOMAIN" '{
    "handle": "@handle",
    "content": "summary of the post",
    "source_url": "https://...",
    "sentiment": 0.7,
    "relevance": 0.6,
    "category": "employee",
    "signal_type": "post"
}'
```

### Step 4: ANALYZE PATTERNS (Database as Memory)

Read recent signals from the DB and detect patterns:

**Stance Changes (most valuable):**
```
Query: accounts whose average sentiment changed direction in the last 7 days
Signal: "Previously bullish insider turns bearish" = CRITICAL
```

**Cluster Events:**
```
Query: 3+ accounts in the same category posting negative signals in same 48h window
Signal: "Employee morale cluster event" = HIGH PRIORITY
```

**Silence Patterns:**
```
Query: Top 20 accounts with no new signals in 14+ days
Signal: Unusual silence may indicate NDA, departure, or strategic shift
```

**Volume Changes:**
```
Query: Signal volume this week vs rolling 4-week average
Signal: >50% increase = something is happening (launch? crisis? controversy?)
Signal: >50% decrease = news cycle moved on, may need fresh account discovery
```

### Step 5: VALIDATE TOP 100 (Account Pruning)

Every 5th cycle, evaluate the account list:

**Promote** (add to Top 100):
- New accounts discovered during scanning that posted 3+ relevant signals
- Accounts from P4 sources that aren't in the current list

**Demote** (remove from Top 100):
- Accounts with 0 signals in 30+ days AND relevance < 50
- Accounts whose posts are consistently irrelevant (relevance < 0.2)
- Accounts that went private or were suspended

**Re-score:**
- Adjust relevance scores based on actual signal value delivered
- An account scored 80 at discovery that consistently produces low-relevance posts → lower score
- An account scored 40 that produced a critical stance-change signal → raise score

Update the DB:
```bash
# Demote inactive account
python3 scripts/signal_db.py add-signal "$DOMAIN" '{
    "handle": "@handle",
    "content": "ACCOUNT_DEMOTED: no signals in 30+ days",
    "sentiment": 0.0,
    "relevance": 0.0,
    "signal_type": "system"
}'
```

### Step 6: COMPUTE PULSE (Aggregate Metrics)

```bash
python3 scripts/signal_db.py update-pulse "$DOMAIN"
```

This computes:
- Weighted sentiment (24h, 7d, 30d)
- Momentum (sentiment change vs previous period)
- Category breakdown (employees vs critics vs customers)
- Bullish/bearish/neutral percentages
- Account coverage (active accounts / total accounts)

### Step 7: PUBLISH (Git as Media)

```bash
# Export to JSON for dashboard
python3 scripts/signal_db.py export "$DOMAIN"

# Update the social-signals-x.md with any account changes
# (only if accounts were promoted/demoted this cycle)

# Commit and push
git add "output/${DOMAIN}/pulse.json" "output/${DOMAIN}/signals.db"
git commit -m "pulse: ${DOMAIN} — sentiment ${SENTIMENT_7D}, ${SIGNAL_COUNT} new signals"
git push origin HEAD
```

**Anyone pulling the repo gets the latest pulse data.** The git history
IS the timeline. `git log output/{DOMAIN}/pulse.json` shows every update.

### Step 8: REPEAT

Go back to Step 1. No pause needed — the next scan starts immediately.

If out of new signals to find, the agent should:
1. Try alternative search queries for accounts that haven't appeared recently
2. Search for new accounts not in the Top 100 (discovery expansion)
3. Run a full account validation pass
4. If truly nothing new: wait until next cycle interval

## Cycle Intervals

| Mode | Interval | Use Case |
|------|----------|----------|
| Crisis | Every 15 min | Active controversy, layoff, security breach |
| Active | Every 1 hour | Normal monitoring during business hours |
| Overnight | Every 4 hours | Low-activity periods |

The agent should detect which mode is appropriate:
- If last cycle found 10+ new signals → switch to Crisis mode
- If last 3 cycles found 0-2 signals → switch to Overnight mode
- Default: Active mode

## Signal Priority Matrix

| Signal Type | Priority | Action |
|---|---|---|
| CEO/founder stance change | CRITICAL | Immediate pulse update + flag |
| Employee cluster event (3+ negative in 48h) | CRITICAL | Cluster alert in pulse |
| Former employee goes public with criticism | HIGH | Deep analysis, cross-reference with P4 |
| Security researcher discloses vulnerability | HIGH | Flag + cross-reference with P3 |
| Major customer announces migration away | HIGH | Churn signal for P6 |
| Competitor CEO comments on target | MEDIUM | Competitive intelligence |
| Industry analyst publishes coverage | MEDIUM | Market positioning signal |
| Generic positive customer mention | LOW | Bulk sentiment update |

## Integration with Dossier Pipeline

The pulse data feeds back into the main pipeline:

```
Pulse DB → P4 Claims Validation (live sentiment data)
Pulse DB → P6 Valuation (morale trajectory, churn signals)
Pulse DB → P7 Report (current pulse as of report date)
```

When a full dossier re-run is triggered:
1. P4 reads pulse.json for current sentiment baseline
2. P4 compares marketing claims against live insider sentiment
3. P7 includes a "Current Pulse" section with the latest metrics

## Important Notes

- This loop runs INDEFINITELY until the human stops it
- Use the database as memory — never start from scratch
- Git is the publish mechanism — commit after every meaningful update
- The Top 100 is a LIVING LIST — promote and demote based on actual value
- Stance changes are the most valuable signal — a bullish insider turning bearish is worth more than 100 neutral mentions
- Never fabricate signals — if WebSearch returns nothing, record "no new signals" and move on
