"""Tests for DSPy Signatures -- one per Dossier phase."""
from __future__ import annotations

import pytest

from dspy.signatures import (
    AcademicLandscape,
    ClaimsTriangulation,
    Discovery,
    FinalReport,
    MarketAnalysis,
    TechnicalAssessment,
    ValuationModel,
    SIGNATURE_CLASSES,
)


class TestSignatureStructure:
    """Verify each Signature has correct input/output fields."""

    def test_discovery_fields(self):
        sig = Discovery
        input_names = set(sig.input_fields.keys())
        output_names = set(sig.output_fields.keys())
        assert "domain" in input_names
        assert "company_profile" in output_names
        assert "tech_stack" in output_names

    def test_market_analysis_fields(self):
        sig = MarketAnalysis
        input_names = set(sig.input_fields.keys())
        output_names = set(sig.output_fields.keys())
        assert "company_profile" in input_names
        assert "competitors" in output_names
        assert "swot" in output_names

    def test_technical_assessment_fields(self):
        sig = TechnicalAssessment
        input_names = set(sig.input_fields.keys())
        output_names = set(sig.output_fields.keys())
        assert "company_profile" in input_names
        assert "architecture" in output_names

    def test_claims_triangulation_fields(self):
        sig = ClaimsTriangulation
        input_names = set(sig.input_fields.keys())
        output_names = set(sig.output_fields.keys())
        assert "discovery_report" in input_names
        assert "technical_report" in input_names
        assert "claims_inventory" in output_names
        assert "materiality_assessment" in output_names

    def test_academic_landscape_fields(self):
        sig = AcademicLandscape
        input_names = set(sig.input_fields.keys())
        output_names = set(sig.output_fields.keys())
        assert "company_profile" in input_names
        assert "publications" in output_names

    def test_valuation_model_fields(self):
        sig = ValuationModel
        input_names = set(sig.input_fields.keys())
        output_names = set(sig.output_fields.keys())
        assert "all_prior_reports" in input_names
        assert "replication_cost" in output_names

    def test_final_report_fields(self):
        sig = FinalReport
        input_names = set(sig.input_fields.keys())
        output_names = set(sig.output_fields.keys())
        assert "all_prior_reports" in input_names
        assert "executive_summary" in output_names

    def test_all_signatures_have_docstrings(self):
        """Docstrings are the optimizable instructions -- they must exist."""
        for sig_cls in SIGNATURE_CLASSES:
            assert sig_cls.__doc__ is not None
            assert len(sig_cls.__doc__.strip()) > 20

    def test_signature_count(self):
        """Exactly 7 signatures -- one per phase."""
        assert len(SIGNATURE_CLASSES) == 7
