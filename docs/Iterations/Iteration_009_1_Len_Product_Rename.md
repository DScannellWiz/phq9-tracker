# Post-Iteration-009: Len Product Rename

Current as of: 2026-09-10  
Status: Implementation complete; pending owner review and commit approval

## Objectives

- Rename the current product from **Mental Health Tracker** to **Len**.
- Align current repository references with `https://github.com/DScannellWiz/len-mental-health`.
- Update current-facing application, generated-output, launcher, installer, and documentation branding.
- Preserve historical Iteration, release, alpha, and provenance records where the former name is factually accurate.
- Leave the `v0.3.0-alpha.1` tag and every existing release artifact unchanged.

## Design Decisions

- Centralize the visible application name in `APPLICATION_NAME` and reuse it for the GUI title, header, command-line description, workbook metadata, scoring explanation, and clinician-report title.
- Use `Len_Analysis_...xlsx` and `Len_Report_...pdf` for newly generated output filenames.
- Rename the source launcher to `Launch Len.bat` and configure future portable packaging to create `Launch Portable Len.bat`.
- Use Len for future installer display names, installation folder, shortcuts, and setup filename.
- Require an explicit future build version, reject `0.3.0-alpha.1` in the current build script, and use `Len-Portable-...` for future portable folder and ZIP names. The Inno Setup script likewise requires its version to be supplied explicitly.
- Retain `phq9_tracker`, `PHQ9Tracker.exe`, `PHQ9_TRACKER_*`, `%LOCALAPPDATA%\PHQ9Tracker`, `phq9_tracker.sqlite`, and `PHQ9_Tracker.ico` as compatibility identifiers. Renaming these would add migration and upgrade risk without improving the visible product experience.
- Keep `projectmentalhealthtracker@gmail.com` because no replacement support address was provided or verified.
- Do not rename the local repository folder during the active tool session. The repository contains a path-bound virtual environment and may be open in PowerShell or other tools; a parent-folder rename is safer as a deliberate manual step after review.

## Files Modified

- `src/phq9_tracker/app.py`
- `src/phq9_tracker/__init__.py`
- `packaging/build_release.ps1`
- `packaging/PHQ9Tracker.iss`
- `README.md`
- `BUILD_AND_RELEASE.md`
- `ROADMAP.md`
- `BugList.md`
- `DEVELOPMENT_JOURNAL.md`
- `PROJECT_ORIGINS.md`
- `docs/product-principles.md`
- `docs/PRIVACY_AND_DATA_HANDLING.md`
- `THIRD_PARTY_NOTICES/README.md`
- `tests/test_iteration_007_2_reporting_portable.py`
- `tests/test_iteration_008_2_clinician_outputs.py`

## Files Renamed or Added

- Renamed `Launch Mental Health Tracker.bat` to `Launch Len.bat`.
- Added this iteration record.
- Added `tests/test_len_branding.py`.

## Historical Records Intentionally Retained

- `docs/Iterations/Iteration_009_Public_Repository_Readiness.md` and earlier iteration documents.
- `docs/alpha/` governance, candidate, and validation records.
- Dated `DEVELOPMENT_JOURNAL.md`, `BUILD_AND_RELEASE.md`, `ROADMAP.md`, and `PROJECT_ORIGINS.md` passages that describe earlier product stages or exact artifacts.
- The `v0.3.0-alpha.1` tag and ignored release/validation artifacts.

## Validation Performed

- All 62 `unittest` tests passed in the project environment. The suite verifies the Len application constant, current launchers and installer text, preserved compatibility identifiers, Len workbook metadata, Len clinician-report title, and new default output filenames. The pre-existing non-failing SQLite `ResourceWarning` still appears during workbook testing.
- Both Iteration 009 Tcl/Tk packaging regression functions passed when exercised directly with the project source path.
- Python compilation passed for `src`, `tests`, and `packaging`.
- The release-license verifier passed under the retained controlled Python 3.12.10 release runtime: 34 notice files and 11 package versions verified. As designed, it rejected the ordinary Python 3.14 project environment because that runtime does not match the pinned historical release manifest.
- PowerShell parsing, the frozen-version build guard, `git diff --check`, and tracked Markdown local-link validation passed.
- The exact quarantined `0.3.0-alpha.1-redistribution.2` ZIP still matches SHA-256 `5A43D176103FCEDBA1FBD36F01C78FDD88237FB27F369C859A9B37C8F497D1DA`, and `v0.3.0-alpha.1` still dereferences to commit `27c7b7f6c576ef6c192432f29884f5074e65ad19`.
- `origin` fetch and push URLs both use `https://github.com/DScannellWiz/len-mental-health.git`.
- Current-facing files contain no stale former-brand reference except explicit historical/freeze explanations and regression-test assertions. Repository-wide remaining former-name references were reviewed as historical provenance.

## Remaining Work

- Owner review and explicit approval before commit.
- Optional manual rename of the local parent folder after closing programs that use the old path.
- Choose a version newer than `0.3.0-alpha.1` before building any Len-branded artifact; then run the full exact-artifact release checklist.
- Inno Setup is unavailable in the current environment, so the updated installer script was reviewed but not compiled. No Len-branded binary was built or launched during this documentation and source rename.

## Lessons Learned

- A product name can change without forcing internal storage and package migrations.
- Historical accuracy is stronger when old records retain the names and filenames that belonged to their exact artifacts.
- Repository, product, executable, data-path, and release-artifact identities are related but distinct compatibility surfaces.
