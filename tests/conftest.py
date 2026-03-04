"""Shared test fixtures for DSPy integration tests."""
from __future__ import annotations

from pathlib import Path

import pytest

DOSSIER_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = DOSSIER_ROOT / "output"
PROMPTS_DIR = DOSSIER_ROOT / "prompts"


@pytest.fixture
def dossier_root():
    return DOSSIER_ROOT


@pytest.fixture
def output_dir():
    return OUTPUT_DIR


@pytest.fixture
def sample_discovery_output():
    """Load okta.com discovery output as sample data."""
    path = OUTPUT_DIR / "okta.com" / "01-discovery.md"
    if path.exists():
        return path.read_text()
    return "# Discovery: okta.com\n\n## Company Identity\nOkta, Inc.\n"


@pytest.fixture
def sample_claims_output():
    """Load okta.com claims output as sample data."""
    path = OUTPUT_DIR / "okta.com" / "04-claims.md"
    if path.exists():
        return path.read_text()
    return "# Claims Validation: Okta\n\n## Claims Inventory\n| # | Claim |\n"
