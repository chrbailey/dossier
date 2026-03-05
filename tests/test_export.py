"""Tests for exporting optimized instructions back to prompt files."""
from __future__ import annotations

from dspy.export import (
    extract_instructions,
    write_optimized_prompt,
    PHASE_PROMPT_FILES,
)


class TestPhasePromptFiles:
    def test_has_seven_entries(self):
        assert len(PHASE_PROMPT_FILES) == 7

    def test_all_files_exist(self, dossier_root):
        prompts_dir = dossier_root / "prompts"
        for phase_id, filename in PHASE_PROMPT_FILES.items():
            path = prompts_dir / filename
            assert path.exists(), f"Missing prompt file: {path}"


class TestExtractInstructions:
    def test_extracts_docstring_from_module(self):
        from dspy.modules import DossierPipeline
        pipeline = DossierPipeline()
        instructions = extract_instructions(pipeline)
        assert "p1" in instructions
        assert "p7" in instructions
        assert isinstance(instructions["p1"], str)
        assert len(instructions["p1"]) > 10


class TestWriteOptimizedPrompt:
    def test_writes_instruction_header(self, tmp_path):
        original = "# Phase 1: Discovery\n\nOriginal instructions here.\n\n## Steps\n1. Do thing\n"
        prompt_file = tmp_path / "p1-discovery.md"
        prompt_file.write_text(original)

        new_instruction = "Improved instruction from DSPy optimization."
        write_optimized_prompt(prompt_file, new_instruction)

        result = prompt_file.read_text()
        assert "Improved instruction from DSPy optimization." in result
        assert "## Steps" in result

    def test_preserves_steps_section(self, tmp_path):
        original = (
            "# Phase 4: Claims Validation\n\n"
            "Cross-reference marketing claims.\n\n"
            "## Steps\n\n"
            "### 4.1 Claims Extraction\n"
            "Extract from Phase 1.\n"
        )
        prompt_file = tmp_path / "p4-claims.md"
        prompt_file.write_text(original)

        write_optimized_prompt(prompt_file, "New DSPy-optimized instruction.")

        result = prompt_file.read_text()
        assert "New DSPy-optimized instruction." in result
        assert "### 4.1 Claims Extraction" in result

    def test_no_sections_only_title(self, tmp_path):
        original = "# Phase 7: Report\n\nSome instructions.\n"
        prompt_file = tmp_path / "p7-report.md"
        prompt_file.write_text(original)

        write_optimized_prompt(prompt_file, "Optimized report instruction.")

        result = prompt_file.read_text()
        assert "# Phase 7: Report" in result
        assert "Optimized report instruction." in result

    def test_original_instruction_replaced(self, tmp_path):
        original = "# Phase 2: Market\n\nOld instruction text.\n\n## Goal\nDo analysis.\n"
        prompt_file = tmp_path / "p2-market.md"
        prompt_file.write_text(original)

        write_optimized_prompt(prompt_file, "New instruction text.")

        result = prompt_file.read_text()
        assert "Old instruction text." not in result
        assert "New instruction text." in result
        assert "## Goal" in result
