"""Tests for the evidence store."""
from __future__ import annotations

import json
import sqlite3
import tempfile
from pathlib import Path

import pytest

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture
def db_path(tmp_path):
    """Provide a temporary database path."""
    return tmp_path / "test_evidence.db"


@pytest.fixture
def store(db_path):
    """Create a fresh evidence store."""
    from scripts.evidence_store import EvidenceStore
    s = EvidenceStore(db_path)
    yield s
    s.close()


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
        store.insert("RLC.001", "only-source", "b")
        # same source, different content — both inserted, entropy = 0
        assert store.source_entropy("RLC.001") == 0.0

    def test_source_entropy_multiple_sources(self, store):
        store.insert("RLC.001", "src-1", "a")
        store.insert("RLC.001", "src-2", "b")
        entropy = store.source_entropy("RLC.001")
        assert entropy == 1.0  # 2 equal sources → entropy = 1.0

    def test_self_citation_ratio(self, store):
        store.insert("RLC.001", "external-1", "a")
        store.insert("RLC.001", "external-2", "b")
        store.insert("RLC.001", "self:prior-cycle", "c")
        ratio = store.self_citation_ratio("RLC.001")
        assert abs(ratio - 0.333) < 0.01

    def test_self_citation_ratio_empty(self, store):
        assert store.self_citation_ratio("RLC.001") == 0.0


class TestSignals:
    def test_add_signal(self, store):
        h = store.insert("RLC.001", "src", "content")
        row = store.get(h)
        sig_id = store.add_signal(row["id"], "RLC.001", "relevance", 0.8, "llm", 1)
        assert sig_id > 0

    def test_multiple_signals_per_evidence(self, store):
        h = store.insert("RLC.001", "src", "content")
        row = store.get(h)
        id1 = store.add_signal(row["id"], "RLC.001", "relevance", 0.8, "llm", 1)
        id2 = store.add_signal(row["id"], "RLC.001", "novelty", 0.6, "llm", 1)
        assert id2 > id1


class TestCycles:
    def test_record_cycle(self, store):
        cid = store.record_cycle("RLC.001", 1, "p1-goal-frame")
        assert cid > 0

    def test_complete_cycle(self, store):
        cid = store.record_cycle("RLC.001", 1, "p1-goal-frame")
        store.complete_cycle(cid, "completed", notes="All good")
        row = store.conn.execute(
            "SELECT * FROM cycles WHERE id = ?", (cid,)
        ).fetchone()
        assert row["status"] == "completed"
        assert row["notes"] == "All good"
        assert row["completed_at"] is not None


class TestTierCounts:
    def test_tier_counts_empty(self, store):
        counts = store.tier_counts("RLC.001")
        assert counts == {}

    def test_tier_counts_after_inserts(self, store):
        h1 = store.insert("RLC.001", "src-a", "content-a")
        store.insert("RLC.001", "src-b", "content-b")
        store.promote("RLC.001", h1, "working")
        counts = store.tier_counts("RLC.001")
        assert counts["raw"] == 1
        assert counts["working"] == 1
