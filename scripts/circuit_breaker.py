"""Circuit breaker for Dossier phase pipeline.

Prevents cascade failures by:
1. Checking phase dependencies before dispatch
2. Loading fallback data from prior successful runs
3. Persisting structured failure/success blocks to PROGRESS.md

Usage (CLI):
    python scripts/circuit_breaker.py can-run P4 output/example.com
    python scripts/circuit_breaker.py fail P3 output/example.com "WebFetch denied"
    python scripts/circuit_breaker.py success P3 output/example.com
    python scripts/circuit_breaker.py status output/example.com
"""
from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Phase dependency DAG — single source of truth for the pipeline graph.
# Prompts/docs reference this; keep them in sync when editing here.
# P4.5 (Red Team) is a mandatory phase that attacks P4's conclusions before
# valuation, so P6 gates on it.
PHASE_DEPENDENCIES: Dict[str, Dict[str, List[str]]] = {
    "P1": {"required": [], "optional": []},
    "P2": {"required": ["P1"], "optional": []},
    "P3": {"required": ["P1"], "optional": []},
    "P5": {"required": ["P1"], "optional": []},
    "P4": {"required": ["P1", "P3"], "optional": ["P2", "P5"]},
    "P4.5": {"required": ["P1", "P3", "P4"], "optional": []},
    "P6": {"required": ["P1", "P2", "P3", "P4", "P4.5"], "optional": ["P5"]},
    "P7": {"required": ["P1", "P2", "P3", "P4", "P4.5", "P6"], "optional": ["P5"]},
}

PHASE_NAMES: Dict[str, str] = {
    "P1": "Discovery",
    "P2": "Market",
    "P3": "Technical",
    "P5": "Academic",
    "P4": "Claims",
    "P4.5": "Red Team",
    "P6": "Valuation",
    "P7": "Report",
}

PHASE_FILES: Dict[str, str] = {
    "P1": "01-discovery.md",
    "P2": "02-market.md",
    "P3": "03-technical.md",
    "P4": "04-claims.md",
    "P4.5": "04.5-red-team.md",
    "P5": "05-academic.md",
    "P6": "06-valuation.md",
    "P7": "07-report.md",
}


def _phase_re(phase: str) -> str:
    """Regex fragment matching a phase id in PROGRESS.md, without prefix
    collisions. `P4` must not match a `P4.5` line, so forbid a following
    digit or dot. The id may still be followed by a space (`P4 Claims`) or a
    colon (`## P4: Claims — FAILED`)."""
    return rf"{re.escape(phase)}(?![\d.])"


class ProgressFile:
    """Reads and writes structured PROGRESS.md state."""

    def __init__(self, output_dir: Path) -> None:
        self.output_dir = Path(output_dir)
        self.progress_path = self.output_dir / "PROGRESS.md"

    def read(self) -> str:
        if self.progress_path.exists():
            return self.progress_path.read_text()
        return ""

    def phase_status(self, phase: str) -> str:
        """Return 'completed', 'failed', 'in_progress', or 'pending'."""
        content = self.read()
        pr = _phase_re(phase)
        # Check for explicit status markers
        if re.search(
            rf"##\s+{pr}.*?FAILED", content, re.IGNORECASE | re.DOTALL
        ):
            return "failed"
        if re.search(
            rf"\[x\]\s+{pr}.*completed", content, re.IGNORECASE
        ):
            return "completed"
        if re.search(
            rf"\[ \]\s+{pr}.*IN PROGRESS", content, re.IGNORECASE
        ):
            return "in_progress"
        # Check if output file exists as ground truth
        output_file = self.output_dir / PHASE_FILES.get(phase, "")
        if output_file.exists() and output_file.stat().st_size > 100:
            return "completed"
        return "pending"

    def all_statuses(self) -> Dict[str, str]:
        return {p: self.phase_status(p) for p in PHASE_DEPENDENCIES}

    def has_output(self, phase: str) -> bool:
        """Check if phase has actual output file with content."""
        output_file = self.output_dir / PHASE_FILES.get(phase, "")
        return output_file.exists() and output_file.stat().st_size > 100

    def persist_failure(self, phase: str, error_msg: str) -> None:
        """Append structured failure block to PROGRESS.md."""
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        name = PHASE_NAMES.get(phase, phase)

        deps = PHASE_DEPENDENCIES.get(phase, {})
        required = deps.get("required", [])
        optional = deps.get("optional", [])

        input_status = []
        for dep in required:
            status = "available" if self.has_output(dep) else "MISSING"
            input_status.append(f"  - {dep} ({PHASE_NAMES.get(dep, dep)}): {status} [required]")
        for dep in optional:
            status = "available" if self.has_output(dep) else "missing"
            input_status.append(f"  - {dep} ({PHASE_NAMES.get(dep, dep)}): {status} [optional]")

        block = (
            f"\n\n## {phase}: {name} — FAILED\n"
            f"- **Error:** {error_msg}\n"
            f"- **Timestamp:** {timestamp}\n"
            f"- **Input status:**\n"
            + "\n".join(input_status)
            + "\n"
        )

        content = self.read()
        # Update checkbox if present
        content = re.sub(
            rf"\[ \]\s+{_phase_re(phase)}.*",
            f"[!] {phase} {name} — FAILED {timestamp}",
            content,
        )
        content += block
        self.progress_path.write_text(content)

    def persist_success(self, phase: str) -> None:
        """Update PROGRESS.md to reflect successful completion."""
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        name = PHASE_NAMES.get(phase, phase)

        content = self.read()
        # Update checkbox
        content = re.sub(
            rf"\[[ !]\]\s+{_phase_re(phase)}.*",
            f"[x] {phase} {name} — completed {timestamp}",
            content,
        )
        self.progress_path.write_text(content)


