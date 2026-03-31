#!/bin/bash
# weekly-monitor.sh -- Weekly sweep for 6 event-dependent questions
# Called by launchd on Sundays at 20:00
set -euo pipefail

DOSSIER_ROOT="/Volumes/OWC drive/Dev/dossier"
CONTRACT="$DOSSIER_ROOT/contracts/signal-monitor.json"
LOG_DIR="$DOSSIER_ROOT/output/signal-curation/logs"
LOG_FILE="$LOG_DIR/monitor-$(date +%Y-%m-%d).log"
EVIDENCE_DB="$DOSSIER_ROOT/data/evidence.db"
CONTEXT_PACK="$DOSSIER_ROOT/output/signal-curation/context/pack.md"
MONITOR_LOG="$DOSSIER_ROOT/output/signal-curation/reports/monitor-log.md"
VENV="$DOSSIER_ROOT/scripts/.venv/bin/python3"

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*" | tee -a "$LOG_FILE"; }

mkdir -p "$LOG_DIR"
log "=== Weekly Signal Monitor started ==="

if [ ! -d "/Volumes/OWC drive/Dev" ]; then log "ABORT: OWC drive not mounted"; exit 1; fi
if [ ! -f "$CONTRACT" ]; then log "ABORT: Contract not found at $CONTRACT"; exit 1; fi
if [ ! -f "$EVIDENCE_DB" ]; then log "ABORT: Evidence DB not found at $EVIDENCE_DB"; exit 1; fi

PRE_COUNTS=$("$VENV" -c "
import sys; sys.path.insert(0, '$DOSSIER_ROOT')
from scripts.evidence_store import EvidenceStore
s = EvidenceStore('$EVIDENCE_DB'); counts = s.tier_counts('RLC.DOSSIER.SIGNAL.001')
print(f'total={sum(counts.values())}'); s.close()
" 2>&1)
log "Pre-run evidence: $PRE_COUNTS"

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

POST_COUNTS=$("$VENV" -c "
import sys; sys.path.insert(0, '$DOSSIER_ROOT')
from scripts.evidence_store import EvidenceStore
s = EvidenceStore('$EVIDENCE_DB'); counts = s.tier_counts('RLC.DOSSIER.SIGNAL.001')
print(f'total={sum(counts.values())}'); s.close()
" 2>&1)
log "Post-run evidence: $POST_COUNTS"

if [ "$PRE_COUNTS" != "$POST_COUNTS" ]; then log "NEW EVIDENCE CAPTURED"; else log "No new evidence this week"; fi
if [ $CLAUDE_EXIT -ne 0 ]; then log "WARNING: Claude Code exited with code $CLAUDE_EXIT"; fi
log "=== Weekly Signal Monitor complete ==="
exit 0
