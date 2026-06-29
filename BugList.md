BUG: Report generation dependency detection



When generating reports or spreadsheets, the application may incorrectly report missing Python dependencies (openpyxl, reportlab, Pillow, pandas) despite a valid Python environment being available.



Investigate:

\- PHQ9\_TRACKER\_BUNDLED\_PYTHON handling

\- Portable mode behavior

\- Installed mode behavior

\- Launcher environment detection

\- Packaging script dependency validation



Expected:

Application automatically locates bundled Python or installed Python environment and generates reports without requiring user configuration.


---

BUG: Incorrect 14-day PHQ-9 scoring logic

Status: Fixed

The app previously displayed a recent/14-day average as if it were the intended clinical-style 14-day PHQ-9 score.

Fix:

- Added `calculate_14_day_symptom_frequency_score(entries)`.
- Counts item presence across the most recent 14 calendar days ending on the most recent entry date.
- Converts item day counts using:
  - 0 days = 0
  - 1 to 6 days = 1
  - 7 to 11 days = 2
  - 12 to 14 days = 3
- Sums converted item scores for the 14-day total score.
- Assigns severity using normal PHQ-9 total score bands.
- Missing calendar days count as no recorded symptom-present day and are documented via `entries_included`.
- Updated GUI dashboard, item summaries, clinician report, and data export labels/calculations.

