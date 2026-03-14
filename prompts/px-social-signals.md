# Phase X: Social Signal Discovery (X/Twitter)

## Goal

Find and rank the **100 most relevant X (Twitter) accounts** for the target company.
This is not a one-shot search — it's an iterative discovery loop inspired by
Karpathy's autoresearch. Each iteration widens the net, scores accounts, and
narrows to the most signal-rich voices.

The output is a ranked watchlist: the 100 accounts most likely to produce
actionable intelligence about the company's real capabilities, team health,
product quality, and market position.

## Why This Matters

Phase 4 (Claims Validation) currently uses X as a single unstructured WebSearch.
This produces anecdotes, not systematic signal coverage. A company like Vercel has
thousands of X accounts posting about it — employees, former employees, customers,
critics, competitors, journalists, VCs, developers. The signal-to-noise ratio is
terrible unless you systematically discover and rank who matters.

## Inputs

- `output/{DOMAIN}/01-discovery.md` — company name, founders, key people, product
- `output/{DOMAIN}/03-technical.md` — GitHub contributors (many have X links in profiles)
- `target.env` — domain

## The Discovery Loop

### Overview

```
┌─────────────────────────────────────────────────────┐
│          X Account Discovery Loop                    │
│                                                      │
│  Attempt 1: SEED — find obvious accounts             │
│  Attempt 2: EXPAND — follow the graph outward        │
│  Attempt 3: DEEPEN — find hidden/niche voices        │
│  Attempt 4: VALIDATE — verify, de-duplicate, rank    │
│                                                      │
│  Each attempt:                                       │
│    Search → Score → Add to candidate pool             │
│    Keep running total of accounts found + scored      │
│    Stop when pool ≥ 200 OR 4 attempts complete       │
│    Final pass: rank and cut to top 100               │
└─────────────────────────────────────────────────────┘
```

### Attempt 1: SEED (Official + Obvious)

Search for the obvious accounts first. These are the baseline.

**Searches to run:**
```
WebSearch: "x.com" OR "twitter.com" "{COMPANY_NAME}" official account
WebSearch: site:x.com "{COMPANY_NAME}"
WebSearch: "{CEO_NAME}" twitter OR x.com
WebSearch: "{CTO_NAME}" twitter OR x.com
WebSearch: "{COMPANY_NAME}" developer advocate twitter
```

**Account categories to find:**
| Category | Examples | Why they matter |
|----------|----------|----------------|
| **Official company** | @vercel, @nextjs | Baseline messaging, announcement timing |
| **CEO/Founders** | @raaboraneda, @rauchg | Unfiltered leadership signals, controversy risk |
| **C-suite** | CTO, VP Eng, VP Product | Technical direction, hiring signals |
| **DevRel/Advocates** | @leeerob, @delabordejonathan | Community temperature, developer sentiment |
| **Official product accounts** | @v0, @turborepo | Product-specific engagement |

**Expected yield:** 10-25 accounts

### Attempt 2: EXPAND (Employee + Community Graph)

Now follow the social graph outward from seed accounts.

**Searches to run:**
```
WebSearch: "{COMPANY_NAME}" employee twitter bio
WebSearch: "{COMPANY_NAME}" engineer "x.com" OR "twitter.com"
WebSearch: site:x.com "{COMPANY_NAME}" "joined" OR "left" OR "ex-"
WebSearch: "{COMPANY_NAME}" "former employee" twitter
WebSearch: "{PRODUCT_NAME}" review OR complaint site:x.com
WebSearch: "{COMPANY_NAME}" investor OR VC twitter
```

**Account categories to find:**
| Category | Examples | Why they matter |
|----------|----------|----------------|
| **Current engineers** | Individual contributors with "{COMPANY}" in bio | Real-time morale, technical opinions |
| **Former employees** | "Ex-{COMPANY}" or "Previously @{COMPANY}" in bio | Exit signals, honest retrospectives |
| **Key customers** | Power users who tweet about the product | Product quality validation |
| **Vocal critics** | People who regularly critique the product | Unsolved pain points, competitor angles |
| **Investors/Board** | VCs who led rounds, board members | Governance signals, follow-on intent |

