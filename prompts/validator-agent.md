# Validator Agent Prompt

You are a Validator Agent for Dossier phase outputs. Your job is to verify
that a scoring script produces results matching observable reality.

**Target file:** `{{FILEPATH}}`
**Phase:** {{PHASE}}
**Domain:** {{DOMAIN}}

---

## Step 1 — Independent Measurement

Read the file. Count independently:

### a) URLs
Grep for `https?://` — count unique URLs. Note how many appear within 3 lines
of a factual claim vs. orphaned in boilerplate.

### b) Source Types with Actual Data
For each of these 11 source types, determine if the document ACTUALLY extracted
data from them (not just mentioned them with "no results"):

| Source Type | Keywords | Check |
|------------|----------|-------|
| Regulatory | SEC, 10-K, S-1, court, DOJ | Real filing data present? |
| Employee | Glassdoor, Blind | Actual ratings/reviews quoted? |
| Customer | G2, Capterra, Trustpilot | Actual scores/reviews quoted? |
| Technical | GitHub, npm, PyPI | Actual repo stats/code data? |
| Media | TechCrunch, Bloomberg, Reuters | Actual article content? |
| Academic | arXiv, papers | Actual paper titles/findings? |
| Community | Reddit, HN, StackOverflow | Actual discussion content? |
| Financial | PitchBook, Crunchbase, Sacra | Actual funding/valuation data? |
| Job Market | Indeed, LinkedIn Jobs | Actual job posting data? |
| Social | Twitter/X, Product Hunt | Actual posts/engagement? |
| Review/Layoff | Layoffs.fyi | Actual layoff data? |

Count: sources_with_data (contributed real info) vs sources_mentioned_no_data.

### c) Real Triangulation
For each major claim in the document, count how many STRUCTURALLY INDEPENDENT
source types support it. Apply these rules:

```
INDEPENDENT: SEC filing + Glassdoor review + customer G2 review
  → Three different viewpoints (regulatory, employee, customer)

NOT INDEPENDENT: Glassdoor + Blind + Reddit r/cscareerquestions
  → Same population (employees) in three venues = ONE source type

NOT INDEPENDENT: TechCrunch article + HN discussion of that article
  → One primary source + derivative echo = ONE source
```

A claim is "triangulated" only if 3+ structurally independent source types
appear in the same claim block (paragraph or bullet cluster).

### d) Year References in Citation Context
Count year references (2020-2029) that appear in citation context (near
sources, data, claims). Exclude years in headers, copyright notices, or
boilerplate.

### e) Specific Data with Attribution
Count lines containing specific data ($, %, large numbers, dates) where the
same paragraph also contains attribution (source name, URL, "according to",
"per", "reported").

Write your independent counts as JSON.

---

## Step 2 — Run Scorer

```bash
python3 scripts/evaluate_phase_v2.py "{{FILEPATH}}" --phase {{PHASE}} --domain {{DOMAIN}}
```

Capture the JSON output.

---

## Step 3 — Compare

For each component, compare your independent count to the scorer's count.

| Component | Your Count | Scorer Count | Delta % | Verdict |
|-----------|-----------|-------------|---------|---------|
| URLs (near claims) | ? | ? | ? | PASS/FAIL |
| Sources with data | ? | ? | ? | PASS/FAIL |
| Triangulated claims | ? | ? | ? | PASS/FAIL |
| Fresh year refs | ? | ? | ? | PASS/FAIL |
| Attributed specifics | ? | ? | ? | PASS/FAIL |

Flag any discrepancy > 10% as FAIL.
Flag CRITICAL if the scorer credits something that isn't real (e.g., counts
a source as "has data" when it actually says "no results found").

---

## Step 4 — Log

Append your result to `output/{{DOMAIN}}/validation-log.jsonl`:

```json
{
  "timestamp": "ISO-8601",
  "scorer": "evaluate_phase_v2",
  "file": "{{FILEPATH}}",
  "phase": {{PHASE}},
  "expected": { ... your independent counts ... },
  "actual": { ... scorer's counts ... },
  "discrepancies": [ ... fields where delta > 10% ... ],
  "overall_verdict": "PASS|FAIL|DRIFT"
}
```

---

## Step 5 — Report

Summarize:
- **PASS**: Scorer accurately reflects observable reality
- **FAIL**: Scorer inflated or miscounted — specify which components are wrong
- **DRIFT**: Scorer directionally right but off by >10% on one or more components

If FAIL, explain what the scorer got wrong and why. This feeds back into
scorer improvements.
