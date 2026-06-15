# Plan: Replace Scoring Theater with Validated Computation

## Problem Statement

Every scoring system in this repo (EDS, SSCS, drift thresholds, sentiment labels)
uses hardcoded weights, arbitrary thresholds, and regex pattern matching that
measures text surface properties rather than actual quality. The scores look
objective but are decoupled from reality.

**Specific failures:**
1. EDS rewards mentioning source names, not actually using those sources
2. EDS counts the word "triangulate" as triangulation evidence
3. SSCS assumes 100 accounts, 25% insiders, 15% high-signal — all arbitrary
4. Drift thresholds (0.15, 0.3, 0.5) have no empirical basis
5. Sentiment labels use hardcoded ranges (±0.1, ±0.3) never validated
6. Quality gates measure "does text exist with right properties" not "are claims true"

## Design Principles

1. **Every metric must define its expected result BEFORE measuring** — the Validator
   Agent states what "correct" looks like, then checks
2. **No hardcoded weights without justification** — weights either come from
   calibration data or are explicitly marked UNCALIBRATED
3. **Log everything** — every score computation writes to `validation-log.jsonl`
   with inputs, expected, actual, pass/fail, and reasoning
4. **Separate measurement from interpretation** — compute raw metrics (real),
   then interpret them (explicit assumptions documented)

---

## Architecture: The Validator Agent Pattern

### How It Works

Every scoring step runs as a two-phase process:

```
┌─────────────────────────────────────────────────────────┐
│                   VALIDATOR AGENT                        │
│                                                         │
│  1. EXPECT: Before running the scorer, the validator    │
│     states expected behavior:                           │
│     - "This file has 12 URLs. url_citation_rate should  │
│       reflect 12 unique URLs, not more."                │
│     - "Source X is mentioned but says 'no results' —    │
│       it should NOT count as found."                    │
│                                                         │
│  2. MEASURE: Run the actual scorer                      │
│                                                         │
│  3. CHECK: Compare expected vs actual                   │
│     - Do the raw counts match observable reality?       │
│     - Did the scorer correctly handle edge cases?       │
│     - Is the interpretation justified by the data?      │
│                                                         │
│  4. LOG: Write result to validation-log.jsonl           │
│     - timestamp, file, scorer, expected, actual,        │
│       verdict (PASS/FAIL/DRIFT), reasoning              │
└─────────────────────────────────────────────────────────┘
```

### Validator Agent Prompt Template

The orchestrator spawns validator agents with this structure:

```
You are a Validator Agent. Your job is to verify that a scoring script
produces results that match observable reality.

PHASE 1 — SET EXPECTATIONS:
Read the input file: {filepath}
Before running the scorer, independently determine:
- Count the actual URLs in the document (grep for https?://)
- Count actual source types that returned real data (not "no results")
- Count actual triangulation instances (where 3+ genuinely independent
  sources support the same claim — not just the word "triangulate")
- Check date references against today's date
- Count lines with genuine specific data vs. vague assertions

Write your expectations as JSON to stdout.

PHASE 2 — RUN SCORER:
Run: python3 scripts/evaluate_phase.py {filepath} --phase {N}
Capture the JSON output.

PHASE 3 — COMPARE:
For each component, compare your independent count to the scorer's count.
Flag any discrepancy > 10% as a FAIL.
Flag any case where the scorer credits something that isn't real as CRITICAL.

PHASE 4 — LOG:
Append a JSONL entry to output/{domain}/validation-log.jsonl
```

---

## Component Redesigns

### 1. evaluate_phase.py → evaluate_phase_v2.py

**What changes:**

| Component | Current (Theater) | New (Validated) |
|-----------|-------------------|-----------------|
| url_citation_rate | Counts URLs in text | Counts URLs AND checks if they appear near claims (within 3 lines) |
| source_coverage | Regex for source name anywhere in text | Requires source name + actual data extracted (not "no results", "not found", "unavailable") |
| triangulation_rate | Regex for word "triangulat" | Requires 3+ genuinely independent source types per claim (using source independence rules from research-program.md) |
| temporal_freshness | Counts year numbers | Counts year numbers that appear in citation context (not in boilerplate/headers) |
| specificity_score | Lines containing $, %, numbers | Lines containing specific data WITH attribution (number + source in same paragraph) |
| weights | 3 hardcoded weight sets | Single weight set, marked UNCALIBRATED, logged with every run, adjustable via research-program.md |

