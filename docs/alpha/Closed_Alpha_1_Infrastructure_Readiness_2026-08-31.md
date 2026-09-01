# Closed Alpha 1 Infrastructure Readiness

Current as of: 2026-08-31

## Release anchor

- Candidate build: `0.3.0-alpha.1`
- Approved package filename: `PHQ9Tracker-Portable-0.3.0-alpha.1.zip`
- Source anchor: commit `f3d6fd6a6f175ca9cf2e936caf9cae7656893d11`, `Release Closed Alpha 1 candidate 0.3.0-alpha.1`
- Candidate state remains frozen. No application source was changed during this infrastructure pass.
- The ZIP has not been uploaded, shared, or distributed. No tag or GitHub Release was created.

## Google infrastructure verified and completed

- Work was performed in the dedicated project administration account.
- The existing `Mental Health Tracker - Closed Alpha 1` Drive structure and separate restricted identity roster were preserved rather than recreated.
- The `02 Forms and Responses` folder now contains five private Forms and their five linked response Sheets:
  - Participation Acknowledgment
  - First-Use Survey
  - Midpoint Survey
  - Final Survey
  - Routine Problem / Feedback
- All five Forms are unpublished and showed zero responses at the end-of-night audit.
- All tester-ID dropdowns contain only the clearly fictional validation ID `MHT-TEST-001`.
- Email collection, sign-in/one-response restrictions, response editing, response summaries, and question shuffling are off. Progress-bar behavior matches each approved specification.
- No file-upload question, health-data request, real tester identity, responder link distribution, or public/link sharing was introduced.

## Reconciliation results

The live Forms were compared with the approved specifications. The following private-draft defects were found and corrected:

- Participation Acknowledgment: added the missing tester-ID and acknowledgment-version dropdowns; added the exact health-data warning before the typed-name field. The Form now has all 14 defined questions, all required, with ten separate `I affirm` checkbox questions.
- First-Use: added the missing local-database-storage clarity scale; added the exact warning before the optional narrative question; confirmed ordinary-path and blocker-path branching. The Form now has all 10 defined questions.
- Midpoint: removed visible Markdown backticks around `None` in the Question 9 prompt. All 11 questions, choices, required states, warning, settings, and confirmation message match the specification.
- Final: changed Questions 3 and 4 from multiple choice to the approved dropdown type. All 15 questions, choices, required states, grid requirement, warning, settings, and confirmation message match the specification.
- Routine Problem / Feedback: created and linked the previously deferred Form and response Sheet using build `0.3.0-alpha.1`; verified all 12 questions, exact warnings, branching, required states, choices, settings, and confirmation message.

The private `Closed Alpha 1 Release and Administration Record` now records the candidate build and approved ZIP filename and explicitly states that no upload or distribution has occurred. Its download URL remains intentionally blank.

## Packaged-candidate validation added at closeout

On August 31, Daniel transferred the exact candidate ZIP to a volunteer's separate Windows computer. The volunteer received and extracted the ZIP on that computer, launched and used the packaged application, and played around in it; Daniel reports that all behavior exercised during the session worked. No Python, Tkinter, or other development runtime was installed or prepared for this test.

This is separate-machine Windows evidence for receiving, extracting, launching, and generally using the packaged candidate. It closes the identified separate-Windows extraction-and-launch gate to the extent supported by those observations. It is not evidence of a pristine virtual machine or freshly installed Windows image, specific SmartScreen or other Windows security-prompt behavior, or exact persistence and output subtests. This test remains distinct from Daniel's earlier extracted EXE and batch-launcher check on his development workstation and Work's installed-mode desktop-control validation.

## Gates that still require Daniel

1. Select the real invited testers and assign their final pseudonymous tester IDs. Keep the identity/contact-to-ID roster Daniel-only and separate from ordinary project records.
2. Replace `MHT-TEST-001` in every tester-ID dropdown with only the final assigned IDs. Do not retain the fictional ID when the Forms are opened for live use.
3. Explicitly authorize Form publication for validation. Publication is required before signed-out/private-browser responder testing can occur.
4. Perform or authorize signed-out/private-browser testing with a fictional administrative identity. Verify required-field blocking, branching, confirmation messages, and absence of unintended access. Delete or clearly label the fictional responses before live use.
5. Perform the fictional end-to-end administrative dry run, including acknowledgment gating and the separate post-gate distribution step, before any real tester receives the package. Observe any still-unverified Windows security-prompt behavior if final risk acceptance requires it.
6. Only after those gates pass, make the final go/no-go decision and explicitly authorize uploading the approved ZIP file, creating anyone-with-the-link viewer access for that ZIP file only, recording the exact download URL, and distributing it individually after each tester's acknowledgment gate passes.

## Recommended next gate

The next administrative gate is tester selection and final tester-ID assignment. That is the prerequisite for finalizing every tester-ID dropdown. Explicit Form-publication authorization, signed-out/private-browser validation, and the fictional end-to-end dry run follow. No tester-facing action is authorized by this report.

## Documentation and Git

This report was synchronized into the canonical repository as part of a documentation-only closeout after the packaged candidate source/release commit. Application source and packaging behavior remain unchanged.

Suggested commit message: `Document Closed Alpha 1 infrastructure readiness`
