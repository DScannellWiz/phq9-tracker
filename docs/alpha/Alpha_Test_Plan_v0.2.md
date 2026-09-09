Current as of: 2026-09-07
Last substantive update: 2026-09-07

# Mental Health Tracker Closed Alpha Test Plan v0.2

> **Historical and superseded:** The formal Closed Alpha plan was abandoned before enrollment or distribution. This document is retained as provenance and is not an active testing, enrollment, Form, or support workflow.

## Document Status

Status: Approved program baseline; supporting materials and release readiness remain to be completed

Test window: Friday, September 4, 2026 through Friday, September 18, 2026

This version incorporates the program-owner decisions that were provisional in v0.1 and establishes the operating boundaries for Closed Alpha 1. It does not authorize distribution by itself. Every participant must complete the versioned Closed Alpha Participation Acknowledgment before receiving the software, and the approved release package and administrative process must still pass their readiness checks.

## Purpose

Closed Alpha 1 exists solely to evaluate and improve the Mental Health Tracker software, its distribution process, supporting documentation, usability, reliability, data integrity, workflows, and the usability of generated outputs.

The alpha is not designed to study participants, their health, behavior, treatment, PHQ-9 or GAD-7 results, health outcomes, or the effects of the software on health outcomes. The project will not collect or analyze participant health data or outcomes. Feedback is about the software and supporting materials only.

## Program Baseline

| Area | Approved baseline |
| --- | --- |
| Test window | September 4-18, 2026 |
| Platform | Windows only |
| Distribution | Approved, versioned portable ZIP with a blank local database |
| Initial cohort | 5-8 deliberately recruited adults |
| Cost or compensation | No fee and no financial or material compensation |
| Primary goals | Software usability, reliability, data integrity, workflow clarity, distribution, documentation, and generated-output usability |
| Participant data | Local-first and participant-controlled |
| Feedback | Google Forms for structured issue intake and milestone surveys |
| Support | `projectmentalhealthtracker@gmail.com`; software and administration only |
| Broader outreach | LinkedIn outreach only after the first cohort and process are reviewed, if warranted |
| Clinician review | Deferred until Closed Alpha 1 feedback is incorporated into a stable candidate report |

## Non-Goals

- Do not evaluate, diagnose, monitor, or provide treatment to participants.
- Do not investigate participant mental health, behavior, treatment, assessment results, or outcomes.
- Do not determine whether the software improves or otherwise affects health outcomes.
- Do not request, receive, retain, or analyze tracker-entered content or other medical or health information.
- Do not use the application or support address for clinical, crisis, emergency, or continuously monitored support.
- Do not rely on a shared cloud database, automatic telemetry, or background upload.
- Do not begin the clinician-review track concurrently with Closed Alpha 1.
- Do not begin broad LinkedIn recruitment before Daniel reviews the first cohort and the supporting process.
- Do not modify application code as part of this documentation iteration.

## Participants and Recruitment

### Eligibility

Participants must:

- Be age 18 or older.
- Have access to a supported Windows computer where they can download, extract, and run a portable application.
- Be willing to complete onboarding, use the application during the test window, and provide brief software-only feedback.
- Understand that the application is unfinished pre-release software and is not medical care, diagnosis, treatment, monitoring, crisis, or emergency software.
- Agree not to rely on the tracker as the only copy of information important to their health or care.

Do not enroll:

- Minors.
- Anyone who would need the application to provide clinical monitoring, emergency response, guaranteed availability, or reliable preservation as the sole copy of important information.
- Anyone who cannot safely retain and back up their local files or follow the supplied backup guidance.

### Initial cohort composition

Recruit for varied software-use perspectives, without asking anyone to disclose a diagnosis or explain why they fit a category:

- About two ordinary or nontechnical Windows users.
- One moderately technical user.
- One person familiar with PHQ-9, GAD-7, or similar self-tracking, if available, without asking how or why they are familiar.
- One person without particular mental-health-tracking familiarity.
- One to three additional useful candidates as available.

