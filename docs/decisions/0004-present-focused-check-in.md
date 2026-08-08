# ADR 0004: Present-Focused Check-In

## Status

Accepted

## Context

Daily recording is the application's primary task. Showing earlier scores, charts, or comparisons during today's assessment can influence how a user judges the current day. Requiring optional context before saving also makes the core task longer and easier to abandon.

## Decision

Open the application to **Today's Check-In** and keep that experience free of historical scores and trend interpretation. Save the core PHQ-9 and GAD-7 assessments before gently offering optional treatment, appointment, or note details. Do not copy or autofill prior symptom responses. Support short-distance catch-up with guarded date navigation while leaving future scheduling to a personal calendar.

## Rationale

A calm, present-focused flow reduces cognitive burden and anchoring from prior results. Completing the core assessment first protects the shortest useful workflow, while the optional follow-up helps capture context without making it a prerequisite.

## Consequences

- Historical information belongs in Review rather than Today's Check-In.
- Missed days can be recovered without turning the application into a second calendar.
- Date changes must preserve unsaved-change protection, load existing records, and prevent future-dated check-ins.
- History / Manage Entries reuses the same calendar-day navigation rules while maintaining its own unsaved-edit boundary; empty dates remain a manage-only state rather than silently creating new daily records.
- Optional details remain separate records even when presented as one daily experience.

## Future Considerations

- Chart point values in Review should be directly discoverable through click or hover callouts that show the date and exact score.
- Direct value access is an accessibility and readability requirement for users who may have difficulty visually tracing a point across a wide chart, not merely a cosmetic enhancement.
