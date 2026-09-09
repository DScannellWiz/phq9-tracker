# Iteration 009: Public Redistribution / Licensing Readiness

Current as of: 2026-09-08  
Status: Tcl/Tk startup repaired; exact candidate passed Daniel's hands-on development-workstation GUI validation; quarantined pending separate distribution authorization

## Objectives

- License Mental Health Tracker under the canonical, unmodified GNU General Public License version 3.
- Preserve Daniel Scannell's copyright identification in project documentation rather than altering the GPL text.
- Build and verify the complete third-party notice set required by the actual Windows portable runtime.
- Make the packaging process fail closed and include the project license and notices in every portable distribution.
- Produce and validate a distinct notice-complete artifact without rewriting the application version or historical evidence.
- Preserve the abandoned Closed Alpha materials as superseded provenance and keep public support software-only.
- Create one local public-readiness commit only if every release and privacy gate passes.

## Design Decisions

- Use `GPL-3.0-only`. Users may use, study, modify, redistribute, and commercially use the program subject to GPLv3. No additional medical, noncommercial, or field-of-use restriction was added.
- Keep `LICENSE` as the canonical GPL text. Put `Copyright © 2026 Daniel Scannell` and the plain-language permissions summary in the README.
- Preserve upstream license and copyright texts verbatim under `THIRD_PARTY_NOTICES`. The packaging manifest records each file's SHA-256 and the exact runtime/package versions.
- Treat license compatibility and notice preservation as separate gates. Compatible BSD, MIT, Apache, zlib, PSF, public-domain, and runtime-exception terms still travel with the binary.
- Use packaging revisions without changing application version `0.3.0-alpha.1`. `redistribution.1` identifies the rejected notice-only attempt; `redistribution.2` identifies the rebuilt Tcl/Tk repair candidate.
- Do not overwrite the old `76DE...` ZIP. It remains historical evidence of functional validation but is retired from public redistribution.
- Allow the old exact ZIP only as a verified input to the narrow notice-repackaging process. That process requires its exact SHA-256, entry count, and privacy-clean inventory, then preserves `PHQ9Tracker.exe` byte-for-byte.
- Reject a package if current GUI startup fails, even when the command-line report paths and historical executable evidence remain strong.
- Treat a process-liveness startup smoke test as necessary but not sufficient. The exact rebuilt hash required a successful hands-on GUI workflow before release-readiness changes could be committed.

## Licensing Inventory

| Distributed component | Exact version | Terms satisfied by |
| --- | --- | --- |
| Project source | `0.3.0-alpha.1` | Root `LICENSE`, canonical GPLv3; copyright statement in README |
| CPython | 3.12.10 | Complete upstream `Doc/license.rst`, including PSF terms and incorporated-software acknowledgments |
| Tcl/Tk | 8.6.15 | Verbatim Tcl/Tk BSD-style `license.terms` |
| PyInstaller bootloader | 6.22.1 | Verbatim GPL-2.0-or-later text, bootloader exception, and runtime-hook terms |
| pandas | 3.0.3 | BSD-3-Clause notice |
| NumPy and bundled code | 2.5.0 | All 17 notice files from the exact Windows wheel, including BSD-3-Clause, 0BSD, MIT, zlib, CC0, OpenBLAS/LAPACK, and GCC-runtime-exception terms |
| Pillow and embedded image/font libraries | 12.2.0 | Complete 78,014-byte upstream wheel license inventory covering Pillow and materially embedded codecs/libraries |
| ReportLab and bundled fonts | 5.0.0 | ReportLab BSD notice plus DarkGarden and Bitstream Vera notices |
| OpenPyXL | 3.1.5 | MIT license from matching source distribution |
| et_xmlfile and incorporated Python code | 2.0.0 | MIT and applicable PSF terms from matching source distribution |
| python-dateutil | 2.9.0.post0 | Dual BSD-3-Clause/Apache-2.0 notice |
| six | 1.17.0 | MIT notice |
| charset-normalizer | 3.4.7 | MIT notice |
| tzdata / IANA database | 2026.2 / 2026b | Apache-2.0 package terms and upstream public-domain data statement |
| OpenSSL | 3.0.16 | Apache-2.0 text in CPython's incorporated-software appendix |
| SQLite | 3.49.1 | Public-domain statement in CPython's incorporated-software appendix |
| Microsoft UCRT / VC runtime | 10.0.26100.4654 / 14.42.34438 | Redistributable/system runtime status retained from the audited package inventory |
| Other CPython support libraries | exact packaged CPython set | libffi, zlib, Expat, libmpdec, and related notices in the complete CPython appendix |

