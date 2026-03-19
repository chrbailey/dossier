# Research Loop — Contract-Driven Ralph Loop Orchestration

## Goal
Execute a continuous research loop defined by a JSON contract. Run all 8 phases per cycle, promoting evidence through durability tiers. Repeat until completion criteria are met.

**Done when:** Convergence criteria met or max iterations reached → output `<promise>LOOP_COMPLETE</promise>`

## Setup

First, read the contract and initialize:

```bash
cd "/Volumes/OWC drive/Dev/dossier"
cat "$CONTRACT"
```

Parse the contract JSON. Extract:
- `contractId` — used for all evidence store operations
- `phases` — the 8-phase definition
- `control` — iteration limits, checkpoints, recursion guards
- `storagePath` — where outputs go

If `${storagePath}/PROGRESS.md` does not exist, create it from `loop/templates/progress-template.md` (replace placeholders with contract values).

If it already exists, read it to determine current cycle and state.

Create the output directory structure:
```bash
mkdir -p "${storagePath}/raw"
mkdir -p "${storagePath}/derived"
mkdir -p "${storagePath}/context"
mkdir -p "${storagePath}/reports"
```

## Phase Execution — Sequential Within Cycle

Unlike the SaaS dossier pipeline (which has DAG dependencies and parallelism), research loop phases run **sequentially** because each phase depends on the prior:

```
P1 Goal Frame
  → P2 Candidate Discovery
    → P3 Evidence Capture
      → P4 Signal Extraction
        → P5 Scoring
          → P6 Synthesis
            → P7 Memory Promotion
              → P8 Next-Loop Planning
```

### First-Cycle Handling

On cycle 1 (no prior data exists):
- **P5 Scoring**: Run, but skip promotion candidate evaluation (no baselines). Instead, establish the baseline tier distribution.
- **P6 Synthesis**: Run, but skip cross-cycle delta (no prior cycle to compare). Prefix the context pack with "BASELINE CYCLE — no prior data for comparison."
- **P7 Memory Promotion**: Run, but only auto-promote raw→working for evidence with confidence >= 0.3. Skip all promotions requiring human review or corroboration (impossible on first cycle).
- **All other phases**: Run normally.

### Per-Phase Execution
For each phase:
1. Read the phase prompt from `loop/prompts/p{N}-{phase}.md`
2. Read the contract JSON for phase-specific config
3. Read prior phase outputs from this cycle
4. Launch a general-purpose sub-agent with the Task tool:
   - Include the phase prompt content
   - Include the contract JSON (or relevant section)
   - Include the evidence store path: `data/evidence.db`
   - Include the output directory path
5. After the agent completes, verify the output
6. Update PROGRESS.md: mark phase complete with timestamp

### Sub-Agent Dispatch Template
```
Task tool parameters:
  subagent_type: "general-purpose"
  description: "Loop P{N} {phase_name}"
  prompt: |
    You are executing Phase {N} of a research loop.

    Contract: {CONTRACT_ID}
    Storage: /Volumes/OWC drive/Dev/dossier/{STORAGE_PATH}
    Evidence DB: /Volumes/OWC drive/Dev/dossier/data/evidence.db
    Cycle: {CYCLE_NUMBER}

    {PHASE_PROMPT_CONTENT}

    Contract config for this phase:
    {PHASE_CONFIG_JSON}

    Prior phase outputs this cycle:
    {PRIOR_OUTPUTS}

    IMPORTANT:
    - Use Firecrawl (via the firecrawl skill) for ALL web collection
    - Use the evidence_store.py script for all evidence operations:
      cd "/Volumes/OWC drive/Dev/dossier"
      python3 -c "from scripts.evidence_store import EvidenceStore; ..."
    - WebFetch may be unavailable — use Firecrawl as the primary web tool
```

## Iteration Logic

Each Ralph Loop iteration = one research cycle:

1. **Read state**: `cat ${storagePath}/PROGRESS.md`
2. **Check anti-recursion guards**:
   - Run: `cd "/Volumes/OWC drive/Dev/dossier" && python3 -c "from scripts.evidence_store import EvidenceStore; s = EvidenceStore(); print('entropy:', s.source_entropy('${CONTRACT_ID}')); print('self_cite:', s.self_citation_ratio('${CONTRACT_ID}')); s.close()"`
   - If entropy < contract.control.recursionGuards.sourceEntropyMinimum → ESCALATE
   - If self_citation > contract.control.recursionGuards.maxSelfCitationRatio → HALT
3. **Execute phases**: Run P1 through P8 sequentially
4. **Update PROGRESS.md**: Increment cycle count, record phase results
5. **Check checkpoint**: If cycle % contract.control.checkpointInterval == 0:
   - Log current state
   - If PromptSpeak MCP available: call `ps_hold_create` for human review
   - Otherwise: write checkpoint note in PROGRESS.md
6. **Check convergence**: If contract.phases.nextLoopPlanning.iterationStrategy has convergenceCriteria:
   - Read the convergence metric from P8 output
   - If met for windowSize consecutive cycles → `<promise>LOOP_COMPLETE</promise>`
7. **Check max iterations**: If cycle >= contract.control.maxIterations → `<promise>LOOP_COMPLETE</promise>`
8. **Continue**: The Ralph Loop stop-hook will re-feed this prompt for the next cycle

## PromptSpeak Governance (when MCP available)

At the start of each cycle, if PromptSpeak MCP tools are accessible:

1. **Validate frame**: Call `ps_validate` with the contract's frame string
2. **Check agent state**: Call `ps_state_get` — if halted, exit gracefully
3. **At checkpoints**: Call `ps_hold_create` with cycle state for human review
4. **On completion**: Call `ps_audit_log` with final loop metrics

If PromptSpeak tools are not available, proceed without governance gates but log the omission in PROGRESS.md.

## Error Handling

If a phase fails:
1. Log the error in PROGRESS.md
2. If phase is P3 (Evidence Capture) and it fails, skip remaining phases this cycle
3. For other phases, note the failure and continue
4. On next cycle, the failed phase runs fresh (no retry of partial state)
5. If the same phase fails 3 cycles in a row, trigger early exit with "escalate"

## Completion

When convergence criteria are met or max iterations reached:

1. Run a final P6 Synthesis to generate the summary context pack
2. Write final anti-recursion metrics to PROGRESS.md
3. Log completion timestamp
4. Output: `<promise>LOOP_COMPLETE</promise>`

## Important Notes
- Always `cd "/Volumes/OWC drive/Dev/dossier"` before running scripts
- The evidence store is at `data/evidence.db` (created automatically)
- Raw evidence goes to `${storagePath}/raw/`
- Derived signals go to `${storagePath}/derived/`
- Reports go to `${storagePath}/reports/`
- Context packs go to `${storagePath}/context/`
- Use Firecrawl for all web data collection — do NOT use raw HTTP requests