**New component added:**

- `negative_evidence_rate`: Fraction of claims where disconfirming evidence was searched for. Rewards adversarial checking, not just confirmation.

**Key code change — source_coverage:**

```python
# CURRENT (theater): Just checks if "glassdoor" appears in text
if re.search(r'glassdoor', text_lower):
    found += 1

# NEW (validated): Checks if glassdoor appears AND has actual data
def source_has_data(text: str, source_pattern: str, source_name: str) -> dict:
    """Check if a source is mentioned AND contributed real data."""
    matches = list(re.finditer(source_pattern, text, re.IGNORECASE))
    if not matches:
        return {"found": False, "has_data": False, "evidence": "not mentioned"}

    for match in matches:
        # Get surrounding paragraph (500 chars each direction)
        start = max(0, match.start() - 500)
        end = min(len(text), match.end() + 500)
        context = text[start:end]

        # Check for negative indicators
        negatives = r'no\s+(results?|data|reviews?|information|listings?|posts?)'
        if re.search(negatives, context, re.IGNORECASE):
            continue

        # Check for positive indicators: actual data follows
        positives = [
            r'\d',           # numbers (ratings, counts, dates)
            r'https?://',    # URLs near the source
            r'[""].*[""]',   # quoted text
            r'\|.*\|',       # table row
        ]
        if any(re.search(p, context[match.end()-start:]) for p in positives):
            return {
                "found": True,
                "has_data": True,
                "evidence": context[match.start()-start:match.end()-start+100].strip()
            }

    return {"found": True, "has_data": False, "evidence": "mentioned but no data extracted"}
```

**Key code change — triangulation_rate:**

```python
# CURRENT (theater): Counts the word "triangulate"
count += len(re.findall(r'triangulat', text, re.IGNORECASE))

# NEW (validated): Parse claim blocks, count distinct source TYPES per claim
def count_real_triangulations(text: str) -> dict:
    """Count claims with 3+ structurally independent source types."""
    SOURCE_TYPES = {
        'regulatory': r'SEC|10-K|10-Q|S-1|court|lawsuit|CFPB|DOJ|FTC',
        'employee': r'glassdoor|blind|employee.review|former.employee',
        'customer': r'G2|capterra|trustpilot|customer.review',
        'technical': r'github|npm|pypi|docker|commit|repository',
        'media': r'techcrunch|bloomberg|reuters|wsj|nyt',
        'academic': r'arxiv|paper|publication|peer.review',
        'community': r'reddit|hacker.news|HN|stack.overflow',
        'financial': r'pitchbook|crunchbase|sacra|funding',
        'job_market': r'indeed|linkedin.jobs?|job.posting|hiring',
    }

    # Split into claim-sized blocks (paragraphs or bullet clusters)
    blocks = re.split(r'\n\n+', text)
    triangulated = 0
    total_claims = 0

    for block in blocks:
        if not block.strip() or len(block) < 50:
            continue
        # Only count blocks that make factual assertions
        if not re.search(r'\d|claim|verify|confirm|evidence', block, re.I):
            continue
        total_claims += 1

        types_found = set()
        for stype, pattern in SOURCE_TYPES.items():
            if re.search(pattern, block, re.IGNORECASE):
                types_found.add(stype)

        if len(types_found) >= 3:
            triangulated += 1

    return {
        "triangulated_claims": triangulated,
        "total_claims": total_claims,
        "rate": triangulated / max(total_claims, 1),
        "source_types_used": list(set().union(
            *[find_types(b) for b in blocks]
        )) if blocks else [],
    }
```

**Weight handling:**

```python
# NEW: Weights are loaded from research-program.md, not hardcoded
# If research-program.md doesn't specify, use defaults BUT log a warning
DEFAULT_WEIGHTS = {
    'url_citation_rate': 0.20,
    'source_coverage': 0.20,
    'triangulation_rate': 0.20,
    'temporal_freshness': 0.15,
    'specificity_score': 0.15,
    'negative_evidence_rate': 0.10,
}
# Every run logs: {"weights_source": "default_uncalibrated", "weights": {...}}
```

---

### 2. score_x_accounts.py → score_x_accounts_v2.py

