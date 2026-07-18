# Mental Health Tracker

A privacy-first desktop application for tracking standardized mental health assessments over time.

The project began as a PHQ-9 tracker and now supports a reusable multi-assessment framework with PHQ-9 and GAD-7 as the first two instruments.

## Current Features

- Today's Check-In for PHQ-9, GAD-7, optional daily notes, and multiple treatment events.
- Existing-date detection that loads and updates daily records without creating accidental duplicates.
- History / Manage Entries tools for editing and confirmed deletion of assessments, notes, and treatment events.
- PHQ-9 daily tracking with preserved legacy database compatibility.
- GAD-7 daily tracking.
- Clearly labeled Daily Severity Scores and 14-Day Symptom Frequency Scores for each assessment.
- An accessible How Scoring Works explanation in the app and clinician report.
- SQLite local storage under the project `data` folder during source runs.
- Clinician discussion reports with a current-versus-previous 14-day executive summary, PHQ-9, GAD-7, treatment events, daily notes, and trend summaries.
- Dashboard cards showing each current 14-Day Symptom Frequency Score and its direction relative to the preceding 14 days.
- CSV/XLSX exports with both assessments.
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
3. Use **Check Date / Load Existing** before changing an earlier date; saving updates the stable records for that day.
4. Select any relevant event checkboxes, or use **Add Custom Event**. Use **History / Manage Entries** to add another legitimate event of the same type.
5. Review current scores and trends on the dashboard, and open **How Scoring Works** for the daily-versus-14-day distinction.
6. Generate clinician reports or exports when you want a local file to discuss with a care team.

Daily check-ins intentionally do not copy or autofill previous responses. Each symptom should be considered independently to encourage mindful reflection and higher-quality recorded data.

## Privacy Philosophy

This app is local-first. It does not intentionally upload assessment responses, notes, treatment events, databases, reports, or exports.

Private runtime data belongs in:

- `data/`
- `reports/`
- `exports/`

Those folders are ignored by Git except for placeholder files and documentation. Do not commit real databases, reports, exports, screenshots, logs, PHI, PII, or secrets.

## Disclaimer

This software is intended to help users track symptoms and prepare for conversations with licensed healthcare professionals. It is not a diagnostic tool and should not replace professional medical advice, crisis support, or emergency care.

## AI-Assisted Development

This project is developed with AI-assisted software engineering under the direction of the repository owner. The owner remains the final reviewer for architecture, privacy, clinical framing, and release decisions.
