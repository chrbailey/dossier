"""Tests for circuit breaker module."""
from __future__ import annotations

import pytest
from pathlib import Path

# Add scripts to path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from circuit_breaker import (
    ProgressFile,
    PhaseDependencies,
    PHASE_DEPENDENCIES,
    PHASE_FILES,
)


@pytest.fixture
def output_dir(tmp_path):
    """Create a temporary output directory with PROGRESS.md."""
    progress = tmp_path / "PROGRESS.md"
    progress.write_text(
        "# Dossier: test.com\n"
        "Started: 2026-03-10T00:00:00Z\n"
        "Iteration: 1\n\n"
        "## Phases\n"
        "- [x] P1 Discovery — completed 2026-03-10T00:05:00Z\n"
        "- [ ] P2 Market — pending\n"
        "- [ ] P3 Technical — IN PROGRESS\n"
        "- [ ] P4 Claims — pending\n"
        "- [ ] P5 Academic — pending\n"
        "- [ ] P6 Valuation — pending\n"
        "- [ ] P7 Report — pending\n"
    )
    return tmp_path


@pytest.fixture
def progress(output_dir):
    return ProgressFile(output_dir)


@pytest.fixture
def checker(progress):
    return PhaseDependencies(progress)


def _create_phase_output(output_dir: Path, phase: str, content: str = "# Phase output\nSome content here that is longer than 100 chars. " * 3) -> None:
    """Helper to create a phase output file."""
    (output_dir / PHASE_FILES[phase]).write_text(content)


class TestProgressFile:
    def test_read_existing(self, progress):
        content = progress.read()
        assert "Dossier: test.com" in content

    def test_read_missing(self, tmp_path):
        p = ProgressFile(tmp_path / "nonexistent")
        assert p.read() == ""

    def test_phase_status_completed(self, progress):
        assert progress.phase_status("P1") == "completed"

    def test_phase_status_in_progress(self, progress):
        assert progress.phase_status("P3") == "in_progress"

    def test_phase_status_pending(self, progress):
        assert progress.phase_status("P2") == "pending"

    def test_phase_status_from_output_file(self, output_dir):
        """If PROGRESS.md says pending but output file exists, trust the file."""
        _create_phase_output(output_dir, "P2")
        p = ProgressFile(output_dir)
        assert p.phase_status("P2") == "completed"

    def test_has_output_true(self, output_dir, progress):
        _create_phase_output(output_dir, "P1")
        assert progress.has_output("P1") is True

    def test_has_output_false(self, progress):
        assert progress.has_output("P2") is False

    def test_has_output_empty_file(self, output_dir, progress):
        (output_dir / PHASE_FILES["P2"]).write_text("short")
        assert progress.has_output("P2") is False

    def test_persist_failure(self, output_dir, progress):
        _create_phase_output(output_dir, "P1")
        progress.persist_failure("P3", "WebFetch denied")
        content = progress.read()
        assert "P3: Technical — FAILED" in content
        assert "WebFetch denied" in content
        assert "P1 (Discovery): available [required]" in content

    def test_persist_failure_updates_checkbox(self, progress):
        progress.persist_failure("P3", "timeout")
        content = progress.read()
        assert "[!] P3 Technical — FAILED" in content
        assert "[ ] P3" not in content

    def test_persist_success(self, progress):
        progress.persist_success("P3")
        content = progress.read()
        assert "[x] P3 Technical — completed" in content
        assert "[ ] P3" not in content

    def test_persist_success_overwrites_failure(self, progress):
        progress.persist_failure("P3", "first attempt failed")
        progress.persist_success("P3")
        content = progress.read()
        assert "[x] P3 Technical — completed" in content

    def test_all_statuses(self, progress):
        statuses = progress.all_statuses()
        assert statuses["P1"] == "completed"
        assert statuses["P3"] == "in_progress"
        assert statuses["P2"] == "pending"


class TestPhaseDependencies:
    def test_p1_can_always_run(self, checker):
        ok, reason = checker.can_run("P1")
        assert ok is True

    def test_p2_can_run_when_p1_has_output(self, output_dir, checker):
        _create_phase_output(output_dir, "P1")
        ok, reason = checker.can_run("P2")
        assert ok is True
        assert "OK" in reason

    def test_p2_cannot_run_without_p1(self, checker):
        ok, reason = checker.can_run("P2")
        assert ok is False
        assert "P1" in reason

    def test_p4_needs_p1_and_p3(self, output_dir, checker):
        # Only P1 available
        _create_phase_output(output_dir, "P1")
        ok, reason = checker.can_run("P4")
        assert ok is False
        assert "P3" in reason

        # Both available
        _create_phase_output(output_dir, "P3")
        ok, reason = checker.can_run("P4")
        assert ok is True

    def test_p4_warns_about_missing_optional(self, output_dir, checker):
        _create_phase_output(output_dir, "P1")
        _create_phase_output(output_dir, "P3")
        ok, reason = checker.can_run("P4")
        assert ok is True
        assert "missing optional" in reason
        assert "P2" in reason

    def test_p6_convergence_point(self, output_dir, checker):
        # P6 needs P1-P4 required, P5 optional
        for p in ["P1", "P2", "P3", "P4"]:
            _create_phase_output(output_dir, p)
        ok, reason = checker.can_run("P6")
        assert ok is True
        assert "P5" in reason  # warns about missing optional

    def test_unknown_phase(self, checker):
        ok, reason = checker.can_run("P99")
        assert ok is False
        assert "Unknown" in reason

    def test_get_runnable_phases_initial(self, tmp_path):
        """Only P1 should be runnable with empty PROGRESS.md."""
        (tmp_path / "PROGRESS.md").write_text("# Dossier: fresh.com\n")
        p = ProgressFile(tmp_path)
        checker = PhaseDependencies(p)
        runnable = checker.get_runnable_phases()
        assert "P1" in runnable

    def test_get_runnable_phases_after_p1(self, tmp_path):
        """P2, P3, P5 runnable after P1 completes."""
        (tmp_path / "PROGRESS.md").write_text("# Dossier: test.com\n")
        _create_phase_output(tmp_path, "P1")
        p = ProgressFile(tmp_path)
        checker = PhaseDependencies(p)
        runnable = checker.get_runnable_phases()
        assert "P2" in runnable
        assert "P3" in runnable
        assert "P5" in runnable
        assert "P4" not in runnable  # needs P3 too

    def test_status_summary(self, output_dir, checker):
        _create_phase_output(output_dir, "P1")
        summary = checker.status_summary()
        assert "Pipeline Status" in summary
        assert "P1" in summary
        assert "completed" in summary

    def test_completed_phases_not_runnable(self, output_dir):
        """Completed phases shouldn't appear in runnable list."""
        p = ProgressFile(output_dir)
        _create_phase_output(output_dir, "P1")
        checker = PhaseDependencies(p)
        runnable = checker.get_runnable_phases()
        assert "P1" not in runnable  # already completed per PROGRESS.md
