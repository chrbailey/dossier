"""Local DSPy integration — proxies to installed dspy for framework internals.

Our local dspy/ directory shadows the installed dspy package. This __init__.py
pre-populates sys.modules with the installed package's submodules so that
DSPy internals (e.g. dspy.predict.parameter) resolve correctly at runtime,
while keeping our local modules (dspy.lm, dspy.signatures, etc.) accessible.
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

# Names of OUR local modules — these must NOT be overwritten by the installed dspy
_LOCAL_MODULES = frozenset({
    "dspy.lm", "dspy.signatures", "dspy.modules",
    "dspy.metrics", "dspy.loader", "dspy.compile", "dspy.export",
    "dspy.__main__",
})


def _install_real_dspy():
    """Import installed dspy and populate sys.modules with its submodules."""
    project_root = str(Path(__file__).resolve().parent.parent)
    orig_path = sys.path[:]

    # Temporarily remove project root so installed dspy is found
    sys.path = [p for p in sys.path if p and str(Path(p).resolve()) != project_root]

    # Clear ALL dspy entries from module cache
    saved_local = {}
    for key in list(sys.modules):
        if key == "dspy" or key.startswith("dspy."):
            saved_local[key] = sys.modules.pop(key)

    # Import the real dspy — populates sys.modules with dspy.predict, etc.
    real_dspy = importlib.import_module("dspy")

    # Force-load key submodules that DSPy internals need
    for submod in ["dspy.predict", "dspy.predict.parameter", "dspy.primitives",
                   "dspy.primitives.base_module", "dspy.teleprompt"]:
        try:
            importlib.import_module(submod)
        except ImportError:
            pass

    # Capture installed submodule entries, EXCLUDING our local module names
    real_submodules = {}
    for k, v in sys.modules.items():
        if k.startswith("dspy.") and k not in _LOCAL_MODULES:
            real_submodules[k] = v

    # Restore path
    sys.path = orig_path

    # Clear everything again
    for key in list(sys.modules):
        if key == "dspy" or key.startswith("dspy."):
            del sys.modules[key]

    # Restore our local saved modules (if any were loaded before)
    sys.modules.update(saved_local)

    # Install all real submodules (dspy.predict, dspy.primitives, etc.)
    # but NEVER overwrite our local modules
    for k, v in real_submodules.items():
        if k not in sys.modules and k not in _LOCAL_MODULES:
            sys.modules[k] = v

    return real_dspy


_real_dspy = _install_real_dspy()

# Re-export commonly used symbols from the installed dspy
BaseLM = _real_dspy.BaseLM
Signature = _real_dspy.Signature
Module = _real_dspy.Module
ChainOfThought = _real_dspy.ChainOfThought
Prediction = _real_dspy.Prediction
Example = _real_dspy.Example
InputField = _real_dspy.InputField
OutputField = _real_dspy.OutputField
configure = _real_dspy.configure
