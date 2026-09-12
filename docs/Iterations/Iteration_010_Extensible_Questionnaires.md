Current as of: 2026-09-12

# Iteration 010 - Extensible Questionnaire Framework

## Objectives

- Present PHQ-9 and GAD-7 as built-in questionnaires in one extensible registry.
- Let a user choose one or more questionnaires for each date and see independent completion status.
- Keep PHQ-9 item 9 behavior specific to PHQ-9.
- Show a universal safety message before questionnaire item 1 and in every PDF footer.
- Support questionnaire-specific 14-day profiles, trends, PDF selection, and workbook selection.
- Keep all Today check-in submit controls reachable at common Windows display heights.
- Establish the metadata contract needed by future custom questionnaires without adding authoring in this iteration.

## Design Decisions

- `QuestionnaireDefinition`, `QUESTIONNAIRES`, and `QUESTIONNAIRE_ORDER` are the public extension vocabulary.
- Existing assessment names, SQLite tables, executable names, environment variables, and PHQ-9 legacy synchronization remain compatibility interfaces.
- The registry includes source, redistribution, maximum-score, item-label, and PHQ-9 item-9 behavior metadata.
- Completion is derived from the presence of a saved questionnaire record for a date. An unselected questionnaire is not saved as an all-zero response.
- The Today page owns a vertical scrollbar and mouse-wheel behavior. After the core check-in is saved, it scrolls to the optional-details controls automatically.
- Output selection filters questionnaire rows and derived 14-day profiles. Notes and treatment events retain their existing daily relationships.
- Only the two already redistributed built-ins are registered. Custom questionnaire authoring remains deferred.

## Migration and Data Compatibility

Iteration 004 already migrated legacy PHQ-9 rows additively into `assessment_entries`. Iteration 010 promotes that generic storage path to the questionnaire framework without rewriting or deleting records. `phq9_entries` remains synchronized for backward compatibility.

No user-data migration step is required. Existing PHQ-9 and GAD-7 records remain available after upgrade.

## Files Modified

- `src/phq9_tracker/app.py`
- `README.md`
- `ROADMAP.md`
- `BugList.md`
- `DEVELOPMENT_JOURNAL.md`

## Files Added

- `tests/test_iteration_010_questionnaires.py`
- `docs/Iterations/Iteration_010_Extensible_Questionnaires.md`

## Validation

- Python compilation
- Full automated unit-test suite
- Git whitespace validation
- Targeted synthetic GAD-7-only PDF and questionnaire-filtered workbook checks
- Automated structural coverage for the Today-page scrollbar and optional-submit reveal
- Live 1180 x 780 Tk layout check confirmed the revealed Save Optional Details button was fully inside the visible viewport after automatic scrolling.

## Remaining Work

- Manual Windows GUI walkthrough of selection, completion labels, resizing, keyboard navigation, and the safety-message placement.
- Custom questionnaire authoring, validation, import/export, and scoring-rule configuration in a later approved iteration.
- Portable packaging and exact-artifact validation as a separate release activity.
