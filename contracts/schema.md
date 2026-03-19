# Research Loop Contract — Schema Reference

Contracts define a complete, governable research iteration loop.

## Type Definition
See: `/Volumes/OWC drive/Dev/promptspeak/mcp-server/src/types/research-loop.ts`

## Contract ID Convention
`RLC.<PROJECT>.<DOMAIN>.<SEQ>`

Example: `RLC.DOSSIER.SIGNAL.001`

## How To Run

```bash
# Set the contract
export CONTRACT=contracts/signal-curation.json

# Launch via Ralph Loop
# /ralph-loop --max-iterations 10 --completion-promise "LOOP_COMPLETE"
# Paste: read loop/ralph-prompt-loop.md and execute with CONTRACT=contracts/signal-curation.json
```

## Evidence Tiers

| Tier | Confidence | Corroboration | Human Review | Description |
|------|-----------|---------------|-------------|-------------|
| raw | 0.0+ | 0 | No | Captured, unprocessed |
| working | 0.3+ | 0 | No | Summarized, in analysis |
| verified | 0.5+ | 1+ | No | Cross-referenced |
| promoted | 0.7+ | 2+ | Yes | Durable memory/context |
| training | 0.8+ | 3+ | Yes | Fine-tuning candidate |
| locked | 0.9+ | 5+ | Yes | Immutable reference |