**What changes:**

| Parameter | Current (Hardcoded) | New (Configurable + Logged) |
|-----------|--------------------|-----------------------------|
| Target account count | 100 (hardcoded) | Read from research-program.md, default 100, logged as UNCALIBRATED |
| Category min count | 3 (hardcoded) | Configurable, default 3 |
| "Perfect" avg relevance | 70 (hardcoded) | Removed — report raw average, let humans interpret |
| Insider target | 25% (hardcoded) | Configurable, default 25%, logged |
| High-signal threshold | 70/100, 15% (hardcoded) | Configurable, logged |
| Weights | {0.15,0.30,0.20,0.20,0.15} | Loaded from config, logged with every run |

**Structural change:** The SSCS score remains as a convenience metric, but the
output now prominently includes the RAW DATA that the score is computed from,
so consumers can judge for themselves:

```json
{
  "raw_metrics": {
    "total_accounts": 87,
    "categories_with_3plus": 6,
    "categories_with_any": 8,
    "avg_relevance": 62.3,
    "insider_pct": 18.4,
    "high_signal_pct": 12.1
  },
  "sscs": 0.67,
  "sscs_calibration": "UNCALIBRATED — weights from research-program.md defaults",
  "validator_notes": [
    "insider_pct 18.4% is below 25% target — 3 categories have <3 accounts",
    "avg_relevance pulled down by 12 accounts scoring <30 — consider filtering"
  ]
}
```

---

### 3. drift_check.py → drift_check_v2.py

**What changes:**

The `SequenceMatcher` similarity is real computation — keep it. The staleness
scoring and drift thresholds are arbitrary — replace.

| Component | Current | New |
|-----------|---------|-----|
| Staleness formula | `0.5 + (year_delta * 0.2)` | Report raw data: newest_year, oldest_year, years_since_newest. NO score. Let consumer decide. |
| Staleness verdicts | FRESH/RECENT/AGING/STALE at hardcoded ranges | Remove verdict labels. Return raw staleness_years and let ralph-prompt.md define policy. |
| Drift thresholds | 0.15/0.3/0.5 hardcoded | Report raw drift (0.0-1.0). Thresholds move to research-program.md as configurable policy. |
| Section comparison | Real (SequenceMatcher) ✓ | Keep as-is |
| Number extraction | Real (regex) ✓ | Keep as-is, add: flag numbers that changed by >20% between versions |

**New output shape:**

```json
{
  "overall_similarity": 0.847,
  "overall_drift": 0.153,
  "newest_reference_year": 2025,
  "years_since_newest": 1,
  "sections": [...],
  "numerical_changes": [
    {
      "context": "ARR estimate",
      "old_value": "$200M",
      "new_value": "$280M",
      "change_pct": 40.0,
      "flag": "MATERIAL_CHANGE"
    }
  ],
  "interpretation_policy": "Thresholds from research-program.md: STABLE < 0.15, CHANGED < 0.50"
}
```

---

### 4. signal_db.py → signal_db_v2.py

**What changes:**

The database schema, import, and aggregation are real — keep them. The sentiment
classification thresholds are arbitrary — separate them.

| Component | Current | New |
|-----------|---------|-----|
| Sentiment labels | Hardcoded ±0.1, ±0.3 | Move thresholds to a `pulse_config` table in SQLite. Log when defaults are used. |
| Bullish/bearish % | Hardcoded ±0.2 | Same — configurable, logged |
| Weighted sentiment | Real (SUM(s*r)/SUM(r)) ✓ | Keep. This is legitimate computation. |
| Momentum | Real (24h delta) ✓ | Keep. |
| Account coverage | Real (active/total) ✓ | Keep. |

**New: sentiment thresholds become configurable:**

```sql
CREATE TABLE IF NOT EXISTS pulse_config (
    key TEXT PRIMARY KEY,
    value REAL,
    source TEXT,  -- 'default_uncalibrated' or 'user_configured'
    updated_at TEXT
);

-- Defaults inserted on init:
INSERT OR IGNORE INTO pulse_config VALUES
    ('bullish_threshold', 0.3, 'default_uncalibrated', datetime('now')),
    ('slight_bullish_threshold', 0.1, 'default_uncalibrated', datetime('now')),
    ('slight_bearish_threshold', -0.1, 'default_uncalibrated', datetime('now')),
    ('bearish_threshold', -0.3, 'default_uncalibrated', datetime('now')),
    ('bullish_pct_threshold', 0.2, 'default_uncalibrated', datetime('now')),
    ('bearish_pct_threshold', -0.2, 'default_uncalibrated', datetime('now'));
```

