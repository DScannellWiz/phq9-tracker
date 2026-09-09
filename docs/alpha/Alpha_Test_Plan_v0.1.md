Current as of: 2026-09-07
Last substantive update: 2026-09-07

# Mental Health Tracker Closed Alpha Test Plan v0.1

> **Historical and superseded:** The formal Closed Alpha plan was abandoned before enrollment or distribution. This document is retained as provenance and is not an active testing, enrollment, Form, or support workflow.

## Document Status

Status: Draft working plan for owner review

Target test window: Friday, September 4, 2026 through Friday, September 18, 2026

This version turns the established closed-alpha decisions into an executable program plan. Items labeled **Provisional - Daniel approval required** are intentionally unresolved. All other items are working assumptions that may be refined as evidence is gathered.

## Purpose

The closed alpha will test whether a small group of Windows users can install, understand, and use the Mental Health Tracker reliably while retaining control of their own information. The program is intended to find usability, reliability, data-integrity, and report-usefulness problems before any broader outreach.

The alpha evaluates the software and its supporting materials. It does not evaluate participants, provide diagnosis or treatment, or conduct clinical research.

## Program Baseline

| Area | Working baseline |
| --- | --- |
| Start date | Friday, September 4, 2026 |
| Initial duration | Two weeks, ending Friday, September 18, 2026 |
| Platform | Windows only |
| Distribution | Versioned portable ZIP with a blank local database |
| Initial cohort | Approximately 5-8 deliberately recruited testers |
| Cost | Free to use during the alpha |
| Primary goals | Usability, reliability, data integrity, and report usefulness |
| Data model | Local-first; each tester retains their own health data |
| Feedback | Structured issue intake plus brief milestone surveys |
| Support | Direct support during the alpha; exact channel is provisional |
| Broader outreach | Deferred until the deliberate first cohort is reviewed |
| Clinician input | Consider a separate review track using fictional or sample reports |

## Non-Goals

- The alpha will not establish clinical efficacy or validate a diagnosis or treatment.
- It will not ask Daniel or the project to become the default custodian of participant health data.
- It will not use a shared cloud database, automatic telemetry, or background upload.
- It will not make the application the sole repository for information important to a participant's health or care.
- It will not begin broad LinkedIn recruitment before the initial cohort and program materials have been reviewed.
- It will not change application code as part of this documentation-planning step.

## Participants and Recruitment

### Initial recruitment approach

Recruit 5-8 people deliberately from trusted personal or professional contacts who are likely to provide candid feedback and who can use a Windows computer without requiring production-scale support. Prefer a varied mix of comfort levels so the test is not limited to technically confident users.

Broader LinkedIn outreach should occur only after the first cohort has completed onboarding and early findings show that the distribution, support, privacy, and feedback processes are workable.

### Eligibility

**Provisional - Daniel approval required**

Recommended initial eligibility:

- Age 18 or older.
- Access to a supported Windows computer where the participant can download, extract, and run a portable application.
- Willingness to complete onboarding, use the application during the two-week window, and provide brief structured feedback.
- Understanding that the alpha is pre-release software and is not diagnostic, treatment, crisis, or emergency software.
- Agreement not to rely on the tracker as the only copy of information important to health or care.

Recommended exclusions:

- Anyone who would need the application to provide clinical monitoring, emergency response, or guaranteed availability.
- Anyone who cannot safely retain their own local files or follow the backup guidance.
- Minors during the initial alpha, until consent, safeguarding, and support requirements have been deliberately designed.

### Tester identity

Assign sequential tester IDs such as `MHT-A001`, `MHT-A002`, and `MHT-A003`. Use the tester ID in feedback records and issue tracking instead of health information or descriptive labels.

**Provisional - Daniel approval required:** Keep any name/contact-to-tester-ID roster separate from issue records, restrict it to Daniel, and destroy it when follow-up is no longer needed. Decide whether fully pseudonymous participation is practical given direct support.

## Participant Data and Privacy Boundaries

The portable application stores its database in the participant's extracted application folder. The participant owns and controls that folder, database, reports, and exports.

The program will not collect participant databases, reports, exports, screenshots containing health information, or journal text by default. Feedback instructions must ask participants to describe the problem without copying symptoms, assessment answers, journal entries, treatment details, or clinician information.

If troubleshooting cannot proceed without an artifact that may contain health information, stop and agree on a specific, minimal, informed transfer before anything is sent. Prefer recreating the issue with fictional data. Do not place received health information in Git, ordinary issue trackers, screenshots, logs, or program summaries.

Participants may stop at any time. They may delete the extracted portable folder, including their database, reports, and exports. Deletion is permanent unless they made their own backup.

### Real versus fictional entries

**Provisional - Daniel approval required**

