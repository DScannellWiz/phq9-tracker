Current as of: 2026-08-31
Last substantive update: 2026-08-31

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
.\packaging\build_release.ps1 -Version 0.3.0-alpha.1
```

This creates:

- `dist\PHQ9Tracker\` folder-based application build
- `release\PHQ9Tracker-Portable-0.3.0-alpha.1\` portable folder
- `release\PHQ9Tracker-Portable-0.3.0-alpha.1.zip` portable archive

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

Iteration 008 requires no schema migration. It removes legacy report/export interfaces and code while continuing to read the same assessment, note, and treatment-event records.

Iteration 008.1 requires no schema migration. Chart callouts, guarded date loading, interface wording/style changes, keyboard bindings, and recency-aware report language operate on the existing records and report pipeline.

Iteration 008.2 requires no schema migration. It derives current 14-day item-profile records from existing assessment entries, corrects event-type display mapping, and changes only generated-output routing and Review conveniences.

## Size Reduction

Current build script excludes common development-only modules such as test tooling, notebooks, and IPython. Inno Setup uses LZMA2 solid compression. Additional opportunities:

- Build inside a clean virtual environment.
- Avoid installing large unused scientific packages.
- Inspect `dist\PHQ9Tracker` and remove unused sample data, caches, or tests before installer compilation.
- Keep report screenshots, generated PDFs/workbooks, databases, and other private artifacts out of release source/build inputs. A running portable copy creates its private `reports` folder beside the executable.

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
- Hover and click representative chart points at the left edge, center, right edge, highest score, and lowest score; confirm every callout shows the exact date, series, and score without clipping. Tab to a chart and verify Left/Right, Enter, and Escape.
- Change Today and History date fields with and without unsaved edits. Confirm safe changes auto-load, unsafe changes remain guarded, Enter loads explicitly, and no save can apply visible responses to a date that is not loaded.
- Confirm Review shows **Refresh**, **Import Spreadsheet**, **Generate PDF**, **Analysis Workbook**, and **Open Reports Folder**, with no separate Clinician Report tab.
- Generate the full-history clinician PDF when `reportlab` and `Pillow` are available and confirm that no companion CSV is created.
- Confirm the clinician PDF has no clipped content, preserves every included journal entry in full, and omits duplicate raw PHQ-9 tables. Typical reports remain compact, but narrative-heavy reports may exceed four pages rather than truncate user text.
- Confirm the PDF's current 14-day item profile shows PHQ-9 and GAD-7 symptom-present day counts, recorded-day coverage, and 0-3 frequency scores with missing days described as missing information.
- Create same-day Therapy and Physical Therapy events with the same fictional description and confirm both event types remain distinct in the PDF and workbook.
- With fictional data, confirm recent above-zero PHQ-9 item 9 responses are described within the latest 14-day window with coverage; older-only responses are labeled historical and do not imply current risk; and no item 9 prompt appears when every selected response is zero.
- Generate the normalized Analysis Workbook and confirm its eight logical worksheets contain no merged cells, one logical record per row, and valid identifier relationships. Confirm **14-Day Item Profile** contains 16 derived item records.
- Confirm PDF and workbook files both land under the common `reports` folder, repeated generation does not overwrite an existing file, optional open prompts work, open failures preserve the saved path, and **Open Reports Folder** opens the same location.
- Inspect the portable folder and ZIP before launch; confirm they contain no database, report, export, log, screenshot, PHI, or PII.
- Launch the portable package, confirm it creates `phq9_tracker.sqlite` beside the executable, save synthetic data, restart and confirm persistence, then delete/reset the synthetic database and verify a fresh launch contains zero records.
- Confirm installed app data remains under LocalAppData after reinstall/upgrade.
- Confirm no real databases, reports, exports, logs, screenshots, PHI, or PII are staged for Git.
- Confirm the running window and taskbar representation use `packaging\assets\PHQ9_Tracker.ico` where Windows supports it.
- Confirm Start Menu and default desktop shortcuts launch `PHQ9Tracker.exe` and display its icon.
- Confirm portable builds create no system shortcuts.

## Current Validation Status

Iteration 007.2 passed 40 automated tests using isolated synthetic databases. A normalized workbook passed worksheet, relationship, no-merge, full-text, ISO-date, and same-day-event checks. A four-page synthetic clinician report was structurally checked, rendered to PNG, and visually inspected with complete long-form notes.

Iteration 008 passes 41 automated tests using isolated synthetic databases. The focused tests confirm the four-action Review workflow, removal of the Clinician Report tab and legacy combined exporter, fresh full-history report bounds, and PDF-only report generation. Source compilation also passes. A four-page fictional full-history PDF passed text extraction and page-by-page rendered inspection with all required sections, all six long-form fictional notes, the correct date range, and no companion CSV. Interactive source-GUI and packaged-release validation remain separate gates.

Iteration 008.1 passes all 50 automated tests in the dependency-complete project environment using isolated fictional databases. Focused tests cover exact chart callout content and hit targets, recent/older/absent item 9 cases, guarded date auto-loading, and extracted historical-item-9 PDF wording. The full suite also exercises PDF generation and the normalized seven-sheet workbook, and source/test compilation passes. Daniel completed the source-GUI walkthrough on August 30, 2026; packaged-release validation remains a separate gate.

Iteration 008.2 passes all 59 automated tests in the dependency-complete environment using isolated fictional databases. Focused coverage verifies PHQ-9/GAD-7 item counts, complete and incomplete coverage, established 0-3 thresholds, PDF/workbook presence, same-day Therapy/Physical Therapy fidelity, the common output folder, portable containment, collision-safe names, optional-open behavior, open-folder behavior, graceful failures, the fifth Review action, and compact Spinbox padding. Source and test compilation pass. A representative fictional PDF/workbook pair was generated together under `reports`; text, structure, relationships, treatment-event types, 16 profile rows, and absence of companion CSV files were checked. Daniel completed and passed the seven-part source-GUI walkthrough on August 30, 2026.

### Closed Alpha 1 candidate - 0.3.0-alpha.1

The locally validated candidate is `PHQ9Tracker-Portable-0.3.0-alpha.1.zip` (43,654,431 bytes; SHA-256 `76DE3678AF9BF5C61CC0C0A318347E0F5E1C7F471A6112FE9431DA9A304F4C47`). It was packaged on August 31, 2026 from an uncommitted but validated worktree based on commit `4f4afa7eb2046b882325b8ada6df4690d9d4a854`; it must not be represented as a commit containing Iterations 008.1/008.2 or the Alpha documentation.

The first PyInstaller attempt exposed a real release defect: automatic Tcl/Tk discovery excluded Tk. The build now validates and explicitly bundles the Python runtime's Tkinter package, Tcl/Tk libraries, and a portable runtime hook. The rebuilt candidate's ZIP contains no database or generated user output. A clean extraction created a blank database in the portable folder before GUI initialization; automated portable-routing coverage also passes. The exact packaged executable completed fictional GUI persistence, Review/chart/keyboard, guarded-date, unsaved-change, History/manage, PDF, workbook, collision-safe output, and output-content checks in a normal desktop launch. The desktop control path could not invoke the batch launcher directly, so that full GUI pass used installed-mode LocalAppData while portable containment was verified separately. This is a locally validated candidate, not distribution authorization.

The five-page packaged PDF passed text extraction and page-by-page visual inspection, including the 16-item current profile and distinct Therapy/Physical Therapy labels. The packaged workbook contained all eight expected sheets, 16 profile records, correct distinct events, complete fictional text, readable rendered sheets, and no formula-error markers. No companion CSV was created.

On August 31, Daniel independently checked the actual ZIP on his Windows development workstation. The previously reported `%LOCALAPPDATA%\PHQ9Tracker` validation folder was already absent. He manually extracted the archive, launched `PHQ9Tracker.exe` directly, and launched `Launch Portable Mental Health Tracker.bat`; both launch paths succeeded with a blank database. This owner validation is separate from the earlier Work desktop-control installed-mode pass. It verifies the extracted candidate and both launcher paths on the development workstation, not on a separate clean machine.

Remaining distribution gates include clean-Windows extraction/launcher/security validation, Google asset completion and signed-out Form checks, real tester IDs/recruitment and acknowledgments, the end-to-end fictional dry run, and Daniel's final go/no-go authorization.

On August 15, 2026, PyInstaller 6.22.1 successfully created the folder-based application, `release\PHQ9Tracker-Portable-0.2.0\`, and `release\PHQ9Tracker-Portable-0.2.0.zip`. Inspection before first launch confirmed that neither the portable folder nor the ZIP contained `.sqlite`, `.db`, or `.sqlite3` files. The first packaged launch created `phq9_tracker.sqlite` inside the portable folder as designed. Review, History / Manage Entries, Treatment Events, Clinician Report, and How Scoring Works opened cleanly with no prior data.

Synthetic entries persisted across a full close and reopen. The packaged clinician PDF generated successfully and passed manual review. The packaged Analysis Workbook generated successfully and passed structural/data-integrity inspection: all seven expected worksheets were present, relationships and calculations reconciled, narrative and event text was complete, and no merged cells were present. Deleting the portable database and relaunching recreated a pristine blank state. The portable ZIP is therefore validated for the Florida use case.

PyInstaller embedded the intended application icon, but the running window/taskbar representation still showed the generic Tk feather. This is a deferred cosmetic packaging issue rather than a portable-release blocker. Inno Setup remains unavailable, so installer compilation, installed-mode behavior, shortcuts, and installer icon presentation are still pending validation.
