Current as of: 2026-08-15
Last substantive update: 2026-08-08

# Iteration 007.1: Navigation and Review Polish

## Status

Complete. Automated validation and the project owner's manual source-GUI walkthrough of the canonical repository passed.

## Objectives

- Keep PHQ-9 and GAD-7 Review chart titles fully readable at normal and minimum supported window sizes.
- Align visible primary-tab order with the present-focused product workflow.
- Add guarded Previous Day and Next Day navigation to History / Manage Entries.
- Provide a calm, non-creating state for historical dates without records.
- Preserve scoring, storage, exports, reports, privacy boundaries, and backward compatibility.

## Design Decisions

- `shift_calendar_date` remains the shared calendar-navigation rule, including automatic month/year rollover and future-date prevention.
- Today and History keep separate snapshots because their editable fields and discard decisions are independent.
- History actions require the visible date to match the loaded date. This prevents edits from being applied after the date field was changed without loading.
- Empty dates are read-only in History. Existing assessments, notes, and events can still be managed, and another treatment event can still be added to a day that already contains records.
- Review charts use live canvas dimensions after layout and redraw on resize. The rendered title's bounding box determines where the legend and plot begin, preventing vertical collision without truncating the title.
- The tab order is defined once and used to add all primary tabs, with Today's Check-In first and explicitly selected at startup.

## Files Modified

- `src/phq9_tracker/app.py`
- `README.md`
- `ROADMAP.md`
- `BugList.md`
- `DEVELOPMENT_JOURNAL.md`
- `docs/decisions/0004-present-focused-check-in.md`

## Files Added

- `tests/test_iteration_007_1_navigation_review.py`
- `docs/Iterations/Iteration_007_1_Navigation_Review_Polish.md`

## Validation Performed

- Python compilation passed for the application and focused test module.
- All 37 automated tests passed using isolated temporary databases and the dependency-complete project virtual environment.
- The nine focused Iteration 007.1 tests cover primary-tab order, History navigation and rollover, existing-record loading, empty dates, future-date blocking, unsaved-change protection, live canvas sizing, and title/legend/plot separation.
- The synthetic database intended for GUI validation was created only under the temporary Codex workspace. No personal tracker database was opened or copied.
- The project owner completed the manual source-GUI walkthrough against the canonical repository with real-world data. Tab order and startup selection, Review chart titles and resize behavior, History navigation and rollover, existing and empty dates, future-date blocking, and unsaved-change protection passed.

## Remaining Work and Known Limitations

- No Iteration 007.1 release-gate work remains.
- Installed and portable package validation remains outside this iteration.

## Privacy and Migration Notes

- No database migration is required.
- No schema, scoring, report, or export behavior changed.
- Validation uses synthetic data through `PHQ9_TRACKER_DB_PATH`; databases, screenshots, reports, exports, and logs must not be staged or committed.

## Lessons Learned

- A responsive canvas must render from its live size, not its configured starting size.
- Unsaved-change protection belongs to an editable workflow boundary; sharing date arithmetic does not mean sharing UI state.
- Empty History dates should communicate absence without turning a maintenance screen into a second data-entry path.
