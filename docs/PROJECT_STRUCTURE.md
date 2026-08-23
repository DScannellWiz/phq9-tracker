Current as of: 2026-08-22
Last substantive update: 2026-08-22

# Project Structure

```text
src/phq9_tracker/     Application source code
data/                 Private local SQLite databases
exports/              Generated normalized XLSX analysis workbooks
reports/              Generated clinician reports and screenshots
docs/                 Documentation
packaging/            Build and installer scripts
tests/                Tests that use fake temporary data
sample_data/          Fake/sample data only
```

Real user data should stay out of GitHub. The repository keeps placeholder files so the intended folders are visible without committing private contents.

The `exports/` directory contains normalized analysis workbooks. These private runtime artifacts are ignored by Git.
