Current as of: 2026-08-28
Last substantive update: 2026-08-28

# Roadmap

## Vision

Build a privacy-first, local-only mental health tracking application that helps users and clinicians identify meaningful trends over time while keeping sensitive health information under the user's control.

## Current Capabilities

- PHQ-9 daily tracking.
- GAD-7 daily tracking.
- Unified Today's Check-In workflow.
- Correct 14-day symptom-frequency scoring for PHQ-9 and GAD-7.
- Local SQLite storage.
- Multi-assessment dashboard.
- Full-history clinician PDF reports.
- Normalized multi-sheet XLSX analysis workbooks.
- Treatment event tracking.
- Daily notes.
- GitHub-ready project structure.
- Automated tests.
- Installer and portable build scripts.

## Completed Iteration 005

Iteration 005 began the Clarity and Insight work by making recent changes understandable at a glance.

Delivered:

- Executive summary at the beginning of the clinician PDF report.
- Adjacent 14-calendar-day comparisons for PHQ-9 and GAD-7.
- Neutral lower, higher, unchanged, and insufficient-data wording.
- Entry-coverage disclosure so missing check-ins are visible.
- Focused dashboard cards that reuse the same comparison logic.
- Automated comparison tests and rendered PDF validation with synthetic data.

## Completed Iteration 004

Iteration 004 introduced the reusable assessment framework and began the transition from PHQ-9 Tracker to Mental Health Tracker.

Delivered:

- Modular assessment definitions for PHQ-9 and GAD-7.
- New generic `assessment_entries` database table.
- Legacy PHQ-9 migration into the generic assessment table.
- Today's Check-In UI for PHQ-9, GAD-7, notes, and optional treatment events.
- Combined dashboard, reports, and exports.
- Tests for GAD-7 scoring, exports, migration, and dependency-gated report generation.

## Iteration 006: Completed

Iteration 006 delivered data integrity, scoring clarity, and application branding. Automated validation and manual source-GUI validation with the existing production database are complete. Real Windows portable-package validation was completed during Iteration 007.2; installer validation remains pending until Inno Setup is available.

Delivered:

- History / Manage Entries for date-based review, stable-ID assessment editing, note editing, and confirmed deletion.
- Existing-date detection and idempotent daily check-in resubmission.
- Multiple treatment-event checkboxes, explicit custom events, and an Add Another Treatment Event workflow.
- Consistent Daily Severity Score and 14-Day Symptom Frequency Score terminology.
- How Scoring Works guidance in the UI and clinician PDF, including coverage disclosure and the mindful-check-in principle.
- Window, executable, installer, Start Menu, and default desktop shortcut icon wiring.
- Focused automated tests for editing, deletion, migration safety, multiple events, and duplicate prevention.

## Iteration 007: Present-Focused Check-In and Meaningful Review

Delivered:

- Today's Check-In opens first, saves PHQ-9/GAD-7 before optional details, and keeps historical comparisons out of the present-tense assessment experience.
- Previous Day and Next Day navigation handles calendar rollover, existing-entry loading, future-date prevention, and unsaved-change protection.
- Review separates recent trends, current/previous ketamine-cycle observations, and long-term charts.
- Deterministic summaries use neutral, non-causal wording and disclose entry coverage.
- The clinician PDF is a two-to-four-page conversation aid centered on overall pattern, symptom highlights, timeline context, treatment-cycle observations, and discussion prompts.
- Duplicate PHQ-9 response tables and redundant raw-detail sections were removed from the primary PDF.
- Report dependency discovery and release-build preflight checks were improved.
- All 28 automated tests passed with isolated synthetic data, and a representative four-page PDF passed rendered visual inspection.

### Development Narrative and Decision Records

Formal development-narrative capture begins around Iteration 007. Earlier project history is documented as a high-level reconstruction rather than contemporaneous notes. Beginning with this iteration, the development journal and architecture decision records are part of the ongoing process for substantial product and architectural work.

## Iteration 007.1: Navigation and Review Polish

Status: Completed

Implemented small, observable refinements:

- Review charts redraw from live canvas dimensions after resizing and reserve separate vertical bands for the full title, legend, and plot.
- The visible primary-tab order begins with **Today's Check-In**, followed by **Review** and **History / Manage Entries**; startup remains on Today's Check-In.
- **History / Manage Entries** reuses the shared one-day calendar shift behavior for Previous Day and Next Day navigation.
- History has its own unsaved-change snapshot and confirmation, blocks future dates, loads existing records, and disables Next Day on the current date.
- Dates without assessments, notes, or treatment events show a calm manage-only empty state with record-changing controls disabled.
- Nine focused Iteration 007.1 tests were added; all 37 automated tests pass with the dependency-complete project virtual environment.

The project owner completed the manual source-GUI walkthrough against the canonical repository with real-world data. Tab order and startup selection, Review chart titles and resize behavior, History navigation and rollover, existing and empty dates, future-date blocking, and unsaved-change protection passed. This focused polish did not change scoring, storage, reports, exports, or the project's privacy boundary.

## Upcoming Iterations

### Iteration 007.2: Reporting & Analysis - Completed

Delivered:

