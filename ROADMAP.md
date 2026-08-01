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
- Clinician PDF reports and companion CSV reports.
- CSV/XLSX data exports.
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

Iteration 006 delivered data integrity, scoring clarity, and application branding. Automated validation and manual source-GUI validation with the existing production database are complete. Installed and portable packaging validation remains pending until PyInstaller and Inno Setup are available.

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

Planned small, observable refinements:

- Fix overlapping or clipped chart titles in Review and keep both assessment panels readable when the window is resized.
- Reorder the primary tabs so **Today's Check-In** is the first tab while continuing to open the application there.
- Add **Previous Day** and **Next Day** navigation to **History / Manage Entries** using the shared date-navigation behavior.
- Preserve unsaved-change protection and future-date prevention when navigating historical dates.
- Show a calm empty state when the selected historical date has no records.

This is a focused documentation and polish scope. It does not change scoring, storage, reports, or the project's privacy boundary.

## Upcoming Iterations

Analysis-ready workbook export:
- Add a normalized, analysis-ready workbook export alongside the existing human-readable spreadsheet. The current presentation-oriented layout distributes data across different areas and is not suitable for independent filtering, sorting, pivoting, or external analysis.
- Organize the analysis-ready workbook into separate tabular worksheets or equivalent normalized datasets for daily assessments, item-level responses, notes, treatment events, and metadata.
- Use one row per logical record, stable identifiers, ISO-formatted dates, explicit assessment-type and item fields, and consistent column names. Do not use merged cells, decorative blank rows, or calculated report-only presentation that obscures the underlying raw data.
- Preserve enough documented relationships between worksheets for users and clinicians to perform their own analysis outside the application and generated clinician report.
- Keep all current scoring, database, report, and export behavior intact.
- Do not perform major data model changes.
- Preserve support for multiple legitimate treatment events on the same date through an explicit “Add another event” action.

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