---

## The Validation Log

### Format: `output/{domain}/validation-log.jsonl`

One JSON object per line, appended after every scoring run:

```json
{
  "timestamp": "2026-06-15T14:32:00Z",
  "scorer": "evaluate_phase_v2",
  "file": "output/vercel.com/04-claims.md",
  "phase": 4,
  "expected": {
    "url_count": 45,
    "sources_with_data": 8,
    "sources_mentioned_no_data": 2,
    "triangulated_claims": 5,
    "total_claims_estimated": 32
  },
  "actual": {
    "url_count": 45,
    "sources_with_data": 8,
    "sources_mentioned_no_data": 2,
    "triangulated_claims": 5,
    "total_claims_estimated": 30
  },
  "discrepancies": [
    {
      "field": "total_claims_estimated",
      "expected": 32,
      "actual": 30,
      "delta_pct": 6.25,
      "verdict": "PASS",
      "reason": "Within 10% tolerance — claim counting heuristic variance"
    }
  ],
  "overall_verdict": "PASS",
  "eds_score": 0.52,
  "weights_used": {"source": "research-program.md", "values": {"...": "..."}},
  "uncalibrated_flags": ["weights are default — no empirical calibration"]
}
```

### Aggregate Validation Report

A new script `scripts/validation_report.py` reads the JSONL log and produces:

```
Validation Summary for vercel.com
==================================
Total scorer runs:     14
PASS:                  11 (78.6%)
FAIL:                   2 (14.3%)
DRIFT:                  1 (7.1%)

Failure Details:
  - 04-claims.md run 2: source_coverage counted "layoffs" keyword as source
    even though context was "no layoffs reported" (FIXED in v2)
  - 06-valuation.md run 1: specificity_score credited numbers in headers
    as specific data (KNOWN LIMITATION)

Uncalibrated Components:
  - All EDS weights (since: 2026-06-15)
  - All SSCS thresholds (since: 2026-06-15)
  - Sentiment classification ranges (since: 2026-06-15)

Recommendation:
  Run backtests against calibration companies to derive empirical weights.
```

---

## Integration with Ralph Loop

### Changes to ralph-prompt.md

Replace the current EDS evaluation block (lines 87-98) with:

```markdown
5. **Evaluate with Validator Agent**:
   For each new phase output, spawn a validator agent:

   Agent:
     description: "Validate P{N} scoring"
     prompt: |
       You are a Validator Agent for Dossier phase {N} output.

       INPUT FILE: output/{DOMAIN}/0{N}-{phase}.md

       STEP 1 — INDEPENDENT MEASUREMENT:
       Read the file. Count independently:
       a) Unique URLs (grep for https?://)
       b) Source types with actual extracted data (not "no results")
       c) Claims with 3+ structurally independent source types
          (use source independence rules: employee sources count as ONE
           type regardless of venue; derivative articles count as ONE)
       d) Year references in citation context (not headers/boilerplate)
       e) Lines with specific data + attribution in same paragraph

       Write your counts as JSON.

       STEP 2 — RUN SCORER:
       python3 scripts/evaluate_phase_v2.py "output/{DOMAIN}/0{N}-{phase}.md" --phase {N}

       STEP 3 — COMPARE:
       Compare your counts to the scorer's counts.
       For each component with >10% discrepancy, explain why.
       Flag CRITICAL if scorer credits something that isn't real.

       STEP 4 — LOG:
       Append result to output/{DOMAIN}/validation-log.jsonl

       STEP 5 — VERDICT:
       Report: PASS (scorer accurate), FAIL (scorer inflated/wrong),
       or DRIFT (scorer directionally right but off by >10%)

6. **Keep or discard** (same as before, but now using validated EDS)
```

### Changes to research-program.md

Add a new section:

