"""DSPy Signatures -- typed I/O contracts for each Dossier phase.

Each Signature defines the input/output schema for one of the 7 due-diligence
phases.  Docstrings serve as the default instructions that DSPy will optimize.
"""
from __future__ import annotations

import sys
from typing import List


def _import_dspy_core():
    """Import Signature, InputField, OutputField from the *installed* dspy.

    Our local ``dspy/`` directory shadows the installed dspy package.  This
    function temporarily adjusts ``sys.path`` to reach the real package,
    imports the needed symbols, then restores everything.
    """
    from pathlib import Path

    orig_path = sys.path[:]
    orig_modules = {k: v for k, v in sys.modules.items() if k.startswith("dspy")}

    try:
        # Remove the project root (parent of local dspy/) from sys.path
        # so the installed dspy package resolves instead of our local directory
        project_root = str(Path(__file__).resolve().parent.parent)
        sys.path = [p for p in sys.path if p and str(Path(p).resolve()) != project_root]
        # Clear cached dspy modules so importlib re-resolves
        for key in list(sys.modules):
            if key.startswith("dspy"):
                del sys.modules[key]

        import dspy as _installed
        return _installed.Signature, _installed.InputField, _installed.OutputField
    finally:
        # Restore everything
        sys.path = orig_path
        # Re-populate dspy module cache with our local package
        for key in list(sys.modules):
            if key.startswith("dspy"):
                del sys.modules[key]
        sys.modules.update(orig_modules)


Signature, InputField, OutputField = _import_dspy_core()


# ---------------------------------------------------------------------------
# Phase 1: Discovery
# ---------------------------------------------------------------------------

class Discovery(Signature):
    """Analyze a SaaS company's public footprint to build a comprehensive
    company profile including identity, technology stack, and product
    description from domain, WHOIS, and website data."""

    domain: str = InputField(desc="Target company domain (e.g. okta.com)")
    whois_data: str = InputField(
        desc="Raw WHOIS registration data for the domain",
        default="",
    )
    website_content: str = InputField(
        desc="Scraped homepage and key pages content",
        default="",
    )

    company_profile: str = OutputField(
        desc="Structured company identity: name, HQ, founding year, headcount, funding"
    )
    tech_stack: str = OutputField(
        desc="Identified technologies, frameworks, and infrastructure"
    )
    product_description: str = OutputField(
        desc="Core product offering, target market, and value proposition"
    )


# ---------------------------------------------------------------------------
# Phase 2: Market Analysis
# ---------------------------------------------------------------------------

class MarketAnalysis(Signature):
    """Evaluate competitive landscape, market sizing, and strategic
    positioning for a SaaS company based on its company profile and
    product description."""

    company_profile: str = InputField(
        desc="Company identity from Phase 1 discovery"
    )
    product_description: str = InputField(
        desc="Core product offering from Phase 1 discovery"
    )

    tam_sam_som: str = OutputField(
        desc="Total addressable, serviceable addressable, and serviceable obtainable market estimates"
    )
    competitors: str = OutputField(
        desc="Direct and indirect competitors with differentiation analysis"
    )
    swot: str = OutputField(
        desc="Strengths, weaknesses, opportunities, and threats analysis"
    )
    positioning: str = OutputField(
        desc="Market positioning relative to competitors and category definition"
    )


# ---------------------------------------------------------------------------
# Phase 3: Technical Assessment
# ---------------------------------------------------------------------------

class TechnicalAssessment(Signature):
    """Assess a SaaS company's engineering quality, architecture decisions,
    and technical moat from public code repositories and technical
    documentation."""

    company_profile: str = InputField(
        desc="Company identity from Phase 1 discovery"
    )
    github_org: str = InputField(
        desc="GitHub organization or user handle for public repos",
        default="",
    )

    architecture: str = OutputField(
        desc="System architecture patterns, cloud infrastructure, and design decisions"
    )
    repo_stats: str = OutputField(
        desc="Repository metrics: stars, forks, contributors, commit frequency, language breakdown"
    )
    code_quality: str = OutputField(
        desc="Code quality indicators: CI/CD, testing, documentation, dependency management"
    )


