# Development Journal

This journal records the human context behind significant product and engineering choices. Formal narrative capture begins around Iteration 007; the earlier entries below are a concise reconstruction from surviving documentation rather than contemporaneous notes.

## Reconstructed Prehistory

### Spreadsheet era

The project began as a spreadsheet created to preserve symptom information across the time between appointments. It established the core practice of recording PHQ-9 responses and looking across a 14-day period rather than relying entirely on memory at the next conversation with a clinician.

### First PHQ-9 application

The spreadsheet evolved into a local PHQ-9 Tracker. The application introduced a more deliberate daily-entry workflow, local SQLite storage, reports, and exports while keeping sensitive information under the user's control. Early scoring work corrected the 14-day calculation so the application followed the symptom-frequency approach established in the spreadsheet prototype.

### Reusable assessments and GAD-7

Iteration 004 changed the project from a single-purpose PHQ-9 tool into a reusable multi-assessment framework. PHQ-9 compatibility was preserved while a generic assessment model and GAD-7 were added. The visible identity shifted to **Mental Health Tracker**, reflecting a broader foundation without discarding established data contracts.

### Data integrity and history management

As daily use exposed the risks of duplicate or hard-to-correct records, Iteration 006 added History / Manage Entries, stable-ID editing, confirmed deletion, and idempotent daily resubmission. It also distinguished **Daily Severity Score** from **14-Day Symptom Frequency Score** and retained explicit support for multiple legitimate treatment events on one date.

### Shift toward conversation-focused reporting

Iteration 005 introduced adjacent 14-day comparisons with neutral language and coverage disclosure. Iteration 007 carried that direction further: detailed records remained available in exports, while the primary clinician report became a compact aid for discussion rather than a long collection of repeated raw tables.

## Iteration 007: Present-Focused Check-In and Meaningful Review

### Context

The application had accumulated useful dashboard, reporting, treatment, and history features, but those capabilities competed with the most immediate task: recording the current day. Showing historical scores while a user was answering today's questions could influence the entry and increase cognitive burden. At the same time, trend and treatment context remained valuable when the user intentionally wanted to review it or prepare for a clinical conversation.

### Decisions

- Make **Today's Check-In** the primary opening experience.
- Keep prior scores, charts, comparisons, and interpretations out of the present-focused check-in.
- Save PHQ-9 and GAD-7 first, then gently offer optional treatment, appointment, or note details.
- Provide **Previous Day** and **Next Day** navigation for short-distance catch-up, with automatic calendar rollover, existing-entry loading, unsaved-change protection, and future-date prevention.
- Place historical interpretation in a separate **Review** experience.
- Divide Review into understandable time horizons: recent trends, simplified current and previous treatment cycles, and long-term trends.
- Use deterministic, neutral language that describes recorded patterns and coverage without diagnosing or claiming that treatment caused a change.
- Replace the long, detail-heavy clinician PDF with a compact, nonjudgmental conversation aid. Keep detailed raw records available through exports.

### Why these choices were made

The Today experience is intentionally present-focused because each symptom response should be considered on its own rather than copied, autofilled, or anchored by prior results. Saving the core assessments before optional detail protects the shortest useful path while still helping users remember relevant context.

Date navigation supports recovery from a recently missed entry without turning the tracker into a second calendar. Its safeguards prevent accidental loss of unsaved work and prevent future-dated check-ins.

Review is separate because reflection is a different activity from recording. Recent trends answer what has been happening lately; the current and previous treatment-cycle views provide limited timeline context around recorded events; long-term charts retain the broader view. Treatment-cycle language remains observational because the recorded sequence alone cannot establish causation.

The clinician report was shortened so it could support a focused conversation. It emphasizes overall patterns, symptom highlights, timeline context, treatment-cycle observations, coverage, and neutral prompts. The app supplies memory and structure; the user supplies lived meaning; the clinician supplies professional interpretation.

### Consequences and lessons

- The interface now distinguishes recording, reviewing, and managing information more clearly.
- The same underlying records continue to support both concise reports and detailed exports.
- Neutral wording and coverage disclosure are product requirements, not cosmetic editing choices.
- Missed days require both honest data handling and a guilt-free recovery path.
- A local-first application can still support rich clinical conversations without automatic sharing or automated clinical judgment.

## August 1, 2026: Reporting and Export Design Workshop

### Context

Review of the clinician report exposed a mismatch between narrative information and a compact table layout: longer journal entries could be shortened even though the user's words may carry context that symptom scores cannot. The discussion also clarified that a clinician report and an analysis workbook serve different purposes.

### Planned refinements

- Optimize the clinician report for reading and the analysis-ready workbook for independent analysis.
- Treat user-authored journal text as primary-source information. Clinician reports should preserve it in full rather than abbreviating or summarizing it.
- Present application observations alongside the user's recorded context without implying that an event caused a symptom or score change.
- Plan a separate, normalized Excel workbook while keeping the clinician report human-readable.

### Open design questions

Report section names, sequence, and narrative flow remain intentionally open. They will be workshopped and tested before implementation rather than being fixed by this planning entry.

## Ongoing Journal Practice

Future iteration entries should capture the context that prompted the work, the decisions made, meaningful alternatives that were rejected or deferred, validation performed, consequences, and lessons learned. Significant product or architectural decisions should also be recorded or amended in `docs/decisions/`.
