"""Tests for the DSPy compile driver."""
from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch, call

import pytest

from dspy.compile import make_metric_fn, compile_dossier, _import_dspy_optimizer


class TestImportDspyOptimizer:
    def test_returns_expected_symbols(self):
        result = _import_dspy_optimizer()
        # Returns a 4-tuple: (BootstrapFewShotWithRandomSearch, Example, Prediction, configure)
        assert len(result) == 4
        BFRS, Example, Prediction, configure = result
        assert BFRS is not None
        assert callable(configure)


class TestMakeMetricFn:
    def test_returns_callable(self):
        fn = make_metric_fn()
        assert callable(fn)

    def test_scores_example_with_prediction(self):
        fn = make_metric_fn()
        # Create mock example and prediction without dspy imports
        example = MagicMock()
        example.scores = {"p7": 0.8}

        prediction = MagicMock()
        prediction.full_report = (
            "## Executive Summary\nGood\n"
            "## Confidence Matrix\nHigh\n"
            "## Next Steps\nDo things"
        )
        prediction.executive_summary = (
            "## Key Strengths\n1. Good\n"
            "## Key Risks\n1. Bad"
        )

        score = fn(example, prediction)
        assert isinstance(score, float)
        assert 0.0 <= score <= 1.0

    def test_scores_zero_for_empty_prediction(self):
        fn = make_metric_fn()
        example = MagicMock()
        example.scores = {"p7": 0.8}

        prediction = MagicMock()
        prediction.full_report = ""
        prediction.executive_summary = ""

        score = fn(example, prediction)
        assert isinstance(score, float)
        assert score == 0.0

    def test_blends_gold_and_computed(self):
        """The metric should blend gold score (from example) with computed score."""
        fn = make_metric_fn()
        example = MagicMock()
        # High gold score
        example.scores = {"p7": 1.0}

        prediction = MagicMock()
        # Prediction with some structure
        prediction.full_report = (
            "## Executive Summary\nGood\n"
            "## Confidence Matrix\nHigh\n"
            "## Next Steps\nDo things"
        )
        prediction.executive_summary = "## Key Strengths\n1. A"

        score_high_gold = fn(example, prediction)

        # Low gold score
        example.scores = {"p7": 0.0}
        score_low_gold = fn(example, prediction)

        # Higher gold should give higher blended score
        assert score_high_gold > score_low_gold

    def test_handles_missing_scores_key(self):
        """Should not crash if example.scores is missing."""
        fn = make_metric_fn()
        example = MagicMock()
        example.scores = {}

        prediction = MagicMock()
        prediction.full_report = "## Executive Summary\nGood"
        prediction.executive_summary = "Good"

        score = fn(example, prediction)
        assert isinstance(score, float)
        assert 0.0 <= score <= 1.0

    def test_handles_missing_prediction_attrs(self):
        """Should handle prediction missing full_report gracefully."""
        fn = make_metric_fn()
        example = MagicMock()
        example.scores = {"p7": 0.5}

        prediction = MagicMock(spec=[])  # Empty spec = no attributes

        score = fn(example, prediction)
        assert isinstance(score, float)
        assert score >= 0.0


