"""Evaluation metrics for Dossier phase outputs.

These run locally (no LLM calls) — they parse output text to score quality.
Used by DSPy optimizers as the metric() function.
"""
from __future__ import annotations

import re

# The 11 signal source types from Phase 4's triangulation matrix
SOURCE_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("glassdoor", re.compile(r"glassdoor", re.IGNORECASE)),
    ("blind", re.compile(r"\bblind\b", re.IGNORECASE)),
    ("reddit", re.compile(r"reddit", re.IGNORECASE)),
    ("hackernews", re.compile(r"hacker\s*news|ycombinator|\bHN\b", re.IGNORECASE)),
    ("linkedin", re.compile(r"linkedin", re.IGNORECASE)),
    ("layoffs", re.compile(r"layoffs?\.fyi|layoff tracker", re.IGNORECASE)),
    ("arxiv", re.compile(r"arxiv|arXiv|google\s*scholar", re.IGNORECASE)),
    ("twitter", re.compile(r"twitter|𝕏|\bX\b.*post", re.IGNORECASE)),
    ("jobs", re.compile(r"job\s*(?:posting|board|listing)|indeed|hired", re.IGNORECASE)),
    ("producthunt", re.compile(r"product\s*hunt|indie\s*hackers", re.IGNORECASE)),
    ("reviews", re.compile(r"\bG2\b|capterra|trustpilot|peer\s*review", re.IGNORECASE)),
]


def section_completeness(text: str, expected_sections: list[str]) -> float:
    """Score 0-1: what fraction of expected markdown sections are present."""
    if not expected_sections:
        return 1.0
    found = 0
    for section in expected_sections:
        # Match ## Section Name or ### Section Name (case-insensitive)
        pattern = re.compile(rf"^#{{2,3}}\s+{re.escape(section)}", re.MULTILINE | re.IGNORECASE)
        if pattern.search(text):
            found += 1
    return found / len(expected_sections)


def source_diversity(text: str) -> float:
    """Score 0-1: fraction of 11 signal source types mentioned."""
    found = sum(1 for _, pattern in SOURCE_PATTERNS if pattern.search(text))
    return found / len(SOURCE_PATTERNS)


def substantiation_ratio(text: str) -> float:
    """Score 0-1: fraction of claims table rows that have non-empty evidence."""
    # Find markdown table rows (lines containing | delimiters, tolerating leading whitespace)
    table_rows = re.findall(r"^\s*\|(.+)\|\s*$", text, re.MULTILINE)
    # Skip header and separator rows
    data_rows = [
        row for row in table_rows
        if not re.match(r"^[\s\-|:]+$", row) and "Claim" not in row and "Evidence" not in row
    ]
    if not data_rows:
        return 0.0

    substantiated = 0
    for row in data_rows:
        cells = [c.strip() for c in row.split("|")]
        # A row is substantiated if any cell after the first has content
        if any(len(cell) > 3 for cell in cells[1:]):
            substantiated += 1

    return substantiated / len(data_rows)


def dossier_phase_metric(text: str, expected_sections: list[str]) -> float:
    """Composite metric for a single dossier phase output.

    Combines:
    - Section completeness (40%)
    - Source diversity (30%)
    - Substantiation ratio (30%)
    """
    completeness = section_completeness(text, expected_sections)
    diversity = source_diversity(text)
    substantiation = substantiation_ratio(text)

    return 0.4 * completeness + 0.3 * diversity + 0.3 * substantiation
