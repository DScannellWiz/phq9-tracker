"""PyInstaller entry point that stabilizes Tcl/Tk paths before app import."""

from __future__ import annotations

import os
import sys


def _tcl_safe_windows_path(path: str) -> str:
    normalized = os.path.abspath(path).replace("\\", "/")
    if os.name != "nt" or normalized.startswith("//?/"):
        return normalized
    if normalized.startswith("//"):
        return "//?/UNC/" + normalized.lstrip("/")
    return "//?/" + normalized


runtime_root = getattr(sys, "_MEIPASS", None)
if runtime_root:
    safe_runtime_root = _tcl_safe_windows_path(runtime_root)
    os.environ["TCL_LIBRARY"] = f"{safe_runtime_root}/_tcl_data"
    os.environ["TK_LIBRARY"] = f"{safe_runtime_root}/_tk_data"

from phq9_tracker.app import main


if __name__ == "__main__":
    main()