Recommended policy: participants may choose realistic fictional/sample entries or their own real entries, but the program should not require real health responses. If a participant chooses to enter real information, it remains local and should not be included in feedback. This preserves a useful real-world usability test without making disclosure of health data a condition of participation.

## Participant Safety and Product Boundaries

Every invitation, onboarding guide, and milestone survey should state plainly:

- Mental Health Tracker is pre-release software.
- It is not diagnostic or treatment software.
- It does not monitor participants or alert Daniel, a clinician, crisis service, or emergency service.
- It should not replace professional medical advice, crisis support, or emergency care.
- It should not be the sole repository for important health information.
- A participant should use established local emergency or crisis resources when urgent help is needed rather than using the tracker or alpha support channel.

Direct alpha support is for software use, installation, data-location questions, and defect reporting. It is not clinical support.

## Distribution and Release Controls

Provide each tester with the same approved, versioned portable ZIP unless a documented replacement build is necessary.

Before distribution:

1. Build the Windows portable package from the reviewed source revision.
2. Confirm the folder and ZIP contain no database, report, export, log, screenshot, PHI, PII, secret, or unrelated user file.
3. Confirm first launch creates a blank local database in the extracted portable folder.
4. Exercise install/extract, launch, save, close/reopen persistence, Review, PDF generation, Analysis Workbook export, and clean reset with fictional data.
5. Record the application version, source revision, ZIP filename, file size, SHA-256 hash, build date, and validation result in the release record.
6. Provide simple extraction, launch, backup, update, and deletion instructions.

Do not silently replace a tester's files. If an updated build is distributed, document whether the tester should continue with the existing folder, copy a database, or start fresh. Any data-transfer instruction must be tested first and must preserve the participant's control of their records.

## Test Schedule

### Before September 4: readiness

- Approve the provisional program decisions.
- Confirm the initial tester list and assign tester IDs.
- Freeze and validate the alpha ZIP.
- Prepare the invitation, onboarding guide, feedback form, issue log, and milestone surveys.
- Run a complete dry run using a new fictional tester identity and a clean Windows environment.

### September 4: onboarding and first-use milestone

- Send the approved ZIP and onboarding materials.
- Ask testers to extract, launch, locate the data folder, complete a fictional or personally chosen check-in, close, reopen, and confirm that the entry remains.
- Collect a very short first-use survey focused on clarity, trust, and blockers.

### September 5-10: ordinary use and direct support

- Ask testers to use the application naturally rather than follow a long script every day.
- Encourage prompt reporting of crashes, blocked workflows, confusing wording, missing records, duplicate records, or unclear privacy behavior.
- Triage issues daily during the opening days, then at a sustainable cadence.

### September 11: midpoint milestone

- Send a brief survey covering ease of check-in, navigation, confidence that data was saved, usefulness of Review, and support experience.
- Review issue patterns and decide whether any problem requires a paused test, replacement build, or clarified instruction.

### September 12-17: review and output scenarios

- Ask testers to inspect chart values, History / Manage Entries, a clinician PDF, and the Analysis Workbook as appropriate.
- Ask for usefulness and clarity feedback without requesting the generated files themselves.
- If the separate clinician-review track is active, provide only approved fictional/sample reports.

### September 18: final milestone and closeout

- Send the final brief survey.
- Remind testers how to retain, back up, or delete their local files.
- Record unresolved issues, support burden, privacy observations, and the recommendation for another closed cycle or broader recruitment.

## Core Test Scenarios

Participants should have a short checklist, not a rigid daily script. The program should obtain evidence for these scenarios across the cohort:

1. Download and extract the portable ZIP.
2. Launch the tracker and understand that it is local-first and pre-release.
3. Complete and save a Today's Check-In.
4. Close and reopen the application and confirm the saved entry remains.
5. Navigate to another date without losing unsaved work or creating an unintended record.
6. Review trends and discover exact chart dates and values.
7. Locate, edit, and intentionally delete a test record.
8. Generate and understand the purpose of the clinician PDF.
9. Generate and understand the purpose of the Analysis Workbook.
10. Locate the portable data and output folders and understand backup/deletion consequences.
11. Report a problem using the tester ID without including health information.

No single tester must exercise every destructive or export scenario with meaningful personal information. Fictional records are appropriate for deletion, reset, report-sharing, or troubleshooting practice.

## Feedback and Issue Intake

Use one structured intake path for defects and one brief survey at first use, midpoint, and closeout. The exact tools may be chosen later, but they must not require health information.

Minimum defect fields:

- Tester ID.
- Date and approximate time.
- Alpha version/build identifier.
- Windows version, if known.
- Area of the application.
- What the tester was trying to do.
- What happened.
- What the tester expected.
- Whether work appeared lost, duplicated, changed, or exposed.
- Whether the issue can be repeated with fictional data.
- Severity: blocker, major, moderate, or minor.