The declared validation dependencies `pypdf` 6.13.3 and `pypdfium2` 5.10.1 are not present in the PyInstaller runtime bundle and are not represented as distributed components.

## Files Modified

- Existing public-readiness documentation: `README.md`, `ROADMAP.md`, `BUILD_AND_RELEASE.md`, `DEVELOPMENT_JOURNAL.md`, `docs/PRIVACY_AND_DATA_HANDLING.md`, the historical Closed Alpha documents, and `docs/decisions/0007-closed-alpha-governance.md`.
- Existing packaging automation: `packaging/build_release.ps1`.
- Existing portable runtime hook: `packaging/pyi_rth_tkinter_portable.py`.

## Files Added

- `LICENSE`
- `SECURITY.md`
- `THIRD_PARTY_NOTICES/` with one inventory file and 34 hashed verbatim license/notice files
- `packaging/requirements-release.txt`
- `packaging/third_party_notice_manifest.json`
- `packaging/verify_release_licenses.py`
- `packaging/repackage_release_with_notices.ps1`
- `packaging/portable_entry.py`
- `tests/test_iteration_009_packaging.py`
- `docs/Iterations/Iteration_009_Public_Repository_Readiness.md`

## Artifact Provenance

Historical base:

- Filename: `PHQ9Tracker-Portable-0.3.0-alpha.1.zip`
- Size: 43,654,431 bytes
- Entries: 1,836
- SHA-256: `76DE3678AF9BF5C61CC0C0A318347E0F5E1C7F471A6112FE9431DA9A304F4C47`
- Source: validated uncommitted worktree based on `4f4afa7eb2046b882325b8ada6df4690d9d4a854`
- Status: historical functional candidate, retired from redistribution for incomplete notices

Notice-complete packaging-only attempt:

- Filename: `PHQ9Tracker-Portable-0.3.0-alpha.1-redistribution.1.zip`
- Size: 43,790,609 bytes
- Entries: 1,916
- Uncompressed bytes: 96,601,444
- SHA-256: `CC1EDC4E9F2A0977C13E931308B7DC3C7B32FD4C2345A6D6221AA75F9B690249`
- Executable SHA-256: `0C8D26741BF00DC53E3533F6E8580993BB2B52A20E968FD1134F2ED22D91CE74`
- Executable relation: byte-for-byte identical to the old validated candidate
- Current repository base: rewritten `main` at `156cf2e331cdf9224275ca6de9a286dbad012f19`; no application source change
- Status: rejected because the mandatory current GUI launch gate failed

The rejected ZIP and folder were moved out of `release/` into the ignored `work/blocked_iteration_009_candidate/` area so they cannot be mistaken for distributable output.

Rebuilt Tcl/Tk repair candidate:

- Filename: `PHQ9Tracker-Portable-0.3.0-alpha.1-redistribution.2.zip`
- Size: 43,745,615 bytes
- Entries: 1,910
- Uncompressed bytes: 96,483,945
- SHA-256: `5A43D176103FCEDBA1FBD36F01C78FDD88237FB27F369C859A9B37C8F497D1DA`
- Executable SHA-256: `D914BDB42E89093959467717A427F6238AD5B99629A635E0E1BE31EDC44E2E59`
- Environment: an isolated, project-local extraction of the official signed CPython 3.12.10 Windows MSI components, Tcl/Tk 8.6.15, and the exact versions in `packaging/requirements-release.txt`; no system-wide Python installation or registry change was made
- Current repository base: `156cf2e331cdf9224275ca6de9a286dbad012f19`; no application source change
- Status: startup smoke tests, non-interactive exact-artifact validation, and Daniel's hands-on development-workstation GUI walkthrough passed; the candidate remains quarantined pending separate authorization for any distribution action

