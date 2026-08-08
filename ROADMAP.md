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

Status: Completed

Implemented small, observable refinements:

- Review charts redraw from live canvas dimensions after resizing and reserve separate vertical bands for the full title, legend, and plot.
- The visible primary-tab order begins with **Today's Check-In**, followed by **Review** and **History / Manage Entries**; startup remains on Today's Check-In.
- **History / Manage Entries** reuses the shared one-day calendar shift behavior for Previous Day and Next Day navigation.
- History has its own unsaved-change snapshot and confirmation, blocks future dates, loads existing records, and disables Next Day on the current date.
- Dates without assessments, notes, or treatment events show a calm manage-only empty state with record-changing controls disabled.
- Nine focused Iteration 007.1 tests were added; all 37 automated tests pass with the dependency-complete project virtual environment.

The project owner completed the manual source-GUI walkthrough against the canonical repository with real-world data. Tab order and startup selection, Review chart titles and resize behavior, History navigation and rollover, existing and empty dates, future-date blocking, and unsaved-change protection passed. This focused polish does not change scoring, storage, reports, exports, or the project's privacy boundary. Iteration 007.2 has not started.

## Upcoming Iterations

### Iteration 007.2: Reporting & Analysis

Planned refinements for a focused future design and implementation iteration:

- Create an analysis-ready Excel workbook as a separate export from the human-readable clinician report.
- Organize the workbook into normalized worksheets for **Daily Assessments**, **Item Responses**, **Notes**, **Treatment Events**, **Treatment Cycles**, and **Metadata**.
- Keep one logical record per row, with stable identifiers, ISO-formatted dates, consistent field names, and documented identifiers and relationships between worksheets so each dataset can be analyzed independently.
- Consider an optional **Daily Summary** worksheet as a derived convenience view, including yes/no columns for common treatment-event types where useful. Normalized **Treatment Events** records remain the source of truth.
- Preserve complete user-authored journal text in clinician reports. Do not truncate or abbreviate the user's own words.
- Restore a fuller **How to Read This Report** explanation in the clinician report. A concise explanation may remain as a reminder, but it should not be the only guidance.
- Explain the difference between **Daily Severity Score** and **14-Day Symptom Frequency Score**, including how entry coverage and missing check-ins affect what can be concluded.
- Revisit clinician-report section names and ordering in a future design workshop before implementation. The final naming and flow remain intentionally undecided.
- Avoid merged cells, decorative blank rows, and report-only presentation that obscures the workbook's underlying data.
- Keep all current scoring, database, report, and export behavior intact.
- Do not perform major data model changes.
- Preserve support for multiple legitimate treatment events on the same date through an explicit “Add another event” action.

### Iteration 008: Micro-UX & Accessibility

Planned small usability and accessibility refinements:

- Make graph point values directly discoverable through click or hover callouts that show the date and exact score.
- Treat graph value discoverability as an accessibility and readability requirement for users who may have difficulty visually tracing a point across a wide chart, not merely as a cosmetic enhancement.
- Load a selected date automatically where doing so safely removes an unnecessary click.
- Use clearer status and confirmation wording.
- Improve button spacing and consistency, along with typography and general readability.
- Add keyboard shortcuts where they genuinely reduce effort or improve navigation.
- Consider scalable text and interface sizing as a future accessibility enhancement.

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
