"""Tests for training data loader — converts dossier outputs to dspy.Examples."""
from __future__ import annotations

from pathlib import Path

import pytest

from dspy.loader import (
    PHASE_EXPECTED_SECTIONS,
    load_dossier_outputs,
    load_single_dossier,
    score_dossier,
)


class TestLoadSingleDossier:
    def test_loads_okta(self, output_dir):
        okta_dir = output_dir / "okta.com"
        if not okta_dir.exists():
            pytest.skip("okta.com output not present")
        result = load_single_dossier(okta_dir)
        assert result is not None
        assert result["domain"] == "okta.com"
        assert "discovery" in result
        assert "claims" in result

    def test_returns_none_for_incomplete(self, tmp_path):
        """Incomplete dossier (missing phases) returns None."""
        incomplete = tmp_path / "incomplete.com"
        incomplete.mkdir()
        (incomplete / "01-discovery.md").write_text("# Discovery\n")
        # Missing other phases
        result = load_single_dossier(incomplete)
        assert result is None


class TestScoreDossier:
    def test_scores_okta(self, output_dir):
        okta_dir = output_dir / "okta.com"
        if not okta_dir.exists():
            pytest.skip("okta.com output not present")
        dossier = load_single_dossier(okta_dir)
        scores = score_dossier(dossier)
        assert "p1" in scores
        assert "p4" in scores
        assert all(0.0 <= v <= 1.0 for v in scores.values())


class TestLoadDossierOutputs:
    def test_loads_all_complete_dossiers(self, output_dir):
        if not output_dir.exists():
            pytest.skip("output directory not present")
        examples = load_dossier_outputs(output_dir)
        assert isinstance(examples, list)
        # We know there are dossiers in output/
        if examples:
            # Check it's a dspy.Example by checking it has domain attribute
            assert hasattr(examples[0], "domain")


class TestPhaseExpectedSections:
    def test_all_seven_phases_defined(self):
        assert len(PHASE_EXPECTED_SECTIONS) == 7
        assert "p1" in PHASE_EXPECTED_SECTIONS
        assert "p7" in PHASE_EXPECTED_SECTIONS