# ---------------------------------------------------------------------------
# Phase 4: Claims Triangulation (Shadow Prediction Market)
# ---------------------------------------------------------------------------

class ClaimsTriangulation(Signature):
    """Triangulate company claims against 11 independent signal sources
    to reconstruct insider knowledge.  Use Bayesian confidence from signal
    convergence across Glassdoor, Blind, Reddit, HN, LinkedIn, layoff
    trackers, arXiv, Twitter/X, job boards, Product Hunt, and review
    sites."""

    discovery_report: str = InputField(
        desc="Full Phase 1 discovery report"
    )
    technical_report: str = InputField(
        desc="Full Phase 3 technical assessment report"
    )

    claims_inventory: str = OutputField(
        desc="Catalog of all verifiable claims made by the company"
    )
    signal_intelligence: str = OutputField(
        desc="Evidence gathered from 11 independent signal sources"
    )
    triangulated_estimates: str = OutputField(
        desc="Bayesian confidence estimates for each claim based on signal convergence"
    )
    materiality_assessment: str = OutputField(
        desc="Impact assessment of confirmed, disputed, and unverifiable claims"
    )


# ---------------------------------------------------------------------------
# Phase 5: Academic Landscape
# ---------------------------------------------------------------------------

class AcademicLandscape(Signature):
    """Map a company's intellectual property position, academic
    publications, and open-source alternatives to assess the depth and
    defensibility of their technical moat."""

    company_profile: str = InputField(
        desc="Company identity from Phase 1 discovery"
    )
    key_personnel: str = InputField(
        desc="Key technical leaders and researchers at the company",
        default="",
    )

    ip_landscape: str = OutputField(
        desc="Patent portfolio analysis, filing trends, and IP strategy assessment"
    )
    publications: str = OutputField(
        desc="Academic papers, conference talks, and research contributions"
    )
    open_source_alternatives: str = OutputField(
        desc="Open-source projects that replicate or threaten the company's core technology"
    )


# ---------------------------------------------------------------------------
# Phase 6: Valuation Model
# ---------------------------------------------------------------------------

class ValuationModel(Signature):
    """Synthesize all prior phase outputs into a financial valuation
    model covering business model analysis, SaaS metrics, replication
    cost estimate, and build-vs-buy recommendation."""

    all_prior_reports: str = InputField(
        desc="Concatenated outputs from Phases 1-5"
    )

    business_model: str = OutputField(
        desc="Revenue model analysis: pricing tiers, unit economics, expansion revenue"
    )
    saas_metrics: str = OutputField(
        desc="Estimated SaaS metrics: ARR, growth rate, churn, LTV/CAC, Rule of 40"
    )
    replication_cost: str = OutputField(
        desc="Engineering cost to rebuild core product from scratch"
    )
    build_vs_buy: str = OutputField(
        desc="Build vs. buy recommendation with breakeven analysis"
    )


# ---------------------------------------------------------------------------
# Phase 7: Final Report
# ---------------------------------------------------------------------------

class FinalReport(Signature):
    """Generate the final due-diligence report with an executive summary
    and comprehensive analysis synthesizing all prior phases into a
    cohesive investment recommendation."""

    all_prior_reports: str = InputField(
        desc="Concatenated outputs from Phases 1-6"
    )

    executive_summary: str = OutputField(
        desc="One-page executive summary with key findings and recommendation"
    )
    full_report: str = OutputField(
        desc="Complete due-diligence report organized by phase with cross-references"
    )


# ---------------------------------------------------------------------------
# Convenience list for iteration
# ---------------------------------------------------------------------------

SIGNATURE_CLASSES: List[type] = [
    Discovery,
    MarketAnalysis,
    TechnicalAssessment,
    ClaimsTriangulation,
    AcademicLandscape,
    ValuationModel,
    FinalReport,
]
