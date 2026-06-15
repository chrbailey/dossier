# Dossier Pipeline — Ralph Loop Orchestration

## Goal
Execute a full SaaS due diligence analysis on the target domain. Run all 7 phases to completion with quality gates, producing a unified report with executive summary.

**Done when:** All 7 phases are marked complete in PROGRESS.md → output `<promise>DOSSIER_COMPLETE</promise>`

## Setup

First, read the target and initialize:
```bash
# Use the project root (wherever this repo is cloned)
DOSSIER_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$DOSSIER_ROOT"
source target.env
echo "Target: $DOMAIN"
```

If `output/${DOMAIN}/PROGRESS.md` does not exist, create it from `templates/progress-template.md` (replace `{{DOMAIN}}` with actual domain, `{{TIMESTAMP}}` with current ISO timestamp).

If it already exists, read it to determine current state.

## Phase Execution Rules

### Phase Dependencies (DAG)
```
P1 → unlocks P2, P3, P5
P1 + P3 → unlocks P4
P1 + P2 + P3 + P4 + P5 → unlocks P6
P6 → unlocks P7
```

### Parallel Execution
When multiple phases are unblocked, dispatch them as parallel sub-agents using the Task tool:
- **After P1 completes:** Launch P2, P3, P5 in parallel (3 agents)
- **After P3 completes:** Launch P4 (if P1 also done)
- **After P4 + P5 complete:** Launch P6
- **After P6 completes:** Launch P7

### Per-Phase Execution
For each phase:
1. Read the phase prompt from `prompts/p{N}-{phase}.md`
2. Read any required input files (prior phase outputs)
3. Launch a general-purpose sub-agent with the Task tool:
   - Include the phase prompt content
   - Include the domain name and output directory
   - Include relevant prior phase outputs as context
4. After the agent completes, verify the output file exists
5. Update PROGRESS.md: mark phase complete with timestamp

### Sub-Agent Dispatch Template
```
Task tool parameters:
  subagent_type: "general-purpose"
  description: "Dossier P{N} {phase_name}"
  prompt: |
    You are executing Phase {N} of a SaaS due diligence analysis.

    Target domain: {DOMAIN}
    Output directory: output/{DOMAIN}/

    {PHASE_PROMPT_CONTENT}

    {PRIOR_PHASE_OUTPUTS_IF_NEEDED}

    Write your output to: output/{DOMAIN}/0{N}-{phase}.md
    Write any raw data to: output/{DOMAIN}/raw/

    IMPORTANT: Include direct URLs for every factual claim where possible.
    WebFetch may be unavailable — use WebSearch as fallback.
```

## Iteration Logic (Autoresearch-Enhanced)

Read `research-program.md` before starting. It defines quality thresholds,
strategy variants, and source weighting rules.

Each Ralph Loop iteration:

1. **Read state**: `cat output/{DOMAIN}/PROGRESS.md`
2. **Find next work**: Identify phases that are:
   - Not yet complete (or below EDS threshold and under max_attempts)
   - Not blocked (all dependencies met)
   - Not currently in progress
3. **Dispatch**: Launch sub-agents for all unblocked phases
4. **Wait**: Sub-agents complete their work
5. **Evaluate with Validator Agent**: For each new phase output, spawn a
   validator agent (see `prompts/validator-agent.md` for the full template):
   
   The validator agent:
   a) Independently reads the file and counts URLs, source types with actual
      data, real triangulations (3+ structurally independent source types),
      year references in citation context, and attributed specifics
   b) Runs the v2 scorer:
      ```bash
      python3 scripts/evaluate_phase_v2.py "output/${DOMAIN}/0N-phase.md" --phase N --domain ${DOMAIN}
      ```
   c) Compares its independent counts to the scorer's counts
   d) Logs the result (expected vs actual) to `output/${DOMAIN}/validation-log.jsonl`
   e) Reports PASS (scorer accurate), FAIL (scorer inflated), or DRIFT (off >10%)
   
   If the validator reports FAIL, investigate the discrepancy before using the score.
   
6. **Keep or discard**:
   - If validated EDS improved over previous best → keep new output, log in PROGRESS.md
   - If EDS regressed → revert to previous best output
   - If first attempt → keep regardless (establishes baseline)
7. **Check quality gate**:
   - If EDS ≥ threshold (see research-program.md) → mark phase complete
   - If EDS < threshold AND attempts < max_attempts → re-run with next strategy variant
   - If EDS < threshold AND attempts = max_attempts → accept best output, mark complete
8. **Update**: Mark completed phases in PROGRESS.md, increment iteration count
9. **Check completion**: If all 7 phases complete → `<promise>DOSSIER_COMPLETE</promise>`
10. **Continue**: If work remains, the loop continues to next iteration

### Expected Iteration Pattern (with quality gates)
```
Iteration 1: Execute P1 Discovery → EDS 0.35
Iteration 2: Execute P2 + P3 + P5 (parallel) → EDS varies
Iteration 3: Execute P4 attempt 1 → EDS 0.42 (below 0.55 threshold)
Iteration 4: Execute P4 attempt 2 (deeper sources) → EDS 0.51
Iteration 5: Execute P4 attempt 3 (triangulation focus) → EDS 0.58 ✓ threshold met
Iteration 6: Execute P6 (needs all prior)
Iteration 7: Execute P7 → COMPLETE
```

## Error Handling

If a phase fails:
1. Log the error in PROGRESS.md under `## Blockers`
2. Mark the phase as `FAILED` (not complete)
3. Continue with other unblocked phases
4. On next iteration, retry the failed phase
5. If a phase fails 3 times, mark as `SKIPPED` and note in Blockers
6. P7 (Report) should still run even if some phases are skipped — it notes gaps

## PROGRESS.md Updates

After each phase completes, update PROGRESS.md:
```markdown
- [x] P{N} {Phase} — completed {ISO_TIMESTAMP}
```

After each iteration, update the iteration count:
```markdown
Iteration: {N}
```

Add notable findings to the `## Notes` section.

## Completion

When ALL phases (P1-P7) are marked complete (or skipped after 3 retries):

1. Verify all output files exist:
   - `output/{DOMAIN}/01-discovery.md`
   - `output/{DOMAIN}/02-market.md`
   - `output/{DOMAIN}/03-technical.md`
   - `output/{DOMAIN}/04-claims.md`
   - `output/{DOMAIN}/05-academic.md`
   - `output/{DOMAIN}/06-valuation.md`
   - `output/{DOMAIN}/07-report.md`
   - `output/{DOMAIN}/executive-summary.md`
2. Update PROGRESS.md with final status
3. Output: `<promise>DOSSIER_COMPLETE</promise>`

## Important Notes
- Use `DOSSIER_ROOT` or relative paths — never hardcode absolute paths
- Python scripts: use `scripts/.venv/bin/python` if venv exists, otherwise `python3`
- Raw data goes to `output/{DOMAIN}/raw/` directory
- Create `output/{DOMAIN}/raw/` if it doesn't exist
- Read target.env for the domain — never hardcode it
- Read `research-program.md` for quality thresholds and strategy variants
- EDS evaluator: `python3 scripts/evaluate_phase.py <file> --phase N`