The `.2` ZIP and folder are retained only in ignored `work/pending_iteration_009_candidate/` validation work. They must not be distributed or treated as approved release output.

## Validation Performed

Passed:

September 7 notice-only attempt and source checks:

- Verified the base ZIP hash, 1,836-entry count, and forbidden-private-file scan before repackaging.
- Verified the canonical project `LICENSE` and 34 verbatim third-party notice files against the committed manifest hashes.
- Verified that the new ZIP contains the root GPL and all 35 notice/index files byte-for-byte.
- Verified archive integrity, 1,916 entries, 96,601,444 uncompressed bytes, and no database, report, workbook, CSV, log, screenshot, or validation-data entry.
- Verified the executable is byte-for-byte identical to the historically validated base.
- Cleanly extracted the exact ZIP and confirmed first startup created a blank database beside the portable launcher.
- Added only project-created fictional data: 14 PHQ-9 records, 14 GAD-7 records, two notes, and three treatment events.
- Ran separate packaged command-line processes after database creation. Persistence across those restarts passed.
- Generated two five-page clinician PDFs and two eight-sheet Analysis Workbooks in the portable `reports` folder; existing outputs were not overwritten.
- Extracted the PDF text and verified date bounds, PHQ-9/GAD-7 coverage, both fictional notes, Therapy, Physical Therapy, ketamine context, and the non-diagnosis statement.
- Rendered and visually inspected all five PDF pages; no clipping, overlap, missing sections, or unreadable user text was found.
- Verified all eight workbook sheets, 28 assessment records, 224 item-response records, two note records, three distinct treatment events, the ketamine cycle relationship, 16 item-profile rows, filters, frozen headers, no merged cells, and no formula-error markers.
- Rendered and visually inspected all eight workbook sheets.
- Re-ran source and test compilation and all 59 automated tests. All passed; the known non-failing SQLite `ResourceWarning` appeared during workbook testing.
- Confirmed automated coverage for collision-safe output naming, portable output routing, Reports Folder behavior, PDF/workbook relationships, and distinct Therapy/Physical Therapy normalization.

September 8 repair and rebuilt-candidate checks:

- Reproduced the failure in the active Python 3.14.5 runtime and in a controlled Python 3.12.10/Tcl/Tk 8.6.15 runtime, proving that missing files and version mismatch were not the cause.
- Isolated the failure to Tcl path normalization in the current sandboxed Windows profile. Tcl removed or doubled path components directly below `C:\Users\<local-user>`; the same libraries initialized successfully when supplied as Windows extended paths (`//?/C:/...`).
- Added a runtime hook and pre-import entry point that set `TCL_LIBRARY` and `TK_LIBRARY` to explicit extended paths inside the PyInstaller bundle. The release verifier uses the same normalization for its source-runtime gate.
- Updated the release build to default to `redistribution.2`, use the pre-import entry point, fail on a PyInstaller error, and verify the executable, `init.tcl`, `tk.tcl`, `_tkinter.pyd`, and Tcl/Tk DLLs before packaging.
- Verified the controlled runtime as Python 3.12.10, Tcl/Tk 8.6.15, PyInstaller 6.22.1, and all other manifest-pinned versions before building.
- Verified the exact `.2` ZIP integrity, 1,910 unique entries, 96,483,945 uncompressed bytes, required runtime files, root GPL, all 34 hashed notice files plus the notice index, and no bundled user database, report, workbook, CSV, log, screenshot, or validation artifact.
- Cleanly extracted the exact ZIP to normal and short paths. Direct-executable and batch-launcher startup each remained alive beyond the smoke-test window; portable batch launch created a blank database in the expected portable location.
- Added only fictional validation data to the short-path extraction: 14 PHQ-9 assessments, 14 GAD-7 assessments, two notes, and three treatment events. Separate exact-executable invocations retained that data.
- Generated two collision-safe five-page PDFs and two collision-safe eight-sheet workbooks. Both PDFs passed text extraction and five-page visual inspection. Both workbooks passed sheet, record, relationship, formula-error, and eight-sheet visual inspection.
- Moved the fictional database aside, relaunched the exact executable, and confirmed creation of a new blank database with zero assessment and treatment-event rows.
- Added two packaging regression tests. Source/test/packaging compilation, all 61 tests, the license verifier, PowerShell parsing, `git diff --check`, Markdown/local-link checks, current/history identity scans, secret scans, and tracked-output privacy checks passed.
- Reverified immediately before the release-readiness documentation update that the quarantined `.2` ZIP still matched SHA-256 `5A43D176103FCEDBA1FBD36F01C78FDD88237FB27F369C859A9B37C8F497D1DA`.

