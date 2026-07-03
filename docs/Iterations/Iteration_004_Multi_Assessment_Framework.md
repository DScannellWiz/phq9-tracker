# Iteration 004 - Multi-Assessment Framework and Modernized User Experience

## Objectives

- Preserve existing PHQ-9 daily tracking, 14-day symptom-frequency scoring, reports, exports, treatment events, and tests.
- Add GAD-7 as the second standardized assessment.
- Introduce a reusable assessment framework for future instruments.
- Replace the old daily entry flow with a unified Today's Check-In.
- Expand dashboard, reports, and exports to include both assessments.
- Maintain privacy-first local storage and GitHub-safe source boundaries.

## Design Decisions

- PHQ-9 remains backward compatible through the existing `phq9_entries` table.
- A new generic `assessment_entries` table stores modular assessments by `assessment_id`.
- Startup migration copies existing PHQ-9 rows into `assessment_entries` with `INSERT OR IGNORE`.
- GAD-7 is defined through the same assessment registry as PHQ-9.
- The 14-day symptom-frequency calculation now accepts an item count and assessment id, so future instruments can reuse it when clinically appropriate.
- The visible application branding now says **Mental Health Tracker**, while the executable and environment variable names remain PHQ-9-oriented for compatibility.

## Migration Strategy

Existing databases are not rewritten destructively.

On startup:

1. The legacy `phq9_entries` table is created or updated if needed.
2. The new `assessment_entries` table is created.
3. Existing PHQ-9 rows are copied into `assessment_entries` only when a matching `assessment_id` and `entry_date` does not already exist.
4. GAD-7 rows are stored directly in `assessment_entries`.

This keeps existing PHQ-9 reports and exports practical while allowing multi-assessment features to use the generic table.

## Files Modified

- `src/phq9_tracker/app.py`
- `tests/test_data_export.py`
- `packaging/build_release.ps1`
- `packaging/PHQ9Tracker.iss`
- `README.md`
- `ROADMAP.md`
- `BUILD_AND_RELEASE.md`

## Files Added

- `tests/test_multi_assessment.py`
- `docs/iterations/Iteration_004_Multi_Assessment_Framework.md`
- `packaging/assets/PHQ9_Tracker.ico`

## Validation Performed

- `python -m unittest discover -s tests`
- `python -m compileall src tests packaging`

The report-generation test is skipped when local PDF/chart dependencies are unavailable. In this session, `reportlab` was unavailable to the active Python environment.

## Extensibility Notes

Future assessments should be added by:

1. Creating an `AssessmentDefinition`.
2. Adding it to `ASSESSMENTS` and `ASSESSMENT_ORDER`.
3. Confirming its scoring bands and whether 14-day symptom-frequency scoring applies.
4. Extending report/export presentation only where the new instrument needs specialized interpretation.

Future security features such as encrypted databases, optional application password, password-protected reports, and encrypted backups should build on the same local-first data boundary rather than changing where private data is stored.

## Remaining Work

- Add explicit schema versioning for future migrations.
- Refactor the single large Tkinter module into smaller modules when the next feature needs it.
- Add PDF rendering verification in an environment with `reportlab`, `Pillow`, and PDF rendering tools installed.
- Consider renaming executable/build artifacts in a future major branding iteration.

## Lessons Learned

The safest multi-assessment path is additive: preserve the known PHQ-9 storage contract, add the generic table beside it, and let tests verify that old and new paths stay aligned.
