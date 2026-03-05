"""Load completed dossier outputs as DSPy training examples.

Scans output/ for domain directories with all 7 phases complete.
Scores each phase using metrics.py and produces dspy.Example objects.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from dspy.metrics import dossier_phase_metric

# Expected markdown sections per phase (used for completeness scoring)
PHASE_EXPECTED_SECTIONS: Dict[str, List[str]] = {
    "p1": ["Company Identity", "Domain & Infrastructure", "Digital Footprint",
           "Tech Stack Signals", "Key Findings"],
    "p2": ["Problem Statement", "Market Size", "Competitive Landscape",
           "SWOT Analysis", "Key Findings"],
    "p3": ["GitHub Presence", "Architecture", "Code Quality",
           "Dependencies", "Key Findings"],
    "p4": ["Claims Inventory", "Internal Signal Intelligence",
           "Triangulated Estimates", "Critical Gaps", "Key Findings"],
    "p5": ["Publications", "Patent Landscape",
           "Open-Source Alternatives", "Key Findings"],
    "p6": ["Business Model", "SaaS Metrics", "Replication",
           "Build vs Buy", "Key Findings"],
    "p7": ["Executive Summary", "Confidence Matrix", "Next Steps"],
}

PHASE_FILES: Dict[str, str] = {
    "p1": "01-discovery.md",
    "p2": "02-market.md",
    "p3": "03-technical.md",
    "p4": "04-claims.md",
    "p5": "05-academic.md",
    "p6": "06-valuation.md",
    "p7": "07-report.md",
}

PHASE_KEYS: Dict[str, str] = {
    "p1": "discovery",
    "p2": "market",
    "p3": "technical",
    "p4": "claims",
    "p5": "academic",
    "p6": "valuation",
    "p7": "report",
}


def load_single_dossier(domain_dir: Path) -> Optional[Dict[str, Any]]:
    """Load all phase outputs for a single domain.

    Returns None if any required phase file is missing.
    """
    domain = domain_dir.name
    result: Dict[str, Any] = {"domain": domain}

    for phase_id, file_name in PHASE_FILES.items():
        path = domain_dir / file_name
        if not path.exists():
            return None  # Incomplete dossier
        result[PHASE_KEYS[phase_id]] = path.read_text()

    # Also load executive summary if available
    exec_path = domain_dir / "executive-summary.md"
    if exec_path.exists():
        result["executive_summary"] = exec_path.read_text()

    return result


def score_dossier(dossier: Dict[str, Any]) -> Dict[str, float]:
    """Score each phase of a loaded dossier using metrics."""
    scores: Dict[str, float] = {}
    for phase_id, text_key in PHASE_KEYS.items():
        text = dossier.get(text_key, "")
        expected = PHASE_EXPECTED_SECTIONS.get(phase_id, [])
        scores[phase_id] = dossier_phase_metric(text, expected)

    return scores


def _import_example_class():
    """Import Example from the *installed* dspy package, bypassing local shadow.

    Our local ``dspy/`` directory shadows the installed dspy package. This
    function temporarily adjusts ``sys.path`` to reach the real package,
    imports ``Example``, then restores everything.
    """
    orig_path = sys.path[:]
    orig_modules = {k: v for k, v in sys.modules.items() if k.startswith("dspy")}

    try:
        project_root = str(Path(__file__).resolve().parent.parent)
        sys.path = [p for p in sys.path if p and str(Path(p).resolve()) != project_root]
        for key in list(sys.modules):
            if key.startswith("dspy"):
                del sys.modules[key]

        import dspy as _installed
        return _installed.Example
    finally:
        sys.path = orig_path
        for key in list(sys.modules):
            if key.startswith("dspy"):
                del sys.modules[key]
        sys.modules.update(orig_modules)


def load_dossier_outputs(output_dir: Path) -> list:
    """Load all complete dossier outputs as DSPy training examples.

    Each Example contains:
    - domain: str
    - discovery, market, technical, claims, academic, valuation, report: str
    - scores: dict[str, float] (per-phase metric scores)
    """
    Example = _import_example_class()
    examples: list = []

    if not output_dir.exists():
        return examples

    for domain_dir in sorted(output_dir.iterdir()):
        if not domain_dir.is_dir():
            continue
        if not (domain_dir / "01-discovery.md").exists():
            continue

        dossier = load_single_dossier(domain_dir)
        if dossier is None:
            continue

        scores = score_dossier(dossier)
        dossier["scores"] = scores

        example = Example(**dossier).with_inputs("domain")
        examples.append(example)

    return examples
