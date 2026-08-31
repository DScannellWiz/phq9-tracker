Current as of: 2026-08-30
Last substantive update: 2026-08-30

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

Status: Completed after Daniel's 2026-08-30 source-GUI walkthrough. Packaged-release validation remains a separate gate.

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
- Daniel confirmed that chart date/score correlation appeared correct, keyboard chart navigation worked, date changes and unsaved-change protection worked, the overall look and feel was acceptable, and several days of ordinary use revealed no general-use issues.
- A non-blocking internal gap between each Spinbox's up/down arrows was carried into 008.2 as minimal visual polish. The walkthrough did not validate packaged 008.1 behavior.

Deferred:

- User-configurable or scalable text and interface sizing remains a future accessibility enhancement because it requires a broader layout and minimum-size review.

### Iteration 008.2: Clinician Output Fidelity and Alpha Output Polish

Status: Complete. Daniel passed the source-GUI walkthrough on August 30, 2026. Closed Alpha candidate `0.3.0-alpha.1` subsequently passed local packaging and fictional packaged validation; distribution remains a separate gate.

Delivered:

- Restore a compact current 14-day symptom profile for PHQ-9 and GAD-7 in the clinician-facing outputs. For each item, present the symptom-present day count and recorded-day coverage as appropriate together with the resulting 0-3 **14-Day Symptom Frequency Score**.
- Reuse the established daily item responses and 14-calendar-day scoring logic. Treat the missing presentation as a regression, not data loss or a scoring-formula defect.
- Preserve the concise conversation-focused PDF and normalized Analysis Workbook purposes; do not bring back the redundant raw-response tables removed in Iteration 007.
- Correct clinician-PDF treatment-event labeling so distinct stored types remain distinguishable. In particular, **Physical Therapy** must not be rendered as counseling **Therapy**, even when the two events share a date and description.
- Add focused regression tests for both assessment types and for two legitimate same-day treatment events with the same description but different stored types. Confirm that the Analysis Workbook preserves the distinct event types.
- Added a normalized **14-Day Item Profile** sheet with one logical current-window record per assessment item; this avoids repeating derived snapshot fields on daily response rows.
- Made `reports` the one generated-output folder for PDF and XLSX files. Portable builds keep it inside the extracted application folder; source runs keep it under the repository.
- Added collision-safe automatic filenames, optional open-after-save prompts, graceful open-failure messages that preserve the saved path, and an **Open Reports Folder** fifth Review action.
- Tightened Spinbox internal arrow padding while retaining spacing between questionnaire items.
- Deliberately deferred user-defined output locations because persistent paths, permissions, removable drives, and settings behavior require a separate design and validation pass before Alpha.

Non-goals:

- No database migration, scoring change, record correction, or deletion of the valid 2026-08-11 events.
- No broader clinician-report redesign, reintroduction of legacy export paths, user-configurable output destination, or database migration.
- The Treatment Cycles comparison chart remains unchanged. A future iteration may overlay the current ketamine cycle and the two previous cycles on one chart using three distinct colors.

### Closed Alpha Program - Planning

Status: Alpha Test Plan v0.2 and Closed Alpha Participation Acknowledgment v0.1 establish the approved baseline. Candidate `0.3.0-alpha.1` is locally packaged and validated. The Tester Guide now contains the real build, ZIP filename, and locally established Windows compatibility; download and Form URLs remain pending. Clean-Windows validation, tester selection, Google completion, final dry run, and distribution authorization remain pending.

Working baseline:

- Target a two-week closed alpha from Friday, September 4 through Friday, September 18, 2026.
- Distribute a validated Windows portable ZIP with a blank local database to an initial deliberately recruited cohort of approximately 5-8 testers.
- Keep the program free to use, with no financial or material compensation, and focused solely on the software, distribution, documentation, usability, reliability, data integrity, workflows, and generated-output usability.
- Preserve local-first handling: testers retain and control their own databases, reports, and exports. The program does not request, collect, retain, or analyze participant health data, outcomes, or tracker-entered content, whether real or fictional.
- Use tester IDs such as `MHT-A001`, a Daniel-only identity roster targeted for destruction 30 days after closeout, Google Forms without file uploads, brief first-use/midpoint/final surveys, and `projectmentalhealthtracker@gmail.com` for software/administrative support only.
- Allow participants to stop and delete their data at any time, and state that the alpha is not diagnostic/treatment software or the sole repository for important health information.
- Recruit deliberately before broader LinkedIn outreach.
- Defer a separate clinician-review track until Closed Alpha 1 feedback is incorporated into a stable candidate report; use only project-created fictional reports when that track begins.
- Require [Closed Alpha Participation Acknowledgment v0.1](docs/alpha/Closed_Alpha_Participation_Acknowledgment_v0.1.md) before software distribution and record the version and acceptance date for each tester.
- Use [Closed Alpha Tester Guide v0.1](docs/alpha/Closed_Alpha_Tester_Guide_v0.1.md) for safe minimum onboarding, local-data and backup guidance, milestone activities, software-only problem reporting, support, and closeout. Do not freeze or distribute it until the tester-facing version/build, ZIP filename, compatibility, download URL, and Form URLs are supplied and confirmed against the approved package and Forms.

Remaining alpha-administration work:

- Select the named 5-8-person cohort without requiring diagnosis or health-history disclosure.
- Secure the dedicated Google account and implement conservative Drive separation, restricted roster access, Forms without uploads, and warnings immediately before free-text fields.
- Supply and confirm the Tester Guide's approved download URL and Google Form URLs; re-confirm compatibility during the clean-Windows dry run.
- Prepare and validate the invitation, Forms, milestone surveys, issue log, release record, replacement-build procedure, and closeout message.
- Record the exact alpha application version, source revision, release filename, and SHA-256 hash, then complete a clean-Windows dry run before distribution.

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
