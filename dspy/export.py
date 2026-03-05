"""Export optimized DSPy instructions back to Dossier prompt markdown files.

Replaces the instruction paragraph (between the # title and ## Steps) in each
phase prompt file with the DSPy-optimized instruction. Preserves all other content.
"""
from __future__ import annotations

import re
import shutil
from datetime import datetime
from pathlib import Path

from dspy.modules import DossierPipeline

DOSSIER_ROOT = Path(__file__).parent.parent
PROMPTS_DIR = DOSSIER_ROOT / "prompts"

PHASE_PROMPT_FILES: dict[str, str] = {
    "p1": "p1-discovery.md",
    "p2": "p2-market.md",
    "p3": "p3-technical.md",
    "p4": "p4-claims.md",
    "p5": "p5-academic.md",
    "p6": "p6-valuation.md",
    "p7": "p7-report.md",
}


def extract_instructions(pipeline: DossierPipeline) -> dict[str, str]:
    """Extract the current instruction (docstring) from each phase module.

    After DSPy optimization, these docstrings contain the optimized instructions.
    """
    instructions: dict[str, str] = {}
    for phase_id, module in pipeline.phases.items():
        sig_cls = module.signature_cls
        doc = sig_cls.__doc__ or ""
        instructions[phase_id] = doc.strip()
    return instructions


def write_optimized_prompt(prompt_file: Path, new_instruction: str) -> None:
    """Replace the instruction section in a prompt file.

    The instruction is the text between the first # heading and the first ## heading.
    Everything from ## onward is preserved as-is.
    """
    content = prompt_file.read_text()

    # Find the first ## heading (Steps, Goal, etc.)
    match = re.search(r"^(## .+)$", content, re.MULTILINE)

    if match:
        after_steps = content[match.start():]

        # Preserve the # title line
        title_match = re.match(r"^(# .+\n)", content)
        title = title_match.group(1) if title_match else ""

        new_content = f"{title}\n{new_instruction}\n\n{after_steps}"
    else:
        title_match = re.match(r"^(# .+\n)", content)
        title = title_match.group(1) if title_match else ""
        new_content = f"{title}\n{new_instruction}\n"

    prompt_file.write_text(new_content)


def export_to_prompts(pipeline: DossierPipeline, backup: bool = True) -> None:
    """Export all optimized instructions from a compiled pipeline to prompt files.

    Args:
        pipeline: The optimized DossierPipeline from DSPy compilation
        backup: If True, create timestamped backup of original prompts
    """
    instructions = extract_instructions(pipeline)

    if backup:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_dir = PROMPTS_DIR / f"backup-{timestamp}"
        backup_dir.mkdir(exist_ok=True)
        for filename in PHASE_PROMPT_FILES.values():
            src = PROMPTS_DIR / filename
            if src.exists():
                shutil.copy2(src, backup_dir / filename)

    for phase_id, instruction in instructions.items():
        filename = PHASE_PROMPT_FILES.get(phase_id)
        if not filename:
            continue
        prompt_file = PROMPTS_DIR / filename
        if not prompt_file.exists():
            continue
        write_optimized_prompt(prompt_file, instruction)

    print(f"Exported optimized instructions to {PROMPTS_DIR}")
    if backup:
        print(f"Originals backed up to {backup_dir}")
