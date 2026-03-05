"""Tests for dossier evaluation metrics."""
from __future__ import annotations

import pytest

from dspy.metrics import (
    dossier_phase_metric,
    section_completeness,
    source_diversity,
    substantiation_ratio,
)


class TestSectionCompleteness:
    def test_all_sections_present(self):
        text = "## Company Identity\nOkta\n## Tech Stack\nJava\n## Key Findings\nGood"
        expected = ["Company Identity", "Tech Stack", "Key Findings"]
        assert section_completeness(text, expected) == 1.0

    def test_some_sections_missing(self):
        text = "## Company Identity\nOkta\n## Key Findings\nGood"
        expected = ["Company Identity", "Tech Stack", "Key Findings"]
        assert section_completeness(text, expected) == pytest.approx(2 / 3, abs=0.01)

    def test_no_sections(self):
        text = "Just some plain text without headers"
        expected = ["Company Identity", "Tech Stack"]
        assert section_completeness(text, expected) == 0.0

    def test_empty_expected(self):
        text = "## Something\ntext"
        assert section_completeness(text, []) == 1.0


class TestSourceDiversity:
    def test_multiple_sources(self):
        text = """
        ## Sources
        - Glassdoor reviews indicate...
        - LinkedIn profiles show...
        - Reddit discussions mention...
        - Hacker News thread confirms...
        """
        score = source_diversity(text)
        assert score >= 4 / 11

    def test_no_sources(self):
        text = "No sources mentioned at all."
        assert source_diversity(text) == 0.0

    def test_all_eleven_sources(self):
        text = (
            "Glassdoor LinkedIn Reddit HackerNews Blind "
            "layoffs.fyi arXiv Twitter job posting "
            "Product Hunt G2 Capterra Trustpilot"
        )
        assert source_diversity(text) >= 9 / 11


class TestSubstantiationRatio:
    def test_all_substantiated(self):
        text = """
        | Claim | Evidence |
        |-------|----------|
        | Fast API | GitHub repo shows 50ms p99 |
        | SOC2 | Certificate published on security page |
        """
        assert substantiation_ratio(text) > 0.5

    def test_no_table(self):
        text = "No claims table here."
        assert substantiation_ratio(text) == 0.0


class TestCompositeMetric:
    def test_returns_float_between_0_and_1(self):
        text = "## Company Identity\nOkta\n## Key Findings\nSome finding"
        expected_sections = ["Company Identity", "Key Findings"]
        score = dossier_phase_metric(text, expected_sections)
        assert 0.0 <= score <= 1.0

    def test_high_quality_output_scores_higher(self):
        good = (
            "## Company Identity\nOkta Inc\n"
            "## Tech Stack\nJava, Go\n"
            "## Key Findings\nStrong presence\n"
            "Source: Glassdoor, LinkedIn, Reddit, G2\n"
            "| Claim | Evidence |\n|---|---|\n| Fast | GitHub benchmarks |"
        )
        bad = "Some text with no structure"
        sections = ["Company Identity", "Tech Stack", "Key Findings"]
        assert dossier_phase_metric(good, sections) > dossier_phase_metric(bad, sections)
