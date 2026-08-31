Current as of: 2026-08-31
Last substantive update: 2026-08-31

# Iteration 008.2: Clinician Output Fidelity and Alpha Output Polish

## Status

Complete. Automated tests, source/test compilation, representative fictional outputs, and Daniel's source-GUI walkthrough passed. Closed Alpha candidate packaging and packaged validation are recorded separately from this feature iteration.

## Objectives

- Restore compact current 14-day per-item profiles for PHQ-9 and GAD-7 in both clinician outputs.
- Preserve Physical Therapy separately from counseling Therapy in clinician presentation.
- Put the PDF and Analysis Workbook in one discoverable local output folder.
- Offer optional file opening and a direct way to open the common folder.
- Tighten the questionnaire Spinbox arrow presentation without redesigning the form.
- Preserve 008.1 behavior, scoring, schema, stored records, migrations, complete journal text, and local-first privacy.

## Design Decisions

- `build_14_day_item_profile()` reuses the established explicit-window scoring function and returns one record per assessment item with symptom-present days, recorded-day coverage, calendar days, and the 0-3 frequency score.
- The PDF presents the profile as compact PHQ-9 and GAD-7 tables. Missing days remain missing information, and no retired raw-response table was restored.
- The Analysis Workbook schema advances to 1.1 and adds **14-Day Item Profile** as an eighth logical sheet. This preserves one logical record per row and avoids repeating a current-window snapshot across daily response rows.
- `normalize_event_type()` recognizes Physical Therapy before the broader Therapy category. The normalized workbook record and PDF label therefore remain distinct while the original stored `event_type` remains unchanged.
- `generated_output_dir()` is the single path authority. Source runs use `<project>\reports`; portable runs use `<extracted-app>\reports`; installed mode uses `%LOCALAPPDATA%\PHQ9Tracker\reports` to avoid writing under Program Files.
- Output names are automatic and collision-safe. Existing files are not overwritten; `_2`, `_3`, and later suffixes are selected as needed.
- Successful generation is followed by an optional open prompt. A Windows association/Explorer failure produces a calm message containing the saved path and does not convert generation into failure.
- **Open Reports Folder** intentionally changes Review from four actions to five.
- User-defined destinations remain deferred because path persistence, permissions, removable drives, and settings migration need their own design and validation.
- Existing ttk Spinboxes retain their widget type and dependency set; internal padding is reduced while row spacing remains between items.

## Files Modified

- `.gitignore`
- `src/phq9_tracker/app.py`
- `tests/test_iteration_007_2_reporting_portable.py`
- `tests/test_iteration_008_review_exports.py`
- `README.md`
- `ROADMAP.md`
- `BugList.md`
- `BUILD_AND_RELEASE.md`
- `DEVELOPMENT_JOURNAL.md`
- `docs/PRIVACY_AND_DATA_HANDLING.md`
- `docs/PROJECT_STRUCTURE.md`
- `docs/alpha/Closed_Alpha_Tester_Guide_v0.1.md`
- `docs/decisions/0005-conversation-focused-reporting.md`
- `docs/Iterations/Iteration_008_Review_and_Clinician_Report_Workflow.md`
- `docs/Iterations/Iteration_008_1_Chart_Accessibility_and_Micro_UX.md`

## Files Added

- `tests/test_iteration_008_2_clinician_outputs.py`
- `docs/Iterations/Iteration_008_2_Clinician_Output_Fidelity_and_Alpha_Polish.md`

## Validation Performed

- Compiled all application and test Python sources.
- Ran the full dependency-complete automated suite: 59 tests passed with no failures or skips.
- Generated a representative fictional full-history PDF and eight-sheet Analysis Workbook using an isolated temporary SQLite database.
- Exercised complete PHQ-9 and incomplete GAD-7 current-window coverage, 0-3 item-frequency thresholds, and same-day Therapy/Physical Therapy events sharing the same fictional description.
- Confirmed 16 item-profile rows, distinct stored and normalized event types, stable worksheet relationships, complete fictional text, and no merged cells.
- Rendered all eight workbook sheets and confirmed readable headers/values, frozen header rows, filters, and no clipped profile fields after the bounded formatting pass.
- Extracted PDF text and confirmed profile headings, coverage wording, both event labels, and both copies of the shared description.
- Rendered every PDF page through the existing validation dependency and inspected the rendered pages for clipping and unreadable layout.
- Confirmed PDF and XLSX outputs land together under `reports`, with no companion or legacy CSV.
- Confirmed Git continues to ignore databases, PDFs, XLSX files, screenshots, logs, and legacy `exports` contents.

## Source-GUI Validation Completed

Daniel completed and passed the source-GUI walkthrough on August 30, 2026. He confirmed collision-safe double generation and both open-prompt paths for the PDF and workbook; **Open Reports Folder**; real PDF item-profile readability and treatment-event fidelity; real workbook **14-Day Item Profile** readability; improved/acceptable Spinbox arrows; and the brief 008.1 regression sanity check.

Candidate `0.3.0-alpha.1` then repeated the applicable workflow with project-created fictional data. Packaging and distribution remain outside the feature scope and are documented in the Closed Alpha candidate release record.

## Known Limitations and Deferred Work

- Output destinations are not user-configurable.
- Default-application opening depends on Windows file associations.
- Installer validation remains separate.
- A future Treatment Cycles enhancement may overlay the current ketamine cycle and two previous cycles on one chart in three distinct colors. It is deliberately deferred and was not implemented for this release.

## Lessons Learned

- A small derived sheet can restore analytical fidelity without denormalizing daily records.
- Broad substring mappings need specific categories checked first when labels have meaningful overlap.
- Saving related outputs together and providing a direct folder action reduces navigation burden without introducing a settings subsystem.
