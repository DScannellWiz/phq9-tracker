Current as of: 2026-09-08
Last substantive update: 2026-09-08

# Closed Alpha 1 Candidate Release Record

> **Historical and superseded:** Closed Alpha 1 was abandoned before enrollment or distribution. This record preserves candidate evidence and limitations; its Form, tester-ID, acknowledgment, and cohort gates are not the current release path.

## Candidate

- Application version/build: `0.3.0-alpha.1`
- ZIP: `PHQ9Tracker-Portable-0.3.0-alpha.1.zip`
- Size: 43,654,431 bytes
- SHA-256: `76DE3678AF9BF5C61CC0C0A318347E0F5E1C7F471A6112FE9431DA9A304F4C47`
- Built: 2026-08-31
- Locally established compatibility: Windows 11, 64-bit
- Status: historically validated locally and on a separate Windows computer, but retired from public redistribution because required third-party notices were incomplete

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

Later on August 31, Daniel transferred the exact candidate ZIP to a volunteer's separate Windows computer. The volunteer received and extracted the ZIP on that computer, launched and used the packaged application, and reported through Daniel that all behavior exercised during that session worked. No Python, Tkinter, or other development runtime was installed or prepared for the test. This supplies separate-machine Windows evidence for receiving, extracting, launching, and generally using the packaged candidate and closes the identified separate-Windows extraction-and-launch gate to that extent. It does not establish a pristine virtual machine or fresh Windows image, specific Windows security-prompt behavior, or exact persistence and output subtests. It remains distinct from Daniel's development-workstation EXE/batch-launcher check and Work's installed-mode desktop-control validation.

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

## Public-Redistribution Follow-Up

The exact 43,654,431-byte, 1,836-entry ZIP above contains compatible components but lacks the project GPL, CPython's required license set, and multiple third-party notices. It must not be uploaded or described as redistribution-ready.

On September 7, 2026, the base hash was reverified and the unchanged executable was packaged with `LICENSE` and the complete notice set as `PHQ9Tracker-Portable-0.3.0-alpha.1-redistribution.1.zip` (43,790,609 bytes; 1,916 entries; SHA-256 `CC1EDC4E9F2A0977C13E931308B7DC3C7B32FD4C2345A6D6221AA75F9B690249`). The executable SHA-256 remained `0C8D26741BF00DC53E3533F6E8580993BB2B52A20E968FD1134F2ED22D91CE74`.

Archive integrity, privacy, notice matching, fictional packaged persistence, repeated PDF/workbook generation, extracted PDF content, five rendered PDF pages, workbook relationships, and eight rendered workbook sheets passed. Current GUI startup did not: the clean extraction terminated with `_tkinter.TclError: Can't find a usable init.tcl`. Therefore this notice-complete ZIP was rejected rather than promoted. The August 31 development-workstation and separate-machine checks remain evidence only for the old `76DE...` ZIP; they are not attributed to the new hash.

On September 8, the failure was isolated to Tcl path normalization under the sandboxed Windows user profile, not to missing or mismatched Tcl/Tk files. The problem reproduced in Python 3.14.5 and an isolated official CPython 3.12.10/Tcl/Tk 8.6.15 environment. Addressing the same Tcl/Tk directories through Windows extended paths allowed initialization. The release runtime hook and a pre-import packaging entry point now establish those bundle-relative paths explicitly; application source did not change.

The full pinned rebuild produced `PHQ9Tracker-Portable-0.3.0-alpha.1-redistribution.2.zip` (43,745,615 bytes; 1,910 entries; SHA-256 `5A43D176103FCEDBA1FBD36F01C78FDD88237FB27F369C859A9B37C8F497D1DA`). Its executable SHA-256 is `D914BDB42E89093959467717A427F6238AD5B99629A635E0E1BE31EDC44E2E59`. Normal- and short-path direct/batch startup smoke tests passed. The exact ZIP also passed GPL/notice and privacy audits, portable blank-database and fictional command-line persistence checks, two collision-safe PDF and workbook generations with content and rendered inspection, reset/relaunch checks, compilation, and all 61 automated tests.

Daniel later completed the required hands-on GUI walkthrough against the exact quarantined `.2` ZIP on his development workstation. He reported that fresh extraction and batch launch, fictional PHQ-9/GAD-7 entry with a note and treatment event, close/reopen persistence, Review/chart interaction, exercised keyboard/date behavior, unsaved-change handling, two collision-safe GUI PDF generations, two collision-safe GUI Analysis Workbook generations, Open Reports Folder, in-app delete/reset, and close/reopen after reset all worked. No Windows Defender or SmartScreen prompt appeared. This record does not infer more detailed observations and does not constitute separate-machine validation of `.2`; no earlier separate-machine evidence is attributed to this hash. The artifact remains quarantined pending separate authorization for any distribution action.

## Remaining Gates

- Obtain Daniel's separate authorization before pushing the release-readiness commit.
- After the push, perform the final GitHub/server privacy and readiness audit before deciding whether to make the repository public.
- Treat separate-machine validation of the exact `.2` hash as an open provenance gap; do not transfer historical evidence to it.
- Obtain Daniel's separate authorization before any visibility change, upload, tag, GitHub Release, or distribution.
- Do not revive or publish the abandoned Closed Alpha Forms, tester-ID, acknowledgment, or cohort workflow.
