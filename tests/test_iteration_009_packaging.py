import os
import runpy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _assert_extended_tcl_paths(runtime_root: Path) -> None:
    expected_root = str(runtime_root.resolve()).replace("\\", "/")
    if sys.platform == "win32":
        expected_root = f"//?/{expected_root}"
    assert os.environ["TCL_LIBRARY"] == f"{expected_root}/_tcl_data"
    assert os.environ["TK_LIBRARY"] == f"{expected_root}/_tk_data"


def test_runtime_hook_uses_tcl_safe_bundle_paths(monkeypatch, tmp_path):
    monkeypatch.setattr(sys, "_MEIPASS", str(tmp_path), raising=False)

    runpy.run_path(str(ROOT / "packaging" / "pyi_rth_tkinter_portable.py"))

    _assert_extended_tcl_paths(tmp_path)


def test_portable_entry_reasserts_tcl_paths_before_app_import(monkeypatch, tmp_path):
    monkeypatch.setattr(sys, "_MEIPASS", str(tmp_path), raising=False)

    runpy.run_path(
        str(ROOT / "packaging" / "portable_entry.py"),
        run_name="iteration_009_packaging_test",
    )

    _assert_extended_tcl_paths(tmp_path)