Names remain intentionally TBD. Do not rely entirely on close family; include people likely to provide candid, independent feedback. If the first cohort and operating process are workable, Daniel may later decide whether broader LinkedIn outreach is warranted.

No participant must disclose a diagnosis, health condition, treatment history, assessment use, or why they fit a recruitment perspective.

## Tester Identity and Record Separation

Assign sequential tester IDs such as `MHT-A001`, `MHT-A002`, and `MHT-A003`.

Daniel may know participant identities to communicate and provide support. GitHub issues, findings, development records, program summaries, and other ordinary project records must use tester IDs rather than participant names.

Maintain one private identity/contact-to-ID roster accessible only to Daniel. Keep it segregated from GitHub, ordinary project records, and the working issue log. The roster may record only the administrative information needed to operate the alpha, including tester ID, contact details, invitation status, acknowledgment version and date, distribution status, and closeout status.

Target destruction of the private roster 30 days after alpha closeout, meaning October 18, 2026, unless a documented administrative need requires a longer period. If retention is extended, record the reason, revised review date, and eventual destruction. Pseudonymized software-testing records may remain as permanent project provenance.

## Participant-Controlled Local Data

Participants may enter real, fictional, random, or mixed data at their discretion. The program will not ask which type they used. Whatever a participant enters belongs to and remains controlled by that participant.

The portable application stores its database in the participant's extracted application folder. Reports and exports are also generated locally. Participants are responsible for backing up information they choose to preserve. Defects, corruption, or data loss are possible because this is unfinished software.

Participants may retain and use the installed alpha after closeout or delete the application and their local data. Deletion is permanent unless they made their own backup.

## Health-Data Firewall

The project requests and accepts feedback about the software only. It does not request, collect, or analyze participant medical or mental-health information or tracker-entered content.

Every invitation, acknowledgment, guide, email, form, and troubleshooting instruction must repeatedly tell testers:

> Do not send assessment responses, journal entries, treatment information, clinician information, generated reports, Analysis Workbooks, databases, screenshots containing entered data, or any other medical or health information, whether real, fictional, random, mixed, or created solely for testing.

This rule applies even when the sender believes the content is fictional or anonymous. The program does not need to determine whether entered content corresponds to a real person.

If medical or health information is received:

1. Do not use, review for substance, analyze, copy into an issue, or intentionally retain it.
2. Delete or destroy it as soon as reasonably practicable after identification.
3. Record only a minimal administrative note, using the tester ID, that prohibited material was identified and destroyed; do not describe the content.
4. Contact the sender only as necessary to obtain non-medical troubleshooting details and remind them of the boundary.
5. Reproduce the software issue with project-created fictional data whenever possible.

No troubleshooting exception permits the project to solicit or retain entered health or medical data.

## Support and Administration

The dedicated support and administrative address is `projectmentalhealthtracker@gmail.com`.

The address is for installation, distribution, documentation, data-location, backup, and software-defect support only. It is not clinical, crisis, emergency, or continuously monitored support. Support is best effort, with a general response target of 24-48 hours rather than a guarantee.

For a blocker or suspected data loss, instruct the tester to stop the affected activity and contact support instead of repeatedly retrying the operation. Daniel may advise whether to pause, use a safe workaround, or resume after investigation.

Routine observations and milestone feedback should go through Google Forms rather than email. Email is the support and administration path for blockers, access problems, and questions that do not require health information.

## Google Workspace Controls

Use a dedicated Google Drive behind the scenes for the approved ZIP, tester materials, release documentation, survey and feedback administration, and alpha program records. The intended tester experience is:

> Email -> approved distribution instructions and link -> Google Forms feedback

Do not store participant health data in Google Drive. Do not enable file uploads in any alpha Google Form. Place the health-data warning immediately before every free-text field, not only at the beginning or end of a form.

Before use, secure the dedicated Google account with:

- Strong, unique credentials.
- Multi-factor authentication or a passkey.
- Reviewed recovery configuration.
- Conservative Drive sharing defaults.
- Folder separation among approved distribution materials, ordinary alpha records, and the restricted identity roster.

The restricted identity roster must remain accessible only to Daniel, segregated from ordinary alpha records, and never placed in GitHub.

## Participation Acknowledgment Gate

Before software distribution, every tester must affirm the current [Closed Alpha Participation Acknowledgment v0.1](Closed_Alpha_Participation_Acknowledgment_v0.1.md).

The roster must record the exact acknowledgment version and acceptance date for each tester. A later revision does not silently replace the version a participant accepted. If a material program change requires renewed acknowledgment, distribute the new version and record the new acceptance before continuing.

The document is a plain-language participation acknowledgment, not an informed-consent document or research-subject form. It must not request health information.

## Distribution and Release Controls

Provide each accepted tester with the same approved, versioned portable ZIP unless a documented replacement build is necessary.

Before distribution:

1. Confirm the participant is 18 or older and has accepted the current acknowledgment.
2. Build the Windows portable package from the reviewed source revision.
3. Confirm the folder and ZIP contain no database, report, export, log, screenshot, PHI, PII, secret, or unrelated user file.
4. Confirm first launch creates a blank local database in the extracted portable folder.
5. Exercise extraction, launch, save, close/reopen persistence, Review, PDF generation, Analysis Workbook export, backup guidance, and clean reset using project-created fictional data.
6. Record the application version, source revision, ZIP filename, file size, SHA-256 hash, build date, and validation result.
7. Provide clear extraction, launch, backup, update, support, closeout, and deletion instructions.

Do not silently replace a tester's files. Test and document any upgrade or data-transfer instruction before distribution, including whether a tester should continue with an existing folder, copy a database, or start fresh.

## Test Schedule

### Before September 4: readiness

- Secure the dedicated Google account and establish the Drive folder boundaries.
- Confirm the first cohort, assign tester IDs, and create the restricted roster.
- Complete the acknowledgment, invitation, tester guide, feedback forms, milestone surveys, issue log, release record, and closeout materials.
- Freeze and validate the alpha ZIP.
- Run the full tester experience with a fictional tester ID and a clean Windows environment.
- Do not distribute software until the acknowledgment and release gates pass.

### September 4: onboarding and first use

- Record acknowledgment version and date before sending the approved distribution link.
- Ask testers to extract, launch, understand local storage, complete a check-in using data of their choice, close, reopen, and confirm that the entry remains.
- Collect a short first-use survey focused on software clarity, trust, and blockers.

### September 5-10: ordinary use and support

- Ask testers to use the application naturally rather than follow a long daily script.
- Encourage prompt software-only reporting of crashes, blocked workflows, confusing wording, missing or duplicate records, and unclear privacy behavior.
- Triage opening-week issues at a sustainable cadence.

### September 11: midpoint milestone

- Send a brief software-only survey covering check-in usability, navigation, confidence that data saved, Review usability, and the support process.
- Decide whether any issue requires a paused scenario, clarified instruction, or replacement build.

### September 12-17: review and output scenarios

- Ask testers to inspect chart values, History / Manage Entries, a locally generated clinician PDF, and a locally generated Analysis Workbook as appropriate.
- Ask for usability and clarity feedback without requesting the generated files, their contents, or screenshots containing entered data.

### September 18: closeout

- Send the final software-only survey.
- Remind testers that they may retain the installed alpha and local data or delete them.
- Explain that the active Closed Alpha 1 feedback and support cycle ends at closeout.
- Record unresolved issues, support burden, privacy-process observations, and the recommendation for another closed cycle or broader recruitment.

After September 18, the distributed build is no longer an active feedback or support version. Later feedback is not part of Closed Alpha 1, and fixes or support for an obsolete build are not promised.

## Core Test Scenarios

Across the cohort, obtain software-only evidence for:

1. Receiving, downloading, and extracting the approved portable ZIP.
2. Launching the tracker and understanding that it is local-first and pre-release.
3. Completing and saving Today's Check-In.
4. Closing and reopening the application and confirming that the saved entry remains.
5. Navigating to another date without losing unsaved work or creating an unintended record.
6. Reviewing trends and discovering exact chart dates and values.
7. Locating, editing, and intentionally deleting a test record.
8. Generating and understanding the purpose of the clinician PDF without submitting it.
9. Generating and understanding the purpose of the Analysis Workbook without submitting it.
10. Locating the portable data and output folders and understanding backup and deletion consequences.
11. Reporting a problem using the tester ID without including entered data or other health information.

No single tester must exercise every destructive or output scenario with meaningful personal information. Participants may use data of their choice locally, but project-created fictional data should be used for reproduction and troubleshooting.

## Feedback and Issue Intake

Use Google Forms for structured defects and first-use, midpoint, and closeout surveys. Forms must not allow file uploads or request health information.

Place this warning immediately before every free-text field:

> Feedback is about the software only. Do not include assessment responses, journal entries, treatment information, clinician information, generated reports, Analysis Workbooks, databases, screenshots containing entered data, or any other medical or health information, whether real, fictional, random, mixed, or created for testing.

Minimum defect fields may include:

- Tester ID.
- Date and approximate time.
- Alpha version or build identifier.
- Windows version, if known.
- Area of the application.
- What software action the tester attempted.
- What occurred.
- What the tester expected.
- Whether work appeared lost, duplicated, changed, or exposed, without reproducing the underlying entered content.
- Whether the issue can be reproduced using project-created fictional data.
- Severity: blocker, major, moderate, or minor.

Surveys may address ease of getting started, workflow clarity, confidence in local saving, mistake recovery, Review usability, generated-output usability, privacy-instruction clarity, software frustrations, valuable features, and willingness to test a later version. Do not ask for diagnoses, assessment values, health experiences, treatments, outcomes, or whether entered data was real.

## Triage and Response

| Severity | Meaning | Program response |
| --- | --- | --- |
| Blocker | Cannot launch or proceed; suspected data loss or corruption; serious privacy-boundary failure | Tell the tester to stop the affected activity, acknowledge promptly, preserve only non-sensitive evidence, and investigate before resumption |
| Major | Core workflow fails or repeatedly produces an incorrect result, but a safe workaround may exist | Prioritize investigation and communicate the workaround, pause, or replacement-build decision |
| Moderate | Important confusion or defect with limited impact | Record, reproduce with project-created fictional data, and prioritize by frequency and risk |
| Minor | Cosmetic issue, wording preference, or low-impact friction | Record and group for later review |

Do not promise an immediate fix for every report. Clarify software behavior and impact without requesting entered data or health details.

## Evaluation and Exit Criteria

Evaluate only the software and program process:

- Can testers receive, extract, launch, use, and revisit the application with the supplied materials?
- What software defects, confusing workflows, or documentation gaps recur?
- Do records persist and remain associated with the intended date in tested scenarios?
- Can testers understand the purposes of Review, History / Manage Entries, the clinician PDF, and the Analysis Workbook?
- Are backup, update, closeout, and deletion instructions understandable?
- Did the support, Google Forms, identity separation, and health-data firewall work as designed?
- Are all blockers and major defects assigned a documented disposition before broader recruitment?

Do not evaluate participant health, behavior, treatment, results, outcomes, or software effects on health outcomes. Completion of the two-week window is not an automatic decision to expand testing.

## Clinician-Review Track

The clinician-review track is deferred until Closed Alpha 1 feedback has been incorporated into a stable candidate report. Do not run it concurrently.

Any later clinician review must remain a separate product-feedback activity using project-created fictional reports. It must not use participant reports, request clinical assessment of a participant, or collect health outcomes.

## Records and Retention

Retain program-level evidence without participant health data:

