"""Tests for anti-recursion guards and silence evidence in EvidenceStore."""
from __future__ import annotations

import json
import math
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


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _insert_sources(store, contract_id, source_counts, cycle=0):
    """Insert evidence with a given distribution of sources.

    source_counts: dict mapping source_id to number of items.
    Each item gets unique content so there are no duplicates.
    """
    seq = 0
    for src, count in source_counts.items():
        for _ in range(count):
            store.insert(contract_id, src, f"content-{src}-{seq}", cycle_number=cycle)
            seq += 1


def _insert_silence(store, contract_id, source_id, days_silent=14,
                    confidence=0.7, last_seen="2026-03-01", cycle=0):
    """Insert a silence evidence event."""
    meta = {
        "type": "silence",
        "last_seen": last_seen,
        "days_silent": days_silent,
        "confidence": confidence,
    }
    return store.insert(
        contract_id, source_id, f"silence-{source_id}-{days_silent}d",
        metadata=meta, cycle_number=cycle,
    )


# ===========================================================================
# Source Entropy
# ===========================================================================

class TestSourceEntropy:
    def test_empty_store_returns_zero(self, store):
        assert store.source_entropy("RLC.001") == 0.0

    def test_one_source_one_item(self, store):
        store.insert("RLC.001", "src-a", "item-1")
        assert store.source_entropy("RLC.001") == 0.0

    def test_one_source_five_items(self, store):
        _insert_sources(store, "RLC.001", {"src-a": 5})
        assert store.source_entropy("RLC.001") == 0.0

    def test_two_sources_equal(self, store):
        _insert_sources(store, "RLC.001", {"src-a": 1, "src-b": 1})
        assert store.source_entropy("RLC.001") == 1.0

    def test_three_sources_equal(self, store):
        _insert_sources(store, "RLC.001", {"src-a": 3, "src-b": 3, "src-c": 3})
        entropy = store.source_entropy("RLC.001")
        assert abs(entropy - math.log2(3)) < 0.01  # ~1.585

    def test_four_sources_equal(self, store):
        _insert_sources(store, "RLC.001", {f"src-{i}": 2 for i in range(4)})
        assert store.source_entropy("RLC.001") == 2.0

    def test_ten_sources_equal(self, store):
        _insert_sources(store, "RLC.001", {f"src-{i}": 1 for i in range(10)})
        entropy = store.source_entropy("RLC.001")
        assert abs(entropy - math.log2(10)) < 0.01  # ~3.322

    def test_two_sources_unequal_9_1(self, store):
        _insert_sources(store, "RLC.001", {"dominant": 9, "rare": 1})
        entropy = store.source_entropy("RLC.001")
        # Highly skewed → low entropy, well below 1.0
        assert 0.0 < entropy < 0.6

    def test_two_sources_slightly_unequal_6_4(self, store):
        _insert_sources(store, "RLC.001", {"src-a": 6, "src-b": 4})
        entropy = store.source_entropy("RLC.001")
        assert 0.9 < entropy < 1.0

    def test_entropy_scoped_to_contract(self, store):
        _insert_sources(store, "RLC.001", {"src-a": 1})
        _insert_sources(store, "RLC.002", {"src-a": 5, "src-b": 5, "src-c": 5})
        # RLC.001 has only one source → entropy 0
        assert store.source_entropy("RLC.001") == 0.0
        # RLC.002 has 3 equal sources → entropy ~1.585
        assert abs(store.source_entropy("RLC.002") - math.log2(3)) < 0.01


# ===========================================================================
# Self-Citation Ratio
# ===========================================================================

class TestSelfCitationRatio:
    def test_empty_store_returns_zero(self, store):
        assert store.self_citation_ratio("RLC.001") == 0.0

    def test_all_external_returns_zero(self, store):
        _insert_sources(store, "RLC.001", {"ext-1": 3, "ext-2": 2})
        assert store.self_citation_ratio("RLC.001") == 0.0

    def test_all_self_cited_returns_one(self, store):
        _insert_sources(store, "RLC.001", {"self:prior": 5})
        assert store.self_citation_ratio("RLC.001") == 1.0

    def test_half_self_cited(self, store):
        _insert_sources(store, "RLC.001", {"ext-1": 5, "self:prior": 5})
        assert store.self_citation_ratio("RLC.001") == 0.5

    def test_one_self_of_ten(self, store):
        _insert_sources(store, "RLC.001", {"ext-1": 9, "self:prior": 1})
        assert store.self_citation_ratio("RLC.001") == 0.1

    def test_different_self_prefixes_all_count(self, store):
        _insert_sources(store, "RLC.001", {
            "self:prior": 1,
            "self:cycle-2": 1,
            "self:summary": 1,
            "ext-1": 3,
        })
        assert store.self_citation_ratio("RLC.001") == 0.5

    def test_myself_does_not_count(self, store):
        _insert_sources(store, "RLC.001", {"myself": 3, "ext-1": 7})
        # "myself" does NOT start with "self:" so ratio is 0
        assert store.self_citation_ratio("RLC.001") == 0.0

    def test_ratio_scoped_to_contract(self, store):
        _insert_sources(store, "RLC.001", {"ext-1": 10})
        _insert_sources(store, "RLC.002", {"self:prior": 10})
        assert store.self_citation_ratio("RLC.001") == 0.0
        assert store.self_citation_ratio("RLC.002") == 1.0


