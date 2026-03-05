"""DSPy optimization driver for Dossier pipeline.

Runs BootstrapFewShotWithRandomSearch on the DossierPipeline to find
optimal few-shot demonstrations. Handles rate-limit recovery by printing
the session_id for resume.

Usage::

    cd "/Volumes/OWC drive/Dev/dossier"
    PYTHONPATH=. dspy/.venv/bin/python -m dspy.compile --model sonnet
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Callable

import dspy  # Our proxy — re-exports installed dspy's classes + settings

from dspy.lm import ClaudeAgentLM
from dspy.loader import load_dossier_outputs, PHASE_EXPECTED_SECTIONS
from dspy.metrics import dossier_phase_metric
from dspy.modules import DossierPipeline

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"
COMPILED_DIR = PROJECT_ROOT / "dspy" / "compiled"


def make_metric_fn() -> Callable:
    """Return a metric function compatible with DSPy optimizers.

    The returned closure scores a P7 (FinalReport) prediction by blending:
    - gold_score: the pre-computed score from training data (30%)
    - computed_score: freshly computed from the prediction text (70%)

    This lets the optimizer reward both fidelity to known-good outputs and
    structural quality in generated outputs.
    """
    p7_sections = PHASE_EXPECTED_SECTIONS.get("p7", [])

    def metric_fn(example: Any, prediction: Any) -> float:
        # Extract gold score from training example
        scores = getattr(example, "scores", None) or {}
        gold_score = scores.get("p7", 0.0) if isinstance(scores, dict) else 0.0

        # Extract prediction text
        full_report = getattr(prediction, "full_report", "") or ""
        exec_summary = getattr(prediction, "executive_summary", "") or ""
        combined_text = f"{full_report}\n\n{exec_summary}"

        if not combined_text.strip():
            return 0.0

        # Compute fresh score from prediction
        computed_score = dossier_phase_metric(combined_text, p7_sections)

        # Blend: 70% computed (rewards optimizer exploration), 30% gold (anchors quality)
        return 0.7 * computed_score + 0.3 * gold_score

    return metric_fn


def compile_dossier(
    model: str = "sonnet",
    num_candidates: int = 3,
    max_bootstrapped_demos: int = 2,
    max_labeled_demos: int = 2,
    output_dir: Path = OUTPUT_DIR,
) -> Any:
    """Run BootstrapFewShotWithRandomSearch on the Dossier pipeline.

    Args:
        model: Claude model name for ClaudeAgentLM (e.g. 'sonnet', 'opus').
        num_candidates: Number of candidate programs to evaluate.
        max_bootstrapped_demos: Max few-shot demos from bootstrapping.
        max_labeled_demos: Max labeled demos to include.
        output_dir: Directory containing completed dossier outputs.

    Returns:
        The compiled (optimized) DossierPipeline.

    Raises:
        ValueError: If no training examples are found.
        RuntimeError: Re-raised after printing session_id on rate-limit errors.
    """
    # Configure LM backend — uses proxy's configure, which modifies the same
    # settings object that DSPy's predict module reads from
    lm = ClaudeAgentLM(model=model)
    dspy.configure(lm=lm)

    # Load training data
    print(f"Loading training data from {output_dir} ...")
    examples = load_dossier_outputs(output_dir)
    if not examples:
        raise ValueError(
            f"No training examples found in {output_dir}. "
            "Run at least one full dossier before compiling."
        )
    print(f"Loaded {len(examples)} training example(s).")

    # Build pipeline and metric
    pipeline = DossierPipeline()
    metric_fn = make_metric_fn()

    # Create optimizer
    optimizer = dspy.BootstrapFewShotWithRandomSearch(
        metric=metric_fn,
        num_candidate_programs=num_candidates,
        max_bootstrapped_demos=max_bootstrapped_demos,
        max_labeled_demos=max_labeled_demos,
    )

    # Run optimization with rate-limit recovery
    try:
        print(f"Starting optimization with {num_candidates} candidates ...")
        compiled_pipeline = optimizer.compile(
            pipeline,
            trainset=examples,
        )
    except RuntimeError as exc:
        if "rate limit" in str(exc).lower():
            session_id = getattr(lm, "_session_id", None)
            print(
                f"\n[RATE LIMITED] Session ID for resume: {session_id}\n"
                f"Re-run with --resume {session_id} once cooldown expires."
            )
        raise

    # Save compiled program
    save_path = COMPILED_DIR / "dossier_latest.json"
    COMPILED_DIR.mkdir(parents=True, exist_ok=True)
    compiled_pipeline.save(str(save_path))
    print(f"Compiled program saved to {save_path}")

    return compiled_pipeline


def main() -> None:
    """CLI entry point for the compile driver."""
    parser = argparse.ArgumentParser(
        description="Compile (optimize) the Dossier pipeline with DSPy."
    )
    parser.add_argument(
        "--model",
        default="sonnet",
        help="Claude model name (default: sonnet)",
    )
    parser.add_argument(
        "--num-candidates",
        type=int,
        default=3,
        help="Number of candidate programs (default: 3)",
    )
    parser.add_argument(
        "--max-bootstrapped-demos",
        type=int,
        default=2,
        help="Max bootstrapped few-shot demos (default: 2)",
    )
    parser.add_argument(
        "--max-labeled-demos",
        type=int,
        default=2,
        help="Max labeled demos (default: 2)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help=f"Training data directory (default: {OUTPUT_DIR})",
    )

    args = parser.parse_args()

    try:
        compile_dossier(
            model=args.model,
            num_candidates=args.num_candidates,
            max_bootstrapped_demos=args.max_bootstrapped_demos,
            max_labeled_demos=args.max_labeled_demos,
            output_dir=args.output_dir,
        )
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError:
        sys.exit(2)


if __name__ == "__main__":
    main()
