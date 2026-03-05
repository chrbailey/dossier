"""DSPy Module wrappers for Dossier phases.

Each PhaseModule wraps a Signature with a dspy.ChainOfThought predictor.
The DossierPipeline composes all 7 phases.
"""
from __future__ import annotations

from collections import OrderedDict
from typing import Any

import dspy  # Our proxy — ensures all DSPy classes share one settings instance

from dspy.signatures import (
    AcademicLandscape,
    ClaimsTriangulation,
    Discovery,
    FinalReport,
    MarketAnalysis,
    TechnicalAssessment,
    ValuationModel,
)

# Use classes from the proxy — they share the same settings/predict module
Module = dspy.Module
ChainOfThought = dspy.ChainOfThought
Prediction = dspy.Prediction


class PhaseModule(Module):
    """Wraps a single Dossier phase Signature as a DSPy Module."""

    def __init__(self, signature_cls) -> None:
        super().__init__()
        self.signature_cls = signature_cls
        self.predictor = ChainOfThought(signature_cls)

    def forward(self, **kwargs: Any):
        return self.predictor(**kwargs)


class DossierPipeline(Module):
    """Composes all 7 Dossier phases as a DSPy Module.

    Note: In compile mode, phases run independently (one at a time).
    The Ralph Loop handles DAG-aware parallel execution at runtime.
    """

    def __init__(self) -> None:
        super().__init__()
        self.phases: OrderedDict[str, PhaseModule] = OrderedDict(
            p1=PhaseModule(Discovery),
            p2=PhaseModule(MarketAnalysis),
            p3=PhaseModule(TechnicalAssessment),
            p4=PhaseModule(ClaimsTriangulation),
            p5=PhaseModule(AcademicLandscape),
            p6=PhaseModule(ValuationModel),
            p7=PhaseModule(FinalReport),
        )

    def forward(self, **kwargs: Any):
        """Run all phases sequentially for optimization."""
        results = {}

        # P1: Discovery
        results["p1"] = self.phases["p1"](
            domain=kwargs.get("domain", ""),
            whois_data=kwargs.get("whois_data", ""),
            website_content=kwargs.get("website_content", ""),
        )

        p1_profile = results["p1"].company_profile
        p1_product = results["p1"].product_description

        # P2: Market
        results["p2"] = self.phases["p2"](
            company_profile=p1_profile,
            product_description=p1_product,
        )

        # P3: Technical
        results["p3"] = self.phases["p3"](
            company_profile=p1_profile,
            github_org=kwargs.get("github_org", ""),
        )

        # P4: Claims
        results["p4"] = self.phases["p4"](
            discovery_report=p1_profile,
            technical_report=results["p3"].architecture,
        )

        # P5: Academic
        results["p5"] = self.phases["p5"](
            company_profile=p1_profile,
            key_personnel=kwargs.get("key_personnel", ""),
        )

        # P6: Valuation
        prior_text = "\n\n---\n\n".join(
            str(results[f"p{i}"]) for i in range(1, 6)
        )
        results["p6"] = self.phases["p6"](all_prior_reports=prior_text)

        # P7: Report
        all_text = "\n\n---\n\n".join(
            str(results[f"p{i}"]) for i in range(1, 7)
        )
        results["p7"] = self.phases["p7"](all_prior_reports=all_text)

        return results["p7"]
