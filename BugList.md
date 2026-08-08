BUG: Report generation dependency detection

Status: Improved in Iteration 007; installed/portable validation pending

Iteration 004 note:

- Automated report tests are dependency-gated because the active Python environment in this Codex session did not expose `reportlab`.
- The app still needs a more reliable installed/portable dependency discovery path before report generation can be considered frictionless in all builds.



When generating reports or spreadsheets, the application may incorrectly report missing Python dependencies (openpyxl, reportlab, Pillow, pandas) despite a valid Python environment being available.



Investigate:

\- PHQ9\_TRACKER\_BUNDLED\_PYTHON handling

\- Portable mode behavior

\- Installed mode behavior

\- Launcher environment detection

\- Packaging script dependency validation



Expected:

Application automatically locates bundled Python or installed Python environment and generates reports without requiring user configuration.

Resolution notes:

- Source report generation now checks `PHQ9_TRACKER_BUNDLED_PYTHON`, `.venv`, and `venv` for a compatible Python environment.
- Candidate environments are validated for the packages required by the requested action before a helper process is started.
- Missing-dependency errors identify the required modules and supported configuration paths.
- The source launcher prefers project-local virtual environments.
- The release script performs a dependency preflight before PyInstaller packaging.
- Automated dependency-probe and full report-generation tests passed. Installed and portable packages still require release-workstation validation.


---

REPORTING NOTE: 14-day executive comparison

Status: Implemented in Iteration 005

- The current period is the 14 calendar days ending on the selected report end date.
- The comparison period is the immediately preceding 14 calendar days.
- PHQ-9 and GAD-7 use the same symptom-frequency conversion already used elsewhere in the app.
- Entry coverage is displayed because missing days count as no recorded symptom-present response.
- If either period has no entries, the report states that there is not enough data for comparison.


---

BUG: Incorrect 14-day PHQ-9 scoring logic

Status: Fixed

The app previously displayed a recent/14-day average as if it were the intended clinical-style 14-day PHQ-9 score.

Fix:

- Added `calculate_14_day_symptom_frequency_score(entries)`.
- Counts item presence across the most recent 14 calendar days ending on the most recent entry date.
- Converts item day counts using:
  - 0 days = 0
  - 1 to 6 days = 1
  - 7 to 11 days = 2
  - 12 to 14 days = 3
- Sums converted item scores for the 14-day total score.
- Assigns severity using normal PHQ-9 total score bands.
- Missing calendar days count as no recorded symptom-present day and are documented via `entries_included`.
- Updated GUI dashboard, item summaries, clinician report, and data export labels/calculations.

---

Application Branding

Status: Open

Description:
Executable and running application do not consistently use the Mental Health Tracker application icon.

Expected:
- EXE icon uses PHQ9_Tracker.ico (or future MentalHealthTracker.ico)
- Window icon uses the same icon
- Installer uses the same icon
- Desktop shortcut defaults to the same icon

Priority:
Low

---

BUG: Duplicate notes and treatment events when updating an existing daily check-in

Status: Fixed in Iteration 006

Priority: High

Description:

When a user resubmits a check-in for a date that already contains data, the application may create additional note and treatment-event records instead of updating the existing records.

Observed behavior:

- A user updated an existing date to add a therapy treatment tag and appointment note.
- The user then submitted the same date again after correcting the GAD-7 responses and changing one word in the note.
- The assessment scores did not appear to duplicate.
- The therapy treatment event and note were duplicated.

Expected:

- The application detects when data already exists for the selected date.
- The user can review and edit the existing PHQ-9, GAD-7, note, and treatment-event data.
- Resubmitting a daily check-in updates existing records by default rather than silently creating duplicates.
- The application provides an explicit option to add an additional treatment event when multiple legitimate events occurred on the same date.
- Users can delete accidental notes, treatment events, or assessment entries.
- Destructive actions require confirmation.

Implementation considerations:

- Add a History or Manage Entries screen.
- Allow users to select a date and view all associated records.
- Provide edit and delete controls for assessments, notes, and treatment events.
- Preserve stable record IDs when updating existing records.
- Distinguish between “Update existing entry” and “Add another event.”
- Add automated tests covering repeated submissions, edits, deletions, and multiple valid treatment events on one date.

