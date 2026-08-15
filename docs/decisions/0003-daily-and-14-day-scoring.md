Current as of: 2026-08-15
Last substantive update: 2026-08-01

# ADR 0003: Daily and 14-Day Scoring

## Status

Accepted

## Context

The application needs to distinguish the score recorded for one check-in from a score summarizing symptom frequency across a 14-calendar-day period. An earlier averaging approach did not match the symptom-frequency method established in the spreadsheet prototype. Missing check-ins also make a calendar-window summary easy to misread.

## Decision

Use the user-facing term **Daily Severity Score** for the total from one assessment entry. Use **14-Day Symptom Frequency Score** for the calendar-window calculation that counts recorded symptom presence by item and converts those counts to the established 0-3 item scale before summing them. Anchor comparisons to explicit calendar windows, apply an assessment's scoring rules only where appropriate, and always disclose entry coverage.

For the current calculation, an unrecorded calendar day contributes no recorded symptom-presence count. In interpretation and language, however, a missed day remains missing information and must not be described as proof that a symptom was absent.

## Rationale

Distinct names prevent a daily severity result from being confused with a longitudinal frequency summary. Fixed calendar windows make adjacent periods comparable, while coverage disclosure exposes the limits created by missing entries.

## Consequences

- UI, reports, exports, and documentation must use the two terms consistently.
- Scoring logic and period boundaries require automated tests.
- Sparse coverage can lower the calculated frequency count, so summaries must show coverage and avoid overclaiming.
- Internal database field names may remain stable when renaming them would create unnecessary compatibility risk.