- Added a separate analysis-ready Excel export with normalized **Daily Assessments**, **Item Responses**, **Notes**, **Treatment Events**, **Treatment Cycles**, and **Metadata** worksheets.
- Added a derived **Daily Summary** convenience worksheet while keeping the normalized worksheets authoritative.
- Used one logical record per row, snake_case field names, ISO dates, stable database-backed or deterministic export identifiers, and documented cross-sheet relationships without merged cells or decorative blank rows.
- Preserved the existing combined CSV/XLSX export for backward compatibility at the time; Iteration 008 later retired this legacy path in favor of the normalized Analysis Workbook.
- Moved a fuller **How to Read This Report** explanation to the beginning of the clinician report and clarified Daily Severity Score, 14-Day Symptom Frequency Score, coverage, and missing check-ins.
- Adopted the compact section flow **Recorded Period Overview**, **Recorded Symptom Trends**, **Treatment Context**, **Journal and Event Context**, and **Conversation Starters**.
- Removed journal-row and character limits. All user-authored notes in the selected period are included verbatim; report length may grow when the recorded narrative requires it.
- Preserved scoring, schema, database routing, legacy PHQ-9 compatibility, and multiple legitimate same-day treatment events.
- Added focused workbook, full-journal, and portable database routing/persistence/reset tests. All 40 automated tests pass with synthetic data.
- Generated and visually inspected a four-page synthetic clinician report.
- Built and validated the real Windows portable package with PyInstaller 6.22.1. The initial folder and ZIP contained no database files; first launch created the portable database in place; the primary screens opened blank; synthetic records persisted across restart; packaged PDF and Analysis Workbook outputs passed review; and database deletion followed by relaunch restored a pristine blank state.
- Validated `PHQ9Tracker-Portable-0.2.0.zip` for the Florida use case. The generic Tk runtime window/taskbar icon remains a deferred cosmetic issue, and installer validation remains pending because Inno Setup is unavailable.

### Future Data Portability & Recovery

Tentative concept; no iteration number is locked:

- Prepare a clean Travel Mode database that contains no historical records.
- Export only records created in that travel database and transactionally append them into an authoritative home database after validating schema, record identity, duplicates, and conflicts.
- After a confirmed import, clear the travel database, create a fresh blank database, and verify that it contains zero assessments, notes, and treatment events.
- Do not implement this as whole-database swapping or silent overwrite behavior.

### Future LAN Sharing

Tentative concept; no iteration number is locked:

- Keep one authoritative database local to a designated host.
- Let LAN clients communicate with an authenticated host/service that is solely responsible for SQLite access.
- Do not open the SQLite file directly over a Windows network share.
- Preserve the local-only boundary: no cloud relay, public Internet service, or automatic external synchronization.

### Iteration 008: Review and Clinician Report Workflow

Status: Implementation, automated source validation, and rendered synthetic-PDF validation complete; interactive GUI and packaged-release validation remain pending.

Delivered:

- Made Review the single access point for the four agreed actions: **Refresh**, **Import Spreadsheet**, **Generate PDF**, and **Analysis Workbook**.
- Removed the separate Clinician Report tab and its start/end-date controls.
- Made **Generate PDF** calculate the full available assessment-history range each time it is selected.
- Stopped creating a companion CSV beside the clinician PDF.
- Retired the legacy combined CSV/XLSX exporter, its Review and File-menu controls, and its command-line entry point.
- Kept the normalized seven-sheet Analysis Workbook as the sole data-export format.
- Preserved scoring, storage, report content, complete journal text, legacy PHQ-9 data compatibility, and the local-only privacy boundary without a schema migration.
- Added focused workflow/range tests and updated earlier report tests. All 41 automated tests pass with isolated synthetic databases, and source compilation passes.
- Generated and inspected a four-page fictional full-history PDF; all required sections and complete long-form notes were present, the date range was correct, and no companion CSV was created.

### Iteration 008.1: Chart Accessibility and Micro-UX

Status: Implementation, full automated validation, and fictional PDF text validation complete; Daniel's source-GUI walkthrough and packaged-release validation remain pending.

Delivered:

- Added graph point callouts that show the date, series, and exact score on hover or click. Charts can receive keyboard focus; Left/Right moves between points, Enter displays a point, and Escape clears the callout.
- Added forgiving but bounded point hit targets so value discovery does not depend on precisely tracing a small marker across a wide chart.
- Made valid changed date fields auto-load when focus moves away only if no unsaved edits could be lost. Dates with unsaved edits remain guarded, and saving is blocked when the typed date differs from the loaded check-in.
- Added Enter-to-load on Today and History date fields and F5 refresh; broader global shortcuts were deliberately avoided because their context could be ambiguous or destructive.
- Clarified loaded-date statuses, unsaved-change choices, permanent-deletion confirmations, and save/export completion messages.
- Made PHQ-9 item 9 report context and Conversation Starters recency-aware. Recent above-zero responses use the most recent 14 calendar days; older above-zero responses remain explicitly historical and do not imply current risk; prompts are omitted when no above-zero response exists; recent coverage and missing-information limits are disclosed.
- Applied consistent Segoe UI defaults, roomier notebook tabs, readable table rows, and more consistent button padding and Review action widths without adding a new UI dependency.
- Preserved scoring, the database schema and records, local-only privacy, complete journal text, and the PDF/Analysis Workbook output contracts.
- Added nine focused tests. All 50 automated tests pass in the dependency-complete environment, including PDF and workbook paths, and source compilation passes.

Deferred:

- User-configurable or scalable text and interface sizing remains a future accessibility enhancement because it requires a broader layout and minimum-size review.

## Security and Privacy

- Optional encrypted database.
- Optional application password.
- Password-protected PDF reports.
- Encrypted backup and restore.
- Password-manager-friendly unlock flow.

## Data Management

- Backup scheduling.
- Restore wizard.
- Database integrity verification.
- Explicit migration history tracking.

## Reporting

- More compact clinician report templates.
- Improved treatment effectiveness summaries.
- Better trend visualization.
- Symptom correlation charts.

## Architecture

- External assessment definition files.
- Reusable scoring and import adapters.
- Configurable questionnaires.
- Plugin-ready assessment library.

## Long-Term Direction

Support multiple validated mental health assessment instruments while remaining local-first, privacy-first, open source, easy to use, and clinically useful for discussion.
