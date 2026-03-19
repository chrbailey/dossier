# Research Loop Composition — Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Compose Dossier's Ralph Loop, PromptSpeak's governance, and Lex's scraping patterns into a contract-driven continuous research loop that curates signals, tracks absences, and promotes evidence through durability tiers.

**Architecture:** A JSON contract (typed by PromptSpeak's `ResearchLoopContract`) defines the 8-phase loop. A new `ralph-prompt-loop.md` reads the contract and dispatches phase sub-agents. A Python SQLite evidence store manages evidence tiers and promotion. Firecrawl (via Claude Code skill) handles all web collection. PromptSpeak MCP tools gate phase boundaries.

**Tech Stack:** Python 3.9 (evidence store), Markdown prompts (loop orchestration), JSON (contract), SQLite (evidence), PromptSpeak MCP (governance), Firecrawl skill (web collection), Ralph Loop plugin (iteration)

**Existing project:** `/Volumes/OWC drive/Dev/dossier/`
**PromptSpeak types:** `/Volumes/OWC drive/Dev/promptspeak/mcp-server/src/types/research-loop.ts`

---

## Scope Note

The existing SaaS due diligence pipeline (`ralph-prompt.md`, `prompts/p1-p7.md`) is **not modified**. The research loop adds alongside it as a new mode. The existing `output/` structure for company dossiers is preserved.

## File Structure

### New Files

| Path | Responsibility |
|------|---------------|
| `contracts/signal-curation.json` | First contract instance (AI voices) |
| `contracts/schema.md` | Human-readable contract format reference |
| `scripts/evidence_store.py` | SQLite evidence CRUD, tier promotion, dedup |
| `loop/ralph-prompt-loop.md` | Contract-driven Ralph Loop orchestrator |
| `loop/prompts/p1-goal-frame.md` | Phase 1: Load contract, validate scope |
| `loop/prompts/p2-candidate-discovery.md` | Phase 2: Find candidates from sources |
| `loop/prompts/p3-evidence-capture.md` | Phase 3: Collect and store raw evidence |
| `loop/prompts/p4-signal-extraction.md` | Phase 4: Score signals, detect absence |
| `loop/prompts/p5-scoring.md` | Phase 5: Apply promotion thresholds |
| `loop/prompts/p6-synthesis.md` | Phase 6: Generate cycle outputs |
| `loop/prompts/p7-memory-promotion.md` | Phase 7: Promote evidence across tiers |
| `loop/prompts/p8-next-loop-planning.md` | Phase 8: Gap analysis, plan next cycle |
| `loop/templates/progress-template.md` | PROGRESS.md template for loop runs |
| `tests/test_evidence_store.py` | Evidence store unit tests |

### Modified Files

| Path | Change |
|------|--------|
| `CLAUDE.md` | Add research loop section with run instructions |

### Existing Files Referenced (Read-Only)

| Path | Why |
|------|-----|
| `ralph-prompt.md` | Pattern reference for loop orchestration |
| `templates/progress-template.md` | Pattern reference for progress tracking |
| `scripts/whois_lookup.py` | Pattern reference for helper script style |

---

## Chunk 1: Evidence Store (Python + SQLite)

The evidence store is the only real code in this project. Everything else is prompts and config. It manages the 6-tier evidence lifecycle defined in `ResearchLoopContract`.

### Task 1: Evidence Store Schema and Init

**Files:**
- Create: `/Volumes/OWC drive/Dev/dossier/scripts/evidence_store.py`
- Create: `/Volumes/OWC drive/Dev/dossier/tests/test_evidence_store.py`

- [ ] **Step 1: Write the failing test for DB init**

```python
# tests/test_evidence_store.py
"""Tests for the evidence store."""
from __future__ import annotations

import os
import sqlite3
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def db_path(tmp_path):
    """Provide a temporary database path."""
    return tmp_path / "test_evidence.db"


@pytest.fixture
def store(db_path):
    """Create a fresh evidence store."""
    from scripts.evidence_store import EvidenceStore
    return EvidenceStore(db_path)


class TestInit:
    def test_creates_database(self, store, db_path):
        """Store init creates the SQLite file."""
        assert db_path.exists()

    def test_creates_tables(self, store, db_path):
        """Store init creates evidence, signals, and cycles tables."""
        conn = sqlite3.connect(db_path)
        tables = [r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()]
        conn.close()
        assert "evidence" in tables
        assert "signals" in tables
        assert "cycles" in tables
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && python -m pytest tests/test_evidence_store.py::TestInit -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'scripts.evidence_store'`

- [ ] **Step 3: Write minimal evidence store with schema**

```python
# scripts/evidence_store.py
"""Evidence store for Dossier Loop.

Manages evidence across 6 durability tiers with promotion gates.
Uses SQLite for local-first persistence.

Tiers (from ResearchLoopContract):
  raw → working → verified → promoted → training → locked

Usage:
  from scripts.evidence_store import EvidenceStore
  store = EvidenceStore()  # uses default path: data/evidence.db
  store.insert("RLC.001", "source-1", "content here", {"key": "val"})
  store.promote("RLC.001", "<hash>", "working", confidence=0.5)
"""
from __future__ import annotations

import hashlib
import json
import math
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

SCHEMA = """
CREATE TABLE IF NOT EXISTS evidence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hash TEXT UNIQUE NOT NULL,
    contract_id TEXT NOT NULL,
    tier TEXT NOT NULL DEFAULT 'raw',
    source_id TEXT NOT NULL,
    content TEXT NOT NULL,
    metadata TEXT,
    confidence REAL DEFAULT 0.0,
    corroboration_count INTEGER DEFAULT 0,
    created_at TEXT NOT NULL,
    updated_at TEXT,
    promoted_at TEXT,
    expires_at TEXT,
    cycle_number INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS signals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    evidence_id INTEGER REFERENCES evidence(id),
    contract_id TEXT NOT NULL,
    dimension TEXT NOT NULL,
    score REAL NOT NULL,
    scorer TEXT NOT NULL,
    cycle_number INTEGER NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS cycles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contract_id TEXT NOT NULL,
    cycle_number INTEGER NOT NULL,
    phase TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    started_at TEXT,
    completed_at TEXT,
    artifacts TEXT,
    notes TEXT
);

CREATE INDEX IF NOT EXISTS idx_evidence_contract ON evidence(contract_id);
CREATE INDEX IF NOT EXISTS idx_evidence_tier ON evidence(tier);
CREATE INDEX IF NOT EXISTS idx_evidence_source ON evidence(source_id);
CREATE INDEX IF NOT EXISTS idx_signals_evidence ON signals(evidence_id);
CREATE INDEX IF NOT EXISTS idx_cycles_contract ON cycles(contract_id, cycle_number);
"""

TIERS = ["raw", "working", "verified", "promoted", "training", "locked"]

DEFAULT_DB = Path(__file__).parent.parent / "data" / "evidence.db"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _hash_content(source_id: str, content: str) -> str:
    """SHA-256 hash of source + content for dedup."""
    return hashlib.sha256(f"{source_id}:{content}".encode()).hexdigest()[:16]


class EvidenceStore:
    """SQLite-backed evidence store with tier promotion."""

    def __init__(self, db_path: Union[str, Path, None] = None):
        self.db_path = Path(db_path) if db_path else DEFAULT_DB
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)

    def close(self):
        self.conn.close()

    def insert(
        self,
        contract_id: str,
        source_id: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None,
        cycle_number: int = 0,
    ) -> Optional[str]:
        """Insert raw evidence. Returns hash, or None if duplicate."""
        h = _hash_content(source_id, content)
        try:
            self.conn.execute(
                """INSERT INTO evidence
                   (hash, contract_id, source_id, content, metadata,
                    created_at, cycle_number)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (h, contract_id, source_id, content,
                 json.dumps(metadata) if metadata else None,
                 _now(), cycle_number),
            )
            self.conn.commit()
            return h
        except sqlite3.IntegrityError:
            # Duplicate — increment corroboration
            self.conn.execute(
                """UPDATE evidence
                   SET corroboration_count = corroboration_count + 1,
                       updated_at = ?
                   WHERE hash = ?""",
                (_now(), h),
            )
            self.conn.commit()
            return None

    def get(self, evidence_hash: str) -> Optional[Dict[str, Any]]:
        """Get evidence by hash."""
        row = self.conn.execute(
            "SELECT * FROM evidence WHERE hash = ?", (evidence_hash,)
        ).fetchone()
        return dict(row) if row else None

    def query(
        self,
        contract_id: str,
        tier: Optional[str] = None,
        source_id: Optional[str] = None,
        limit: int = 100,
    ) -> List[Dict[str, Any]]:
        """Query evidence with optional filters."""
        sql = "SELECT * FROM evidence WHERE contract_id = ?"
        params: list = [contract_id]
        if tier:
            sql += " AND tier = ?"
            params.append(tier)
        if source_id:
            sql += " AND source_id = ?"
            params.append(source_id)
        sql += " ORDER BY created_at DESC LIMIT ?"
        params.append(limit)
        return [dict(r) for r in self.conn.execute(sql, params).fetchall()]

    def promote(
        self,
        contract_id: str,
        evidence_hash: str,
        target_tier: str,
        confidence: Optional[float] = None,
    ) -> bool:
        """Promote evidence to a higher tier. Returns success."""
        if target_tier not in TIERS:
            return False
        row = self.get(evidence_hash)
        if not row or row["contract_id"] != contract_id:
            return False
        current_idx = TIERS.index(row["tier"])
        target_idx = TIERS.index(target_tier)
        if target_idx <= current_idx:
            return False  # Can only promote upward
        updates = {"tier": target_tier, "promoted_at": _now(), "updated_at": _now()}
        if confidence is not None:
            updates["confidence"] = confidence
        set_clause = ", ".join(f"{k} = ?" for k in updates)
        self.conn.execute(
            f"UPDATE evidence SET {set_clause} WHERE hash = ?",
            list(updates.values()) + [evidence_hash],
        )
        self.conn.commit()
        return True

    def add_signal(
        self,
        evidence_id: int,
        contract_id: str,
        dimension: str,
        score: float,
        scorer: str,
        cycle_number: int,
    ) -> int:
        """Record a signal score for evidence."""
        cur = self.conn.execute(
            """INSERT INTO signals
               (evidence_id, contract_id, dimension, score, scorer,
                cycle_number, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (evidence_id, contract_id, dimension, score, scorer,
             cycle_number, _now()),
        )
        self.conn.commit()
        return cur.lastrowid

    def record_cycle(
        self,
        contract_id: str,
        cycle_number: int,
        phase: str,
        status: str = "pending",
    ) -> int:
        """Record a cycle phase execution."""
        cur = self.conn.execute(
            """INSERT INTO cycles
               (contract_id, cycle_number, phase, status, started_at)
               VALUES (?, ?, ?, ?, ?)""",
            (contract_id, cycle_number, phase, status, _now()),
        )
        self.conn.commit()
        return cur.lastrowid

    def complete_cycle(self, cycle_id: int, status: str, notes: Optional[str] = None):
        """Mark a cycle phase as complete."""
        self.conn.execute(
            """UPDATE cycles SET status = ?, completed_at = ?, notes = ?
               WHERE id = ?""",
            (status, _now(), notes, cycle_id),
        )
        self.conn.commit()

    def source_entropy(self, contract_id: str) -> float:
        """Shannon entropy of source distribution. Anti-recursion guard."""
        rows = self.conn.execute(
            """SELECT source_id, COUNT(*) as cnt
               FROM evidence WHERE contract_id = ?
               GROUP BY source_id""",
            (contract_id,),
        ).fetchall()
        if not rows:
            return 0.0
        total = sum(r["cnt"] for r in rows)
        entropy = 0.0
        for r in rows:
            p = r["cnt"] / total
            if p > 0:
                entropy -= p * math.log2(p)
        return round(entropy, 3)

    def self_citation_ratio(self, contract_id: str) -> float:
        """Fraction of evidence sourced from own prior outputs. Anti-recursion guard."""
        total = self.conn.execute(
            "SELECT COUNT(*) FROM evidence WHERE contract_id = ?",
            (contract_id,),
        ).fetchone()[0]
        if total == 0:
            return 0.0
        self_refs = self.conn.execute(
            """SELECT COUNT(*) FROM evidence
               WHERE contract_id = ? AND source_id LIKE 'self:%'""",
            (contract_id,),
        ).fetchone()[0]
        return round(self_refs / total, 3)

    def tier_counts(self, contract_id: str) -> Dict[str, int]:
        """Count evidence per tier."""
        rows = self.conn.execute(
            """SELECT tier, COUNT(*) as cnt FROM evidence
               WHERE contract_id = ? GROUP BY tier""",
            (contract_id,),
        ).fetchall()
        return {r["tier"]: r["cnt"] for r in rows}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && python -m pytest tests/test_evidence_store.py::TestInit -v`
Expected: PASS (2 tests)

- [ ] **Step 5: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add scripts/evidence_store.py tests/test_evidence_store.py
git commit -m "feat: add evidence store with SQLite schema and tier promotion"
```

### Task 2: Evidence Store — Insert, Dedup, Promote

**Files:**
- Modify: `/Volumes/OWC drive/Dev/dossier/tests/test_evidence_store.py`

- [ ] **Step 1: Write failing tests for insert, dedup, promote**

```python
# Append to tests/test_evidence_store.py

class TestInsert:
    def test_insert_returns_hash(self, store):
        h = store.insert("RLC.001", "source-1", "test content")
        assert h is not None
        assert len(h) == 16

    def test_insert_duplicate_returns_none(self, store):
        store.insert("RLC.001", "source-1", "same content")
        h2 = store.insert("RLC.001", "source-1", "same content")
        assert h2 is None

    def test_duplicate_increments_corroboration(self, store):
        h = store.insert("RLC.001", "source-1", "content")
        store.insert("RLC.001", "source-1", "content")
        row = store.get(h)
        assert row["corroboration_count"] == 1

    def test_insert_with_metadata(self, store):
        h = store.insert("RLC.001", "src", "text", {"key": "val"})
        row = store.get(h)
        import json
        assert json.loads(row["metadata"]) == {"key": "val"}


class TestPromote:
    def test_promote_raw_to_working(self, store):
        h = store.insert("RLC.001", "src", "content")
        assert store.promote("RLC.001", h, "working", confidence=0.4)
        row = store.get(h)
        assert row["tier"] == "working"
        assert row["confidence"] == 0.4

    def test_cannot_demote(self, store):
        h = store.insert("RLC.001", "src", "content")
        store.promote("RLC.001", h, "verified", confidence=0.6)
        assert not store.promote("RLC.001", h, "raw")

    def test_cannot_promote_wrong_contract(self, store):
        h = store.insert("RLC.001", "src", "content")
        assert not store.promote("RLC.999", h, "working")


class TestQuery:
    def test_query_by_contract(self, store):
        store.insert("RLC.001", "src", "content-a")
        store.insert("RLC.002", "src", "content-b")
        results = store.query("RLC.001")
        assert len(results) == 1

    def test_query_by_tier(self, store):
        h = store.insert("RLC.001", "src-a", "content-a")
        store.insert("RLC.001", "src-b", "content-b")
        store.promote("RLC.001", h, "working")
        results = store.query("RLC.001", tier="working")
        assert len(results) == 1


class TestAntiRecursion:
    def test_source_entropy_single_source(self, store):
        store.insert("RLC.001", "only-source", "a")
        store.insert("RLC.001", "only-source", "b")  # different content
        assert store.source_entropy("RLC.001") == 0.0

    def test_source_entropy_multiple_sources(self, store):
        store.insert("RLC.001", "src-1", "a")
        store.insert("RLC.001", "src-2", "b")
        entropy = store.source_entropy("RLC.001")
        assert entropy > 0.9  # 2 equal sources → entropy = 1.0

    def test_self_citation_ratio(self, store):
        store.insert("RLC.001", "external-1", "a")
        store.insert("RLC.001", "external-2", "b")
        store.insert("RLC.001", "self:prior-cycle", "c")
        ratio = store.self_citation_ratio("RLC.001")
        assert abs(ratio - 0.333) < 0.01
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && python -m pytest tests/test_evidence_store.py -v -k "not TestInit"`
Expected: All new tests PASS (the implementation is already in Task 1's Step 3)

Note: If tests already pass because the implementation was written ahead, that's fine. If any fail, fix the implementation.

- [ ] **Step 3: Run full test suite**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && python -m pytest tests/test_evidence_store.py -v`
Expected: All tests PASS

- [ ] **Step 4: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add tests/test_evidence_store.py
git commit -m "test: evidence store insert, dedup, promote, anti-recursion"
```

---

## Chunk 2: Contract Instance + Loop Orchestration

### Task 3: Contract JSON — First Instance

**Files:**
- Create: `/Volumes/OWC drive/Dev/dossier/contracts/signal-curation.json`
- Create: `/Volumes/OWC drive/Dev/dossier/contracts/schema.md`

- [ ] **Step 1: Create the contracts directory**

```bash
mkdir -p "/Volumes/OWC drive/Dev/dossier/contracts"
```

- [ ] **Step 2: Write the first contract instance**

Write `/Volumes/OWC drive/Dev/dossier/contracts/signal-curation.json`:

```json
{
  "contractId": "RLC.DOSSIER.SIGNAL.001",
  "version": 1,
  "name": "AI Signal Curation Loop",
  "description": "Continuously curate the most important voices, signals, and absences in AI research and deployment",
  "frame": "⊕◇⟳▶α",
  "phases": {
    "goalFrame": {
      "objective": "Monitor key AI voices for signal shifts, emerging patterns, and meaningful silences",
      "commandersIntent": "Know what the smartest people in AI are saying and not saying, before it becomes consensus",
      "sourceUniverse": [
        {
          "sourceId": "karpathy",
          "name": "Andrej Karpathy",
          "tier": "primary",
          "trustWeight": 0.9,
          "freshnessHorizon": 168,
          "domains": ["ai-research", "training", "infrastructure"],
          "verificationRequired": false
        },
        {
          "sourceId": "dario-amodei",
          "name": "Dario Amodei",
          "tier": "primary",
          "trustWeight": 0.9,
          "freshnessHorizon": 336,
          "domains": ["ai-safety", "scaling", "policy"],
          "verificationRequired": false
        },
        {
          "sourceId": "sama",
          "name": "Sam Altman",
          "tier": "secondary",
          "trustWeight": 0.6,
          "freshnessHorizon": 72,
          "domains": ["product", "deployment", "funding"],
          "verificationRequired": true
        },
        {
          "sourceId": "demis-hassabis",
          "name": "Demis Hassabis",
          "tier": "primary",
          "trustWeight": 0.85,
          "freshnessHorizon": 336,
          "domains": ["ai-research", "science", "deepmind"],
          "verificationRequired": false
        },
        {
          "sourceId": "yann-lecun",
          "name": "Yann LeCun",
          "tier": "primary",
          "trustWeight": 0.8,
          "freshnessHorizon": 168,
          "domains": ["ai-research", "open-source", "architectures"],
          "verificationRequired": false
        },
        {
          "sourceId": "jim-fan",
          "name": "Jim Fan",
          "tier": "secondary",
          "trustWeight": 0.7,
          "freshnessHorizon": 72,
          "domains": ["embodied-ai", "foundation-models", "nvidia"],
          "verificationRequired": false
        },
        {
          "sourceId": "emad-mostaque",
          "name": "Emad Mostaque",
          "tier": "rumor",
          "trustWeight": 0.3,
          "freshnessHorizon": 48,
          "domains": ["open-source", "stability", "deployment"],
          "verificationRequired": true
        },
        {
          "sourceId": "harrison-chase",
          "name": "Harrison Chase",
          "tier": "secondary",
          "trustWeight": 0.7,
          "freshnessHorizon": 72,
          "domains": ["agents", "langchain", "developer-tools"],
          "verificationRequired": false
        },
        {
          "sourceId": "swyx",
          "name": "Shawn Wang (swyx)",
          "tier": "secondary",
          "trustWeight": 0.75,
          "freshnessHorizon": 72,
          "domains": ["ai-engineering", "developer-tools", "meta-analysis"],
          "verificationRequired": false
        },
        {
          "sourceId": "simon-willison",
          "name": "Simon Willison",
          "tier": "primary",
          "trustWeight": 0.85,
          "freshnessHorizon": 72,
          "domains": ["developer-tools", "llm-applications", "open-source"],
          "verificationRequired": false
        }
      ],
      "freshnessHorizon": 168,
      "failureConditions": [
        "Zero new evidence collected for 3 consecutive cycles",
        "Source entropy drops below 1.0 (overreliance on single source)",
        "Self-citation ratio exceeds 30%"
      ]
    },
    "candidateDiscovery": {
      "allowedSources": ["karpathy", "dario-amodei", "sama", "demis-hassabis", "yann-lecun", "jim-fan", "emad-mostaque", "harrison-chase", "swyx", "simon-willison"],
      "blockedSources": [],
      "discoveryStrategy": "breadth_first",
      "maxCandidatesPerCycle": 50
    },
    "evidenceCapture": {
      "captureFields": ["post_text", "timestamp", "url", "reply_count", "repost_count", "linked_urls", "topic_tags"],
      "rawStoragePath": "raw/",
      "hashAlgorithm": "sha256",
      "deduplication": {
        "strategy": "exact",
        "semanticThreshold": 0.85
      }
    },
    "signalExtraction": {
      "dimensions": [
        {"name": "relevance", "description": "How relevant to current AI landscape", "scorer": "llm", "weight": 0.25},
        {"name": "novelty", "description": "New information vs rehash of known", "scorer": "llm", "weight": 0.20},
        {"name": "momentum", "description": "Is this gaining traction across sources", "scorer": "rule", "weight": 0.15},
        {"name": "contradiction", "description": "Does this contradict established patterns", "scorer": "llm", "weight": 0.15},
        {"name": "source_originality", "description": "Original thought vs echo/repost", "scorer": "llm", "weight": 0.15},
        {"name": "silence_anomaly", "description": "Unexpected absence or topic avoidance", "scorer": "hybrid", "weight": 0.10}
      ],
      "negativeEvidence": {
        "enabled": true,
        "silenceThreshold": 168,
        "baselinePeriod": 30,
        "absenceTypes": ["posting_gap", "topic_absence", "synchronized_silence", "behavioral_divergence"]
      }
    },
    "scoring": {
      "promotionThresholds": {
        "raw": {"minConfidence": 0.0, "minCorroboration": 0, "requiresHumanReview": false, "maxAge": 168},
        "working": {"minConfidence": 0.3, "minCorroboration": 0, "requiresHumanReview": false, "maxAge": 168},
        "verified": {"minConfidence": 0.5, "minCorroboration": 1, "requiresHumanReview": false, "maxAge": 336},
        "promoted": {"minConfidence": 0.7, "minCorroboration": 2, "requiresHumanReview": true, "maxAge": 720},
        "training": {"minConfidence": 0.8, "minCorroboration": 3, "requiresHumanReview": true, "maxAge": 2160},
        "locked": {"minConfidence": 0.9, "minCorroboration": 5, "requiresHumanReview": true, "maxAge": 8760}
      },
      "humanReviewTriggers": [
        "confidence_regression",
        "accusatory_claim",
        "high_contradiction_score",
        "synchronized_silence_detected"
      ]
    },
    "synthesis": {
      "outputArtifacts": [
        {"name": "signals.jsonl", "format": "jsonl", "path": "derived/signals.jsonl", "retention": "permanent"},
        {"name": "patterns.md", "format": "md", "path": "reports/patterns.md", "retention": "rolling", "rollingWindowDays": 30},
        {"name": "watchlist_changes.md", "format": "md", "path": "reports/watchlist-changes.md", "retention": "rolling", "rollingWindowDays": 7},
        {"name": "context_pack.md", "format": "md", "path": "context/pack.md", "retention": "permanent"},
        {"name": "silence_report.md", "format": "md", "path": "reports/silence-report.md", "retention": "rolling", "rollingWindowDays": 14}
      ],
      "crossCycleDelta": true
    },
    "memoryPromotion": {
      "promotionPolicy": {
        "rawToWorking": {"minConfidence": 0.3, "minCorroboration": 0, "requiresHumanReview": false, "maxAge": 168},
        "workingToVerified": {"minConfidence": 0.5, "minCorroboration": 1, "requiresHumanReview": false, "maxAge": 336},
        "verifiedToPromoted": {"minConfidence": 0.7, "minCorroboration": 2, "requiresHumanReview": true, "maxAge": 720},
        "promotedToTraining": {"minConfidence": 0.8, "minCorroboration": 3, "requiresHumanReview": true, "maxAge": 2160},
        "trainingToLocked": {"minConfidence": 0.9, "minCorroboration": 5, "requiresHumanReview": true, "maxAge": 8760}
      },
      "alternativeHypothesisRequired": true,
      "minConfidenceForPromotion": 0.3
    },
    "nextLoopPlanning": {
      "gapAnalysis": true,
      "priorityRebalancing": true,
      "iterationStrategy": "adaptive",
      "convergenceCriteria": {
        "metric": "new_evidence_count",
        "threshold": 3,
        "windowSize": 2
      }
    }
  },
  "control": {
    "maxIterations": 10,
    "checkpointInterval": 3,
    "completionPromise": "LOOP_COMPLETE",
    "earlyExitConditions": [
      {"condition": "source_entropy < 1.0", "action": "escalate", "message": "Source diversity too low — overreliance detected"},
      {"condition": "self_citation_ratio > 0.3", "action": "halt", "message": "Self-citation ratio exceeded 30%"},
      {"condition": "zero_evidence_cycles >= 3", "action": "halt", "message": "No new evidence for 3 consecutive cycles"}
    ],
    "backoffStrategy": "none",
    "backoffBaseMs": 0,
    "recursionGuards": {
      "maxSelfCitationRatio": 0.2,
      "sourceEntropyMinimum": 1.5,
      "hypothesisDiversityCheck": true
    }
  },
  "epistemicProgression": {
    "startStatus": "HYPOTHESIS",
    "targetStatus": "CORROBORATED",
    "transitions": []
  },
  "storagePath": "output/signal-curation/",
  "status": "draft",
  "createdAt": "2026-03-17T00:00:00Z",
  "createdBy": "christopherbailey"
}
```

- [ ] **Step 3: Write the schema reference doc**

Write `/Volumes/OWC drive/Dev/dossier/contracts/schema.md`:

```markdown
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
```

- [ ] **Step 4: Validate contract JSON is well-formed**

Run: `python3 -c "import json; json.load(open('/Volumes/OWC drive/Dev/dossier/contracts/signal-curation.json'))" && echo "Valid JSON"`
Expected: `Valid JSON`

- [ ] **Step 5: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add contracts/
git commit -m "feat: add first research loop contract (AI signal curation)"
```

### Task 4: Contract-Driven Ralph Loop Orchestrator

**Files:**
- Create: `/Volumes/OWC drive/Dev/dossier/loop/ralph-prompt-loop.md`
- Create: `/Volumes/OWC drive/Dev/dossier/loop/templates/progress-template.md`

- [ ] **Step 1: Create directory structure**

```bash
mkdir -p "/Volumes/OWC drive/Dev/dossier/loop/prompts"
mkdir -p "/Volumes/OWC drive/Dev/dossier/loop/templates"
```

- [ ] **Step 2: Write the progress template**

Write `/Volumes/OWC drive/Dev/dossier/loop/templates/progress-template.md`:

```markdown
# Research Loop: {{CONTRACT_ID}}
Started: {{TIMESTAMP}}
Cycle: 0

## Contract
- Name: {{CONTRACT_NAME}}
- Sources: {{SOURCE_COUNT}}
- Max iterations: {{MAX_ITERATIONS}}

## Phases (per cycle)
- [ ] P1 Goal Frame — validate scope and load contract
- [ ] P2 Candidate Discovery — find candidates from sources
- [ ] P3 Evidence Capture — collect and store raw evidence
- [ ] P4 Signal Extraction — score signals, detect absence
- [ ] P5 Scoring — apply promotion thresholds
- [ ] P6 Synthesis — generate cycle output artifacts
- [ ] P7 Memory Promotion — promote evidence across tiers
- [ ] P8 Next-Loop Planning — gap analysis, plan next cycle

## Anti-Recursion Guards
- Source entropy: (not yet computed)
- Self-citation ratio: (not yet computed)
- Hypothesis diversity: (not yet checked)

## Cycle Log
- (auto-populated during execution)

## Blockers
- None
```

- [ ] **Step 3: Write the contract-driven Ralph Loop orchestrator**

Write `/Volumes/OWC drive/Dev/dossier/loop/ralph-prompt-loop.md`:

```markdown
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
      python3 scripts/evidence_store.py insert <contract_id> <source_id> <content>
    - WebFetch may be unavailable — use Firecrawl as the primary web tool
```

## Iteration Logic

Each Ralph Loop iteration = one research cycle:

1. **Read state**: `cat ${storagePath}/PROGRESS.md`
2. **Check anti-recursion guards**:
   - Run: `python3 -c "from scripts.evidence_store import EvidenceStore; s = EvidenceStore(); print('entropy:', s.source_entropy('${CONTRACT_ID}')); print('self_cite:', s.self_citation_ratio('${CONTRACT_ID}'))"`
   - If entropy < contract.control.recursionGuards.sourceEntropyMinimum → ESCALATE
   - If self_citation > contract.control.recursionGuards.maxSelfCitationRatio → HALT
3. **Execute phases**: Run P1 through P8 sequentially
4. **Update PROGRESS.md**: Increment cycle count, record phase results
5. **Check checkpoint**: If cycle % contract.control.checkpointInterval == 0:
   - Log current state
   - If PromptSpeak MCP available: call `ps_hold_create` for human review
   - Otherwise: write checkpoint note in PROGRESS.md
6. **Check convergence**: If contract.phases.nextLoopPlanning.iterationStrategy == "convergence":
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

1. Run a final P6 Synthesis with `is_final: true` to generate the summary context pack
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
```

- [ ] **Step 4: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add loop/
git commit -m "feat: add contract-driven Ralph Loop orchestrator"
```

---

## Chunk 3: Phase Prompts (8 phases)

### Task 5: Phase Prompts P1-P4

**Files:**
- Create: `/Volumes/OWC drive/Dev/dossier/loop/prompts/p1-goal-frame.md`
- Create: `/Volumes/OWC drive/Dev/dossier/loop/prompts/p2-candidate-discovery.md`
- Create: `/Volumes/OWC drive/Dev/dossier/loop/prompts/p3-evidence-capture.md`
- Create: `/Volumes/OWC drive/Dev/dossier/loop/prompts/p4-signal-extraction.md`

- [ ] **Step 1: Write P1 — Goal Frame**

Write `/Volumes/OWC drive/Dev/dossier/loop/prompts/p1-goal-frame.md`:

```markdown
# Phase 1: Goal Frame

## Purpose
Load the contract, validate the research scope, and set up this cycle's execution context.

## Inputs
- Contract JSON (provided by orchestrator)
- PROGRESS.md (current state)
- Evidence store metrics (entropy, self-citation ratio)

## Process

1. **Parse contract** — extract goalFrame section
2. **Validate freshness** — check that the contract's freshnessHorizon hasn't been exceeded since last cycle
3. **Check failure conditions** — evaluate each condition in goalFrame.failureConditions:
   - "Zero new evidence collected for 3 consecutive cycles" → check PROGRESS.md cycle log
   - "Source entropy drops below 1.0" → check evidence store
   - "Self-citation ratio exceeds 30%" → check evidence store
4. **If any failure condition is true** → write failure report and HALT
5. **Output the cycle plan**: which sources to query, what to look for, freshness constraints

## Output
Write to: `${storagePath}/cycle-${CYCLE}/p1-goal-frame.md`

```markdown
# Cycle ${CYCLE} — Goal Frame

## Objective
${contract.phases.goalFrame.objective}

## Commander's Intent
${contract.phases.goalFrame.commandersIntent}

## Active Sources This Cycle
| Source | Tier | Trust | Domains | Fresh Until |
|--------|------|-------|---------|-------------|
(table from sourceUniverse, filtered by allowedSources)

## Anti-Recursion Status
- Source entropy: ${value} (minimum: ${guard})
- Self-citation ratio: ${value} (maximum: ${guard})
- Hypothesis diversity: ${status}

## Failure Conditions
(evaluate each, show pass/fail)

## Cycle Focus
(based on gap analysis from prior cycle's P8, or default to broad scan)
```
```

- [ ] **Step 2: Write P2 — Candidate Discovery**

Write `/Volumes/OWC drive/Dev/dossier/loop/prompts/p2-candidate-discovery.md`:

```markdown
# Phase 2: Candidate Discovery

## Purpose
Find candidate content from the source universe for this cycle.

## Inputs
- P1 output (active sources, cycle focus)
- Contract candidateDiscovery config
- Prior cycle's P8 output (if exists — gap analysis tells us what to look for)

## Process

1. **For each allowed source**, use Firecrawl to search for recent content:
   - Search: `"{source name}" site:x.com OR site:twitter.com` (for X/Twitter posts)
   - Search: `"{source name}" blog OR announcement` (for blog posts)
   - Respect maxCandidatesPerCycle cap
2. **Apply discoveryStrategy**:
   - `breadth_first`: equal attention across all sources
   - `depth_first`: focus on sources flagged by prior cycle's gap analysis
   - `adaptive`: prioritize sources with highest recent signal scores
3. **For each candidate found**, record:
   - URL
   - Source attribution
   - Snippet/summary
   - Timestamp (when posted)
   - Type (post, article, thread, announcement)

## Output
Write to: `${storagePath}/cycle-${CYCLE}/p2-candidates.jsonl`

One JSON object per line:
```json
{"source_id": "karpathy", "url": "https://...", "snippet": "...", "timestamp": "2026-03-...", "type": "post"}
```

Also write a summary to: `${storagePath}/cycle-${CYCLE}/p2-candidate-discovery.md`

## Important
- Use Firecrawl's search tool for discovery — it handles JS rendering and anti-bot
- Do NOT try to use X/Twitter API directly
- If a source has no recent content, that IS a finding — record it as a silence candidate
- Respect the contract's freshnessHorizon — skip content older than that
```

- [ ] **Step 3: Write P3 — Evidence Capture**

Write `/Volumes/OWC drive/Dev/dossier/loop/prompts/p3-evidence-capture.md`:

```markdown
# Phase 3: Evidence Capture

## Purpose
Collect full content for discovered candidates and store as raw evidence.

## Inputs
- P2 output (candidates JSONL)
- Contract evidenceCapture config
- Evidence store path

## Process

1. **For each candidate** in P2 output:
   a. Use Firecrawl to fetch the full content at the candidate URL
   b. Extract the fields specified in contract.phases.evidenceCapture.captureFields
   c. Compute content hash using the specified algorithm
   d. Check deduplication:
      - `exact`: hash match against evidence store
      - `semantic`: (future — for now, exact only)
      - `both`: check both
   e. If new: insert into evidence store as `raw` tier
   f. If duplicate: the store auto-increments corroboration_count

2. **For silence candidates** (sources with no recent content):
   a. Record a "silence event" in the evidence store with source_id and metadata noting the absence
   b. Include: last known post timestamp (from prior cycles), days silent, expected posting frequency

3. **Store raw artifacts** to `${storagePath}/raw/cycle-${CYCLE}/`

## Evidence Store Operations

Insert evidence:
```bash
cd "/Volumes/OWC drive/Dev/dossier"
python3 -c "
from scripts.evidence_store import EvidenceStore
store = EvidenceStore()
h = store.insert('${CONTRACT_ID}', '${SOURCE_ID}', '''${CONTENT}''', ${METADATA_JSON}, ${CYCLE})
print(f'hash={h}' if h else 'duplicate (corroboration incremented)')
store.close()
"
```

## Output
Write to: `${storagePath}/cycle-${CYCLE}/p3-evidence-capture.md`

Summary of:
- Total candidates processed
- New evidence inserted (count, by source)
- Duplicates found (corroboration bumps)
- Silence events recorded
- Any capture failures
```

- [ ] **Step 4: Write P4 — Signal Extraction**

Write `/Volumes/OWC drive/Dev/dossier/loop/prompts/p4-signal-extraction.md`:

```markdown
# Phase 4: Signal Extraction

## Purpose
Score each piece of new evidence across the contract's signal dimensions, and detect absence patterns.

## Inputs
- P3 output (evidence capture summary, hashes of new evidence)
- Contract signalExtraction config (dimensions + negative evidence config)
- Evidence store (query raw evidence from this cycle)

## Process

### Positive Signal Scoring

1. **Query this cycle's raw evidence** from the store
2. **For each evidence item**, score across all dimensions:
   - `relevance` (LLM): How relevant to current AI landscape? 0.0–1.0
   - `novelty` (LLM): New information vs known? 0.0–1.0
   - `momentum` (rule): Is this topic mentioned by 2+ sources this cycle? 0/1
   - `contradiction` (LLM): Does this contradict established patterns? 0.0–1.0
   - `source_originality` (LLM): Original thought vs echo? 0.0–1.0
   - `silence_anomaly` (hybrid): Unexpected absence signal? 0.0–1.0
3. **Compute composite score**: weighted sum of dimension scores
4. **Record signals** in the evidence store via `add_signal()`

### Negative Evidence Detection

1. **Check posting gaps**: For each source in sourceUniverse:
   - Query evidence store for most recent evidence from that source
   - If gap exceeds silenceThreshold → record as silence_anomaly
2. **Check topic absence**: Based on prior cycle's top topics:
   - If a source normally discusses topic X but didn't this cycle → flag
3. **Check synchronized silence**: If 3+ sources go quiet simultaneously:
   - Record as synchronized_silence event
4. **Check behavioral divergence**: Compare this cycle's topic distribution per source against baseline:
   - Significant shift → flag as behavioral_divergence

## Signal Store Operations

```bash
cd "/Volumes/OWC drive/Dev/dossier"
python3 -c "
from scripts.evidence_store import EvidenceStore
store = EvidenceStore()
store.add_signal(${EVIDENCE_ID}, '${CONTRACT_ID}', '${DIMENSION}', ${SCORE}, '${SCORER}', ${CYCLE})
store.close()
"
```

## Output
Write to: `${storagePath}/cycle-${CYCLE}/p4-signals.jsonl` (one signal per line)
Write to: `${storagePath}/cycle-${CYCLE}/p4-signal-extraction.md` (narrative summary)

The narrative should include:
- Top 5 highest-scoring evidence items
- Any contradiction signals
- Any silence/absence anomalies
- Cross-source convergence patterns
```

- [ ] **Step 5: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add loop/prompts/p1-goal-frame.md loop/prompts/p2-candidate-discovery.md loop/prompts/p3-evidence-capture.md loop/prompts/p4-signal-extraction.md
git commit -m "feat: add research loop phase prompts P1-P4"
```

### Task 6: Phase Prompts P5-P8

**Files:**
- Create: `/Volumes/OWC drive/Dev/dossier/loop/prompts/p5-scoring.md`
- Create: `/Volumes/OWC drive/Dev/dossier/loop/prompts/p6-synthesis.md`
- Create: `/Volumes/OWC drive/Dev/dossier/loop/prompts/p7-memory-promotion.md`
- Create: `/Volumes/OWC drive/Dev/dossier/loop/prompts/p8-next-loop-planning.md`

- [ ] **Step 1: Write P5 — Scoring**

Write `/Volumes/OWC drive/Dev/dossier/loop/prompts/p5-scoring.md`:

```markdown
# Phase 5: Scoring

## Purpose
Apply promotion thresholds from the contract to determine which evidence qualifies for tier advancement.

## Inputs
- P4 output (signals JSONL, signal extraction summary)
- Contract scoring config (promotionThresholds, humanReviewTriggers)
- Evidence store (current tier distribution)

## Process

1. **Query all evidence** for this contract at each tier
2. **For each evidence item**, check if it meets the promotion threshold for the next tier:
   - Confidence >= threshold.minConfidence?
   - Corroboration >= threshold.minCorroboration?
   - Age <= threshold.maxAge?
   - If threshold.requiresHumanReview → flag for review, do NOT auto-promote
3. **Check human review triggers**:
   - confidence_regression: any evidence whose confidence dropped since last cycle
   - accusatory_claim: any evidence tagged as ClaimType.ACCUSATORY
   - high_contradiction_score: contradiction signal > 0.7
   - synchronized_silence_detected: from P4's negative evidence
4. **Generate promotion candidates list** — evidence that qualifies for the next tier
5. **Generate hold list** — evidence that needs human review before promotion

## Output
Write to: `${storagePath}/cycle-${CYCLE}/p5-scoring.md`

Include:
- Promotion candidates (hash, current tier, target tier, scores)
- Hold items (hash, trigger reason, current confidence)
- Tier distribution (counts per tier)
- Any regression warnings
```

- [ ] **Step 2: Write P6 — Synthesis**

Write `/Volumes/OWC drive/Dev/dossier/loop/prompts/p6-synthesis.md`:

```markdown
# Phase 6: Synthesis

## Purpose
Generate this cycle's output artifacts as defined in the contract.

## Inputs
- All prior phase outputs (P1-P5) for this cycle
- Contract synthesis config (outputArtifacts, crossCycleDelta)
- Prior cycle's outputs (for delta comparison)

## Process

For each artifact in contract.phases.synthesis.outputArtifacts:

### signals.jsonl (derived/signals.jsonl)
- Append this cycle's scored signals to the rolling JSONL file
- Each line: `{"cycle": N, "evidence_hash": "...", "composite_score": 0.X, "dimensions": {...}, "timestamp": "..."}`

### patterns.md (reports/patterns.md)
- Identify recurring themes across this cycle's evidence
- Note cross-source convergence (same topic from 2+ sources)
- Flag emerging patterns vs decaying ones
- If crossCycleDelta: compare against prior cycle's patterns.md

### watchlist_changes.md (reports/watchlist-changes.md)
- Sources that changed behavior this cycle
- New high-scoring sources
- Sources that went silent
- Topic shifts per source

### context_pack.md (context/pack.md)
- **This is the key output** — a distilled context document suitable for injection into future Claude sessions
- Structure: top signals, key patterns, active hypotheses, source health
- Keep under 2000 tokens for context efficiency
- Include: what matters NOW, what changed, what to watch

### silence_report.md (reports/silence-report.md)
- All negative evidence from this cycle
- Silence durations per source
- Synchronized silence events
- Behavioral divergence flags

## Cross-Cycle Delta
If contract.phases.synthesis.crossCycleDelta is true:
- Read prior cycle's pattern report
- Highlight: new patterns, disappeared patterns, intensified patterns, reversed patterns
- Use prefix markers: [NEW], [GONE], [STRONGER], [WEAKER], [REVERSED]

## Output
Write all artifacts to their configured paths within `${storagePath}/`.
Write summary to: `${storagePath}/cycle-${CYCLE}/p6-synthesis.md`
```

- [ ] **Step 3: Write P7 — Memory Promotion**

Write `/Volumes/OWC drive/Dev/dossier/loop/prompts/p7-memory-promotion.md`:

```markdown
# Phase 7: Memory Promotion

## Purpose
Execute tier promotions identified in P5, applying the contract's promotion policy.

## Inputs
- P5 output (promotion candidates, hold items)
- Contract memoryPromotion config
- Evidence store

## Process

1. **Read P5's promotion candidates list**
2. **For each candidate**:
   a. If alternativeHypothesisRequired and no alternative logged → SKIP, note in output
   b. If target tier requires human review → DO NOT promote, add to hold queue
   c. Otherwise → execute promotion via evidence store:

```bash
cd "/Volumes/OWC drive/Dev/dossier"
python3 -c "
from scripts.evidence_store import EvidenceStore
store = EvidenceStore()
result = store.promote('${CONTRACT_ID}', '${HASH}', '${TARGET_TIER}', confidence=${CONFIDENCE})
print('promoted' if result else 'failed')
store.close()
"
```

3. **For hold items** (need human review):
   - If PromptSpeak MCP available: call `ps_hold_create` with evidence summary
   - Otherwise: write hold items to `${storagePath}/cycle-${CYCLE}/holds.json`

4. **Update evidence confidence** based on this cycle's signal scores:
   - New confidence = weighted average of signal dimension scores

## Alternative Hypothesis Logging
When alternativeHypothesisRequired is true, for each promoted evidence item, record:
- Main interpretation
- At least one alternative explanation
- Confidence in each
- Evidence count supporting each

Write to: `${storagePath}/cycle-${CYCLE}/p7-hypotheses.md`

## Output
Write to: `${storagePath}/cycle-${CYCLE}/p7-memory-promotion.md`

Include:
- Promotions executed (count, tier transitions)
- Promotions held for review (count, reasons)
- Promotions skipped (missing alternative hypothesis)
- Updated tier distribution
```

- [ ] **Step 4: Write P8 — Next-Loop Planning**

Write `/Volumes/OWC drive/Dev/dossier/loop/prompts/p8-next-loop-planning.md`:

```markdown
# Phase 8: Next-Loop Planning

## Purpose
Analyze this cycle's results and plan the next cycle's focus.

## Inputs
- All phase outputs from this cycle
- Contract nextLoopPlanning config
- Evidence store metrics (tier counts, entropy, self-citation)
- PROGRESS.md (cycle history)

## Process

### Gap Analysis (if enabled)
1. Which sources had zero evidence this cycle?
2. Which signal dimensions had consistently low scores?
3. Which hypotheses lack alternative explanations?
4. Which topics from prior cycles were not observed this cycle?
5. What evidence is approaching staleness (nearing maxAge)?

### Priority Rebalancing (if enabled)
1. Rank sources by average signal score this cycle
2. Rank sources by silence anomaly score (high = investigate more)
3. Suggest discoveryStrategy adjustment for next cycle:
   - If all sources covered evenly → maintain breadth_first
   - If specific sources showing high signal → suggest depth_first on those
   - If gaps identified → suggest adaptive focus on undersampled sources

### Convergence Check (if iterationStrategy == "convergence")
1. Read convergence metric (e.g., new_evidence_count) from this cycle
2. Compare against threshold
3. Track consecutive cycles meeting threshold
4. If windowSize consecutive cycles meet threshold → convergence achieved

### Anti-Recursion Assessment
1. Current source entropy
2. Current self-citation ratio
3. Hypothesis diversity (how many distinct interpretations exist)
4. Recommendation: safe to continue / caution / halt

## Output
Write to: `${storagePath}/cycle-${CYCLE}/p8-next-loop-planning.md`

Include:
- Gap analysis results
- Priority adjustments for next cycle
- Convergence status (met/not met, consecutive count)
- Anti-recursion assessment
- Recommended focus areas for next cycle
- Whether any earlyExitConditions are approaching

Also write: `${storagePath}/cycle-${CYCLE}/p8-next-tasks.json`
```json
{
  "cycle": N,
  "convergence_met": false,
  "consecutive_convergence_cycles": 0,
  "recommended_strategy": "breadth_first",
  "priority_sources": ["karpathy", "simon-willison"],
  "gaps": ["No data from demis-hassabis in 2 cycles"],
  "anti_recursion": {"entropy": 2.1, "self_cite": 0.05, "status": "healthy"},
  "exit_conditions_approaching": []
}
```
```

- [ ] **Step 5: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add loop/prompts/p5-scoring.md loop/prompts/p6-synthesis.md loop/prompts/p7-memory-promotion.md loop/prompts/p8-next-loop-planning.md
git commit -m "feat: add research loop phase prompts P5-P8"
```

---

## Chunk 4: Integration — CLAUDE.md + Dry Run

### Task 7: Update CLAUDE.md

**Files:**
- Modify: `/Volumes/OWC drive/Dev/dossier/CLAUDE.md`

- [ ] **Step 1: Add research loop section to CLAUDE.md**

Append to the existing CLAUDE.md:

```markdown

## Research Loop Mode

In addition to SaaS due diligence (the original mode), Dossier now supports contract-driven research loops.

### How To Run

```bash
# 1. Check/edit the contract
cat contracts/signal-curation.json

# 2. Run the loop via Ralph Loop
export CONTRACT=contracts/signal-curation.json
# /ralph-loop --max-iterations 10 --completion-promise "LOOP_COMPLETE"
# When prompted, read loop/ralph-prompt-loop.md and execute
```

### File Conventions
- Contracts: `contracts/*.json`
- Loop orchestrator: `loop/ralph-prompt-loop.md`
- Phase prompts: `loop/prompts/p{N}-{phase}.md`
- Evidence database: `data/evidence.db`
- Cycle outputs: `output/{contract-storage-path}/cycle-{N}/`
- Reports: `output/{contract-storage-path}/reports/`
- Context packs: `output/{contract-storage-path}/context/`

### Evidence Store
```bash
# Query evidence
python3 -c "from scripts.evidence_store import EvidenceStore; s = EvidenceStore(); print(s.tier_counts('RLC.DOSSIER.SIGNAL.001'))"

# Check anti-recursion
python3 -c "from scripts.evidence_store import EvidenceStore; s = EvidenceStore(); print('entropy:', s.source_entropy('RLC.DOSSIER.SIGNAL.001')); print('self_cite:', s.self_citation_ratio('RLC.DOSSIER.SIGNAL.001'))"
```

### PromptSpeak Governance
When PromptSpeak MCP tools are available:
- Frame validation at cycle start
- Hold gates at checkpoint intervals
- Audit logging on completion
- Frame: `⊕◇⟳▶α` (strict, technical, iterative, execute, primary)
```

- [ ] **Step 2: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add CLAUDE.md
git commit -m "docs: add research loop mode to CLAUDE.md"
```

### Task 8: Integration Dry Run

**Files:** None created — this is a validation task.

- [ ] **Step 1: Verify project structure**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
find . -not -path './.venv/*' -not -path './.git/*' -not -path './.pytest_cache/*' -not -path './output/*' -not -path './__pycache__/*' -not -path './dspy/__pycache__/*' -not -path './tests/__pycache__/*' -not -path './scripts/.venv/*' -type f | sort
```

Expected: All new files present alongside existing ones.

- [ ] **Step 2: Run evidence store tests**

```bash
cd "/Volumes/OWC drive/Dev/dossier" && python -m pytest tests/test_evidence_store.py -v
```

Expected: All tests PASS.

- [ ] **Step 3: Validate contract JSON**

```bash
python3 -c "
import json
c = json.load(open('/Volumes/OWC drive/Dev/dossier/contracts/signal-curation.json'))
print(f'Contract: {c[\"contractId\"]}')
print(f'Sources: {len(c[\"phases\"][\"goalFrame\"][\"sourceUniverse\"])}')
print(f'Dimensions: {len(c[\"phases\"][\"signalExtraction\"][\"dimensions\"])}')
print(f'Artifacts: {len(c[\"phases\"][\"synthesis\"][\"outputArtifacts\"])}')
print(f'Max iterations: {c[\"control\"][\"maxIterations\"]}')
weights = sum(d['weight'] for d in c['phases']['signalExtraction']['dimensions'])
print(f'Dimension weights sum: {weights} (should be 1.0)')
"
```

Expected:
```
Contract: RLC.DOSSIER.SIGNAL.001
Sources: 10
Dimensions: 6
Artifacts: 5
Max iterations: 10
Dimension weights sum: 1.0 (should be 1.0)
```

- [ ] **Step 4: Verify PromptSpeak types compile**

```bash
cd "/Volumes/OWC drive/Dev/promptspeak/mcp-server" && npx tsc --noEmit 2>&1; echo "EXIT: $?"
```

Expected: `EXIT: 0`

- [ ] **Step 5: Run PromptSpeak test suite**

```bash
cd "/Volumes/OWC drive/Dev/promptspeak/mcp-server" && npm test 2>&1 | tail -5
```

Expected: `829 passed`

- [ ] **Step 6: Final commit — add .gitignore for data/**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
echo "data/" >> .gitignore
git add .gitignore
git commit -m "chore: gitignore evidence database directory"
```

---

## Summary

| Task | Files | Tests | Commits |
|------|-------|-------|---------|
| 1. Evidence Store schema | `scripts/evidence_store.py`, `tests/test_evidence_store.py` | 2 | 1 |
| 2. Evidence Store CRUD | `tests/test_evidence_store.py` (extend) | 11 | 1 |
| 3. Contract JSON | `contracts/signal-curation.json`, `contracts/schema.md` | 0 | 1 |
| 4. Loop Orchestrator | `loop/ralph-prompt-loop.md`, `loop/templates/progress-template.md` | 0 | 1 |
| 5. Phase Prompts P1-P4 | `loop/prompts/p{1-4}*.md` | 0 | 1 |
| 6. Phase Prompts P5-P8 | `loop/prompts/p{5-8}*.md` | 0 | 1 |
| 7. CLAUDE.md update | `CLAUDE.md` | 0 | 1 |
| 8. Integration dry run | None | validation | 1 |

**Total: 14 new files, 1 modified file, 13 tests, 8 commits**

## What This Does NOT Include (Deferred)

- `ps_research_loop_validate` MCP tool — future PromptSpeak tool for contract validation
- Dossier Loop skill (`/dossier-loop`) — skill wrapper for launching from any session
- Semantic dedup (requires Pinecone or local embeddings)
- X API integration (uses Firecrawl web search instead)
- launchd scheduling (manual launch via Ralph Loop for now)
- Training data export pipeline (Phase 5+ of evidence tiers)
