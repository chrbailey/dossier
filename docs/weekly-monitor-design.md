# Weekly Signal Monitor -- Design Doc

**Contract:** RLC.DOSSIER.SIGNAL.002 (narrowed monitor, derived from RLC.DOSSIER.SIGNAL.001)
**Parent:** RLC.DOSSIER.SIGNAL.001 (converged-early, 3 cycles, 148 evidence items)
**Purpose:** Track 6 event-dependent open questions on a weekly cadence
**Schedule:** Sundays at 20:00 local time

## Rationale

The original signal curation loop converged after 3 cycles. The remaining open questions are not research-dependent (more searching won't resolve them) -- they are **event-dependent**. They resolve when something happens: a court rules, a deadline passes, testimony occurs, or results are published.

A full 8-phase loop is overkill. These questions need a lightweight weekly sweep: discover new evidence (P2), capture it (P3), and update the context pack if anything changed (P6). No scoring, no promotion, no gap analysis -- just a watch.

### The 6 Questions

| # | Question | Trigger Type | Expected Window |
|---|----------|-------------|-----------------|
| Q1 | Anthropic v. Trump administration court ruling | Court filing / ruling | 2026 Q2-Q3 |
| Q2 | NDAA June 2026 AI governance enforcement deadline | Legislative deadline | June 2026 |
| Q3 | SAE consciousness replication on Anthropic's models | Research publication | Unknown |
| Q4 | Kalinowski Senate testimony possibility | Congressional hearing | Q2 2026 |
| Q5 | V-JEPA generalization to language tasks | Research publication | 2026 H1 |
| Q6 | Pentagon in-house AI viability | Policy / procurement | 2026 H2 |

---

## 1. Narrowed Contract JSON

Save to: `contracts/signal-monitor.json`

```json
{
  "contractId": "RLC.DOSSIER.SIGNAL.002",
  "version": 1,
  "name": "Weekly Signal Monitor (Event-Dependent Questions)",
  "description": "Lightweight weekly sweep for 6 event-dependent questions from the converged signal curation loop",
  "parentContract": "RLC.DOSSIER.SIGNAL.001",
  "frame": "⊘◇◀α",
  "questions": [
    {
      "id": "Q1",
      "label": "Anthropic v. Trump court ruling",
      "searchQueries": [
        "Anthropic lawsuit Trump administration ruling",
        "Anthropic v. Trump court decision 2026",
        "Anthropic supply chain designation court"
      ],
      "triggerType": "court_ruling",
      "relatedHashes": ["0dc66a56", "283dc6b0", "24b66bac"],
      "expectedWindow": "2026-Q2/Q3",
      "resolved": false
    },
    {
      "id": "Q2",
      "label": "NDAA June 2026 AI governance deadline",
      "searchQueries": [
        "NDAA 2026 AI governance enforcement",
        "FY2026 NDAA artificial intelligence compliance",
        "Pentagon AI governance team deadline June 2026"
      ],
      "triggerType": "legislative_deadline",
      "relatedHashes": ["aee96e9d"],
      "expectedWindow": "2026-06",
      "resolved": false
    },
    {
      "id": "Q3",
      "label": "SAE consciousness replication on Anthropic models",
      "searchQueries": [
        "sparse autoencoder consciousness replication Claude",
        "SAE deception features Anthropic models",
        "AI consciousness empirical replication 2026"
      ],
      "triggerType": "research_publication",
      "relatedHashes": ["681b2b9b", "c6b0cc1d"],
      "expectedWindow": "unknown",
      "resolved": false
    },
    {
      "id": "Q4",
      "label": "Kalinowski Senate testimony",
      "searchQueries": [
        "Kalinowski Senate testimony AI",
        "Kalinowski Congress hearing 2026",
        "OpenAI whistleblower Senate AI committee"
      ],
      "triggerType": "congressional_hearing",
      "relatedHashes": ["9146b931", "23643bc9"],
      "expectedWindow": "2026-Q2",
      "resolved": false
    },
    {
      "id": "Q5",
      "label": "V-JEPA generalization to language tasks",
      "searchQueries": [
        "V-JEPA language tasks results",
        "V-JEPA NLP benchmark",
        "JEPA text generalization LeCun 2026"
      ],
      "triggerType": "research_publication",
      "relatedHashes": ["41eb0f91", "9eb3f5ee"],
      "expectedWindow": "2026-H1",
      "resolved": false
    },
    {
      "id": "Q6",
      "label": "Pentagon in-house AI viability",
      "searchQueries": [
        "Pentagon in-house AI development",
        "DoD AI without Anthropic OpenAI",
        "military AI internal capability 2026"
      ],
      "triggerType": "policy_procurement",
      "relatedHashes": ["5dd1fcda"],
      "expectedWindow": "2026-H2",
      "resolved": false
    }
  ],
  "phases": {
    "discovery": {
      "strategy": "targeted",
      "maxResultsPerQuery": 5,
      "freshnessHorizon": 168,
      "fallbackToWebSearch": true
    },
    "capture": {
      "captureFields": ["post_text", "timestamp", "url", "topic_tags"],
      "hashAlgorithm": "sha256",
      "deduplication": {
        "strategy": "exact",
        "semanticThreshold": 0.85
      }
    },
    "synthesis": {
      "updateContextPack": true,
      "contextPackPath": "output/signal-curation/context/pack.md",
      "appendixPath": "output/signal-curation/reports/monitor-log.md",
      "onlyUpdateIfNewEvidence": true
    }
  },
  "control": {
    "cadence": "weekly",
    "maxRuntime": 600,
    "completionCondition": "all_questions_resolved",
    "autoResolve": false,
    "evidenceDb": "data/evidence.db",
    "parentContractId": "RLC.DOSSIER.SIGNAL.001"
  },
  "storagePath": "output/signal-curation/",
  "status": "active",
  "createdAt": "2026-03-19T00:00:00Z",
  "createdBy": "christopherbailey"
}
```

Key design choices:
- **Frame `⊘◇◀α`**: neutral mode (not strict -- this is a watch, not enforcement), technical domain, retrieve action, primary agent. No execute symbol because nothing is being acted on.
- **3 search queries per question**: specific enough to catch real events, broad enough to catch adjacent coverage.
- **`relatedHashes`**: links back to parent contract evidence for continuity.
- **`freshnessHorizon: 168`**: 7 days, matches the weekly cadence.
- **No scoring/promotion phases**: evidence goes into the store as raw, gets scored only if it resolves a question.
- **`autoResolve: false`**: questions are marked resolved only by human decision.

---

## 2. Wrapper Script

Save to: `scripts/weekly-monitor.sh`

```bash
#!/bin/bash
# weekly-monitor.sh -- Weekly sweep for 6 event-dependent questions
# Called by launchd on Sundays at 20:00
# Invokes Claude Code to run the narrowed discovery/capture/synthesis loop

set -euo pipefail

# --- Config ---
DOSSIER_ROOT="/Volumes/OWC drive/Dev/dossier"
CONTRACT="$DOSSIER_ROOT/contracts/signal-monitor.json"
LOG_DIR="$DOSSIER_ROOT/output/signal-curation/logs"
LOG_FILE="$LOG_DIR/monitor-$(date +%Y-%m-%d).log"
EVIDENCE_DB="$DOSSIER_ROOT/data/evidence.db"
CONTEXT_PACK="$DOSSIER_ROOT/output/signal-curation/context/pack.md"
MONITOR_LOG="$DOSSIER_ROOT/output/signal-curation/reports/monitor-log.md"
VENV="$DOSSIER_ROOT/scripts/.venv/bin/python3"

# --- Functions ---
log() {
    echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" | tee -a "$LOG_FILE"
}

# --- Preflight ---
mkdir -p "$LOG_DIR"
log "=== Weekly Signal Monitor started ==="

# 1. Check OWC drive
if [ ! -d "/Volumes/OWC drive/Dev" ]; then
    log "ABORT: OWC drive not mounted"
    exit 1
fi

# 2. Check contract exists
if [ ! -f "$CONTRACT" ]; then
    log "ABORT: Contract not found at $CONTRACT"
    exit 1
fi

# 3. Check evidence DB exists
if [ ! -f "$EVIDENCE_DB" ]; then
    log "ABORT: Evidence DB not found at $EVIDENCE_DB"
    exit 1
fi

# 4. Get pre-run tier counts for comparison
PRE_COUNTS=$("$VENV" -c "
import sys
sys.path.insert(0, '$DOSSIER_ROOT')
from scripts.evidence_store import EvidenceStore
s = EvidenceStore('$EVIDENCE_DB')
counts = s.tier_counts('RLC.DOSSIER.SIGNAL.001')
total = sum(counts.values())
print(f'total={total}')
s.close()
" 2>&1)
log "Pre-run evidence: $PRE_COUNTS"

# 5. Run the monitor via Claude Code
log "Launching Claude Code monitor session..."

claude --print \
    --allowedTools "Bash,Read,Write,Edit,WebSearch,Grep,Glob" \
    --model claude-sonnet-4-20250514 \
    --max-turns 30 \
    "You are running the weekly signal monitor for the AI dossier.

Read the contract at: $CONTRACT
Read the current context pack at: $CONTEXT_PACK

For each unresolved question in the contract:
1. Run each searchQuery using WebSearch (freshnessHorizon: last 7 days)
2. If results contain NEW information not already in the evidence store, capture it:
   cd \"$DOSSIER_ROOT\"
   python3 -c \"from scripts.evidence_store import EvidenceStore; ...\"
   Use contract_id 'RLC.DOSSIER.SIGNAL.001' (parent contract, shared evidence store)
3. If a question appears RESOLVED by the evidence, note it but do NOT mark resolved

After all questions are checked:
- If ANY new evidence was captured, append a dated entry to: $MONITOR_LOG
- If new evidence is significant (court ruling, official announcement, published results),
  update the Contradictions & Open Questions section of: $CONTEXT_PACK
- Write a summary of findings (or 'no new evidence') to stdout

Evidence DB: $EVIDENCE_DB
Working directory: $DOSSIER_ROOT

IMPORTANT: Do not fabricate evidence. If WebSearch returns nothing new, say so.
Do not mark questions as resolved without clear evidence of resolution." \
    >> "$LOG_FILE" 2>&1

CLAUDE_EXIT=$?

# 6. Get post-run tier counts
POST_COUNTS=$("$VENV" -c "
import sys
sys.path.insert(0, '$DOSSIER_ROOT')
from scripts.evidence_store import EvidenceStore
s = EvidenceStore('$EVIDENCE_DB')
counts = s.tier_counts('RLC.DOSSIER.SIGNAL.001')
total = sum(counts.values())
print(f'total={total}')
s.close()
" 2>&1)
log "Post-run evidence: $POST_COUNTS"

# 7. Compare
if [ "$PRE_COUNTS" != "$POST_COUNTS" ]; then
    log "NEW EVIDENCE CAPTURED (counts changed)"
else
    log "No new evidence this week"
fi

if [ $CLAUDE_EXIT -ne 0 ]; then
    log "WARNING: Claude Code exited with code $CLAUDE_EXIT"
fi

log "=== Weekly Signal Monitor complete ==="
exit 0
```

Key design choices:
- **`claude --print`**: non-interactive, output only. No dangerously-skip-permissions -- the allowed tools are explicitly scoped.
- **`--model claude-sonnet-4-20250514`**: Sonnet for cost efficiency. This is a search-and-capture task, not deep analysis.
- **`--max-turns 30`**: 6 questions x 3 queries each = 18 searches, plus capture and synthesis. 30 turns is generous.
- **Pre/post evidence count comparison**: simple way to detect if anything was captured without parsing Claude's output.
- **Shared evidence store**: new evidence goes into the SAME `evidence.db` under the parent contract ID. This preserves corroboration counting and tier continuity.

---

## 3. launchd Plist

Save to: `~/Library/LaunchAgents/com.dossier.weekly-monitor.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.dossier.weekly-monitor</string>

    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>/Volumes/OWC drive/Dev/dossier/scripts/weekly-monitor.sh</string>
    </array>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>0</integer>
        <key>Hour</key>
        <integer>20</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>

    <key>StandardOutPath</key>
    <string>/Volumes/OWC drive/Dev/dossier/output/signal-curation/logs/launchd-stdout.log</string>

    <key>StandardErrorPath</key>
    <string>/Volumes/OWC drive/Dev/dossier/output/signal-curation/logs/launchd-stderr.log</string>

    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin</string>
        <key>HOME</key>
        <string>/Users/christopherbailey</string>
    </dict>

    <key>WorkingDirectory</key>
    <string>/Volumes/OWC drive/Dev/dossier</string>

    <key>RunAtLoad</key>
    <false/>

    <key>Nice</key>
    <integer>10</integer>

    <key>ProcessType</key>
    <string>Background</string>
</dict>
</plist>
```

Key design choices:
- **`Weekday 0` (Sunday), `Hour 20`**: evening run, machine likely idle.
- **`RunAtLoad: false`**: does not fire on login. Only on schedule.
- **`Nice: 10`**: low priority. This is background work.
- **`PATH` includes `/opt/homebrew/bin`**: ensures `claude` CLI is found on Apple Silicon.
- **`HOME` explicitly set**: launchd agents sometimes lose HOME, which breaks `~/.claude/` config resolution.
- **OWC drive path in ProgramArguments**: the wrapper script handles the mount check and aborts gracefully if unmounted.

---

## 4. Setup Instructions

### Install (one-time)

```bash
# 1. Create the contract file
# Copy the JSON from Section 1 into:
#   /Volumes/OWC drive/Dev/dossier/contracts/signal-monitor.json

# 2. Create the wrapper script
# Copy the script from Section 2 into:
#   /Volumes/OWC drive/Dev/dossier/scripts/weekly-monitor.sh
chmod +x "/Volumes/OWC drive/Dev/dossier/scripts/weekly-monitor.sh"

# 3. Create the log directory
mkdir -p "/Volumes/OWC drive/Dev/dossier/output/signal-curation/logs"

# 4. Create the monitor log (append-only)
touch "/Volumes/OWC drive/Dev/dossier/output/signal-curation/reports/monitor-log.md"

# 5. Copy the plist
# Copy the XML from Section 3 into:
#   ~/Library/LaunchAgents/com.dossier.weekly-monitor.plist

# 6. Validate the plist
plutil -lint ~/Library/LaunchAgents/com.dossier.weekly-monitor.plist
```

### Load (when ready)

```bash
launchctl load ~/Library/LaunchAgents/com.dossier.weekly-monitor.plist
```

### Test manually

```bash
# Dry run (same as launchd would invoke)
bash "/Volumes/OWC drive/Dev/dossier/scripts/weekly-monitor.sh"

# Check logs after
cat "/Volumes/OWC drive/Dev/dossier/output/signal-curation/logs/monitor-$(date +%Y-%m-%d).log"
```

### Unload

```bash
launchctl unload ~/Library/LaunchAgents/com.dossier.weekly-monitor.plist
```

### Check status

```bash
launchctl list | grep dossier
```

---

## 5. Output Structure

After the monitor runs, outputs land here:

```
output/signal-curation/
├── context/
│   └── pack.md                    # Updated if significant new evidence
├── logs/
│   ├── monitor-2026-03-23.log     # Per-run log (dated)
│   ├── launchd-stdout.log         # launchd stdout capture
│   └── launchd-stderr.log         # launchd stderr capture
└── reports/
    └── monitor-log.md             # Append-only log of findings per week
```

### monitor-log.md format

Each weekly run appends a section:

```markdown
## 2026-03-23

**New evidence:** 2 items
- Q1 (Anthropic v. Trump): Court scheduled oral arguments for April 14 [hash: abc12345]
- Q4 (Kalinowski): Senate AI subcommittee announced witness list, Kalinowski not listed [hash: def67890]

**No updates:** Q2, Q3, Q5, Q6

---
```

If no new evidence:

```markdown
## 2026-03-23

**No new evidence this week.** All 6 questions remain open.

---
```

---

## 6. Resolution Protocol

When a question is resolved (human determination, not automatic):

1. Edit `contracts/signal-monitor.json` -- set `"resolved": true` on the question
2. Add a note to `monitor-log.md` with the resolution hash and date
3. When all 6 are resolved, unload the launchd agent:
   ```bash
   launchctl unload ~/Library/LaunchAgents/com.dossier.weekly-monitor.plist
   ```
4. Write a final synthesis update to the context pack

---

## 7. Cost Estimate

Per weekly run:
- 6 questions x 3 queries = 18 WebSearch calls
- ~30 Claude Sonnet turns at ~1K tokens each = ~30K tokens
- Evidence capture: negligible (SQLite writes)
- **Estimated cost: ~$0.10-0.20/week** (Sonnet pricing, mostly search + short completions)

Monthly: ~$0.50-0.80. Negligible.

---

## 8. Failure Modes

| Failure | Script Behavior | Recovery |
|---------|----------------|----------|
| OWC drive unmounted | Logs ABORT, exits 1 | Run manually when mounted, or wait for next Sunday |
| Claude CLI not in PATH | launchd stderr log captures error | Fix PATH in plist EnvironmentVariables |
| Evidence DB locked | Python sqlite3 raises, Claude session fails | Retry manually; check for zombie processes |
| WebSearch unavailable | Claude notes "no results" per question | No action needed; next week will retry |
| All questions already resolved | Script runs, finds no unresolved questions, exits clean | Unload the agent |
| Claude exceeds --max-turns | Session truncates, partial results captured | Check log; increase max-turns if needed |