class PhaseDependencies:
    """Checks whether a phase can run given current pipeline state."""

    def __init__(self, progress: ProgressFile) -> None:
        self.progress = progress

    def can_run(self, phase: str) -> Tuple[bool, str]:
        """Check if phase can run. Returns (ok, reason)."""
        deps = PHASE_DEPENDENCIES.get(phase)
        if deps is None:
            return False, f"Unknown phase: {phase}"

        required = deps["required"]
        missing_required = []
        for dep in required:
            if not self.progress.has_output(dep):
                missing_required.append(dep)

        if missing_required:
            names = ", ".join(
                f"{p} ({PHASE_NAMES.get(p, p)})" for p in missing_required
            )
            return False, f"Missing required inputs: {names}"

        # Check optional — warn but don't block
        optional = deps["optional"]
        missing_optional = [
            p for p in optional if not self.progress.has_output(p)
        ]

        if missing_optional:
            names = ", ".join(
                f"{p} ({PHASE_NAMES.get(p, p)})" for p in missing_optional
            )
            return True, f"OK (missing optional: {names})"

        return True, "OK — all inputs available"

    def get_runnable_phases(self) -> List[str]:
        """Return list of phases that can run right now."""
        runnable = []
        for phase in PHASE_DEPENDENCIES:
            status = self.progress.phase_status(phase)
            if status in ("completed", "in_progress"):
                continue
            ok, _ = self.can_run(phase)
            if ok:
                runnable.append(phase)
        return runnable

    def status_summary(self) -> str:
        """Human-readable status of all phases."""
        lines = ["## Pipeline Status\n"]
        lines.append("| Phase | Name | Status | Can Run | Detail |")
        lines.append("|-------|------|--------|---------|--------|")

        for phase in ["P1", "P2", "P3", "P5", "P4", "P4.5", "P6", "P7"]:
            name = PHASE_NAMES.get(phase, phase)
            status = self.progress.phase_status(phase)
            ok, detail = self.can_run(phase)
            can_run = "YES" if ok else "NO"
            if status == "completed":
                can_run = "—"
                detail = "done"
            lines.append(f"| {phase} | {name} | {status} | {can_run} | {detail} |")

        return "\n".join(lines)


def main() -> None:
    """CLI entry point for sub-agent and Ralph Loop use."""
    if len(sys.argv) < 3:
        print("Usage: python scripts/circuit_breaker.py <command> <phase> <output_dir> [error_msg]")
        print("Commands: can-run, fail, success, status")
        sys.exit(1)

    command = sys.argv[1]
    output_dir_idx = 3 if command != "status" else 2

    if command == "status":
        output_dir = Path(sys.argv[2])
        progress = ProgressFile(output_dir)
        checker = PhaseDependencies(progress)
        print(checker.status_summary())
        runnable = checker.get_runnable_phases()
        if runnable:
            print(f"\nReady to dispatch: {', '.join(runnable)}")
        else:
            print("\nNo phases ready to dispatch.")
        return

    phase = sys.argv[2]
    output_dir = Path(sys.argv[3])
    progress = ProgressFile(output_dir)
    checker = PhaseDependencies(progress)

    if command == "can-run":
        ok, reason = checker.can_run(phase)
        print(f"{'YES' if ok else 'NO'}: {reason}")
        sys.exit(0 if ok else 1)

    elif command == "fail":
        error_msg = sys.argv[4] if len(sys.argv) > 4 else "Unknown error"
        progress.persist_failure(phase, error_msg)
        print(f"Recorded failure for {phase}: {error_msg}")

    elif command == "success":
        progress.persist_success(phase)
        print(f"Recorded success for {phase}")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
