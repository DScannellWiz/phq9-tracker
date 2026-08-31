Current as of: 2026-08-29
Last substantive update: 2026-08-29

# Privacy and Data Handling

This project is designed for local use. It should not upload PHQ-9 records or treatment notes.

Private data belongs in:

- `data/` for local SQLite databases
- `reports/` for generated clinician PDFs and normalized XLSX Analysis Workbooks

Do not commit:

- Real user databases
- PHQ-9 spreadsheets
- Reports or exports
- Screenshots containing personal health data
- Logs that may contain health details

Sample or fake data may be committed only under `sample_data/` and must be clearly artificial.

Portable release archives must not contain a user database or any generated private artifact. A portable launch creates and uses `phq9_tracker.sqlite` inside its own extracted folder. Release validation must use synthetic data, prove persistence across restart, and return the portable folder to a verified blank state before distribution or travel use.

## Closed Alpha Handling

Closed-alpha testers retain control of the database and all generated outputs. The portable database remains in the extracted application folder. PDFs and Analysis Workbooks are generated locally under the portable application's common `reports` folder, which remains inside the extracted folder. Testers may enter real, fictional, random, or mixed data at their discretion, and the program does not ask which. Entered content remains controlled by the tester.

The alpha requests and accepts feedback about the software only. It does not request, collect, retain, or analyze participant medical or mental-health information, health outcomes, or tracker-entered content. Feedback instructions must repeatedly tell testers not to submit assessment answers, journal entries, treatment information, clinician information, generated reports, Analysis Workbooks, databases, logs, screenshots containing entered data, or other medical or health information, whether real, fictional, random, mixed, or created for testing.

If medical or health information is received, do not use, analyze, or intentionally retain it. Delete or destroy it as soon as reasonably practicable after identification. Contact the sender only as necessary to request non-medical troubleshooting details. Reproduce the issue with project-created fictional data; there is no troubleshooting exception for soliciting or retaining entered health or medical data.

Use tester IDs such as `MHT-A001` in GitHub, findings, development records, and other ordinary program records. Keep the identity/contact-to-ID roster accessible only to Daniel and segregated from GitHub and ordinary project records. Target its destruction 30 days after alpha closeout unless a documented administrative need requires otherwise. Pseudonymized software-testing records may remain as project provenance.

Google Forms must not allow file uploads and must show the health-data warning immediately before every free-text field. The dedicated Google Drive may hold approved distribution files and ordinary alpha administration records, but it must not hold participant health data. The restricted identity roster must be separated from ordinary alpha records.

Participation does not make the project a monitoring, clinical-support, crisis, or emergency service. Testers may stop and delete their local files at any time; they must be told that deletion is permanent without their own backup and that the alpha should not be the sole repository for important health information.

Future Travel Mode and LAN-sharing concepts do not weaken the local-first boundary. Travel import must be validated and append-only against an authoritative home database; LAN clients must use an authoritative local host/service rather than opening SQLite directly over a network share.
