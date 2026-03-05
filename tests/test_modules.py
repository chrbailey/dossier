"""Tests for DSPy Module wrappers — one per Dossier phase."""
from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from dspy.modules import DossierPipeline, PhaseModule


class TestPhaseModule:
    def test_init_stores_signature(self):
        from dspy.signatures import Discovery
        mod = PhaseModule(Discovery)
        assert mod.signature_cls is Discovery
        assert mod.predictor is not None

    def test_forward_calls_predictor(self):
        from dspy.signatures import Discovery
        mod = PhaseModule(Discovery)
        # Mock the predictor to avoid needing a real LM
        mock_pred = MagicMock()
        # Create a mock Prediction-like object
        mock_result = MagicMock()
        mock_result.company_profile = "Okta Inc"
        mock_result.tech_stack = "Java, Go"
        mock_result.product_description = "Identity platform"
        mock_pred.return_value = mock_result
        mod.predictor = mock_pred

        result = mod.forward(
            domain="okta.com",
            whois_data="{}",
            website_content="{}",
        )
        assert result.company_profile == "Okta Inc"
        mock_pred.assert_called_once()


class TestDossierPipeline:
    def test_has_seven_phase_modules(self):
        pipeline = DossierPipeline()
        assert len(pipeline.phases) == 7
        assert "p1" in pipeline.phases
        assert "p7" in pipeline.phases

    def test_phase_order(self):
        pipeline = DossierPipeline()
        keys = list(pipeline.phases.keys())
        assert keys == ["p1", "p2", "p3", "p4", "p5", "p6", "p7"]
