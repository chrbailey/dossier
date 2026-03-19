# Dry Run Fixes + 10x Test Coverage — Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix all 7 issues surfaced by the Cycle 1 dry run and expand test coverage from 21 to ~200 tests.

**Architecture:** Code fixes to evidence_store.py (add cycle_number filter, batch scoring, silence confidence). Prompt fixes to 4 markdown files (fallback guidance, cycle-1 logic). Massive test expansion via parallel agent swarm — each agent owns a test domain.

**Tech Stack:** Python 3.11, pytest, SQLite, Markdown

---

## Issues to Fix

| # | Issue | Fix | File |
|---|-------|-----|------|
| 1 | Firecrawl fallback missing in prompts | Add WebSearch fallback to P2, P3 | `loop/prompts/p2-*.md`, `p3-*.md` |
| 2 | No cycle-1 skip logic | Add first-cycle awareness for P5/P7 | `loop/ralph-prompt-loop.md` |
| 3 | add_signal() not structured for batch use | Add `score_evidence()` batch method | `scripts/evidence_store.py` |
| 4 | No cycle_number filter in query() | Add parameter | `scripts/evidence_store.py` |
| 5 | P6 first-cycle delta handling | Add "no prior cycle" branch | `loop/prompts/p6-*.md` |
| 6 | Silence confidence not tracked | Add confidence to silence metadata convention | `scripts/evidence_store.py` (doc) |
| 7 | Contract validation untested | Add contract JSON validation tests | `tests/test_contract.py` |

## Test Expansion: 21 → ~200

| Agent | Test Domain | Target Count |
|-------|-------------|-------------|
| A | Insert edge cases, query filters, get edge cases | ~40 |
| B | Promotion lifecycle (all tier paths, policies, boundaries) | ~40 |
| C | Signals, cycles, batch scoring, composite scores | ~40 |
| D | Anti-recursion guards, silence evidence, thresholds | ~40 |
| E | Contract validation, integration scenarios, data integrity | ~40 |

## Execution Strategy

1. Fix evidence_store.py directly (3 code changes)
2. Dispatch 5 agents in parallel: test agents A-E
3. Dispatch 1 agent for prompt fixes (markdown only)
4. Run full test suite to verify
5. Commit
