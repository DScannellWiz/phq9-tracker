"""Fail-closed verification for the Windows release licensing inputs."""

from __future__ import annotations

import hashlib
import argparse
import importlib.metadata
import json
import os
import sqlite3
import ssl
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = Path(__file__).with_name("third_party_notice_manifest.json")
NOTICE_ROOT = ROOT / "THIRD_PARTY_NOTICES"


def tcl_safe_windows_path(path: Path) -> str:
    """Return an extended path so Tcl preserves sandboxed profile directories."""
    normalized = str(path.resolve()).replace("\\", "/")
    if sys.platform != "win32" or normalized.startswith("//?/"):
        return normalized
    if normalized.startswith("//"):
        return "//?/UNC/" + normalized.lstrip("/")
    return "//?/" + normalized


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--notice-only",
        action="store_true",
        help="Verify committed license text without checking the active Python runtime.",
    )
    args = parser.parse_args()
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    problems: list[str] = []

    if not args.notice_only:
        python_base = Path(sys.base_prefix)
        if sys.platform == "win32":
            os.environ["TCL_LIBRARY"] = tcl_safe_windows_path(
                python_base / "tcl" / "tcl8.6"
            )
            os.environ["TK_LIBRARY"] = tcl_safe_windows_path(
                python_base / "tcl" / "tk8.6"
            )
        import tkinter

        runtime = manifest["runtime"]
        tcl_patchlevel = "unavailable"
        tk_patchlevel = "unavailable"
        try:
            root = tkinter.Tk()
            root.withdraw()
            tcl_patchlevel = str(root.tk.call("info", "patchlevel"))
            tk_patchlevel = str(root.tk.call("package", "require", "Tk"))
            root.destroy()
        except tkinter.TclError as exc:
            problems.append(f"Tcl/Tk initialization failed: {exc}")
        actual_runtime = {
            "python": ".".join(map(str, sys.version_info[:3])),
            "openssl": ssl.OPENSSL_VERSION,
            "sqlite": sqlite3.sqlite_version,
            "tcl": tcl_patchlevel,
            "tk": tk_patchlevel,
        }
        for name, expected in runtime.items():
            actual = actual_runtime[name]
            if actual != expected:
                problems.append(f"runtime {name}: expected {expected!r}, found {actual!r}")

        for package_name, expected_version in manifest["packages"].items():
            try:
                actual_version = importlib.metadata.version(package_name)
            except importlib.metadata.PackageNotFoundError:
                problems.append(f"package {package_name}: not installed")
                continue
            if actual_version != expected_version:
                problems.append(
                    f"package {package_name}: expected {expected_version!r}, found {actual_version!r}"
                )

    expected_notice_paths = set(manifest["notices"])
    actual_notice_paths = {
        path.relative_to(NOTICE_ROOT).as_posix()
        for path in NOTICE_ROOT.rglob("*")
        if path.is_file() and path.name != "README.md"
    }
    missing = sorted(expected_notice_paths - actual_notice_paths)
    unexpected = sorted(actual_notice_paths - expected_notice_paths)
    if missing:
        problems.append(f"missing notice files: {missing}")
    if unexpected:
        problems.append(f"unexpected unmanifested notice files: {unexpected}")

    for relative_path, expected_hash in manifest["notices"].items():
        notice_path = NOTICE_ROOT / relative_path
        if notice_path.is_file():
            actual_hash = sha256(notice_path)
            if actual_hash != expected_hash:
                problems.append(
                    f"notice {relative_path}: expected SHA-256 {expected_hash}, found {actual_hash}"
                )

    project_license = ROOT / "LICENSE"
    expected_project_hash = manifest["project_license_sha256"]
    if not project_license.is_file():
        problems.append("project LICENSE is missing")
    elif sha256(project_license) != expected_project_hash:
        problems.append("project LICENSE does not match the recorded canonical GPLv3 text")

    if problems:
        print("Release licensing verification FAILED:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print(
        "Release licensing verification passed: "
        f"{len(expected_notice_paths)} notice files"
        + ("." if args.notice_only else f" and {len(manifest['packages'])} package versions.")
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
