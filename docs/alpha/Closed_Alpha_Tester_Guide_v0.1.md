Current as of: 2026-09-07
Last substantive update: 2026-09-07

# Mental Health Tracker Closed Alpha Tester Guide v0.1

> **Historical and unused:** The formal Closed Alpha plan was abandoned before enrollment or distribution. Public users should follow the root README instead; no tester ID, acknowledgment, milestone Form, or private download is required.

## Before You Begin

Mental Health Tracker Closed Alpha 1 runs from **September 4 through September 18, 2026**. It is voluntary software testing for adults age 18 or older. The application is unfinished pre-release software and may contain defects.

You must complete **Closed Alpha Participation Acknowledgment v0.1** before the software is distributed to you. You will also receive a tester ID such as `MHT-A001`. Use that ID whenever you submit feedback or contact support so your software reports can be tracked without putting your name in ordinary project records.

This alpha tests the software, its distribution and documentation, usability, reliability, data integrity, workflows, and the usability of generated outputs. **You, your health, and your outcomes are not being evaluated.**

## Feedback Is Software Only

You may enter real, fictional, random, or mixed data locally at your discretion. The project will not ask which type you used. Whatever you enter remains local and under your control.

**Do not send assessment responses, journal entries, treatment information, clinician information, generated PDFs, Analysis Workbooks, databases, screenshots containing entered data, or any other medical or health information, whether real, fictional, random, mixed, anonymous, or created for testing.**

This rule applies to Forms, email, support requests, and every other feedback route. If medical or health information is submitted or received, the project will not use, analyze, or intentionally retain it and will delete or destroy it as soon as reasonably practicable after identification.

## Release Information

- Tester ID: **[SUPPLIED INDIVIDUALLY]**
- Application version/build identifier: **0.3.0-alpha.1**
- Approved ZIP filename: **PHQ9Tracker-Portable-0.3.0-alpha.1.zip**
- Approved download URL: **[TBD]**
- Supported Windows versions/architecture: **Windows 11, 64-bit**
- First-use survey: **[TBD - GOOGLE FORM URL]**
- Routine problem/feedback form: **[TBD - GOOGLE FORM URL]**
- Midpoint survey: **[TBD - GOOGLE FORM URL]**
- Final survey: **[TBD - GOOGLE FORM URL]**

The Google Forms will not accept file uploads.

Use Google Forms for routine feedback and milestone surveys. Use the support email for access or administrative questions, blockers, and suspected data loss.

## Download, Extract, and Launch

1. Use only the approved download link sent for this alpha.
2. Download the ZIP, then use Windows to **Extract All** into a folder you control. Do not run the application from inside the ZIP.
3. Open the extracted folder and run `Launch Portable Mental Health Tracker.bat`.
4. If Windows blocks the file, the launcher is missing, or the application does not open, stop and contact support. Do not disable security protections or repeatedly retry based on guessed instructions.

This is a portable application. It does not use a normal installer or create system shortcuts.

## Your Local Data

Mental Health Tracker is local-first. It does not intentionally upload your assessment responses, notes, treatment events, database, reports, or exports.

On first launch, the portable application creates `phq9_tracker.sqlite` in the extracted application folder, beside the executable. That file is the local database. Closing and reopening the application should use the same database as long as you launch the same extracted copy.

When you generate a clinician PDF or Analysis Workbook, the application saves it in the `reports` folder inside the extracted application folder and asks whether you want to open it. **Open Reports Folder** in Review opens the same location later. Do not send a generated file or its contents to the project.

Because this is unfinished software, data could be lost, corrupted, duplicated, changed, or fail to save. You are responsible for backing up anything you want to preserve. **Do not use this alpha as the only copy of important information.**

### Backing Up

The safest simple backup for this portable alpha is:

1. Fully close Mental Health Tracker.
2. Copy the entire extracted application folder to a separate location you control.
3. Confirm the copied folder includes the `reports` subfolder if you want to preserve generated PDFs or Analysis Workbooks.

Do not copy, replace, rename, or move the database while the application is open. Contact software support before trying to replace the active database or move data into another build.

## September 4: First-Use Milestone

For your first session:

1. Extract and launch the application.
2. Make sure you understand that the database is stored locally in the extracted folder.
3. Complete one check-in using data of your choice.
4. Close the application completely.
5. Reopen the same extracted copy and confirm that the entry remains.
6. Complete the first-use survey.

That is enough for the first milestone. Use the application naturally after that; the goal is to learn whether the software itself is understandable.

## September 5-10: Natural Use

Use the application in whatever way is natural for you. There is no rigid daily script.

Please report software problems such as crashes, confusing or blocked workflows, missing or duplicate records, unclear wording, or privacy behavior that does not match what this guide led you to expect.

## September 11: Midpoint

Complete the brief software-only midpoint survey. It will ask about getting started, navigation, confidence that work saved, Review, and the support process. Do not include entered content or health information.

## September 12-17: Review and Outputs

As appropriate, explore:

- **Review**, including whether chart dates and values are understandable.
- **History / Manage Entries**.
- A clinician PDF generated locally with **Generate PDF**.
- A normalized Analysis Workbook generated locally with **Analysis Workbook**.

Evaluate whether these areas and outputs are clear and useful. **Do not send the PDF, workbook, screenshots containing entered data, or any of their contents.**

## What We Would Like You to Notice

- What felt obvious, and what felt confusing?
- Were you confident that your work saved?
- Could you find your way around without detailed instructions?
- Was the wording clear and calm?
- Did Review help you understand what the application recorded?
- Were the PDF and Analysis Workbook purposes understandable?
- Did anything unexpected happen?
- Were the local-storage and privacy explanations clear?

## How to Report a Problem Without Sending Your Data

Use the routine problem/feedback Form when available. Include only:

- Your tester ID.
- The area or feature involved.
- The software action you attempted.
- What actually happened.
- What you expected to happen.
- Any error text shown by the application.
- The approximate date and time.
- Whether work appeared lost, duplicated, or changed, without describing the entered content.
- Whether the problem happens again without including entered content.

Forms have no file-upload option. The safest default is **no screenshots**. A non-sensitive screenshot showing only the application interface may be used only if software support specifically requests it and you confirm that it contains no entered data or other medical or health information.

For a blocker or suspected data loss, **stop the affected activity** and email support instead of repeatedly retrying it.

## Support and Safety

Software and administrative support: `projectmentalhealthtracker@gmail.com`

Support is best effort, generally targeted within 24-48 hours, but that timing is not guaranteed. The inbox is not continuously monitored.

Mental Health Tracker and its support do not provide medical care, diagnosis, treatment, clinical monitoring, crisis response, emergency response, or guaranteed availability. The application does not alert Daniel, a clinician, a crisis service, or emergency services.

For urgent, clinical, crisis, or emergency needs, use the appropriate professional, crisis, or emergency resources. Do not send health details to the project.

## September 18: Final Survey and Closeout

Complete the final software-only survey. The active Closed Alpha 1 feedback and support cycle ends on September 18, 2026. Fixes or support for this obsolete pre-release build are not promised afterward.

You may keep the extracted application and your local data, or delete them. To remove the portable alpha, fully close the application and delete its extracted folder. This removes the application, its database, and its `reports` subfolder. Make a backup first if there is anything you want to keep.

Thank you for helping evaluate the software.

## Related Documents

- [Closed Alpha Test Plan v0.2](Alpha_Test_Plan_v0.2.md)
- [Closed Alpha Participation Acknowledgment v0.1](Closed_Alpha_Participation_Acknowledgment_v0.1.md)
