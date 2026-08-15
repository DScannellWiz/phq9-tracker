Current as of: 2026-08-15
Last substantive update: 2026-08-15

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

The source launcher prefers a project-local `.venv` or `venv` when present. Report generation also checks `PHQ9_TRACKER_BUNDLED_PYTHON`, then those project-local environments, before reporting exactly which packages are unavailable.

The release script performs a dependency preflight before invoking PyInstaller. This fails early when report or export dependencies are missing instead of producing an incomplete package.

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

Portable builds retain the executable icon and create no system shortcuts. The launcher is named `Launch Portable Mental Health Tracker.bat`.

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

The installer deploys the folder-based app under Program Files, creates a Start Menu shortcut under **Mental Health Tracker**, selects desktop-shortcut creation by default, and registers an uninstaller in Windows Apps & Features. Both shortcuts explicitly use the executable's embedded Mental Health Tracker icon.

Installed builds store user data in:

```text
%LOCALAPPDATA%\PHQ9Tracker\phq9_tracker.sqlite
```

This preserves user data during upgrades because installer file replacement does not overwrite LocalAppData.

## Database Migration

Iteration 004 keeps the legacy `phq9_entries` table and adds `assessment_entries`.

On startup, existing PHQ-9 rows are copied into `assessment_entries` using `INSERT OR IGNORE`. GAD-7 entries are stored only in `assessment_entries`. This keeps older PHQ-9 behavior intact while giving future assessments a reusable storage path.

Iteration 006 requires no schema migration. It adds stable-ID update/delete operations over the existing tables, keeps legacy PHQ-9 rows synchronized, and prevents deleted PHQ-9 assessments from being recreated by the startup migration.

Iteration 007 also requires no schema migration. Date navigation, Review summaries, treatment-cycle windows, and the compact clinician report operate on the existing assessment, note, and treatment-event records.

Iteration 007.2 requires no schema migration. Its normalized analysis workbook derives stable relationships from existing assessment IDs, treatment-event IDs, and deterministic date/item identifiers.

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
- Navigate across month and year boundaries, confirm an existing date auto-loads, verify future dates are blocked, and confirm unsaved-change protection.
- Open Review and inspect recent, treatment-cycle, and long-term views using synthetic data.
- Generate clinician PDF and CSV report when `reportlab` and `Pillow` are available.
- Confirm the clinician PDF has no clipped content, preserves every selected-period journal entry in full, and omits duplicate raw PHQ-9 tables. Typical reports remain compact, but narrative-heavy reports may exceed four pages rather than truncate user text.
- Export CSV and Excel data-only spreadsheets.
- Export the normalized analysis workbook and confirm its seven logical worksheets contain no merged cells, one logical record per row, and valid identifier relationships.
- Inspect the portable folder and ZIP before launch; confirm they contain no database, report, export, log, screenshot, PHI, or PII.
- Launch the portable package, confirm it creates `phq9_tracker.sqlite` beside the executable, save synthetic data, restart and confirm persistence, then delete/reset the synthetic database and verify a fresh launch contains zero records.
- Confirm installed app data remains under LocalAppData after reinstall/upgrade.
- Confirm no real databases, reports, exports, logs, screenshots, PHI, or PII are staged for Git.
- Confirm the running window and taskbar representation use `packaging\assets\PHQ9_Tracker.ico` where Windows supports it.
- Confirm Start Menu and default desktop shortcuts launch `PHQ9Tracker.exe` and display its icon.
- Confirm portable builds create no system shortcuts.

## Current Validation Status

Iteration 007.2 passed 40 automated tests using isolated synthetic databases. A normalized workbook passed worksheet, relationship, no-merge, full-text, ISO-date, and same-day-event checks. A four-page synthetic clinician report was structurally checked, rendered to PNG, and visually inspected with complete long-form notes.

The portable database-routing test confirmed that portable mode selects a database beside the executable, persists synthetic data across a reopen, and returns to zero records after deletion and clean reinitialization. The actual executable/ZIP build could not be completed because PyInstaller was unavailable and its attempted workspace-only installation stalled; Inno Setup was also unavailable. Until a release workstation completes the package test, ZIP contents, executable launch behavior, shortcuts, and final Windows icon presentation remain unconfirmed packaging limitations.

An attempted source-GUI smoke test also stopped before window creation because the available bundled Python runtime could not locate a usable Tcl/Tk `init.tcl`. Automated logic, workbook, and PDF validation passed, but no interactive GUI result is claimed for this environment.
