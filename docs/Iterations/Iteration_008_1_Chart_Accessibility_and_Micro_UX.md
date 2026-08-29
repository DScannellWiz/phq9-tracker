Current as of: 2026-08-28
Last substantive update: 2026-08-28

# Iteration 008.1: Chart Accessibility and Micro-UX

## Status

Implementation, full automated validation, source compilation, and fictional PDF text validation are complete. Daniel's interactive source-GUI walkthrough and packaged-release validation remain pending.

## Objectives

- Make every Review chart point's date and exact score directly discoverable.
- Remove unnecessary date-loading clicks without risking unsaved work or cross-date saves.
- Clarify statuses, confirmations, and successful-action wording.
- Make PHQ-9 item 9 Conversation Starters recency-aware and explicit about recent check-in coverage.
- Improve spacing, consistency, typography, and keyboard access without broadening the iteration into a redesign.
- Preserve scoring, schema/data, local-only privacy, complete journal text, and existing PDF/XLSX output behavior.

## Design Decisions

- Review canvases retain the existing responsive chart architecture. Each rendered point now has a testable date/series/score record and a forgiving 12-pixel hit target.
- Hover shows a temporary callout. Clicking locks it; clicking away or pressing Escape clears it. Focused charts use Left/Right to move between points and Enter to show a point.
- Today and History date fields load a valid changed date after focus leaves only when their current snapshot is unchanged. Unsaved edits block automatic loading and remain visible. Enter remains an explicit load action.
- Today's Check-In tracks the loaded date separately and refuses to save when the typed date differs, preventing visible responses from being applied to an unreviewed day.
- F5 refresh is the only application-wide shortcut. Potentially ambiguous global save or date-navigation shortcuts were not added.
- UI polish reuses Segoe UI and Tk/ttk configuration already available in the application. No theme or accessibility package was introduced.
- The item 9 recent window is the 14 calendar days ending on the report end date. Recent above-zero responses, older-only above-zero responses, and no above-zero responses are separate deterministic cases.
- Older item 9 responses remain dated historical context and explicitly do not establish or indicate current risk. Missing recent days are described as missing information.
- User-configurable/scalable sizing is deferred because it requires a broader minimum-window and layout review.

## Files Modified

- `src/phq9_tracker/app.py`
- `tests/test_iteration_007_1_navigation_review.py`
- `README.md`
- `ROADMAP.md`
- `BugList.md`
- `BUILD_AND_RELEASE.md`
- `DEVELOPMENT_JOURNAL.md`
- `docs/decisions/0005-conversation-focused-reporting.md`

## Files Added

- `tests/test_iteration_008_1_accessibility_micro_ux.py`
- `docs/Iterations/Iteration_008_1_Chart_Accessibility_and_Micro_UX.md`

## Validation Performed

- Ran the 17 focused Iteration 008.1 and navigation tests; all passed.
- Ran all 50 automated tests in the dependency-complete project environment with an isolated fictional database path; all passed with no skips.
- Exercised the existing normalized seven-sheet Analysis Workbook and PDF-generation tests.
- Generated a fictional older-item-9 PDF, extracted its text, and verified historical wording, 2-of-14 recent coverage, no current-risk inference, and absence of the retired “support is needed now” wording.
- Compiled application and test source successfully.
- Confirmed no database file was copied into the implementation workspace and no schema migration was introduced.

## Remaining Manual Validation

- Inspect hover and locked callouts at left/right chart edges, high/low values, and resized/minimum window dimensions.
- Tab into each Review chart and verify visible focus behavior plus Left/Right, Enter, and Escape.
- Confirm date focus changes auto-load only when safe and preserve unsaved Today/History edits when not safe.
- Review updated status, confirmation, and completion wording in context.
- Inspect button spacing, notebook tabs, typography, table rows, wrapping, and minimum-window readability.
- Generate fictional recent, historical-only, and all-zero item 9 reports and inspect the rendered pages.
- Repeat the focused workflow in a packaged portable build before release. Installer validation remains separate while Inno Setup is unavailable.

## Lessons Learned

- Accessibility can often be improved by exposing exact information already present in the model rather than redesigning the visualization.
- Automatic behavior should be conditional on a proven safe state; preserving a loaded-date identity prevents convenience from weakening data integrity.
- Safety-sensitive historical wording needs an explicit recency boundary and coverage disclosure, not just a generic disclaimer.
