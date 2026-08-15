Current as of: 2026-08-15
Last substantive update: 2026-08-01

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

## Second-Slice Scope: Present-Focused Check-In and Meaningful Review

1. Add one-day Previous Day and Next Day navigation with automatic month/year rollover.
2. Load existing records for the selected date, prevent future check-ins, and confirm before discarding unsaved changes.
3. Replace the dashboard with a separate Review experience containing recent trends, treatment-cycle views, and long-term trends.
4. Generate concise local summaries from deterministic comparison logic rather than an AI service.
5. Limit treatment-cycle visualization to the current and previous windows bounded by recorded ketamine infusion dates. Describe timing without claiming treatment caused a change.
6. Replace the long clinician PDF with a two-to-four-page conversation-focused summary. Keep detailed data available through CSV/XLSX exports rather than repeating raw tables in the primary PDF.
7. Remove the duplicated PHQ-9 response table and the causal-sounding ketamine improvement/baseline section.
8. Improve report dependency discovery and release-build preflight checks.

## Design Details

- Today never displays prior scores or trends. Date navigation is a catch-up tool, not a second calendar.
- Unsaved-change detection compares the visible assessment and optional-detail fields with the most recently loaded or saved state.
- Natural-language highlights compare recorded symptom presence in adjacent 14-day periods. They use neutral terms such as higher, lower, more often, and less often.
- Coverage always identifies how many check-ins were recorded. Missing days are missing information, not evidence that a symptom was absent.
- Review has three internal views: Recent Trends, Treatment Cycles, and Long-Term Trends.
- The clinician report contains Period at a Glance, Recorded Trends, Treatment-Cycle Observations, and Timeline Highlights/Discussion Prompts.
- The report retains a concise factual PHQ-9 self-harm-item observation without presenting it as a current-safety assessment.
- No database schema, scoring formula, record identifier, editing operation, or cloud/privacy boundary changes in this slice.

## Validation Performed

- 28 automated tests passed using isolated synthetic databases, including all earlier scoring, migration, editing, duplicate-prevention, and export tests.
- New tests cover month/year rollover, future-date blocking, neutral summary wording, treatment-cycle boundaries, dependency probing, PDF section structure, removal of duplicate raw tables, and the two-to-four-page target.
- The synthetic clinician PDF rendered as four letter-size pages and was visually inspected for hierarchy, clipping, page transitions, charts, tables, and footers.
- Python compilation passed for application and test sources.

## Files Modified

- `src/phq9_tracker/app.py`
- `tests/test_iteration_007_ux.py`
- `Launch Mental Health Tracker.bat`
- `packaging/build_release.ps1`
- `README.md`
- `ROADMAP.md`
- `BugList.md`
- `BUILD_AND_RELEASE.md`
- `docs/Iterations/Iteration_007_Today_Flow_Design.md`

## Remaining Work and Limitations

- Complete an interactive source-GUI walkthrough with an isolated database.
- Validate installed and portable builds on a Windows release workstation with PyInstaller and Inno Setup.
- Treatment cycles currently use ketamine infusion anchors because that is the established cycle-based treatment in the application. Generalized cycle configuration remains future work.
- Natural-language summaries are intentionally deterministic and limited; they do not diagnose, recommend treatment, or infer causation.
