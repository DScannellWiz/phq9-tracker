Current as of: 2026-08-22
Last substantive update: 2026-08-22

# Mental Health Tracker

A privacy-first desktop application for tracking standardized mental health assessments over time.

The project began as a PHQ-9 tracker and now supports a reusable multi-assessment framework with PHQ-9 and GAD-7 as the first two instruments.

## Current Features

- Today's Check-In for PHQ-9, GAD-7, optional daily notes, and multiple treatment events.
- Previous Day and Next Day navigation in both Today's Check-In and History / Manage Entries, with automatic calendar rollover, future-date prevention, existing-record loading, and separate unsaved-change protection for each workflow.
- Existing-date detection that loads and updates daily records without creating accidental duplicates.
- History / Manage Entries tools for editing and confirmed deletion of assessments, notes, and treatment events, plus a calm read-only state when a selected date has no records.
- PHQ-9 daily tracking with preserved legacy database compatibility.
- GAD-7 daily tracking.
- Clearly labeled Daily Severity Scores and 14-Day Symptom Frequency Scores for each assessment.
- An accessible How Scoring Works explanation in the app and clinician report.
- SQLite local storage under the project `data` folder during source runs.
- A separate Review experience with concise, deterministic symptom summaries, recent charts, current/previous ketamine-cycle views, and long-term trends.
- Compact clinician discussion reports centered on scoring context, recorded patterns, treatment context, complete user-authored journal text, and neutral conversation prompts. Reports expand as needed rather than truncating journal entries.
- A normalized XLSX analysis workbook with Daily Assessments, Item Responses, Notes, Treatment Events, Treatment Cycles, Metadata, and a derived Daily Summary.
- Treatment event tracking.
- Automated tests for scoring, migration, exports, and report behavior where local dependencies are available.

## Installation

Use Python 3.12 or later on Windows.

```powershell
python -m pip install -r requirements.txt
python -m phq9_tracker
```

For source runs, execute commands from the project root so the app can locate `data`, `exports`, and `reports`.

## Basic Usage

1. Open the application.
2. Use **Today's Check-In** to enter PHQ-9 and GAD-7 responses for the day.
3. Use **Previous Day** or **Next Day** for short-distance catch-up. Month and year boundaries are handled automatically, existing entries load automatically, and future check-ins are blocked.
4. Open **Review** when you want historical summaries, recent trends, treatment-cycle views, or long-term charts. Review information is intentionally kept out of Today's Check-In.
5. Use **History / Manage Entries** to move one day at a time, edit existing records, or add another legitimate event to a day that already has records. Empty dates remain read-only and direct you back to Today's Check-In for new daily recording.
6. Select any relevant event checkboxes in Today's Check-In, or use **Add Custom Event** for another event type.
7. From **Review**, use **Generate PDF** when you want a readable full-history conversation aid. Use **Analysis Workbook** when you want normalized data for filtering, sorting, pivoting, or independent analysis.

Daily check-ins intentionally do not copy or autofill previous responses. Each symptom should be considered independently to encourage mindful reflection and higher-quality recorded data.

## Privacy Philosophy

This app is local-first. It does not intentionally upload assessment responses, notes, treatment events, databases, reports, or exports.

Portable builds are designed to start with a blank database inside the extracted portable folder. Do not add an existing user database to a portable ZIP unless the user has made a separate, informed data-transfer decision.

Private runtime data belongs in:

- `data/`
- `reports/`
- `exports/`

Those folders are ignored by Git except for placeholder files and documentation. Do not commit real databases, reports, exports, screenshots, logs, PHI, PII, or secrets.

## Disclaimer

This software is intended to help users track symptoms and prepare for conversations with licensed healthcare professionals. It is not a diagnostic tool and should not replace professional medical advice, crisis support, or emergency care.

## Project Documentation

- [Project Origins](PROJECT_ORIGINS.md) explains the human problem that started the project and its intended division of labor.
- [Development Journal](DEVELOPMENT_JOURNAL.md) records the reconstructed prehistory and the context behind significant iterations.
- [Product Principles](docs/product-principles.md) defines the stable philosophical core and adaptable implementation layers.
- [Architecture Decision Records](docs/decisions/) document significant product and architectural decisions.

## AI-Assisted Development

This project is developed with AI-assisted software engineering under the direction of the repository owner. The owner remains the final reviewer for architecture, privacy, clinical framing, and release decisions.