# ===========================================================================
# Silence Events
# ===========================================================================

class TestSilenceEvents:
    def test_no_silence_events_returns_empty(self, store):
        store.insert("RLC.001", "src-1", "normal content")
        assert store.get_silence_events("RLC.001") == []

    def test_insert_and_retrieve_silence_event(self, store):
        _insert_silence(store, "RLC.001", "analyst-feed", days_silent=14)
        events = store.get_silence_events("RLC.001")
        assert len(events) == 1
        meta = json.loads(events[0]["metadata"])
        assert meta["type"] == "silence"
        assert meta["days_silent"] == 14

    def test_silence_low_confidence_preserved(self, store):
        _insert_silence(store, "RLC.001", "weak-signal", confidence=0.3)
        events = store.get_silence_events("RLC.001")
        meta = json.loads(events[0]["metadata"])
        assert meta["confidence"] == 0.3

    def test_filter_by_cycle_number(self, store):
        _insert_silence(store, "RLC.001", "src-a", cycle=1)
        _insert_silence(store, "RLC.001", "src-b", cycle=2)
        events_c1 = store.get_silence_events("RLC.001", cycle_number=1)
        events_c2 = store.get_silence_events("RLC.001", cycle_number=2)
        assert len(events_c1) == 1
        assert len(events_c2) == 1

    def test_regular_evidence_excluded(self, store):
        store.insert("RLC.001", "src-1", "normal stuff", {"key": "val"})
        _insert_silence(store, "RLC.001", "src-1", days_silent=7)
        events = store.get_silence_events("RLC.001")
        assert len(events) == 1
        meta = json.loads(events[0]["metadata"])
        assert meta["type"] == "silence"

    def test_multiple_silence_events_across_cycles(self, store):
        _insert_silence(store, "RLC.001", "src-a", days_silent=7, cycle=1)
        _insert_silence(store, "RLC.001", "src-a", days_silent=14, cycle=2)
        _insert_silence(store, "RLC.001", "src-a", days_silent=21, cycle=3)
        events = store.get_silence_events("RLC.001")
        assert len(events) == 3

    def test_silence_has_standard_evidence_fields(self, store):
        _insert_silence(store, "RLC.001", "src-a")
        events = store.get_silence_events("RLC.001")
        ev = events[0]
        assert "id" in ev
        assert "hash" in ev
        assert "tier" in ev
        assert "contract_id" in ev
        assert "source_id" in ev
        assert "content" in ev
        assert "created_at" in ev
        assert ev["tier"] == "raw"
        assert ev["contract_id"] == "RLC.001"

    def test_silence_can_be_promoted(self, store):
        h = _insert_silence(store, "RLC.001", "src-a")
        assert h is not None
        ok = store.promote("RLC.001", h, "working", confidence=0.5)
        assert ok
        ev = store.get(h)
        assert ev["tier"] == "working"

    def test_silence_confidence_tracks_search_vs_real(self, store):
        _insert_silence(store, "RLC.001", "search-artifact", confidence=0.2)
        _insert_silence(store, "RLC.001", "confirmed-quiet", confidence=0.9)
        events = store.get_silence_events("RLC.001")
        confidences = sorted(
            json.loads(e["metadata"])["confidence"] for e in events
        )
        assert confidences == [0.2, 0.9]

    def test_mixed_silence_and_regular_only_returns_silence(self, store):
        store.insert("RLC.001", "src-1", "regular-a")
        store.insert("RLC.001", "src-2", "regular-b")
        _insert_silence(store, "RLC.001", "src-3", days_silent=10)
        store.insert("RLC.001", "src-4", "regular-c", {"notes": "not silence"})
        _insert_silence(store, "RLC.001", "src-5", days_silent=20)
        events = store.get_silence_events("RLC.001")
        assert len(events) == 2
        for ev in events:
            meta = json.loads(ev["metadata"])
            assert meta["type"] == "silence"


# ===========================================================================
# Threshold Checking (integration)
# ===========================================================================