The form should state: **Do not include assessment answers, journal text, treatment details, clinician information, reports, exports, databases, or screenshots containing health information.**

Minimum survey themes:

- Ease of getting started.
- Clarity of the daily check-in.
- Confidence that data is saved locally.
- Ease of recovering from a mistake or missed day.
- Usefulness and understandability of Review.
- Usefulness and understandability of the clinician PDF.
- Trust in the privacy explanation.
- Most frustrating or confusing moment.
- Most valuable part.
- Willingness to continue using or recommend testing the next version.

## Triage and Response

| Severity | Meaning | Program response |
| --- | --- | --- |
| Blocker | Cannot launch or proceed; confirmed or credible data loss/corruption; serious privacy-boundary failure | Acknowledge promptly, stop the affected scenario or distribution, preserve non-sensitive evidence, and investigate before asking others to continue |
| Major | Core workflow fails or repeatedly produces an incorrect result, but a safe workaround may exist | Prioritize investigation and communicate the workaround or replacement-build decision |
| Moderate | Important confusion or defect with limited impact | Record, reproduce with fictional data, and schedule based on frequency and risk |
| Minor | Cosmetic issue, wording preference, or low-impact friction | Record and group for later review |

Do not promise immediate fixes for every report. Acknowledge receipt, clarify the impact without requesting health details, and tell the tester whether to continue, use a workaround, or pause.

**Provisional - Daniel approval required:** Choose the direct support channel, expected response window, days/hours of availability, and backup contact plan. The published expectation must be realistic for one program owner.

## Evaluation and Exit Criteria

At closeout, assess evidence by the four primary goals.

### Usability

- Testers can extract, launch, complete a check-in, and return to saved information with the supplied instructions.
- Repeated confusion points are identified and prioritized.
- Testers can distinguish Today's Check-In, Review, History / Manage Entries, clinician PDF, and Analysis Workbook purposes.

### Reliability

- Launch, save, reopen, navigation, report, and export failures are counted by build and scenario.
- Blockers and major defects have a known disposition before broader recruitment.

### Data integrity

- There is no unresolved confirmed irreversible data loss, corruption, unintended duplication, cross-date save, or privacy-boundary failure attributable to the alpha build.
- Backup, update, and deletion instructions are understandable and tested.

### Report usefulness

- Users can explain what the clinician PDF is for and whether it would help a conversation.
- Clinician reviewers, if included, evaluate only fictional/sample reports and comment on clarity, completeness, and discussion usefulness rather than participant care.

A larger alpha or broader LinkedIn outreach should begin only after Daniel reviews the findings, known risks, support burden, and unresolved high-severity issues. Completion of two weeks alone is not an automatic release decision.

## Separate Clinician-Review Track

This track is optional and separate from participant testing. Provide a small set of clearly fictional reports representing different coverage levels and histories. Ask reviewers about readability, terminology, missing context, risk of overinterpretation, and usefulness in a time-limited conversation.

Do not provide participant reports or ask clinicians to assess a participant. Clinician feedback is product feedback, not clinical advice or research data.

**Provisional - Daniel approval required:** Decide whether this track begins during the first two-week alpha or after participant feedback identifies a stable report version.

## Decisions Requiring Daniel's Approval

Before invitations are sent, Daniel should approve:

1. Final eligibility and exclusion criteria, including the recommended adults-only boundary.
2. Whether testers may participate pseudonymously and how the private contact roster will be retained and destroyed.
3. Whether testers may use either fictional or real entries, with no requirement to disclose real responses.
4. The direct support channel, response expectations, and availability.
5. Whether testers receive any compensation or only free alpha access; “free” currently means no fee to use the software.
6. The first cohort membership and wording of the invitation.
7. Timing of the separate fictional-data clinician-review track.

## Records to Retain

Retain program-level evidence without participant health data:

- Approved plan version and decision log.
- Tester-ID roster rules and, separately, the restricted contact roster while needed.
- Alpha release record and hash.
- Invitation and onboarding versions.
- Blank survey and feedback templates.
- Issue log using tester IDs.
- Build changes and replacement-build notices.
- Aggregated milestone findings.
- Closeout decision and lessons learned.

The development journal should summarize meaningful program decisions and rationale. It should not reproduce participant health information or confidential feedback verbatim.

## Known Limitations of v0.1

- The exact support and feedback tools are not selected.
- Invitation, onboarding, survey, issue-log, and release-record templates still need to be written.
- The exact alpha build/version and hash are not yet available.
- Eligibility, pseudonymity, use of real versus fictional entries, compensation, and clinician-track timing await Daniel's approval.
- This plan does not by itself authorize distribution or broader recruitment.
