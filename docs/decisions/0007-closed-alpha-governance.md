Current as of: 2026-09-07
Last substantive update: 2026-09-07

# ADR 0007: Closed Alpha Governance and Health-Data Firewall

## Status

Superseded for program operation on 2026-09-07. The formal Closed Alpha was abandoned before enrollment or distribution. Its cohort, tester-ID, acknowledgment, schedule, and private-Form workflow is not active. The categorical health-data firewall remains accepted for public support and issue handling.

## Context

The first external test needs enough participant identity information for communication and enough structured feedback to improve the software. The application also handles sensitive local content, so ordinary troubleshooting practices such as collecting databases, reports, screenshots, or entered examples would create privacy risk and conflict with the local-first design.

The program's purpose also matters. Closed Alpha 1 is intended to improve this software and its immediate distribution, documentation, workflows, reliability, data integrity, and generated-output usability. It is not intended to study participants, health, behavior, treatment, assessment results, outcomes, or effects on health.

## Decision

- Operate Closed Alpha 1 as software product/usability/functionality testing for 5-8 adults from September 4-18, 2026.
- Use tester IDs in GitHub and ordinary project records. Keep the identity/contact-to-ID roster accessible only to Daniel, segregated from GitHub, and targeted for destruction 30 days after closeout unless a documented administrative need requires otherwise.
- Permit participants to enter real, fictional, random, or mixed data locally without asking which, while treating all entered content as out of scope for collection.
- Accept software-only feedback. Never request assessment responses, journal entries, treatment or clinician information, generated reports, Analysis Workbooks, databases, screenshots containing entered data, or other medical or health information, even when fictional or created for testing.
- Do not use, analyze, or intentionally retain prohibited material that is received, regardless of whether it was sent accidentally or intentionally; delete or destroy it as soon as reasonably practicable after identification and seek only non-medical troubleshooting details.
- Require a versioned, plain-language Closed Alpha Participation Acknowledgment before distribution. Do not call it informed consent and do not describe testers as research subjects.
- Use Google Forms without file uploads, show the health-data warning immediately before every free-text field, and use `projectmentalhealthtracker@gmail.com` only for software and administrative support.
- Defer clinician review until participant feedback has been incorporated into a stable candidate report.

## Rationale

A categorical health-data firewall is easier for testers and the project owner to follow than a policy requiring judgments about whether submitted content is real, identifiable, or necessary. Tester IDs preserve useful project provenance while reducing routine exposure of participant identity. A separate acknowledgment records the material conditions of participation without importing research terminology into a product-testing program.

The governance posture also documents the project's interpretation of its own purpose. Maryland incorporates the federal human-subject framework, whose research definition turns on a systematic investigation designed to develop or contribute to generalizable knowledge. The alpha is deliberately limited to improving the software and its immediate process and does not collect or analyze health data or outcomes. This is a project decision and risk posture, not a binding legal determination or legal advice; Daniel chose to proceed without paid legal review.

## Consequences

- Troubleshooting may take longer because participant files and entered content are not accepted.
- Project-created fictional reproduction data becomes the preferred diagnostic evidence.
- The private roster requires access control, a destruction target, and a documented exception if retained beyond October 18, 2026.
- Google Forms, email templates, the Tester Guide, issue handling, and closeout materials must implement the same warning and record-separation rules.
- Pseudonymized software feedback may remain permanently; participant identities and entered content do not belong in permanent project records.
- Later work that proposes health-data collection, outcome analysis, clinical claims, broader telemetry, or a research purpose requires a new decision and a fresh compliance review before implementation.

## References

- [Mental Health Tracker Closed Alpha Test Plan v0.2](../alpha/Alpha_Test_Plan_v0.2.md)
- [Closed Alpha Participation Acknowledgment v0.1](../alpha/Closed_Alpha_Participation_Acknowledgment_v0.1.md)
- [Closed Alpha Tester Guide v0.1](../alpha/Closed_Alpha_Tester_Guide_v0.1.md)
- [Maryland Health-General § 13-2001](https://mgaleg.maryland.gov/2026RS/Statute_Web/ghg/13-2001.pdf)
- [Maryland Health-General § 13-2002](https://mgaleg.maryland.gov/2026RS/Statute_Web/ghg/13-2002.pdf)
- [HHS OHRP: What Is Human Subjects Research?](https://www.hhs.gov/ohrp/education-and-outreach/online-education/human-research-protection-training/lesson-2-what-is-human-subjects-research/index.html)
