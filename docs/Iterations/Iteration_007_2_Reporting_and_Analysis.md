Current as of: 2026-08-15
Last substantive update: 2026-08-15

# Iteration 007.2: Reporting and Analysis

## Status

Implementation, automated source-level validation, and real Windows portable-package validation are complete. The portable ZIP is validated for the immediate Florida use case. Installer validation remains pending because Inno Setup is unavailable. The packaged runtime window/taskbar icon still shows the generic Tk feather and is tracked as a deferred cosmetic packaging issue rather than a release blocker.

## Objectives

- Add a separate normalized Excel workbook for independent analysis.
- Preserve all selected-period user-authored journal text in clinician reports.
- Restore a complete scoring, coverage, and missing-check-in explanation.
- Improve clinician-report naming and flow while keeping the normal case compact and conversation-focused.
- Validate the blank portable-database behavior for the immediate Florida use case without using production PHI.
- Document future Travel Mode and LAN-only sharing concepts without implementing them.

## Design Decisions

- The existing combined export remains unchanged for backward compatibility.
- The new workbook uses **Daily Assessments**, **Item Responses**, **Notes**, **Treatment Events**, **Treatment Cycles**, **Metadata**, and a derived **Daily Summary**.
- Existing SQLite assessment and treatment-event IDs are retained in export fields. Deterministic `day:YYYY-MM-DD`, assessment-item, note-date, and cycle-date identifiers provide relationships where no separate database entity exists.
- Normalized worksheets are authoritative. Daily Summary may join identifiers and expose common event flags only as a convenience view.
- The clinician report begins with **How to Read This Report** and uses the sequence **Recorded Period Overview**, **Recorded Symptom Trends**, **Treatment Context**, **Journal and Event Context**, and **Conversation Starters**.
- All notes in the selected date range are included without character or row limits. Report length may expand to preserve narrative integrity.
- No scoring or schema migration was introduced.

## Files Modified

- `src/phq9_tracker/app.py`
- `tests/test_iteration_007_ux.py`
- `README.md`
- `ROADMAP.md`
- `BugList.md`
- `BUILD_AND_RELEASE.md`
- `DEVELOPMENT_JOURNAL.md`
- `docs/decisions/0005-conversation-focused-reporting.md`
- `docs/PRIVACY_AND_DATA_HANDLING.md`
- `docs/PROJECT_STRUCTURE.md`

## Files Added

- `tests/test_iteration_007_2_reporting_portable.py`
- `docs/Iterations/Iteration_007_2_Reporting_and_Analysis.md`

## Validation Performed

- All 40 automated tests passed with isolated synthetic databases.
- Python compilation passed for application and test code.
- Workbook validation confirmed exact logical worksheets, snake_case fields, no merged cells, stable cross-sheet relationships, ISO dates, complete note text, and independent rows for two legitimate same-day events.
- Portable source-level validation confirmed a frozen portable launch selects a database beside the executable, synthetic data persists after reopen, and deleting/reinitializing the database returns assessment and treatment-event counts to zero.
- A four-page synthetic clinician report passed text extraction and complete-note checks, then every page was rendered and visually inspected for clipping, overlap, special-character handling, tables, charts, section transitions, footers, and page numbering.
- Source and packaging files consistently reference `packaging/assets/PHQ9_Tracker.ico`.
- The attempted source-GUI smoke test stopped before the application window opened because the available Python runtime could not find a usable `init.tcl`. No interactive GUI result is claimed.
- PyInstaller 6.22.1 built the folder-based application successfully and created `release\PHQ9Tracker-Portable-0.2.0\` and `release\PHQ9Tracker-Portable-0.2.0.zip`.
- Before first launch, both the portable folder and ZIP were inspected and contained no `.sqlite`, `.db`, or `.sqlite3` files.
- The first packaged launch created `phq9_tracker.sqlite` inside the portable folder. Review, History / Manage Entries, Treatment Events, Clinician Report, and How Scoring Works opened cleanly with no prior data.
- Synthetic entries persisted across a full close and reopen. The packaged clinician PDF generated successfully and passed manual review.
- The packaged Analysis Workbook generated successfully and passed structural and data-integrity inspection. Its seven worksheets were **Daily Assessments**, **Item Responses**, **Notes**, **Treatment Events**, **Treatment Cycles**, **Metadata**, and **Daily Summary**; relationships and calculations reconciled, narrative and event text was complete, and no merged cells were present.
- Deleting the portable database and relaunching recreated a pristine blank state.
- PyInstaller embedded the intended icon, but the running window/taskbar representation still showed the generic Tk feather. This is a deferred cosmetic packaging issue, not a blocker for the validated portable ZIP.

## Remaining Work

- Resolve and revalidate the runtime window/taskbar icon so it uses the intended application icon instead of the generic Tk feather.
- Install Inno Setup, then compile and test the installer, including installed-mode launch, LocalAppData persistence, Start Menu behavior, desktop-shortcut behavior, and installed icon presentation.

## Deferred Architecture Concepts

### Data Portability and Recovery

A future Travel Mode should create a clean database with no historical records. On return, the application should validate and transactionally append only travel-created records into an authoritative home database, report duplicates or conflicts, then clear the travel database and verify zero assessments, notes, and treatment events. Iteration numbering remains intentionally open.

### LAN Sharing

A future LAN-only mode should keep SQLite local to one authoritative host. Clients should communicate with an authenticated local host/service; they must not open the SQLite file directly across a network share. Cloud relay and public Internet access remain out of scope. Iteration numbering remains intentionally open.

## Lessons Learned

- A readable clinical aid and an analysis workbook need different structures.
- “Compact” must describe information design, not the deletion of user-authored context.
- Export identifiers can provide stable analytical relationships without prematurely changing the database schema.
- Portable database behavior can be tested safely with synthetic data, but source-level routing evidence is not a substitute for validating the final packaged ZIP.
- A portable package can be suitable for a specific release use case even when a cosmetic runtime-icon defect and the separate installer-validation path remain open, provided the limitation is documented and privacy/data-integrity checks pass.
