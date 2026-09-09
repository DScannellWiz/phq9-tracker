import os
import sys


def _tcl_safe_windows_path(path: str) -> str:
    """Keep Tcl from losing profile-directory components during normalization."""
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
