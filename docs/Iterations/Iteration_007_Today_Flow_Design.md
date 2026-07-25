# Iteration 007: Today Flow Design

## Objectives

- Make the first and primary application experience a calm, present-focused way to record today.
- Keep the core PHQ-9 and GAD-7 check-in quick while retaining intentional item-by-item reflection.
- Help users remember optional treatment events, appointments, and notes without making those details mandatory.
- Preserve local-only privacy, existing records, scoring, exports, reports, and multi-event behavior.

## Design Decisions

- The application opens to Today's Check-In rather than the dashboard.
- The Today flow does not display previous scores, charts, trends, or comparisons. Those belong in a later, separate Review experience.
- The core assessment is completed and saved before one gentle follow-up asks whether anything else should be recorded about today.
- The follow-up offers treatment or appointment, personal note, and not-right-now choices. It uses the existing quick treatment-event types, an Other option, and optional descriptive text.
- Missed days are handled without pressure. The primary invitation remains today's entry; date-based history and existing-date tools continue to support optional correction or backfill.
- Treatment events continue to be stored as independent records even when they appear as part of one daily experience. No database migration is required.
- The tracker records completed care and lived experience. A personal calendar remains responsible for future appointments and reminders.
- Clinician sharing remains local and manual. This iteration does not add automatic sharing, cloud synchronization, a clinician portal, medical recommendations, or causal treatment claims.

## First-Slice Scope

1. Select Today's Check-In when the application opens.
2. Present the date and core assessments without dashboard information.
3. Save the core assessment with the existing duplicate-safe, stable-record behavior.
4. Present an optional post-save add-details step for treatment events, appointments, and notes.
5. Confirm completion without showing comparative scores or interpretive feedback.

## Deferred Work

- Personal Review with a simple 14-day score and comparison to the preceding 14 days.
- Clinician-report organization and visual refinement.
- Dashboard cards, charts, and other Review-area visualizations.
- Carefully labeled treatment-pattern observations, only after sufficient reliable data and with no treatment advice or causal claims.
- Analysis-ready workbook export work already listed in the roadmap.

## Validation Plan

- Verify opening behavior, core-save behavior, optional-detail behavior, existing-date loading, and multiple same-day treatment events with automated tests where practical.
- Perform manual source-GUI validation using synthetic or non-sensitive data only.
- Confirm no prior scores, charts, or comparisons appear in the Today flow.
- Confirm local data paths, report behavior, export behavior, and the existing database schema remain unchanged.

## Documentation Changes in This Planning Step

- Updated `ROADMAP.md` to sequence Iteration 007 around the Today-flow checkpoint and record its scope boundary.
- Added this design record before application implementation.

## Remaining Work

- Review this design record with the repository owner before modifying application behavior.
- Implement the Today-flow layout and sequencing in a separate development step.
