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

## Completed Iteration 004

Iteration 004 introduced the reusable assessment framework and began the transition from PHQ-9 Tracker to Mental Health Tracker.

Delivered:

- Modular assessment definitions for PHQ-9 and GAD-7.
- New generic `assessment_entries` database table.
- Legacy PHQ-9 migration into the generic assessment table.
- Today's Check-In UI for PHQ-9, GAD-7, notes, and optional treatment events.
- Combined dashboard, reports, and exports.
- Tests for GAD-7 scoring, exports, migration, and dependency-gated report generation.

## Upcoming Iterations

- Dashboard should include item-level GAD-7 14-day scores, similar to PHQ-9.
- Add a clearer “Today’s Check-In” dashboard card.
- Improve visual layout toward the mockup: cards, spacing, navigation, and trend chart.
- Polish branding and icon behavior.

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
