Current as of: 2026-08-15
Last substantive update: 2026-08-15

# Project Structure

```text
src/phq9_tracker/     Application source code
data/                 Private local SQLite databases
exports/              Generated CSV/XLSX exports
reports/              Generated clinician reports and screenshots
docs/                 Documentation
packaging/            Build and installer scripts
tests/                Tests that use fake temporary data
sample_data/          Fake/sample data only
```

Real user data should stay out of GitHub. The repository keeps placeholder files so the intended folders are visible without committing private contents.

The `exports/` directory may contain both the backward-compatible combined export and the separate normalized analysis workbook. Both are private runtime artifacts and are ignored by Git.
