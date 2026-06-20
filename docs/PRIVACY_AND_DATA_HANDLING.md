# Privacy and Data Handling

This project is designed for local use. It should not upload PHQ-9 records or treatment notes.

Private data belongs in:

- `data/` for local SQLite databases
- `reports/` for generated PDF/CSV clinician reports
- `exports/` for generated CSV/XLSX data exports

Do not commit:

- Real user databases
- PHQ-9 spreadsheets
- Reports or exports
- Screenshots containing personal health data
- Logs that may contain health details

Sample or fake data may be committed only under `sample_data/` and must be clearly artificial.
