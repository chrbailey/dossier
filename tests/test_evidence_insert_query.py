"""Tests for evidence store insert, query, and get edge cases."""
from __future__ import annotations

import json
import re
import sys
import time
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


# ── 1. Insert basics ────────────────────────────────────────────────

class TestInsertBasics:
    def test_insert_returns_hash(self, store):
        h = store.insert("C.001", "src-1", "some content")
        assert h is not None

    def test_hash_is_16_char_hex(self, store):
        h = store.insert("C.001", "src-1", "some content")
        assert len(h) == 16
        assert re.fullmatch(r"[0-9a-f]{16}", h)

    def test_different_content_gives_different_hashes(self, store):
        h1 = store.insert("C.001", "src-1", "content alpha")
        h2 = store.insert("C.001", "src-1", "content beta")
        assert h1 != h2

    def test_same_content_same_source_gives_same_hash(self, store):
        """First insert returns hash, second returns None (dedup), but underlying hash is identical."""
        from scripts.evidence_store import _hash_content
        h1 = store.insert("C.001", "src-1", "identical")
        expected = _hash_content("src-1", "identical")
        assert h1 == expected

    def test_insert_stores_contract_id(self, store):
        h = store.insert("C.001", "src-1", "data")
        row = store.get(h)
        assert row["contract_id"] == "C.001"

    def test_insert_stores_source_id(self, store):
        h = store.insert("C.001", "src-1", "data")
        row = store.get(h)
        assert row["source_id"] == "src-1"

    def test_insert_default_tier_is_raw(self, store):
        h = store.insert("C.001", "src-1", "data")
        row = store.get(h)
        assert row["tier"] == "raw"

    def test_insert_sets_created_at(self, store):
        h = store.insert("C.001", "src-1", "data")
        row = store.get(h)
        assert row["created_at"] is not None
        assert row["created_at"].endswith("Z")


# ── 2. Insert edge cases ────────────────────────────────────────────

class TestInsertEdgeCases:
    def test_empty_content_string(self, store):
        h = store.insert("C.001", "src-1", "")
        assert h is not None
        row = store.get(h)
        assert row["content"] == ""

    def test_very_long_content(self, store):
        big = "x" * 10_000
        h = store.insert("C.001", "src-1", big)
        assert h is not None
        row = store.get(h)
        assert len(row["content"]) == 10_000

    def test_unicode_content(self, store):
        text = "Привет мир 你好世界 🌍"
        h = store.insert("C.001", "src-1", text)
        row = store.get(h)
        assert row["content"] == text

    def test_special_characters_in_content(self, store):
        text = "SELECT * FROM t; DROP TABLE--; <script>alert('x')</script>"
        h = store.insert("C.001", "src-1", text)
        row = store.get(h)
        assert row["content"] == text

    def test_none_metadata(self, store):
        h = store.insert("C.001", "src-1", "data", metadata=None)
        row = store.get(h)
        assert row["metadata"] is None

    def test_dict_metadata(self, store):
        h = store.insert("C.001", "src-1", "data", metadata={"k": "v"})
        row = store.get(h)
        assert json.loads(row["metadata"]) == {"k": "v"}

    def test_nested_metadata(self, store):
        meta = {"outer": {"inner": [1, 2, 3], "flag": True}, "tag": None}
        h = store.insert("C.001", "src-1", "data", metadata=meta)
        row = store.get(h)
        assert json.loads(row["metadata"]) == meta

    def test_cycle_number_zero_default(self, store):
        h = store.insert("C.001", "src-1", "data")
        row = store.get(h)
        assert row["cycle_number"] == 0

    def test_cycle_number_positive(self, store):
        h = store.insert("C.001", "src-1", "data", cycle_number=5)
        row = store.get(h)
        assert row["cycle_number"] == 5

    def test_default_confidence_is_zero(self, store):
        h = store.insert("C.001", "src-1", "data")
        row = store.get(h)
        assert row["confidence"] == 0.0

    def test_default_corroboration_count_is_zero(self, store):
        h = store.insert("C.001", "src-1", "data")
        row = store.get(h)
        assert row["corroboration_count"] == 0


# ── 3. Deduplication ────────────────────────────────────────────────

