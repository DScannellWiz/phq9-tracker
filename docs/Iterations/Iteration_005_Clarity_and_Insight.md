# Iteration 005: Clarity and Insight

## Objectives

- Add an executive summary to the beginning of the clinician PDF report.
- Compare the latest 14 calendar days with the immediately preceding 14 days.
- Show the same recent trend direction on the dashboard without redesigning the full interface.
- Preserve local-first privacy, existing scoring behavior, and backward compatibility.

## Design Decisions

The comparison uses two fixed, adjacent calendar windows anchored to the selected report end date. It does not use the latest 14 saved rows because that would shift the represented dates when check-ins are missing.

Each window uses the existing symptom-frequency method: an item is counted as present on a recorded day when its response is greater than zero, and the number of present days is converted to a 0-3 item score. Missing days continue to count as no recorded symptom-present response. The report therefore displays entry coverage for both periods.

Trend language is deterministic and non-diagnostic:

- A lower score is described as lower.
- A higher score is described as higher.
- Equal scores are described as unchanged.
- A comparison with no recorded entries in either period is described as insufficient.

The dashboard enhancement reuses this same calculation to prevent the report and interface from disagreeing.

## Files Modified

- `src/phq9_tracker/app.py`
- `tests/test_period_comparison.py`
- `README.md`
- `ROADMAP.md`
- `BugList.md`
- `docs/Iterations/Iteration_005_Clarity_and_Insight.md`

## Validation Performed

- Compiled application and test source files.
- Ran the complete unit-test suite using fake and temporary data only.
- Generated a clinician PDF from 28 days of synthetic PHQ-9 and GAD-7 entries.
- Rendered the first two PDF pages to images and visually checked the executive summary, comparison table, table of contents, page transition, and footer.
- Confirmed that the canonical GitHub repository and real runtime database were not modified.

## Remaining Work

- Complete the broader card-based dashboard redesign.
- Add trend charts directly to the dashboard.
- Consider an item-level "most changed symptoms" section in a later reporting iteration.
- Resolve the existing installed/portable dependency-detection bug.

## Lessons Learned

Calendar-window boundaries must be explicit in health-tracking summaries. Comparing saved-row counts can appear equivalent when entries are complete but becomes misleading when users miss check-in days.
