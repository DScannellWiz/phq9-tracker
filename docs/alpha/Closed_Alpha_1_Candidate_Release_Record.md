Current as of: 2026-08-31
Last substantive update: 2026-08-31

# Closed Alpha 1 Candidate Release Record

## Candidate

- Application version/build: `0.3.0-alpha.1`
- ZIP: `PHQ9Tracker-Portable-0.3.0-alpha.1.zip`
- Size: 43,654,431 bytes
- SHA-256: `76DE3678AF9BF5C61CC0C0A318347E0F5E1C7F471A6112FE9431DA9A304F4C47`
- Built: 2026-08-31
- Locally established compatibility: Windows 11, 64-bit
- Status: packaged candidate validated locally and on a separate Windows computer; not distributed and not a final go/no-go

The exact build value for the Routine Problem / Feedback Form is `0.3.0-alpha.1`.

## Source Provenance

Packaging used an uncommitted but validated canonical worktree based on Git commit `4f4afa7eb2046b882325b8ada6df4690d9d4a854` (`4f4afa7 Document planned clinician output fidelity fixes`). The worktree included approved Iterations 008.1 and 008.2 and Closed Alpha documentation changes. Those changes were not staged or committed, so the base commit must not be represented as containing the candidate source.

## Pre-Build Validation

- Source and test Python compilation passed.
- Full dependency-complete suite passed: 59/59, no failures or skips.
- One non-failing Python `ResourceWarning` about delayed SQLite connection cleanup appeared during workbook testing.
- `git diff --check` passed; line-ending warnings were informational.
- No files were staged.
- Sensitive/local generated artifacts in the canonical workspace were identified and excluded. The release source snapshot and candidate archive contained no database, reports, workbooks, screenshots, CSV files, logs, credentials, private rosters, or Google administrative records.

## Packaging Result

The first build attempt was rejected because PyInstaller's automatic Tcl/Tk discovery excluded Tkinter. The release script was corrected to validate and explicitly bundle Tkinter, Tcl/Tk libraries, and a portable runtime hook. The rebuilt archive contained 1,836 entries and no database.

A clean extraction started with no database. Starting it in portable mode created `phq9_tracker.sqlite` beside the executable before GUI initialization, confirming portable containment. Automated tests independently cover portable database and `reports` routing. The exact packaged executable then completed the full fictional GUI workflow in a normal Windows desktop launch; because the desktop-control path could not invoke the batch launcher directly, that GUI run used installed-mode LocalAppData while portable routing was verified separately.

On August 31, 2026, Daniel independently checked the actual candidate on his Windows development workstation. The previously reported `%LOCALAPPDATA%\PHQ9Tracker` validation folder was already absent. He manually extracted `PHQ9Tracker-Portable-0.3.0-alpha.1.zip`, launched `PHQ9Tracker.exe` directly from the extraction, and then launched `Launch Portable Mental Health Tracker.bat`; both launches succeeded and each presented a blank database. This is owner validation of the extracted candidate and both launch paths on the development workstation. It is distinct from the earlier Work desktop-control installed-mode pass and is not a separate clean-machine validation.

Later on August 31, Daniel transferred the exact candidate ZIP to a volunteer's separate Windows computer. The volunteer received and extracted the ZIP on that computer, launched and used the packaged application, and played around in it; Daniel reported that all behavior exercised during that session worked. No Python, Tkinter, or other development runtime was installed or prepared for the test. This supplies separate-machine Windows evidence for receiving, extracting, launching, and generally using the packaged candidate and closes the identified separate-Windows extraction-and-launch gate to that extent. It does not establish a pristine virtual machine or fresh Windows image, specific Windows security-prompt behavior, or exact persistence and output subtests. It remains distinct from Daniel's development-workstation EXE/batch-launcher check and Work's installed-mode desktop-control validation.

## Fictional Packaged Validation

- Started blank on Today's Check-In and primary screens were blank.
- Saved fictional PHQ-9, GAD-7, note, Therapy, and Physical Therapy records; close/relaunch persistence passed.
- Review charts, exact point callout, keyboard navigation, guarded date behavior, unsaved-change protection, and History/manage behavior passed.
- PDF and workbook each generated twice with collision-safe names into the common `reports` folder. No companion CSV appeared.
- Optional open prompts were exercised. Excel opened the workbook. The PDF association launched Brave, which reported that it could not see the file even though immediate filesystem checks confirmed both PDFs existed; the application preserved successful generation. Daniel's source-GUI walkthrough had already passed the PDF open behavior.
- The five-page PDF passed extraction and rendered-page inspection. It contained the complete fictional note, all 16 current-profile items with 1-of-14 coverage, and distinct Physical Therapy and Therapy rows sharing the same description.
- The workbook contained eight expected sheets, 16 profile records, correct relationships, distinct event rows, complete fictional text, readable formatting, and no formula-error markers.
- The distribution folder and ZIP remained pristine and database-free throughout validation.

The earlier desktop-control run reported a project-created fictional database and four generated outputs under `%LOCALAPPDATA%\PHQ9Tracker` because that controlled workspace lacked deletion access. When Daniel checked on August 31, that folder was already absent. No cleanup action remains from that run.

## Remaining Gates

- If needed for final risk acceptance, observe any still-unverified Windows security-prompt behavior during the fictional end-to-end dry run; a volunteer's test did not record that detail.
- Publish the five private Forms only after Daniel's explicit authorization, then validate them signed out/private-browser and complete the end-to-end fictional tester dry run.
- Select real testers, assign tester IDs, and complete the Participation Acknowledgment before distribution.
- Confirm the final Guide/download/Form values and Daniel's final go/no-go.
- Do not distribute, upload, publish Forms, create a tag or GitHub Release, or treat this local validation as distribution authorization.
