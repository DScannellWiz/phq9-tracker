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

## August 7, 2026: Iteration 007.1 Navigation and Review Polish

### Context

Daily use exposed a small group of observable interface issues after Iteration 007: Review titles could collide with legends or draw beyond a canvas after resizing, Today's Check-In opened first but was not the first visible primary tab, and History required manual date entry even though Today already had guarded day navigation. An entirely empty History date also looked too much like an editable new record.

### Decisions

- Keep the scope to navigation, empty-state, and Review-layout polish; do not begin reporting or export work.
- Make the visible primary-tab order match the intended workflow: record today, review intentionally, then manage historical records.
- Reuse the existing calendar-day shift logic in History while keeping a separate History edit snapshot and confirmation message.
- Treat History as a manager of existing records. When a date is entirely empty, explain that calmly and disable record-changing controls rather than implying a load error or offering an accidental creation path.
- Redraw Review charts from their live canvas dimensions and derive legend/plot positions from the rendered title bounds, so resizing preserves the full title and separates it from chart content.

### Validation and status

All 37 automated tests pass in the dependency-complete project virtual environment. The nine focused Iteration 007.1 tests cover tab order, History navigation and rollover, existing and empty dates, future-date blocking, unsaved-change cancellation, and the responsive chart-layout rules. Python compilation also passes.

The project owner subsequently completed the manual source-GUI walkthrough against the canonical repository with real-world data. Tab order and startup selection, Review chart titles and resize behavior, History navigation and rollover, existing and empty dates, future-date blocking, and unsaved-change protection passed. Iteration 007.1 is complete. No scoring, schema, export, report, or privacy-boundary changes were made, and Iteration 007.2 was not started.

## August 8, 2026: Iteration 007.1 Review with Synthetic Data

### Context

Reviewing Iteration 007.1 with synthetic data showed that the application now feels more coherent and intentionally layered: record today, review recent patterns, and prepare for a clinician discussion. The revised hierarchy and Review experience made the product's purpose easier to understand without changing its local-first or non-diagnostic role.

### Design observations

- The XLSX export should support independent analysis through separate logical worksheets rather than combining unlike records into a presentation-oriented sheet. The normalized workbook planned for Iteration 007.2 should preserve one logical record per row and stable relationships between datasets.
- The current short scoring explanation is accurate, but it is not sufficient as the only explanation. A fuller **How to Read This Report** section should explain **Daily Severity Score**, **14-Day Symptom Frequency Score**, and the effect of entry coverage and missing check-ins; a concise version may remain as a reminder.
- Exact graph values should be directly discoverable through a tooltip or click callout that shows the date and score. Requiring a user to visually trace a point across a wide chart can make important numerical information difficult to read.
- Possible automatic date loading, cleaner status and confirmation wording, more consistent button spacing, useful keyboard shortcuts, and typography and readability refinements belong together as micro-UX work.

### Deliberate deferral

These refinements were deliberately assigned to Iteration 007.2 and Iteration 008 rather than being rushed into the focused Iteration 007.1 polish scope. This keeps the current iteration observable and contained while preserving the newly agreed reporting, analysis, and accessibility needs for deliberate design and validation.

## Ongoing Journal Practice

Future iteration entries should capture the context that prompted the work, the decisions made, meaningful alternatives that were rejected or deferred, validation performed, consequences, and lessons learned. Significant product or architectural decisions should also be recorded or amended in `docs/decisions/`.