**Expected yield:** 30-60 additional accounts

### Attempt 3: DEEPEN (Hidden + Niche Voices)

Search for accounts that don't show up in obvious queries but carry high signal.

**Searches to run:**
```
WebSearch: "{COMPANY_NAME}" layoffs OR "let go" site:x.com
WebSearch: "{COMPANY_NAME}" vs "{COMPETITOR_1}" twitter
WebSearch: "{COMPANY_NAME}" pricing OR billing complaint site:x.com
WebSearch: "{COMPANY_NAME}" security OR breach OR vulnerability twitter
WebSearch: "{PRODUCT_NAME}" migration OR "switched from" OR "switched to" twitter
WebSearch: "{COMPANY_NAME}" enterprise OR SOC2 OR compliance twitter
WebSearch: "{FOUNDER_NAME}" controversy OR backlash twitter
WebSearch: "{COMPANY_NAME}" hiring OR "we're hiring" twitter (recent)
WebSearch: "{COMPANY_NAME}" acquisition OR "acquired by" OR "acquiring" twitter
```

**Account categories to find:**
| Category | Examples | Why they matter |
|----------|----------|----------------|
| **Industry analysts** | SaaS analysts, cloud analysts | Independent assessment |
| **Tech journalists** | Reporters covering the space | Upcoming coverage, leak signals |
| **Competitor employees** | Engineers at competing companies | Competitive intelligence, feature comparison |
| **Migration voices** | "Switched from X to Y" posters | Churn/growth signals |
| **Security researchers** | People who've audited/tested the product | Vulnerability signals |
| **Recruiter accounts** | Recruiters posting {COMPANY} roles | Hiring velocity signals |

**Expected yield:** 30-50 additional accounts

### Attempt 4: VALIDATE (Score + Rank + Cut)

No new discovery. This pass validates and ranks the full candidate pool.

**For each candidate account:**

1. **Verify the account exists** — WebSearch for the exact handle
2. **Check activity** — is the account active (posted in last 90 days)?
3. **Score relevance** (see scoring rubric below)
4. **De-duplicate** — remove accounts that are clearly the same person across handles
5. **Rank** — sort by relevance score descending
6. **Cut** — keep top 100

---

## Relevance Scoring Rubric

Each account gets a relevance score (0-100) based on these factors:

### Signal Value (0-40 points)

| Factor | Points | Criteria |
|--------|--------|----------|
| **Insider access** | 0-15 | Current employee (15), former employee (12), customer (8), observer (3) |
| **Specificity** | 0-10 | Posts specific technical/product details (10) vs generic mentions (2) |
| **Frequency** | 0-10 | Posts about {COMPANY} weekly (10), monthly (6), rarely (2) |
| **Candor** | 0-5 | Shares critical/honest views (5) vs only positive/marketing (1) |

### Reach (0-25 points)

| Factor | Points | Criteria |
|--------|--------|----------|
| **Follower count** | 0-10 | 100K+ (10), 10K-100K (7), 1K-10K (4), <1K (1) |
| **Engagement rate** | 0-10 | High reply/RT ratio (10), moderate (5), low (2) |
| **Network position** | 0-5 | Connected to other high-relevance accounts (5), isolated (1) |

### Timeliness (0-20 points)

| Factor | Points | Criteria |
|--------|--------|----------|
| **Recency** | 0-10 | Active this month (10), this quarter (6), this year (3), older (1) |
| **Trend relevance** | 0-10 | Posts during key events (launches, crises, earnings) (10), random timing (3) |

### Uniqueness (0-15 points)

