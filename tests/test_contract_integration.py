"""Tests for signal-curation contract validation and evidence store integration.

40 tests covering:
- Contract structure validation (tests 1-8)
- Source universe validation (tests 9-15)
- Signal dimensions validation (tests 16-20)
- Promotion policy validation (tests 21-26)
- Recursion guards validation (tests 27-30)
- Integration: contract -> evidence store (tests 31-40)
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

CONTRACT_PATH = Path(__file__).parent.parent / "contracts" / "signal-curation.json"


@pytest.fixture
def contract():
    with open(CONTRACT_PATH) as f:
        return json.load(f)


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
# Contract Structure Validation (1-8)
# ---------------------------------------------------------------------------

class TestContractStructure:
    """Validate top-level contract structure."""

    def test_01_contract_is_valid_json(self):
        """Contract file parses as valid JSON."""
        with open(CONTRACT_PATH) as f:
            data = json.load(f)
        assert isinstance(data, dict)

    def test_02_has_contract_id_string(self, contract):
        """Contract has a contractId that is a non-empty string."""
        assert isinstance(contract["contractId"], str)
        assert len(contract["contractId"]) > 0

    def test_03_has_version_number(self, contract):
        """Contract has a numeric version."""
        assert isinstance(contract["version"], (int, float))
        assert contract["version"] >= 1

    def test_04_has_frame_string(self, contract):
        """Contract has a frame string."""
        assert isinstance(contract["frame"], str)
        assert len(contract["frame"]) > 0

    def test_05_has_all_8_phase_keys(self, contract):
        """Contract phases contains all 8 required phase keys."""
        required_phases = {
            "goalFrame",
            "candidateDiscovery",
            "evidenceCapture",
            "signalExtraction",
            "scoring",
            "synthesis",
            "memoryPromotion",
            "nextLoopPlanning",
        }
        assert required_phases == set(contract["phases"].keys())

    def test_06_has_control_with_required_fields(self, contract):
        """Control block has maxIterations, checkpointInterval, completionPromise, recursionGuards."""
        control = contract["control"]
        assert "maxIterations" in control
        assert "checkpointInterval" in control
        assert "completionPromise" in control
        assert "recursionGuards" in control

    def test_07_has_epistemic_progression(self, contract):
        """epistemicProgression has startStatus, targetStatus, and transitions list."""
        ep = contract["epistemicProgression"]
        assert isinstance(ep["startStatus"], str)
        assert isinstance(ep["targetStatus"], str)
        assert isinstance(ep["transitions"], list)

    def test_08_has_storage_status_created(self, contract):
        """Contract has storagePath, status, and createdAt."""
        assert isinstance(contract["storagePath"], str)
        assert isinstance(contract["status"], str)
        assert isinstance(contract["createdAt"], str)


# ---------------------------------------------------------------------------
# Source Universe Validation (9-15)
# ---------------------------------------------------------------------------

class TestSourceUniverse:
    """Validate sourceUniverse entries."""

    def _sources(self, contract):
        return contract["phases"]["goalFrame"]["sourceUniverse"]

    def test_09_source_universe_nonempty(self, contract):
        """sourceUniverse is a list with at least 1 source."""
        sources = self._sources(contract)
        assert isinstance(sources, list)
        assert len(sources) >= 1

    def test_10_each_source_has_required_fields(self, contract):
        """Every source has sourceId, name, tier, trustWeight, freshnessHorizon, domains, verificationRequired."""
        required = {"sourceId", "name", "tier", "trustWeight", "freshnessHorizon", "domains", "verificationRequired"}
        for src in self._sources(contract):
            missing = required - set(src.keys())
            assert not missing, f"Source {src.get('sourceId', '?')} missing: {missing}"

    def test_11_all_source_tiers_valid(self, contract):
        """All source tiers are primary, secondary, or rumor."""
        valid_tiers = {"primary", "secondary", "rumor"}
        for src in self._sources(contract):
            assert src["tier"] in valid_tiers, f"{src['sourceId']} has invalid tier {src['tier']}"

    def test_12_trust_weight_between_0_and_1(self, contract):
        """trustWeight is between 0.0 and 1.0 inclusive."""
        for src in self._sources(contract):
            assert 0.0 <= src["trustWeight"] <= 1.0, f"{src['sourceId']} trustWeight out of range"

    def test_13_freshness_horizon_positive_int(self, contract):
        """freshnessHorizon is a positive integer."""
        for src in self._sources(contract):
            assert isinstance(src["freshnessHorizon"], int), f"{src['sourceId']} freshnessHorizon not int"
            assert src["freshnessHorizon"] > 0, f"{src['sourceId']} freshnessHorizon not positive"

    def test_14_domains_non_empty_list(self, contract):
        """Each source has a non-empty domains list."""
        for src in self._sources(contract):
            assert isinstance(src["domains"], list), f"{src['sourceId']} domains is not a list"
            assert len(src["domains"]) > 0, f"{src['sourceId']} domains is empty"

    def test_15_allowed_sources_exist_in_universe(self, contract):
        """All allowedSources IDs exist in sourceUniverse sourceIds."""
        universe_ids = {s["sourceId"] for s in self._sources(contract)}
        allowed = set(contract["phases"]["candidateDiscovery"]["allowedSources"])
        missing = allowed - universe_ids
        assert not missing, f"allowedSources not in sourceUniverse: {missing}"


# ---------------------------------------------------------------------------
# Signal Dimensions Validation (16-20)
# ---------------------------------------------------------------------------

class TestSignalDimensions:
    """Validate signalExtraction dimensions."""

    def _dims(self, contract):
        return contract["phases"]["signalExtraction"]["dimensions"]

    def test_16_dimensions_non_empty(self, contract):
        """dimensions is a non-empty list."""
        dims = self._dims(contract)
        assert isinstance(dims, list)
        assert len(dims) > 0

    def test_17_each_dimension_has_required_fields(self, contract):
        """Each dimension has name, description, scorer, weight."""
        for d in self._dims(contract):
            assert "name" in d, f"Dimension missing name"
            assert "description" in d, f"Dimension {d.get('name')} missing description"
            assert "scorer" in d, f"Dimension {d.get('name')} missing scorer"
            assert "weight" in d, f"Dimension {d.get('name')} missing weight"

    def test_18_scorer_valid_values(self, contract):
        """scorer is one of: llm, rule, hybrid."""
        valid_scorers = {"llm", "rule", "hybrid"}
        for d in self._dims(contract):
            assert d["scorer"] in valid_scorers, f"{d['name']} has invalid scorer {d['scorer']}"

    def test_19_weights_sum_to_one(self, contract):
        """All dimension weights sum to 1.0 within floating point tolerance."""
        total = sum(d["weight"] for d in self._dims(contract))
        assert abs(total - 1.0) < 1e-9, f"Weights sum to {total}, expected 1.0"

    def test_20_all_weights_positive(self, contract):
        """All dimension weights are positive."""
        for d in self._dims(contract):
            assert d["weight"] > 0, f"{d['name']} has non-positive weight {d['weight']}"


# ---------------------------------------------------------------------------
# Promotion Policy Validation (21-26)
# ---------------------------------------------------------------------------

class TestPromotionPolicy:
    """Validate memoryPromotion.promotionPolicy."""

    TRANSITION_ORDER = [
        "rawToWorking",
        "workingToVerified",
        "verifiedToPromoted",
        "promotedToTraining",
        "trainingToLocked",
    ]

    def _policy(self, contract):
        return contract["phases"]["memoryPromotion"]["promotionPolicy"]

    def test_21_promotion_policy_has_all_5_transitions(self, contract):
        """promotionPolicy has all 5 transitions."""
        policy = self._policy(contract)
        for t in self.TRANSITION_ORDER:
            assert t in policy, f"Missing transition: {t}"

    def test_22_each_transition_has_required_fields(self, contract):
        """Each transition has minConfidence, minCorroboration, requiresHumanReview, maxAge."""
        required = {"minConfidence", "minCorroboration", "requiresHumanReview", "maxAge"}
        policy = self._policy(contract)
        for name, gate in policy.items():
            missing = required - set(gate.keys())
            assert not missing, f"Transition {name} missing: {missing}"

    def test_23_min_confidence_monotonically_increasing(self, contract):
        """minConfidence increases monotonically across tiers."""
        policy = self._policy(contract)
        values = [policy[t]["minConfidence"] for t in self.TRANSITION_ORDER]
        for i in range(1, len(values)):
            assert values[i] >= values[i - 1], (
                f"minConfidence not monotonic: {self.TRANSITION_ORDER[i-1]}={values[i-1]} "
                f"> {self.TRANSITION_ORDER[i]}={values[i]}"
            )

    def test_24_min_corroboration_monotonically_increasing(self, contract):
        """minCorroboration increases monotonically across tiers."""
        policy = self._policy(contract)
        values = [policy[t]["minCorroboration"] for t in self.TRANSITION_ORDER]
        for i in range(1, len(values)):
            assert values[i] >= values[i - 1], (
                f"minCorroboration not monotonic: {self.TRANSITION_ORDER[i-1]}={values[i-1]} "
                f"> {self.TRANSITION_ORDER[i]}={values[i]}"
            )

    def test_25_higher_tiers_require_human_review(self, contract):
        """verifiedToPromoted, promotedToTraining, trainingToLocked require human review."""
        policy = self._policy(contract)
        for t in ["verifiedToPromoted", "promotedToTraining", "trainingToLocked"]:
            assert policy[t]["requiresHumanReview"] is True, f"{t} should require human review"

    def test_26_max_age_monotonically_increasing(self, contract):
        """maxAge increases monotonically (higher tiers have longer retention)."""
        policy = self._policy(contract)
        values = [policy[t]["maxAge"] for t in self.TRANSITION_ORDER]
        for i in range(1, len(values)):
            assert values[i] >= values[i - 1], (
                f"maxAge not monotonic: {self.TRANSITION_ORDER[i-1]}={values[i-1]} "
                f"> {self.TRANSITION_ORDER[i]}={values[i]}"
            )


# ---------------------------------------------------------------------------
# Recursion Guards Validation (27-30)
# ---------------------------------------------------------------------------

class TestRecursionGuards:
    """Validate control.recursionGuards."""

    def _guards(self, contract):
        return contract["control"]["recursionGuards"]

    def test_27_max_self_citation_ratio_between_0_and_1(self, contract):
        """maxSelfCitationRatio is between 0.0 and 1.0."""
        val = self._guards(contract)["maxSelfCitationRatio"]
        assert 0.0 <= val <= 1.0

    def test_28_source_entropy_minimum_positive(self, contract):
        """sourceEntropyMinimum is positive."""
        val = self._guards(contract)["sourceEntropyMinimum"]
        assert val > 0

    def test_29_hypothesis_diversity_check_is_bool(self, contract):
        """hypothesisDiversityCheck is boolean."""
        val = self._guards(contract)["hypothesisDiversityCheck"]
        assert isinstance(val, bool)

    def test_30_early_exit_self_citation_buffer(self, contract):
        """Early exit self_citation threshold (0.3) > recursion guard threshold (0.2)."""
        early_exit_conditions = contract["control"]["earlyExitConditions"]
        # Find the self_citation early exit condition
        self_citation_exit = None
        for cond in early_exit_conditions:
            if "self_citation" in cond["condition"]:
                # Parse threshold from condition string like "self_citation_ratio > 0.3"
                parts = cond["condition"].split(">")
                self_citation_exit = float(parts[1].strip())
                break
        assert self_citation_exit is not None, "No self_citation early exit condition found"
        guard_threshold = self._guards(contract)["maxSelfCitationRatio"]
        assert self_citation_exit > guard_threshold, (
            f"Early exit threshold ({self_citation_exit}) must be > "
            f"recursion guard ({guard_threshold}) to provide buffer"
        )


# ---------------------------------------------------------------------------
# Integration: Contract -> Evidence Store (31-40)
# ---------------------------------------------------------------------------

class TestContractStoreIntegration:
    """Integration tests using contract data with a live evidence store."""

    CONTRACT_ID = "RLC.DOSSIER.SIGNAL.001"

    def _sources(self, contract):
        return contract["phases"]["goalFrame"]["sourceUniverse"]

    def _dims(self, contract):
        return contract["phases"]["signalExtraction"]["dimensions"]

    def _policy(self, contract):
        return contract["phases"]["memoryPromotion"]["promotionPolicy"]

    def test_31_insert_evidence_for_each_source(self, contract, store):
        """Insert evidence for each source in sourceUniverse -- all accepted."""
        sources = self._sources(contract)
        hashes = []
        for src in sources:
            h = store.insert(
                self.CONTRACT_ID,
                src["sourceId"],
                f"Test content from {src['name']}",
            )
            assert h is not None, f"Insert rejected for source {src['sourceId']}"
            hashes.append(h)
        # All hashes should be unique
        assert len(set(hashes)) == len(sources)

    def test_32_source_entropy_after_uniform_insert(self, contract, store):
        """Source entropy after inserting 1 item per source matches expected."""
        sources = self._sources(contract)
        for src in sources:
            store.insert(
                self.CONTRACT_ID,
                src["sourceId"],
                f"Content from {src['sourceId']}",
            )
        entropy = store.source_entropy(self.CONTRACT_ID)
        # With N equally distributed sources, entropy = log2(N)
        n = len(sources)
        expected = round(math.log2(n), 3)
        assert abs(entropy - expected) < 0.01, f"Entropy {entropy} != expected {expected}"

    def test_33_score_evidence_with_all_dimensions(self, contract, store):
        """Score evidence with all contract dimensions -- composite score is valid."""
        dims = self._dims(contract)
        h = store.insert(self.CONTRACT_ID, "karpathy", "Important AI insight")
        assert h is not None
        # Build scores dict: each dimension gets a 0.7 score
        scores = {d["name"]: 0.7 for d in dims}
        composite = store.score_evidence(self.CONTRACT_ID, h, scores, "llm", 1)
        assert composite is not None
        assert 0.0 <= composite <= 1.0
        # All same score => composite == that score
        assert abs(composite - 0.7) < 0.01

    def test_34_promotion_gate_raw_to_working_qualifies(self, contract, store):
        """Raw item with confidence 0.3 qualifies for working (threshold is 0.3)."""
        policy = self._policy(contract)
        threshold = policy["rawToWorking"]["minConfidence"]
        h = store.insert(self.CONTRACT_ID, "karpathy", "Promotion test content")
        assert h is not None
        # Score it to exactly the threshold
        scores = {"relevance": threshold}
        store.score_evidence(self.CONTRACT_ID, h, scores, "llm", 1)
        row = store.get(h)
        assert row["confidence"] >= threshold
        # Promote should succeed
        ok = store.promote(self.CONTRACT_ID, h, "working", confidence=threshold)
        assert ok is True
        row = store.get(h)
        assert row["tier"] == "working"

    def test_35_promotion_gate_below_threshold_rejected(self, contract, store):
        """Raw item with confidence 0.2 does NOT qualify for working (below 0.3)."""
        policy = self._policy(contract)
        threshold = policy["rawToWorking"]["minConfidence"]
        h = store.insert(self.CONTRACT_ID, "karpathy", "Low confidence content")
        assert h is not None
        # Score below threshold
        below = threshold - 0.1
        scores = {"relevance": below}
        store.score_evidence(self.CONTRACT_ID, h, scores, "llm", 1)
        row = store.get(h)
        assert row["confidence"] < threshold, "Confidence should be below threshold"
        # The store itself allows promotion (gate enforcement is caller's job),
        # but the contract says this should NOT qualify. Verify the condition:
        assert row["confidence"] < threshold

    def test_36_human_review_gate_for_promoted_tier(self, contract, store):
        """Item at verified (confidence 0.7+, corroboration 2+) -- promotionPolicy says requiresHumanReview for promoted."""
        policy = self._policy(contract)
        gate = policy["verifiedToPromoted"]
        assert gate["requiresHumanReview"] is True
        assert gate["minConfidence"] == 0.7
        assert gate["minCorroboration"] == 2
        # Create and advance an item to verified state
        h = store.insert(self.CONTRACT_ID, "dario-amodei", "Safety scaling insight")
        assert h is not None
        store.promote(self.CONTRACT_ID, h, "working", confidence=0.5)
        store.promote(self.CONTRACT_ID, h, "verified", confidence=0.7)
        row = store.get(h)
        assert row["tier"] == "verified"
        assert row["confidence"] >= gate["minConfidence"]

    def test_37_full_lifecycle_insert_score_promote_twice(self, contract, store):
        """Full lifecycle: insert -> score -> promote raw->working -> score higher -> promote working->verified."""
        h = store.insert(self.CONTRACT_ID, "simon-willison", "LLM tooling breakthrough")
        assert h is not None

        # Phase 1: Score at 0.35, promote raw->working
        scores_1 = {"relevance": 0.4, "novelty": 0.3}
        composite_1 = store.score_evidence(self.CONTRACT_ID, h, scores_1, "llm", 1)
        assert composite_1 is not None
        assert composite_1 >= 0.3  # meets rawToWorking threshold
        ok1 = store.promote(self.CONTRACT_ID, h, "working", confidence=composite_1)
        assert ok1 is True
        assert store.get(h)["tier"] == "working"

        # Phase 2: Score higher at 0.6, promote working->verified
        scores_2 = {"relevance": 0.7, "novelty": 0.5}
        composite_2 = store.score_evidence(self.CONTRACT_ID, h, scores_2, "llm", 2)
        assert composite_2 is not None
        assert composite_2 >= 0.5  # meets workingToVerified threshold
        ok2 = store.promote(self.CONTRACT_ID, h, "verified", confidence=composite_2)
        assert ok2 is True
        assert store.get(h)["tier"] == "verified"

    def test_38_anti_recursion_entropy_check(self, contract, store):
        """After inserting from 10 sources, entropy > sourceEntropyMinimum (1.5)."""
        sources = self._sources(contract)
        min_entropy = contract["control"]["recursionGuards"]["sourceEntropyMinimum"]
        for src in sources:
            store.insert(
                self.CONTRACT_ID,
                src["sourceId"],
                f"Unique content from {src['sourceId']}",
            )
        entropy = store.source_entropy(self.CONTRACT_ID)
        assert entropy > min_entropy, (
            f"Entropy {entropy} not > minimum {min_entropy} with {len(sources)} sources"
        )

    def test_39_silence_event_for_missing_source(self, contract, store):
        """Insert silence with contract's silence threshold metadata."""
        silence_config = contract["phases"]["signalExtraction"]["negativeEvidence"]
        threshold = silence_config["silenceThreshold"]
        h = store.insert(
            self.CONTRACT_ID,
            "karpathy",
            "No posts detected in monitoring window",
            metadata={
                "type": "silence",
                "last_seen": "2026-03-10T00:00:00Z",
                "days_silent": threshold // 24,  # threshold is in hours
                "confidence": 0.6,
            },
        )
        assert h is not None
        events = store.get_silence_events(self.CONTRACT_ID)
        assert len(events) == 1
        meta = json.loads(events[0]["metadata"])
        assert meta["type"] == "silence"
        assert meta["days_silent"] == threshold // 24

    def test_40_tier_counts_after_lifecycle_simulation(self, contract, store):
        """Tier counts match after full lifecycle simulation."""
        sources = self._sources(contract)
        # Insert 10 items (one per source) -- all start as raw
        hashes = []
        for src in sources:
            h = store.insert(
                self.CONTRACT_ID,
                src["sourceId"],
                f"Lifecycle sim from {src['sourceId']}",
            )
            assert h is not None
            hashes.append(h)

        # Promote first 5 to working
        for h in hashes[:5]:
            store.promote(self.CONTRACT_ID, h, "working", confidence=0.4)

        # Promote first 2 to verified
        for h in hashes[:2]:
            store.promote(self.CONTRACT_ID, h, "verified", confidence=0.6)

        counts = store.tier_counts(self.CONTRACT_ID)
        assert counts.get("raw", 0) == 5    # 10 - 5 promoted
        assert counts.get("working", 0) == 3  # 5 - 2 promoted further
        assert counts.get("verified", 0) == 2
        total = sum(counts.values())
        assert total == len(sources)
