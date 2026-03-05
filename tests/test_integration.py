"""Integration tests -- verify full pipeline wiring without live LLM calls."""
from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from dspy.compile import compile_dossier, make_metric_fn
from dspy.export import export_to_prompts, extract_instructions, PHASE_PROMPT_FILES
from dspy.loader import load_dossier_outputs, load_single_dossier, score_dossier
from dspy.modules import DossierPipeline


class TestEndToEnd:
    def test_loader_to_metric(self, output_dir):
        """Training data loads and metric scores it."""
        if not output_dir.exists():
            pytest.skip("No output directory")
        examples = load_dossier_outputs(output_dir)
        if not examples:
            pytest.skip("No complete dossiers")

        metric = make_metric_fn()
        # Score the first example's report as if it were a prediction
        ex = examples[0]
        # Create a mock prediction with the report text
        pred = MagicMock()
        pred.executive_summary = getattr(ex, "executive_summary", "")
        pred.full_report = ex.report
        score = metric(ex, pred)
        assert 0.0 <= score <= 1.0
        print(f"  {ex.domain}: score={score:.3f}")

    def test_pipeline_structure(self):
        """Pipeline has correct phase ordering and module types."""
        pipeline = DossierPipeline()
        assert list(pipeline.phases.keys()) == [
            "p1", "p2", "p3", "p4", "p5", "p6", "p7"
        ]
        for mod in pipeline.phases.values():
            assert hasattr(mod, "predictor")

    def test_extract_and_export_round_trip(self, tmp_path):
        """Instructions extract from pipeline and write to files."""
        pipeline = DossierPipeline()
        instructions = extract_instructions(pipeline)
        assert len(instructions) == 7

        # Create fake prompt files
        for phase_id, inst in instructions.items():
            filename = PHASE_PROMPT_FILES[phase_id]
            prompt_file = tmp_path / filename
            prompt_file.write_text(f"# Phase\n\nOriginal.\n\n## Steps\n1. Do thing\n")

        # Monkeypatch PROMPTS_DIR
        with patch("dspy.export.PROMPTS_DIR", tmp_path):
            export_to_prompts(pipeline, backup=False)

        # Verify instructions were written
        for phase_id, filename in PHASE_PROMPT_FILES.items():
            content = (tmp_path / filename).read_text()
            assert "## Steps" in content  # Steps preserved
            assert "Original." not in content  # Old instruction replaced

    def test_score_all_existing_dossiers(self, output_dir):
        """Score every completed dossier and print results."""
        if not output_dir.exists():
            pytest.skip("No output directory")
        examples = load_dossier_outputs(output_dir)
        if not examples:
            pytest.skip("No complete dossiers")

        print("\n  Dossier Quality Scores:")
        print("  " + "-" * 60)
        for ex in examples:
            domain_dir = output_dir / ex.domain
            dossier = load_single_dossier(domain_dir)
            scores = score_dossier(dossier)
            avg = sum(scores.values()) / len(scores)
            print(f"  {ex.domain:20s}  avg={avg:.3f}  " +
                  "  ".join(f"p{i}={scores[f'p{i}']:.2f}" for i in range(1, 8)))
