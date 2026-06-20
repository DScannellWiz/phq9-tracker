# Local PHQ-9 Tracker

A local-first desktop PHQ-9 tracking application with SQLite storage, manual entry, data export, and clinician discussion reports.

This project is intended to keep health data on the user's computer. It should not upload PHQ-9 records, notes, treatment markers, reports, or exports.

## Project Structure

```text
src/phq9_tracker/     Application source code
data/                 Private local SQLite databases
exports/              Generated CSV/XLSX data exports
reports/              Generated clinician reports and screenshots
docs/                 Project documentation
packaging/            Build and installer scripts
tests/                Automated tests
sample_data/          Fake/sample data only
```

## Privacy Rules

Do not commit real health data.

Private files belong in:

- `data/` for SQLite databases
- `reports/` for generated PDF/CSV clinician reports
- `exports/` for generated CSV/XLSX exports

The `.gitignore` is configured to exclude real databases, reports, exports, logs, caches, screenshots, and build artifacts. Keep fake data only in `sample_data/`.

## Running From Source

```powershell
python -m pip install -r requirements.txt
$env:PYTHONPATH = "$PWD\src"
python -m phq9_tracker --launch
```

Or open:

```text
Launch PHQ-9 Tracker.bat
```

## Features

- Import PHQ-9 entries from Excel.
- Store entries in a local SQLite database.
- Show recent entries and item averages.
- Calculate PHQ-9 totals and severity categories.
- Allow manual daily entry and optional notes/tags.
- Track treatment events, including ketamine, therapy, and medication changes.
- Export data-only CSV/XLSX files.
- Generate clinician discussion reports with a clickable table of contents, Question 9 monitoring, current status, recent score summaries, item charts, and ketamine response review.

## Data Locations

Source runs store the database at:

```text
data/phq9_tracker.sqlite
```

Installed builds store user data under `%LOCALAPPDATA%\PHQ9Tracker` by default. Portable builds can set `PHQ9_TRACKER_PORTABLE=1` to keep the database beside the executable.

## AI-Assisted Development

This is an AI-assisted project directed by the repository owner. Changes should be reviewed by the owner before release, especially changes affecting clinical report wording, data handling, packaging, or privacy boundaries.

## Disclaimer

This report is for discussion with a licensed clinician and is not a diagnosis.
