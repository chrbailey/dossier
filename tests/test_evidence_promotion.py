"""Tests for evidence store promotion lifecycle.

Covers: basic promotion, sequential promotion, demotion prevention,
same-tier rejection, confidence tracking, timestamps, edge cases,
tier counts, and contract isolation.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

CONTRACT = "RLC.TEST"


@pytest.fixture
def db_path(tmp_path):
    return tmp_path / "test.db"


@pytest.fixture
def store(db_path):
    from scripts.evidence_store import EvidenceStore

    s = EvidenceStore(db_path)
    yield s
    s.close()


def _insert(store, contract_id=CONTRACT, source="src-1", content="evidence text"):
    """Helper: insert one piece of evidence and return its hash."""
    h = store.insert(contract_id, source, content)
    assert h is not None
    return h


# ---------------------------------------------------------------------------
# 1. Basic promotion (skip tiers is allowed)
# ---------------------------------------------------------------------------

class TestBasicPromotion:
    def test_raw_to_working(self, store):
        h = _insert(store)
        assert store.promote(CONTRACT, h, "working") is True
        assert store.get(h)["tier"] == "working"

    def test_raw_to_verified(self, store):
        h = _insert(store)
        assert store.promote(CONTRACT, h, "verified") is True
        assert store.get(h)["tier"] == "verified"

    def test_raw_to_promoted(self, store):
        h = _insert(store)
        assert store.promote(CONTRACT, h, "promoted") is True
        assert store.get(h)["tier"] == "promoted"

    def test_raw_to_training(self, store):
        h = _insert(store)
        assert store.promote(CONTRACT, h, "training") is True
        assert store.get(h)["tier"] == "training"

    def test_raw_to_locked(self, store):
        h = _insert(store)
        assert store.promote(CONTRACT, h, "locked") is True
        assert store.get(h)["tier"] == "locked"


# ---------------------------------------------------------------------------
# 2. Sequential promotion (full ladder)
# ---------------------------------------------------------------------------

class TestSequentialPromotion:
    def test_full_ladder(self, store):
        """Promote through every tier in order: raw -> working -> ... -> locked."""
        h = _insert(store)
        for tier in ["working", "verified", "promoted", "training", "locked"]:
            assert store.promote(CONTRACT, h, tier) is True
            assert store.get(h)["tier"] == tier

    def test_full_ladder_with_confidence(self, store):
        """Full ladder with rising confidence at each step."""
        h = _insert(store)
        for i, tier in enumerate(["working", "verified", "promoted", "training", "locked"], 1):
            conf = round(i * 0.2, 1)
            assert store.promote(CONTRACT, h, tier, confidence=conf) is True
            row = store.get(h)
            assert row["tier"] == tier
            assert row["confidence"] == conf


# ---------------------------------------------------------------------------
# 3. Demotion prevention
# ---------------------------------------------------------------------------

class TestDemotionPrevention:
    def test_working_to_raw_fails(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "working")
        assert store.promote(CONTRACT, h, "raw") is False
        assert store.get(h)["tier"] == "working"

    def test_verified_to_working_fails(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "verified")
        assert store.promote(CONTRACT, h, "working") is False
        assert store.get(h)["tier"] == "verified"

    def test_locked_to_raw_fails(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "locked")
        assert store.promote(CONTRACT, h, "raw") is False
        assert store.get(h)["tier"] == "locked"

    def test_locked_to_training_fails(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "locked")
        assert store.promote(CONTRACT, h, "training") is False
        assert store.get(h)["tier"] == "locked"

    def test_locked_to_promoted_fails(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "locked")
        assert store.promote(CONTRACT, h, "promoted") is False

    def test_locked_to_verified_fails(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "locked")
        assert store.promote(CONTRACT, h, "verified") is False

    def test_locked_to_working_fails(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "locked")
        assert store.promote(CONTRACT, h, "working") is False


# ---------------------------------------------------------------------------
# 4. Same-tier promotion fails
# ---------------------------------------------------------------------------

class TestSameTierFails:
    def test_raw_to_raw(self, store):
        h = _insert(store)
        assert store.promote(CONTRACT, h, "raw") is False

    def test_working_to_working(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "working")
        assert store.promote(CONTRACT, h, "working") is False

    def test_verified_to_verified(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "verified")
        assert store.promote(CONTRACT, h, "verified") is False

    def test_promoted_to_promoted(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "promoted")
        assert store.promote(CONTRACT, h, "promoted") is False

    def test_locked_to_locked(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "locked")
        assert store.promote(CONTRACT, h, "locked") is False


# ---------------------------------------------------------------------------
# 5. Confidence tracking
# ---------------------------------------------------------------------------

class TestConfidenceTracking:
    def test_promote_with_confidence(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "working", confidence=0.5)
        assert store.get(h)["confidence"] == 0.5

    def test_promote_without_confidence_preserves_existing(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "working", confidence=0.7)
        store.promote(CONTRACT, h, "verified")  # no confidence arg
        assert store.get(h)["confidence"] == 0.7

    def test_promote_updates_confidence(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "working", confidence=0.3)
        store.promote(CONTRACT, h, "verified", confidence=0.9)
        assert store.get(h)["confidence"] == 0.9

    def test_insert_has_zero_confidence(self, store):
        h = _insert(store)
        assert store.get(h)["confidence"] == 0.0


# ---------------------------------------------------------------------------
# 6. promoted_at timestamp
# ---------------------------------------------------------------------------

class TestPromotedAtTimestamp:
    def test_promoted_at_set_on_promotion(self, store):
        h = _insert(store)
        assert store.get(h)["promoted_at"] is None
        store.promote(CONTRACT, h, "working")
        assert store.get(h)["promoted_at"] is not None

    def test_promoted_at_updated_on_higher_tier(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "working")
        ts1 = store.get(h)["promoted_at"]
        # Small delay to ensure timestamp differs
        time.sleep(0.01)
        store.promote(CONTRACT, h, "verified")
        ts2 = store.get(h)["promoted_at"]
        assert ts2 >= ts1


# ---------------------------------------------------------------------------
# 7. Wrong contract
# ---------------------------------------------------------------------------

class TestWrongContract:
    def test_promote_wrong_contract_returns_false(self, store):
        h = _insert(store, contract_id="RLC.AAA")
        assert store.promote("RLC.BBB", h, "working") is False

    def test_wrong_contract_does_not_alter_tier(self, store):
        h = _insert(store, contract_id="RLC.AAA")
        store.promote("RLC.BBB", h, "working")
        assert store.get(h)["tier"] == "raw"


# ---------------------------------------------------------------------------
# 8. Nonexistent hash
# ---------------------------------------------------------------------------

class TestNonexistentHash:
    def test_fake_hash_returns_false(self, store):
        assert store.promote(CONTRACT, "deadbeef00000000", "working") is False

    def test_fake_hash_no_side_effects(self, store):
        h = _insert(store)
        store.promote(CONTRACT, "deadbeef00000000", "working")
        assert store.get(h)["tier"] == "raw"


# ---------------------------------------------------------------------------
# 9. Invalid tier name
# ---------------------------------------------------------------------------

class TestInvalidTier:
    def test_invalid_tier_returns_false(self, store):
        h = _insert(store)
        assert store.promote(CONTRACT, h, "invalid_tier") is False

    def test_invalid_tier_does_not_alter_evidence(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "invalid_tier")
        assert store.get(h)["tier"] == "raw"


# ---------------------------------------------------------------------------
# 10. Tier counts after operations
# ---------------------------------------------------------------------------

class TestTierCounts:
    def test_tier_counts_single_insert(self, store):
        _insert(store)
        counts = store.tier_counts(CONTRACT)
        assert counts.get("raw", 0) == 1

    def test_tier_counts_after_promotion(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "working")
        counts = store.tier_counts(CONTRACT)
        assert counts.get("raw", 0) == 0
        assert counts.get("working", 0) == 1

    def test_tier_counts_multiple_inserts_and_promotions(self, store):
        h1 = _insert(store, content="one")
        h2 = _insert(store, content="two")
        h3 = _insert(store, content="three")
        store.promote(CONTRACT, h1, "working")
        store.promote(CONTRACT, h2, "verified")
        counts = store.tier_counts(CONTRACT)
        assert counts.get("raw", 0) == 1
        assert counts.get("working", 0) == 1
        assert counts.get("verified", 0) == 1


# ---------------------------------------------------------------------------
# 11. Multiple items at different tiers
# ---------------------------------------------------------------------------

class TestMultipleItemsDifferentTiers:
    def test_3_raw_2_working_1_verified(self, store):
        raws = [_insert(store, content=f"raw-{i}") for i in range(6)]
        # Promote 3 to working
        for h in raws[:3]:
            store.promote(CONTRACT, h, "working")
        # Promote 1 of those 3 to verified
        store.promote(CONTRACT, raws[0], "verified")
        counts = store.tier_counts(CONTRACT)
        assert counts.get("raw", 0) == 3
        assert counts.get("working", 0) == 2
        assert counts.get("verified", 0) == 1


# ---------------------------------------------------------------------------
# 12. Tier counts isolation between contracts
# ---------------------------------------------------------------------------

class TestTierCountsIsolation:
    def test_different_contracts_independent(self, store):
        h1 = _insert(store, contract_id="RLC.X", content="x-content")
        h2 = _insert(store, contract_id="RLC.Y", content="y-content")
        store.promote("RLC.X", h1, "locked")
        counts_x = store.tier_counts("RLC.X")
        counts_y = store.tier_counts("RLC.Y")
        assert counts_x.get("locked", 0) == 1
        assert counts_x.get("raw", 0) == 0
        assert counts_y.get("raw", 0) == 1
        assert counts_y.get("locked", 0) == 0

    def test_empty_contract_has_empty_counts(self, store):
        _insert(store, contract_id="RLC.A", content="a-content")
        counts = store.tier_counts("RLC.EMPTY")
        assert counts == {}

    def test_promotion_in_one_contract_does_not_affect_other(self, store):
        h1 = _insert(store, contract_id="RLC.P", content="p-data")
        h2 = _insert(store, contract_id="RLC.Q", content="q-data")
        store.promote("RLC.P", h1, "verified")
        # h2 in RLC.Q should still be raw
        assert store.get(h2)["tier"] == "raw"
        assert store.tier_counts("RLC.Q") == {"raw": 1}


# ---------------------------------------------------------------------------
# 13. Additional edge cases
# ---------------------------------------------------------------------------

class TestEdgeCases:
    def test_promote_returns_bool_true(self, store):
        """promote() return type is bool, not truthy int."""
        h = _insert(store)
        result = store.promote(CONTRACT, h, "working")
        assert result is True
        assert type(result) is bool

    def test_promote_returns_bool_false(self, store):
        """Failed promote() return type is bool, not falsy None."""
        h = _insert(store)
        result = store.promote(CONTRACT, h, "raw")
        assert result is False
        assert type(result) is bool

    def test_training_to_locked_only_valid_step_from_training(self, store):
        h = _insert(store)
        store.promote(CONTRACT, h, "training")
        # Only locked is above training
        for bad_tier in ["raw", "working", "verified", "promoted", "training"]:
            assert store.promote(CONTRACT, h, bad_tier) is False
        assert store.promote(CONTRACT, h, "locked") is True
