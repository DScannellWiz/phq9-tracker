# Build and Release Notes

## Packaging Choice

Use a folder-based PyInstaller build (`--onedir`) rather than a single-file executable. This keeps startup faster, makes troubleshooting easier, reduces antivirus false positives, and supports bundled assets and future report templates more cleanly.

The executable name remains `PHQ9Tracker.exe` for backward compatibility during the transition, while the visible application name is now **Mental Health Tracker**.

## Dependencies

Recommended build environment:

- Python 3.12 or 3.13 from python.org with Tcl/Tk installed
- `pandas`
- `openpyxl`
- `Pillow`
- `reportlab`
- `pypdfium2` for screenshot/PDF verification
- `pyinstaller`
- Inno Setup 6 for the Windows installer

Install example:

```powershell
python -m pip install pandas openpyxl Pillow reportlab pypdfium2 pyinstaller
```

## Build Executable and Portable Version

```powershell
cd <project-root>
.\packaging\build_release.ps1 -Version 0.2.0
```

This creates:

- `dist\PHQ9Tracker\` folder-based application build
- `release\PHQ9Tracker-Portable-0.2.0\` portable folder
- `release\PHQ9Tracker-Portable-0.2.0.zip` portable archive

The portable launcher sets `PHQ9_TRACKER_PORTABLE=1`, which keeps `phq9_tracker.sqlite` inside the portable folder.

## Application Icon

The build uses the existing icon asset:

```text
packaging\assets\PHQ9_Tracker.ico
```

This icon was copied from the user's shared application icon template folder and should remain a checked-in packaging asset unless replaced intentionally in a future branding iteration.

## Build Installer

Install Inno Setup, then compile:

```powershell
iscc .\packaging\PHQ9Tracker.iss
```

The installer deploys the folder-based app under Program Files, creates Start Menu shortcuts under **Mental Health Tracker**, optionally creates a desktop shortcut, and registers an uninstaller in Windows Apps & Features.

Installed builds store user data in:

```text
%LOCALAPPDATA%\PHQ9Tracker\phq9_tracker.sqlite
```

This preserves user data during upgrades because installer file replacement does not overwrite LocalAppData.

## Database Migration

Iteration 004 keeps the legacy `phq9_entries` table and adds `assessment_entries`.

On startup, existing PHQ-9 rows are copied into `assessment_entries` using `INSERT OR IGNORE`. GAD-7 entries are stored only in `assessment_entries`. This keeps older PHQ-9 behavior intact while giving future assessments a reusable storage path.

## Size Reduction

Current build script excludes common development-only modules such as test tooling, notebooks, and IPython. Inno Setup uses LZMA2 solid compression. Additional opportunities:

- Build inside a clean virtual environment.
- Avoid installing large unused scientific packages.
- Inspect `dist\PHQ9Tracker` and remove unused sample data, caches, or tests before installer compilation.
- Keep report screenshots, generated PDFs, databases, and exports out of the packaged app folder.

## Versioning

Update these together for each release:

- `packaging\build_release.ps1` `-Version`
- `packaging\PHQ9Tracker.iss` `MyAppVersion`
- Release zip and installer filenames

## Validation Checklist

- Launch installed app.
- Launch portable app.
- Confirm existing PHQ-9 database rows migrate into `assessment_entries`.
- Save a Today's Check-In with PHQ-9, GAD-7, notes, and optional treatment event.
- Generate clinician PDF and CSV report when `reportlab` and `Pillow` are available.
- Export CSV and Excel data-only spreadsheets.
- Confirm installed app data remains under LocalAppData after reinstall/upgrade.
- Confirm no real databases, reports, exports, logs, screenshots, PHI, or PII are staged for Git.