Resolution:

- Today's Check-In detects and loads existing dates and uses assessment upserts plus synchronized day-level note updates.
- Daily event selections update the first matching date/type record rather than appending another copy.
- History / Manage Entries preserves stable assessment and event IDs during edits and requires confirmation before deletion.
- The explicit Add Another Treatment Event action can intentionally create a second legitimate event, including another event of the same type.
- Automated duplicate-prevention, editing, deletion, migration, and multiple-event tests passed with synthetic data.
- Manual GUI validation completed successfully with the existing production database: prior entries loaded, edits persisted after restart, repeated saves created no duplicates, multiple same-day treatment events were retained, and confirmed deletion behaved as intended.
- Installed and portable distribution validation remains pending because PyInstaller and Inno Setup were unavailable; this packaging limitation does not affect the source-run duplicate-entry fix.

---

## BUG: Duplicate PHQ-9 14-day response table in clinician report

Status: Fixed in Iteration 007

Priority: Medium

Description:

The clinician report renders the same PHQ-9 14-day response data twice:

- “Most Recent 14-Day Symptom Responses”
- “Recent Symptom Detail”

Both sections contain the same dates, item values, totals, and severity labels.

Expected:

- Keep a single PHQ-9 14-day response table.
- Remove the duplicate section unless it is redesigned to provide genuinely different information.
- Prefer retaining “Most Recent 14-Day Symptom Responses” and removing the redundant “Recent Symptom Detail” section.
- Add a regression test that verifies the table is rendered only once.

Resolution:

- Replaced the raw-detail-heavy primary PDF with a compact conversation-focused report.
- Removed both redundant PHQ-9 raw response-table headings from the primary PDF; detailed records remain in data exports.
- Added a rendered-report regression test that confirms the old duplicate sections are absent and the report remains within the two-to-four-page target.

---

## Iteration 007.1: Navigation and Review Polish

Status: Completed

Priority: Small polish batch

Scope:

- Fix the overlapping or clipped Review chart titles.
- Reorder the tabs so **Today's Check-In** is the first tab and remains the startup selection.
- Add **Previous Day** and **Next Day** navigation to **History / Manage Entries** by reusing the established date-navigation behavior.
- Preserve unsaved-change protection and future-date prevention.
- Show a calm empty state for dates with no historical records.

Expected:

- PHQ-9 and GAD-7 Review chart titles remain fully readable and do not collide with chart or legend content, including at smaller supported window sizes.
- The visible tab order follows the primary workflow: today's recording first, intentional Review second, and historical maintenance afterward.
- History navigation handles month and year rollover, loads existing records, and does not discard unsaved edits without confirmation.
- Users cannot navigate to or create future-dated check-ins through the shared controls.
- A date without assessments, notes, or treatment events is described calmly and provides an understandable path to another date.

Implementation:

- Review charts now redraw using the live canvas width and height and place the legend below the rendered title before the plot begins.
- The tab order is Today's Check-In, Review, History / Manage Entries, Treatment Events, Clinician Report, and How Scoring Works; startup explicitly selects Today's Check-In.
- History reuses the shared calendar-day shift logic, preserves month/year rollover, loads existing records, blocks future dates, and confirms before discarding unsaved edits.
- Empty dates use a calm manage-only status and disable record-changing controls so History does not become an accidental new-entry flow.
- Nine focused tests cover tab order, History navigation and rollover, existing and empty dates, future-date blocking, unsaved-change protection, and responsive chart layout. The dependency-complete test run passed all 37 tests.

Validation:

- The project owner completed the manual source-GUI walkthrough against the canonical repository with real-world data. Tab order and startup selection, Review chart titles and resize behavior, History navigation and rollover, existing and empty dates, future-date blocking, and unsaved-change protection passed.
- Iteration 007.1 is complete. Installed and portable package validation remains outside this iteration.

---

## Future enhancement: Reporting clarity and chart value discoverability

Status: Planned for Iterations 007.2 and 008; not classified as a defect

- Restore a fuller clinician-report scoring explanation so users and clinicians can understand Daily Severity Score, 14-Day Symptom Frequency Score, and the role of coverage and missing check-ins.
- Make chart point dates and exact scores directly discoverable through click or hover callouts as an accessibility and readability improvement.