Daniel's September 8 hands-on development-workstation walkthrough of that exact `.2` ZIP passed the required manual checks he exercised:

- fresh extraction and batch-launcher startup;
- fictional PHQ-9/GAD-7 entry with a note and treatment event, followed by close/reopen persistence;
- Review/chart interaction and keyboard/date behavior where exercised;
- sensible unsaved-change behavior;
- two GUI-generated PDFs and two GUI-generated Analysis Workbooks with collision-safe separate files;
- Open Reports Folder opening the correct folder; and
- in-app delete/reset followed by close/reopen confirmation that the data was gone and the application relaunched normally.

Daniel reported that no Windows Defender or SmartScreen prompt appeared. This records only the successful checks Daniel reported and does not infer more detailed observations. It is hands-on validation on Daniel's development workstation, not separate-machine validation of the `.2` hash. The September 7 notice-only attempt remains rejected because its batch launcher and direct executable terminated with `_tkinter.TclError: Can't find a usable init.tcl`; historical checks of the old `76DE...` ZIP remain tied only to that hash.

## Root Cause, Repair, and Release Decision

The packaged Tcl/Tk files were present and matched the intended versions. The failure arose when Tcl canonicalized paths under the sandboxed Windows user profile and lost path components before looking for `init.tcl`. Supplying the same locations as Windows extended paths made Tcl/Tk initialize. The repair is explicit and portable within the bundle: the runtime hook and the entry point establish extended `TCL_LIBRARY` and `TK_LIBRARY` values before the application imports Tkinter. No application behavior or business logic changed.

The original startup blocker is resolved: both the direct executable and the batch launcher pass current normal-path and short-path startup smoke tests, and Daniel's hands-on development-workstation walkthrough closes the specified GUI validation gate for the exact `.2` hash. The historical Windows and separate-machine evidence applies only to the old `76DE...` ZIP and is not attributed to the `.2` hash; separate-machine validation of `.2` remains unavailable.

Accordingly:

- the `.2` ZIP remains quarantined rather than distributed;
- no push, tag, GitHub Release, upload, repository visibility change, Google change, social post, or distribution occurred.

## Remaining Work

- Obtain Daniel's separate approval before pushing the release-readiness commit.
- After the push, perform the final GitHub/server privacy and readiness audit before Daniel decides whether to make the repository public.
- Separate-machine validation of the exact `.2` hash remains an explicitly documented gap; no historical separate-machine result is transferred to it.
- A repository visibility change, tag, GitHub Release, ZIP upload, distribution, or public announcement requires separate authorization.

## Lessons Learned

- A functionally validated binary can still fail redistribution compliance when runtime notices are incomplete.
- A notice-only archive change creates a new exact artifact and requires new validation even when the executable bytes do not change.
- Reproducible packaging requires both dependency versions and notice hashes; an unpinned or broken Tcl/Tk environment is a release risk.
- Historical validation should remain visible without being stretched to cover a new hash.
- An installed file can exist and have the correct version while still being unusable because a platform API canonicalizes its path incorrectly. Release checks must test initialization, not only presence.
- A launch process remaining alive proves the startup crash is repaired, but it does not prove application workflows. Exact-artifact approval must preserve that distinction.