class TestThresholdIntegration:
    def test_low_entropy_triggers_guard(self, store):
        """A single dominant source keeps entropy below 1.5."""
        _insert_sources(store, "RLC.001", {"dominant": 20, "minor": 1})
        entropy = store.source_entropy("RLC.001")
        assert entropy < 1.5

    def test_high_self_citation_triggers_guard(self, store):
        """More than 20% self-citation should trigger the guard."""
        _insert_sources(store, "RLC.001", {"ext-1": 7, "self:prior": 3})
        ratio = store.self_citation_ratio("RLC.001")
        assert ratio > 0.2

    def test_ten_source_fifty_item_high_entropy(self, store):
        """Balanced 10-source store has entropy above 3.0."""
        _insert_sources(store, "RLC.001", {f"src-{i}": 5 for i in range(10)})
        entropy = store.source_entropy("RLC.001")
        assert entropy > 3.0
        assert abs(entropy - math.log2(10)) < 0.01

    def test_gradual_self_citation_increase(self, store):
        """Adding self-citations progressively increases the ratio."""
        # Start with 10 external
        _insert_sources(store, "RLC.001", {"ext-1": 10})
        assert store.self_citation_ratio("RLC.001") == 0.0

        # Add 2 self-citations: 2/12
        _insert_sources(store, "RLC.001", {"self:c1": 2})
        r1 = store.self_citation_ratio("RLC.001")
        assert abs(r1 - 2 / 12) < 0.01

        # Add 3 more self-citations: 5/15
        _insert_sources(store, "RLC.001", {"self:c2": 3})
        r2 = store.self_citation_ratio("RLC.001")
        assert abs(r2 - 5 / 15) < 0.01

        # Ratio increased
        assert r2 > r1

    def test_entropy_and_ratio_independent(self, store):
        """Self-citations affect ratio but also affect entropy via source distribution."""
        _insert_sources(store, "RLC.001", {
            "ext-a": 5, "ext-b": 5, "ext-c": 5, "self:prior": 5,
        })
        # 4 equal sources → entropy = 2.0
        assert store.source_entropy("RLC.001") == 2.0
        # 5 out of 20 are self → ratio = 0.25
        assert store.self_citation_ratio("RLC.001") == 0.25

    def test_silence_does_not_affect_entropy_source(self, store):
        """Silence events use the same source_id mechanism and affect entropy."""
        _insert_sources(store, "RLC.001", {"ext-a": 5, "ext-b": 5})
        entropy_before = store.source_entropy("RLC.001")
        _insert_silence(store, "RLC.001", "silence-watcher", days_silent=14)
        entropy_after = store.source_entropy("RLC.001")
        # Adding a third source increases entropy
        assert entropy_after > entropy_before

    def test_silence_events_counted_in_self_citation_if_self_source(self, store):
        """Silence events from self: sources count toward self-citation ratio."""
        _insert_sources(store, "RLC.001", {"ext-1": 9})
        _insert_silence(store, "RLC.001", "self:monitor", days_silent=7)
        ratio = store.self_citation_ratio("RLC.001")
        assert ratio == 0.1

    def test_single_source_entropy_below_guard(self, store):
        """Even 50 items from one source has zero entropy."""
        _insert_sources(store, "RLC.001", {"mono-src": 50})
        assert store.source_entropy("RLC.001") == 0.0
        assert store.self_citation_ratio("RLC.001") == 0.0

    def test_both_guards_pass_healthy_store(self, store):
        """A well-sourced store passes both guards comfortably."""
        _insert_sources(store, "RLC.001", {f"feed-{i}": 4 for i in range(8)})
        assert store.source_entropy("RLC.001") >= 1.5
        assert store.self_citation_ratio("RLC.001") <= 0.2

    def test_both_guards_fail_degenerate_store(self, store):
        """A store dominated by self-citations fails both guards."""
        _insert_sources(store, "RLC.001", {"self:loop": 18, "ext-1": 2})
        assert store.source_entropy("RLC.001") < 1.5
        assert store.self_citation_ratio("RLC.001") > 0.2

    def test_silence_scoped_to_contract(self, store):
        """get_silence_events respects contract_id boundary."""
        _insert_silence(store, "RLC.001", "src-a", days_silent=10)
        _insert_silence(store, "RLC.002", "src-b", days_silent=20)
        assert len(store.get_silence_events("RLC.001")) == 1
        assert len(store.get_silence_events("RLC.002")) == 1

    def test_silence_last_seen_roundtrip(self, store):
        """The last_seen timestamp survives insert/retrieve."""
        ts = "2026-02-15T12:00:00Z"
        _insert_silence(store, "RLC.001", "src-a", last_seen=ts)
        events = store.get_silence_events("RLC.001")
        meta = json.loads(events[0]["metadata"])
        assert meta["last_seen"] == ts
