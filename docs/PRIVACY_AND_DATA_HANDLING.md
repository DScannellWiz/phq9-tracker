Current as of: 2026-08-22
Last substantive update: 2026-08-22

# Privacy and Data Handling

This project is designed for local use. It should not upload PHQ-9 records or treatment notes.

Private data belongs in:

- `data/` for local SQLite databases
- `reports/` for generated clinician PDFs
- `exports/` for generated normalized XLSX analysis workbooks

Do not commit:

- Real user databases
- PHQ-9 spreadsheets
- Reports or exports
- Screenshots containing personal health data
- Logs that may contain health details

Sample or fake data may be committed only under `sample_data/` and must be clearly artificial.

Portable release archives must not contain a user database or any generated private artifact. A portable launch creates and uses `phq9_tracker.sqlite` inside its own extracted folder. Release validation must use synthetic data, prove persistence across restart, and return the portable folder to a verified blank state before distribution or travel use.

Future Travel Mode and LAN-sharing concepts do not weaken the local-first boundary. Travel import must be validated and append-only against an authoritative home database; LAN clients must use an authoritative local host/service rather than opening SQLite directly over a network share.