```markdown
## Scoring Configuration

All weights and thresholds below are UNCALIBRATED defaults.
To calibrate: run backtests against calibration/ companies, compare
predicted scores to known outcomes, adjust weights to minimize error.

### EDS Weights
| Component | Weight | Calibration Status |
|-----------|--------|-------------------|
| url_citation_rate | 0.20 | UNCALIBRATED |
| source_coverage | 0.20 | UNCALIBRATED |
| triangulation_rate | 0.20 | UNCALIBRATED |
| temporal_freshness | 0.15 | UNCALIBRATED |
| specificity_score | 0.15 | UNCALIBRATED |
| negative_evidence_rate | 0.10 | UNCALIBRATED |

### Drift Thresholds
| Threshold | Value | Calibration Status |
|-----------|-------|-------------------|
| stable_max_drift | 0.15 | UNCALIBRATED |
| changed_max_drift | 0.50 | UNCALIBRATED |
| material_number_change_pct | 20.0 | UNCALIBRATED |

### Sentiment Thresholds
| Label | Min Value | Calibration Status |
|-------|-----------|-------------------|
| BULLISH | > 0.3 | UNCALIBRATED |
| SLIGHTLY BULLISH | > 0.1 | UNCALIBRATED |
| NEUTRAL | > -0.1 | UNCALIBRATED |
| SLIGHTLY BEARISH | > -0.3 | UNCALIBRATED |
| BEARISH | ≤ -0.3 | UNCALIBRATED |
```

---

## Implementation Order

### Step 1: Validation Log Infrastructure
- Create `scripts/validation_log.py` — append/read JSONL log
- Create `scripts/validation_report.py` — summarize log entries
- **Files:** 2 new scripts (~100 LOC each)

### Step 2: evaluate_phase_v2.py
- Replace source_coverage with data-aware source detection
- Replace triangulation_rate with independence-aware counting
- Replace specificity_score with attribution-aware counting
- Add negative_evidence_rate
- Load weights from research-program.md (fall back to defaults)
- Log every run to validation-log.jsonl
- **Files:** 1 rewritten script (~300 LOC)
- **Backwards compatible:** Same CLI interface, same JSON output schema
  with additional fields

### Step 3: score_x_accounts_v2.py
- Make all thresholds configurable via research-program.md
- Add raw_metrics section to output
- Log every run to validation-log.jsonl
- Mark all thresholds as UNCALIBRATED in output
- **Files:** 1 rewritten script (~250 LOC)

### Step 4: drift_check_v2.py
- Remove staleness verdict labels (return raw years_since_newest)
- Move drift thresholds to research-program.md
- Add numerical change detection (flag >20% changes)
- Log to validation-log.jsonl
- **Files:** 1 rewritten script (~300 LOC)

### Step 5: signal_db_v2.py
- Add pulse_config table for sentiment thresholds
- Load thresholds from DB instead of hardcoding
- Log threshold source in pulse export
- **Files:** 1 rewritten script (~450 LOC)

### Step 6: Validator Agent Integration
- Update ralph-prompt.md with validator agent dispatch
- Update research-program.md with configurable weights/thresholds
- Add validator prompt template to prompts/
- **Files:** 3 modified files

### Step 7: Calibration Runner
- Create `scripts/calibrate.py` — runs all scorers against calibration/
  backtest files, compares to known outcomes, reports optimal weights
- This is how you eventually replace UNCALIBRATED with CALIBRATED
- **Files:** 1 new script (~200 LOC)

---

## What This Does NOT Change

1. **whois_lookup.py** — Real API wrapper, no changes needed
2. **arxiv_search.py** — Real API wrapper, no changes needed
3. **Phase prompts (P1-P7)** — Research instructions are legitimate, no changes
4. **viewer/pulse.html** — Display only, no computation to fix
5. **SequenceMatcher similarity** in drift_check — real computation, kept as-is

## What Success Looks Like

After implementation:

1. Every scoring run produces a validation log entry showing expected vs. actual
2. No score is produced without documenting its calibration status
3. A fabricated document full of source names and numbers scores LOW (not high)
   because source_coverage checks for actual data, not just name mentions
4. The word "triangulate" alone doesn't earn triangulation points — you need
   3+ structurally independent source types in the same claim block
5. `python3 scripts/validation_report.py output/vercel.com/` shows a clear
   audit trail of every scoring decision
6. All weights and thresholds are in research-program.md where the human can
   see and adjust them, not buried in Python code
