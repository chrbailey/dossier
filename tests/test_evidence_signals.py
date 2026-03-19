"""Tests for signals, cycles, and batch scoring in EvidenceStore."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture
def db_path(tmp_path):
    return tmp_path / "test.db"


@pytest.fixture
def store(db_path):
    from scripts.evidence_store import EvidenceStore

    s = EvidenceStore(db_path)
    yield s
    s.close()


def _insert(store, contract_id="RLC.001", source="src", content="content"):
    """Helper: insert evidence and return (hash, row)."""
    h = store.insert(contract_id, source, content)
    row = store.get(h)
    return h, row


# ---------------------------------------------------------------------------
# 1. add_signal basics
# ---------------------------------------------------------------------------

class TestAddSignal:
    def test_returns_positive_id(self, store):
        _, row = _insert(store)
        sig_id = store.add_signal(row["id"], "RLC.001", "relevance", 0.8, "llm", 1)
        assert sig_id > 0

    def test_stores_correct_dimension(self, store):
        _, row = _insert(store)
        store.add_signal(row["id"], "RLC.001", "novelty", 0.7, "llm", 1)
        signals = store.query_signals("RLC.001", dimension="novelty")
        assert len(signals) == 1
        assert signals[0]["dimension"] == "novelty"

    def test_stores_correct_score(self, store):
        _, row = _insert(store)
        store.add_signal(row["id"], "RLC.001", "relevance", 0.85, "llm", 1)
        signals = store.query_signals("RLC.001")
        assert signals[0]["score"] == 0.85

    def test_stores_correct_scorer(self, store):
        _, row = _insert(store)
        store.add_signal(row["id"], "RLC.001", "relevance", 0.5, "rule", 1)
        signals = store.query_signals("RLC.001")
        assert signals[0]["scorer"] == "rule"

    def test_multiple_signals_per_evidence(self, store):
        _, row = _insert(store)
        id1 = store.add_signal(row["id"], "RLC.001", "relevance", 0.8, "llm", 1)
        id2 = store.add_signal(row["id"], "RLC.001", "novelty", 0.6, "llm", 1)
        id3 = store.add_signal(row["id"], "RLC.001", "depth", 0.9, "llm", 1)
        assert id1 < id2 < id3
        signals = store.query_signals("RLC.001", evidence_id=row["id"])
        assert len(signals) == 3


# ---------------------------------------------------------------------------
# 2. score_evidence batch
# ---------------------------------------------------------------------------

class TestScoreEvidenceBatch:
    def test_scores_six_dimensions(self, store):
        h, _ = _insert(store)
        dims = {
            "relevance": 0.9, "novelty": 0.7, "depth": 0.8,
            "accuracy": 0.6, "sourcing": 0.5, "actionability": 0.4,
        }
        composite = store.score_evidence("RLC.001", h, dims, "llm", 1)
        assert composite is not None

    def test_returns_composite_average(self, store):
        h, _ = _insert(store)
        dims = {
            "relevance": 0.9, "novelty": 0.7, "depth": 0.8,
            "accuracy": 0.6, "sourcing": 0.5, "actionability": 0.4,
        }
        composite = store.score_evidence("RLC.001", h, dims, "llm", 1)
        expected = round(sum(dims.values()) / len(dims), 3)
        assert composite == expected

    def test_updates_evidence_confidence(self, store):
        h, _ = _insert(store)
        composite = store.score_evidence(
            "RLC.001", h, {"a": 0.8, "b": 0.6}, "llm", 1,
        )
        row = store.get(h)
        assert row["confidence"] == composite

    def test_returns_none_for_nonexistent_hash(self, store):
        result = store.score_evidence("RLC.001", "badhash", {"a": 1.0}, "llm", 1)
        assert result is None

    def test_returns_none_for_wrong_contract(self, store):
        h, _ = _insert(store, contract_id="RLC.001")
        result = store.score_evidence("RLC.999", h, {"a": 1.0}, "llm", 1)
        assert result is None


# ---------------------------------------------------------------------------
# 3. score_evidence math
# ---------------------------------------------------------------------------

class TestScoreEvidenceMath:
    def test_two_dims_average(self, store):
        h, _ = _insert(store)
        composite = store.score_evidence(
            "RLC.001", h, {"a": 1.0, "b": 0.0}, "llm", 1,
        )
        assert composite == 0.5

    def test_three_dims_average(self, store):
        h, _ = _insert(store)
        composite = store.score_evidence(
            "RLC.001", h, {"a": 0.8, "b": 0.6, "c": 0.4}, "llm", 1,
        )
        assert composite == 0.6

    def test_single_dimension_returns_that_score(self, store):
        h, _ = _insert(store)
        composite = store.score_evidence(
            "RLC.001", h, {"only": 0.73}, "llm", 1,
        )
        assert composite == 0.73

    def test_empty_scores_returns_zero(self, store):
        h, _ = _insert(store)
        composite = store.score_evidence("RLC.001", h, {}, "llm", 1)
        assert composite == 0.0


# ---------------------------------------------------------------------------
# 4. score_evidence creates signals
# ---------------------------------------------------------------------------

class TestScoreEvidenceCreatesSignals:
    def test_signals_created_for_each_dimension(self, store):
        h, row = _insert(store)
        dims = {"relevance": 0.9, "novelty": 0.7, "depth": 0.8}
        store.score_evidence("RLC.001", h, dims, "llm", 1)
        signals = store.query_signals("RLC.001", evidence_id=row["id"])
        assert len(signals) == 3
        found_dims = {s["dimension"] for s in signals}
        assert found_dims == {"relevance", "novelty", "depth"}

    def test_signal_scores_match_input(self, store):
        h, row = _insert(store)
        dims = {"relevance": 0.9, "novelty": 0.7}
        store.score_evidence("RLC.001", h, dims, "hybrid", 1)
        signals = store.query_signals("RLC.001", evidence_id=row["id"])
        score_map = {s["dimension"]: s["score"] for s in signals}
        assert score_map["relevance"] == 0.9
        assert score_map["novelty"] == 0.7


# ---------------------------------------------------------------------------
# 5. query_signals filters
# ---------------------------------------------------------------------------

class TestQuerySignals:
    def _seed(self, store):
        """Seed two pieces of evidence with signals across 2 cycles."""
        h1, r1 = _insert(store, content="evidence-a")
        h2, r2 = _insert(store, content="evidence-b")
        store.add_signal(r1["id"], "RLC.001", "relevance", 0.9, "llm", 1)
        store.add_signal(r1["id"], "RLC.001", "novelty", 0.7, "llm", 1)
        store.add_signal(r2["id"], "RLC.001", "relevance", 0.6, "llm", 2)
        store.add_signal(r2["id"], "RLC.001", "depth", 0.8, "rule", 2)
        return r1, r2

    def test_filter_by_cycle_number(self, store):
        self._seed(store)
        results = store.query_signals("RLC.001", cycle_number=1)
        assert len(results) == 2
        assert all(s["cycle_number"] == 1 for s in results)

    def test_filter_by_dimension(self, store):
        self._seed(store)
        results = store.query_signals("RLC.001", dimension="relevance")
        assert len(results) == 2
        assert all(s["dimension"] == "relevance" for s in results)

    def test_filter_by_evidence_id(self, store):
        r1, _ = self._seed(store)
        results = store.query_signals("RLC.001", evidence_id=r1["id"])
        assert len(results) == 2

    def test_combined_filters(self, store):
        r1, _ = self._seed(store)
        results = store.query_signals(
            "RLC.001", cycle_number=1, dimension="relevance", evidence_id=r1["id"],
        )
        assert len(results) == 1
        assert results[0]["score"] == 0.9

    def test_empty_results(self, store):
        results = store.query_signals("RLC.NONEXISTENT")
        assert results == []


# ---------------------------------------------------------------------------
# 6. record_cycle
# ---------------------------------------------------------------------------

class TestRecordCycle:
    def test_returns_positive_id(self, store):
        cid = store.record_cycle("RLC.001", 1, "p1-goal-frame")
        assert cid > 0

    def test_stores_phase(self, store):
        cid = store.record_cycle("RLC.001", 1, "p3-search")
        row = store.conn.execute(
            "SELECT * FROM cycles WHERE id = ?", (cid,),
        ).fetchone()
        assert row["phase"] == "p3-search"

    def test_stores_status(self, store):
        cid = store.record_cycle("RLC.001", 1, "p1-goal-frame", status="running")
        row = store.conn.execute(
            "SELECT * FROM cycles WHERE id = ?", (cid,),
        ).fetchone()
        assert row["status"] == "running"

    def test_started_at_is_set(self, store):
        cid = store.record_cycle("RLC.001", 1, "p1-goal-frame")
        row = store.conn.execute(
            "SELECT * FROM cycles WHERE id = ?", (cid,),
        ).fetchone()
        assert row["started_at"] is not None


# ---------------------------------------------------------------------------
# 7. complete_cycle
# ---------------------------------------------------------------------------

class TestCompleteCycle:
    def test_sets_completed_at(self, store):
        cid = store.record_cycle("RLC.001", 1, "p1-goal-frame")
        store.complete_cycle(cid, "completed")
        row = store.conn.execute(
            "SELECT * FROM cycles WHERE id = ?", (cid,),
        ).fetchone()
        assert row["completed_at"] is not None

    def test_updates_status(self, store):
        cid = store.record_cycle("RLC.001", 1, "p1-goal-frame")
        store.complete_cycle(cid, "failed")
        row = store.conn.execute(
            "SELECT * FROM cycles WHERE id = ?", (cid,),
        ).fetchone()
        assert row["status"] == "failed"

    def test_stores_notes(self, store):
        cid = store.record_cycle("RLC.001", 1, "p1-goal-frame")
        store.complete_cycle(cid, "completed", notes="Phase ran cleanly")
        row = store.conn.execute(
            "SELECT * FROM cycles WHERE id = ?", (cid,),
        ).fetchone()
        assert row["notes"] == "Phase ran cleanly"

    def test_notes_can_be_none(self, store):
        cid = store.record_cycle("RLC.001", 1, "p1-goal-frame")
        store.complete_cycle(cid, "completed")
        row = store.conn.execute(
            "SELECT * FROM cycles WHERE id = ?", (cid,),
        ).fetchone()
        assert row["notes"] is None


# ---------------------------------------------------------------------------
# 8. Cycle lifecycle: record -> complete for all 8 phases
# ---------------------------------------------------------------------------

PHASES = [
    "p1-goal-frame",
    "p2-plan",
    "p3-search",
    "p4-extract",
    "p5-score",
    "p6-synthesize",
    "p7-review",
    "p8-publish",
]


class TestCycleLifecycle:
    def test_all_eight_phases_in_sequence(self, store):
        cycle_ids = []
        for phase in PHASES:
            cid = store.record_cycle("RLC.001", 1, phase)
            cycle_ids.append(cid)
            store.complete_cycle(cid, "completed", notes=f"Done: {phase}")

        assert len(cycle_ids) == 8
        # IDs should be strictly increasing
        for i in range(len(cycle_ids) - 1):
            assert cycle_ids[i] < cycle_ids[i + 1]

    def test_completed_phases_have_timestamps(self, store):
        for phase in PHASES:
            cid = store.record_cycle("RLC.001", 1, phase)
            store.complete_cycle(cid, "completed")
            row = store.conn.execute(
                "SELECT * FROM cycles WHERE id = ?", (cid,),
            ).fetchone()
            assert row["started_at"] is not None
            assert row["completed_at"] is not None


# ---------------------------------------------------------------------------
# 9. Multiple cycles
# ---------------------------------------------------------------------------

class TestMultipleCycles:
    def test_record_cycle_1_and_2_independently(self, store):
        c1 = store.record_cycle("RLC.001", 1, "p1-goal-frame")
        c2 = store.record_cycle("RLC.001", 2, "p1-goal-frame")
        assert c1 != c2

        r1 = store.conn.execute(
            "SELECT * FROM cycles WHERE id = ?", (c1,),
        ).fetchone()
        r2 = store.conn.execute(
            "SELECT * FROM cycles WHERE id = ?", (c2,),
        ).fetchone()
        assert r1["cycle_number"] == 1
        assert r2["cycle_number"] == 2


# ---------------------------------------------------------------------------
# 10. Signal across cycles
# ---------------------------------------------------------------------------

class TestSignalAcrossCycles:
    def test_same_evidence_scored_in_two_cycles(self, store):
        h, row = _insert(store)
        store.add_signal(row["id"], "RLC.001", "relevance", 0.7, "llm", 1)
        store.add_signal(row["id"], "RLC.001", "relevance", 0.9, "llm", 2)

        c1 = store.query_signals("RLC.001", cycle_number=1)
        c2 = store.query_signals("RLC.001", cycle_number=2)
        assert len(c1) == 1
        assert c1[0]["score"] == 0.7
        assert len(c2) == 1
        assert c2[0]["score"] == 0.9

    def test_query_all_cycles_returns_both(self, store):
        h, row = _insert(store)
        store.add_signal(row["id"], "RLC.001", "relevance", 0.7, "llm", 1)
        store.add_signal(row["id"], "RLC.001", "relevance", 0.9, "llm", 2)

        all_signals = store.query_signals("RLC.001", dimension="relevance")
        assert len(all_signals) == 2


# ---------------------------------------------------------------------------
# 11. Composite score updates confidence
# ---------------------------------------------------------------------------

class TestCompositeUpdatesConfidence:
    def test_confidence_matches_composite(self, store):
        h, _ = _insert(store)
        # Before scoring, confidence is default 0.0
        assert store.get(h)["confidence"] == 0.0

        composite = store.score_evidence(
            "RLC.001", h, {"a": 0.8, "b": 0.6, "c": 0.4}, "llm", 1,
        )
        row = store.get(h)
        assert row["confidence"] == composite
        assert row["confidence"] == 0.6

    def test_updated_at_is_set_after_scoring(self, store):
        h, _ = _insert(store)
        store.score_evidence("RLC.001", h, {"a": 1.0}, "llm", 1)
        row = store.get(h)
        assert row["updated_at"] is not None

    def test_rescore_overwrites_confidence(self, store):
        h, _ = _insert(store)
        store.score_evidence("RLC.001", h, {"a": 0.4}, "llm", 1)
        assert store.get(h)["confidence"] == 0.4
        store.score_evidence("RLC.001", h, {"a": 1.0}, "llm", 2)
        assert store.get(h)["confidence"] == 1.0


# ---------------------------------------------------------------------------
# 12. Edge cases
# ---------------------------------------------------------------------------

class TestEdgeCases:
    def test_signal_created_at_is_populated(self, store):
        _, row = _insert(store)
        store.add_signal(row["id"], "RLC.001", "relevance", 0.5, "llm", 1)
        signals = store.query_signals("RLC.001")
        assert signals[0]["created_at"] is not None
        assert "Z" in signals[0]["created_at"] or "T" in signals[0]["created_at"]

    def test_default_cycle_status_is_pending(self, store):
        cid = store.record_cycle("RLC.001", 1, "p1-goal-frame")
        row = store.conn.execute(
            "SELECT * FROM cycles WHERE id = ?", (cid,),
        ).fetchone()
        assert row["status"] == "pending"

    def test_query_signals_wrong_contract_returns_empty(self, store):
        _, row = _insert(store, contract_id="RLC.001")
        store.add_signal(row["id"], "RLC.001", "relevance", 0.8, "llm", 1)
        results = store.query_signals("RLC.999")
        assert results == []