- Approved plan and acknowledgment versions.
- Decision record and development-journal entries.
- Blank invitation, tester-guide, survey, and feedback templates.
- Release record and ZIP hash.
- Pseudonymized issue log using tester IDs.
- Replacement-build notices.
- Aggregated software and process findings that contain no entered data or health information.
- Closeout decision and lessons learned.

The restricted identity/contact-to-ID roster is a separate administrative record, accessible only to Daniel and targeted for destruction on October 18, 2026 unless a documented administrative need requires otherwise. Pseudonymized software-testing records may remain as permanent project provenance.

## Compliance and Project Risk Posture

Daniel understands that assistant discussion is not legal advice and does not interpret it as legal advice. He chose to proceed without paid legal review because of cost, while deliberately adopting a conservative software-testing and health-data-minimization posture.

Maryland Health-General § 13-2001 incorporates the federal human-subject framework's definition of research. Under 45 C.F.R. § 46.102(l), the Common Rule definition turns on whether an activity is a systematic investigation, including testing and evaluation, designed to develop or contribute to generalizable knowledge. Maryland Health-General § 13-2002 applies the federal human-subject protections when an activity is research using a human subject.

Closed Alpha 1 is intentionally structured as product and software usability/functionality testing, not clinical or behavioral research. Its purpose is to improve this software and its immediate program process. It does not request or analyze participant health information, assessment results, treatment information, health outcomes, or the effects of the software on health.

This is a documented project decision and risk posture, not a binding legal determination. Participants are called testers or participants, not research subjects, and the participation document is not called informed consent.

Authoritative references reviewed:

- [Maryland Health-General § 13-2001](https://mgaleg.maryland.gov/2026RS/Statute_Web/ghg/13-2001.pdf)
- [Maryland Health-General § 13-2002](https://mgaleg.maryland.gov/2026RS/Statute_Web/ghg/13-2002.pdf)
- [45 C.F.R. § 46.102 (eCFR)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/subpart-A/section-46.102)
- [HHS OHRP: What Is Human Subjects Research?](https://www.hhs.gov/ohrp/education-and-outreach/online-education/human-research-protection-training/lesson-2-what-is-human-subjects-research/index.html)

## Approved Decisions and Remaining Implementation Work

All seven decisions marked provisional in v0.1 are resolved in this version: eligibility and exclusions, pseudonymous project records, participant choice of local entered data, support channel and expectations, no compensation, recruitment approach, and deferred clinician review.

Remaining work is operational rather than a reopened program-policy decision:

- Select the 5-8 named testers.
- Confirm the exact alpha application version, source revision, release filename, and SHA-256 hash.
- Build and validate the invitation, Tester Guide, Google Forms, milestone surveys, issue log, release record, Drive folder structure, replacement-build procedure, and closeout message.
- Complete the clean-Windows dry run and release-readiness decision.

## Related Records

- [Closed Alpha Test Plan v0.1](Alpha_Test_Plan_v0.1.md) preserves the earlier provisional baseline.
- [Closed Alpha Participation Acknowledgment v0.1](Closed_Alpha_Participation_Acknowledgment_v0.1.md) is the required pre-distribution participant-facing record.
- [Closed Alpha Tester Guide v0.1](Closed_Alpha_Tester_Guide_v0.1.md) provides the participant-facing safe-use, milestone, feedback, support, and closeout instructions. Its substantive content is ready to freeze once the tester-facing version/build, ZIP filename, compatibility, download URL, and Form URLs are filled and confirmed against the frozen package. Internal build and release controls remain governed by this plan and the release-readiness records.
- [Closed Alpha 1 Candidate Release Record](Closed_Alpha_1_Candidate_Release_Record.md) records candidate `0.3.0-alpha.1`, the local package evidence, source provenance, ZIP size/hash, and remaining pre-distribution gates.
- [ADR 0007: Closed Alpha Governance and Health-Data Firewall](../decisions/0007-closed-alpha-governance.md) records the durable governance decision.