| Factor | Points | Criteria |
|--------|--------|----------|
| **Perspective gap** | 0-10 | Provides viewpoint no other account covers (10), duplicates existing coverage (2) |
| **Category coverage** | 0-5 | Fills an underrepresented category (5), redundant category (1) |

---

## Output

Write `output/{DOMAIN}/social-signals-x.md`:

```markdown
# X Signal Map: {COMPANY_NAME}

## Discovery Summary
- Accounts discovered: {TOTAL_CANDIDATES}
- Accounts in final Top 100: 100
- Discovery iterations: {N}
- Date: {ISO_TIMESTAMP}

## Category Distribution
| Category | Count | Top Account |
|----------|-------|-------------|
| Official / Company | | |
| Leadership (CEO, CTO, founders) | | |
| Current employees | | |
| Former employees | | |
| Customers / Power users | | |
| Critics | | |
| Investors / Board | | |
| Industry analysts / Journalists | | |
| Competitors | | |
| Other | | |

## Top 100 Accounts (Ranked by Relevance)

| Rank | Handle | Name | Category | Relevance | Followers | Signal Summary |
|------|--------|------|----------|-----------|-----------|----------------|
| 1 | @handle | Name | Category | 85/100 | 150K | Key signals this account provides |
| 2 | ... | | | | | |

## High-Signal Accounts (Top 10 Deep Profiles)

### 1. @handle — Name (Category)
- **Why they matter:** [1-2 sentences]
- **Key posts:** [Notable tweets about {COMPANY}]
- **Signal type:** [What intelligence they provide]
- **Watch for:** [What future posts from them would signal]

### 2. @handle — Name (Category)
...

## Signal Gaps
- Categories with <5 accounts (underrepresented viewpoints)
- Missing perspectives (e.g., no security researchers found)
- Accounts that likely exist but couldn't be discovered via WebSearch

## Monitoring Recommendations
- **Daily watch:** [Top 5 accounts to check daily for breaking signals]
- **Weekly scan:** [Top 20 accounts for weekly sentiment tracking]
- **Event triggers:** [Accounts to check during specific events: launches, earnings, crises]

## Search Queries Used
[Log every WebSearch query and how many accounts it yielded]
```

## Quality Criteria

- Every account must have a verified handle (not guessed)
- Every relevance score must show its component breakdown
- Category distribution should cover all 9 categories — if a category has 0 accounts, note it as a gap
- Former employees are especially valuable — invest extra search effort here
- De-duplicate carefully: same person may have personal + professional accounts
- Distinguish active accounts (posted in 90 days) from dormant ones
- If WebSearch returns no results for a query, note it and try alternative phrasing
- Prefer accounts that post ABOUT the company, not accounts that merely follow it

## Integration with Phase 4

After this phase produces the Top 100 list, Phase 4 (Claims Validation) can use it to:
1. Search for specific accounts' posts about claimed features
2. Track sentiment trajectory across the most relevant voices
3. Identify convergence/divergence between insider accounts and marketing
4. Detect coordinated messaging (multiple accounts posting similar content simultaneously)

The Top 100 list transforms Phase 4 from "search and hope" to "monitor known high-signal sources."

## How to Run This Phase

This phase can run:
- **Standalone:** Before or after the main pipeline, as a research sprint
- **As P4 pre-work:** Run before Phase 4 to seed the claims validation with known accounts
- **As a Ralph Loop sub-phase:** Integrated into the main pipeline between P1 and P4

### Standalone execution:
```
Task tool parameters:
  subagent_type: "general-purpose"
  description: "Dossier PX Social Signal Discovery"
  prompt: |
    You are executing the Social Signal Discovery phase.
    Target domain: {DOMAIN}
    Output directory: output/{DOMAIN}/

    {THIS_PROMPT_CONTENT}

    Prior discovery data: {P1_DISCOVERY_OUTPUT}

    Write output to: output/{DOMAIN}/social-signals-x.md
```
