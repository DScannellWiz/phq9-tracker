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

## Upcoming Iterations

Iteration 007: User Experience Refresh

Goals:
- Move toward the card-based dashboard mockup.
- Separate PHQ-9 and GAD-7 item summaries into distinct sections.
- Make Today’s Check-In the central workflow.
- Add trend chart area for PHQ-9 and GAD-7.
- Improve spacing, alignment, and readability.
- Refine interface layout and visual hierarchy without adding unrelated features.
- Reorganize the clinician report so interpretation guidance and high-value clinical content appear earlier.
- Move the scoring explanation near the beginning of the clinician report, ideally immediately after the title or within an early How to Read This Report section.
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