class TestCompileDossier:
    @patch("dspy.compile._import_dspy_optimizer")
    @patch("dspy.compile.load_dossier_outputs")
    @patch("dspy.compile.ClaudeAgentLM")
    def test_compile_basic_flow(
        self, mock_lm_cls, mock_load, mock_import_optimizer
    ):
        """Verify compile_dossier wires up optimizer correctly."""
        # Set up the installed dspy mocks
        mock_configure = MagicMock()
        mock_BFRS = MagicMock()
        mock_Example = MagicMock()
        mock_Prediction = MagicMock()
        mock_import_optimizer.return_value = (
            mock_BFRS,
            mock_Example,
            mock_Prediction,
            mock_configure,
        )

        # Mock the optimizer instance and its compile method
        mock_optimizer_instance = MagicMock()
        mock_compiled_program = MagicMock()
        mock_compiled_program.save = MagicMock()
        mock_optimizer_instance.compile.return_value = mock_compiled_program
        mock_BFRS.return_value = mock_optimizer_instance

        # Mock training data
        mock_example = MagicMock()
        mock_example.scores = {"p7": 0.8}
        mock_load.return_value = [mock_example]

        # Mock LM
        mock_lm = MagicMock()
        mock_lm._session_id = "sess_123"
        mock_lm_cls.return_value = mock_lm

        result = compile_dossier(
            model="sonnet",
            num_candidates=2,
            max_bootstrapped_demos=1,
            max_labeled_demos=1,
        )

        # Verify configure was called with our LM
        mock_configure.assert_called_once()
        # Verify optimizer was created
        mock_BFRS.assert_called_once()
        # Verify compile was called
        mock_optimizer_instance.compile.assert_called_once()
        # Verify result is the compiled program
        assert result is mock_compiled_program

    @patch("dspy.compile._import_dspy_optimizer")
    @patch("dspy.compile.load_dossier_outputs")
    @patch("dspy.compile.ClaudeAgentLM")
    def test_compile_saves_to_disk(
        self, mock_lm_cls, mock_load, mock_import_optimizer, tmp_path
    ):
        """Verify the compiled program is saved to disk."""
        mock_configure = MagicMock()
        mock_BFRS = MagicMock()
        mock_Example = MagicMock()
        mock_Prediction = MagicMock()
        mock_import_optimizer.return_value = (
            mock_BFRS,
            mock_Example,
            mock_Prediction,
            mock_configure,
        )

        mock_optimizer_instance = MagicMock()
        mock_compiled = MagicMock()
        mock_compiled.save = MagicMock()
        mock_optimizer_instance.compile.return_value = mock_compiled
        mock_BFRS.return_value = mock_optimizer_instance

        mock_lm = MagicMock()
        mock_lm._session_id = None
        mock_lm_cls.return_value = mock_lm

        mock_example = MagicMock()
        mock_example.scores = {"p7": 0.5}
        mock_load.return_value = [mock_example]

        with patch("dspy.compile.COMPILED_DIR", tmp_path):
            result = compile_dossier(model="sonnet")

        # save() should have been called
        mock_compiled.save.assert_called_once()

    @patch("dspy.compile._import_dspy_optimizer")
    @patch("dspy.compile.load_dossier_outputs")
    @patch("dspy.compile.ClaudeAgentLM")
    def test_compile_no_training_data_raises(
        self, mock_lm_cls, mock_load, mock_import_optimizer
    ):
        """Should raise ValueError when no training data is found."""
        mock_configure = MagicMock()
        mock_BFRS = MagicMock()
        mock_Example = MagicMock()
        mock_Prediction = MagicMock()
        mock_import_optimizer.return_value = (
            mock_BFRS,
            mock_Example,
            mock_Prediction,
            mock_configure,
        )

        mock_lm = MagicMock()
        mock_lm_cls.return_value = mock_lm

        mock_load.return_value = []  # No training data

        with pytest.raises(ValueError, match="No training examples"):
            compile_dossier(model="sonnet")

    @patch("dspy.compile._import_dspy_optimizer")
    @patch("dspy.compile.load_dossier_outputs")
    @patch("dspy.compile.ClaudeAgentLM")
    def test_compile_rate_limit_recovery(
        self, mock_lm_cls, mock_load, mock_import_optimizer, capsys
    ):
        """Rate limit errors should print session_id for recovery."""
        mock_configure = MagicMock()
        mock_BFRS = MagicMock()
        mock_Example = MagicMock()
        mock_Prediction = MagicMock()
        mock_import_optimizer.return_value = (
            mock_BFRS,
            mock_Example,
            mock_Prediction,
            mock_configure,
        )

        mock_optimizer_instance = MagicMock()
        mock_optimizer_instance.compile.side_effect = RuntimeError(
            "rate limit exceeded"
        )
        mock_BFRS.return_value = mock_optimizer_instance

        mock_lm = MagicMock()
        mock_lm._session_id = "sess_abc123"
        mock_lm_cls.return_value = mock_lm

        mock_example = MagicMock()
        mock_example.scores = {"p7": 0.5}
        mock_load.return_value = [mock_example]

        with pytest.raises(RuntimeError, match="rate limit"):
            compile_dossier(model="sonnet")

        captured = capsys.readouterr()
        assert "sess_abc123" in captured.out

    @patch("dspy.compile._import_dspy_optimizer")
    @patch("dspy.compile.load_dossier_outputs")
    @patch("dspy.compile.ClaudeAgentLM")
    def test_compile_passes_optimizer_params(
        self, mock_lm_cls, mock_load, mock_import_optimizer
    ):
        """Verify optimizer params are forwarded correctly."""
        mock_configure = MagicMock()
        mock_BFRS = MagicMock()
        mock_Example = MagicMock()
        mock_Prediction = MagicMock()
        mock_import_optimizer.return_value = (
            mock_BFRS,
            mock_Example,
            mock_Prediction,
            mock_configure,
        )

        mock_optimizer_instance = MagicMock()
        mock_compiled = MagicMock()
        mock_compiled.save = MagicMock()
        mock_optimizer_instance.compile.return_value = mock_compiled
        mock_BFRS.return_value = mock_optimizer_instance

        mock_lm = MagicMock()
        mock_lm._session_id = None
        mock_lm_cls.return_value = mock_lm

        mock_example = MagicMock()
        mock_example.scores = {"p7": 0.5}
        mock_load.return_value = [mock_example]

        compile_dossier(
            model="opus",
            num_candidates=5,
            max_bootstrapped_demos=3,
            max_labeled_demos=4,
        )

        # Check BFRS was created with correct params
        bfrs_kwargs = mock_BFRS.call_args
        assert bfrs_kwargs.kwargs.get("num_candidate_programs") == 5 or \
            bfrs_kwargs[1].get("num_candidate_programs") == 5
        assert bfrs_kwargs.kwargs.get("max_bootstrapped_demos") == 3 or \
            bfrs_kwargs[1].get("max_bootstrapped_demos") == 3
        assert bfrs_kwargs.kwargs.get("max_labeled_demos") == 4 or \
            bfrs_kwargs[1].get("max_labeled_demos") == 4

        # Check LM model was "opus"
        mock_lm_cls.assert_called_once_with(model="opus")