class TestDeduplication:
    def test_exact_duplicate_returns_none(self, store):
        store.insert("C.001", "src-1", "dup content")
        h2 = store.insert("C.001", "src-1", "dup content")
        assert h2 is None

    def test_duplicate_increments_corroboration_count(self, store):
        h = store.insert("C.001", "src-1", "dup content")
        store.insert("C.001", "src-1", "dup content")
        row = store.get(h)
        assert row["corroboration_count"] == 1

    def test_triple_duplicate_increments_to_two(self, store):
        h = store.insert("C.001", "src-1", "dup content")
        store.insert("C.001", "src-1", "dup content")
        store.insert("C.001", "src-1", "dup content")
        row = store.get(h)
        assert row["corroboration_count"] == 2

    def test_different_source_same_content_not_duplicate(self, store):
        """Hash includes source_id, so same content from different sources are distinct."""
        h1 = store.insert("C.001", "src-A", "shared content")
        h2 = store.insert("C.001", "src-B", "shared content")
        assert h1 is not None
        assert h2 is not None
        assert h1 != h2

    def test_duplicate_updates_updated_at(self, store):
        h = store.insert("C.001", "src-1", "dup content")
        row_before = store.get(h)
        assert row_before["updated_at"] is None
        store.insert("C.001", "src-1", "dup content")
        row_after = store.get(h)
        assert row_after["updated_at"] is not None

    def test_duplicate_different_contract_still_deduplicates(self, store):
        """Hash is source_id + content only, so same source+content under different contracts deduplicates."""
        h1 = store.insert("C.001", "src-1", "same")
        h2 = store.insert("C.999", "src-1", "same")
        assert h1 is not None
        assert h2 is None


# ── 4. Get ──────────────────────────────────────────────────────────

class TestGet:
    def test_get_nonexistent_returns_none(self, store):
        assert store.get("0000000000000000") is None

    def test_get_returns_dict(self, store):
        h = store.insert("C.001", "src-1", "data")
        row = store.get(h)
        assert isinstance(row, dict)

    def test_get_returns_all_expected_keys(self, store):
        h = store.insert("C.001", "src-1", "data", metadata={"a": 1}, cycle_number=3)
        row = store.get(h)
        expected_keys = {
            "id", "hash", "contract_id", "tier", "source_id", "content",
            "metadata", "confidence", "corroboration_count", "created_at",
            "updated_at", "promoted_at", "expires_at", "cycle_number",
        }
        assert set(row.keys()) == expected_keys

    def test_get_values_match_insert(self, store):
        h = store.insert("C.001", "src-1", "payload", metadata={"x": 99}, cycle_number=2)
        row = store.get(h)
        assert row["hash"] == h
        assert row["contract_id"] == "C.001"
        assert row["source_id"] == "src-1"
        assert row["content"] == "payload"
        assert json.loads(row["metadata"]) == {"x": 99}
        assert row["cycle_number"] == 2
        assert row["tier"] == "raw"
        assert row["confidence"] == 0.0
        assert row["corroboration_count"] == 0
        assert row["promoted_at"] is None
        assert row["expires_at"] is None


# ── 5. Query basics ─────────────────────────────────────────────────

class TestQueryBasics:
    def test_query_filter_by_contract(self, store):
        store.insert("C.001", "src-1", "alpha")
        store.insert("C.002", "src-2", "beta")
        results = store.query("C.001")
        assert len(results) == 1
        assert results[0]["contract_id"] == "C.001"

    def test_query_filter_by_tier(self, store):
        h = store.insert("C.001", "src-1", "alpha")
        store.insert("C.001", "src-2", "beta")
        store.promote("C.001", h, "working")
        results = store.query("C.001", tier="working")
        assert len(results) == 1
        assert results[0]["tier"] == "working"

    def test_query_filter_by_source_id(self, store):
        store.insert("C.001", "src-A", "alpha")
        store.insert("C.001", "src-B", "beta")
        results = store.query("C.001", source_id="src-A")
        assert len(results) == 1
        assert results[0]["source_id"] == "src-A"

    def test_query_filter_by_cycle_number(self, store):
        store.insert("C.001", "src-1", "alpha", cycle_number=1)
        store.insert("C.001", "src-2", "beta", cycle_number=2)
        results = store.query("C.001", cycle_number=1)
        assert len(results) == 1
        assert results[0]["cycle_number"] == 1

    def test_query_multiple_filters(self, store):
        store.insert("C.001", "src-A", "one", cycle_number=1)
        store.insert("C.001", "src-A", "two", cycle_number=2)
        store.insert("C.001", "src-B", "three", cycle_number=1)
        results = store.query("C.001", source_id="src-A", cycle_number=1)
        assert len(results) == 1
        assert results[0]["content"] == "one"


# ── 6. Query edge cases ─────────────────────────────────────────────

class TestQueryEdgeCases:
    def test_empty_results(self, store):
        results = store.query("NONEXISTENT")
        assert results == []

    def test_limit_one(self, store):
        store.insert("C.001", "src-1", "alpha")
        store.insert("C.001", "src-2", "beta")
        results = store.query("C.001", limit=1)
        assert len(results) == 1

    def test_limit_zero_returns_empty(self, store):
        store.insert("C.001", "src-1", "alpha")
        results = store.query("C.001", limit=0)
        assert len(results) == 0

    def test_order_by_created_at_desc(self, store):
        store.insert("C.001", "src-1", "first")
        store.insert("C.001", "src-2", "second")
        store.insert("C.001", "src-3", "third")
        results = store.query("C.001")
        timestamps = [r["created_at"] for r in results]
        assert timestamps == sorted(timestamps, reverse=True)

    def test_query_across_contracts_returns_only_matching(self, store):
        store.insert("C.001", "src-1", "alpha")
        store.insert("C.002", "src-2", "beta")
        store.insert("C.003", "src-3", "gamma")
        results = store.query("C.002")
        assert len(results) == 1
        assert results[0]["contract_id"] == "C.002"

    def test_source_id_filter_is_exact_not_like(self, store):
        store.insert("C.001", "src", "data-a")
        store.insert("C.001", "src-extended", "data-b")
        results = store.query("C.001", source_id="src")
        assert len(results) == 1
        assert results[0]["source_id"] == "src"

    def test_query_returns_list_of_dicts(self, store):
        store.insert("C.001", "src-1", "alpha")
        results = store.query("C.001")
        assert isinstance(results, list)
        assert all(isinstance(r, dict) for r in results)


# ── 7. Cross-contract isolation ──────────────────────────────────────

class TestCrossContractIsolation:
    def test_insert_into_a_and_b_query_a_sees_only_a(self, store):
        store.insert("C.A", "src-1", "alpha-data")
        store.insert("C.B", "src-2", "beta-data")
        results_a = store.query("C.A")
        results_b = store.query("C.B")
        assert len(results_a) == 1
        assert len(results_b) == 1
        assert results_a[0]["contract_id"] == "C.A"
        assert results_b[0]["contract_id"] == "C.B"

    def test_many_contracts_isolated(self, store):
        for i in range(5):
            store.insert(f"C.{i}", f"src-{i}", f"content-{i}")
        for i in range(5):
            results = store.query(f"C.{i}")
            assert len(results) == 1
            assert results[0]["contract_id"] == f"C.{i}"


# ── 8. Metadata preservation ────────────────────────────────────────

class TestMetadataPreservation:
    def test_complex_nested_json_round_trip(self, store):
        meta = {
            "sources": ["web", "api", "manual"],
            "scores": {"relevance": 0.95, "novelty": 0.3},
            "nested": {"deep": {"deeper": True}},
            "nullable": None,
            "count": 42,
        }
        h = store.insert("C.001", "src-1", "data", metadata=meta)
        row = store.get(h)
        assert json.loads(row["metadata"]) == meta

    def test_metadata_with_unicode(self, store):
        meta = {"note": "数据来源：互联网", "emoji": "🔬"}
        h = store.insert("C.001", "src-1", "data", metadata=meta)
        row = store.get(h)
        assert json.loads(row["metadata"]) == meta

    def test_empty_dict_metadata_stored_as_none(self, store):
        """Empty dict is falsy, so the store treats it like None."""
        h = store.insert("C.001", "src-1", "data", metadata={})
        row = store.get(h)
        assert row["metadata"] is None

    def test_metadata_with_list_values(self, store):
        meta = {"tags": ["finance", "saas", "growth"], "version": [1, 0, 3]}
        h = store.insert("C.001", "src-1", "data", metadata=meta)
        row = store.get(h)
        assert json.loads(row["metadata"]) == meta
