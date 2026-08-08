# ADR 0005: Conversation-Focused Reporting

## Status

Accepted

## Context

Earlier clinician reports accumulated repeated raw tables and detail that made the main discussion aid long and difficult to scan. Users and clinicians still need access to underlying records, but the primary report serves a different purpose from a complete data export.

## Decision

Make the primary clinician report a compact, local conversation aid focused on overall patterns, symptom highlights, timeline context, treatment-cycle observations, entry coverage, and neutral discussion prompts. Keep detailed raw records available through CSV/XLSX exports instead of repeating them throughout the PDF.

## Rationale

A concise report is easier to use during a limited clinical conversation. Separating summary presentation from raw-data access preserves both usability and transparency.

## Consequences

- Report summaries must be traceable to deterministic calculations and recorded data.
- Detailed exports remain part of the product, not an optional substitute for preserved raw information.
- Report length and rendered layout require validation with synthetic data.
- The report supports discussion but does not diagnose, recommend treatment, or replace professional judgment.

## Future Considerations

- A planned analysis-ready workbook would use separate normalized **Daily Assessments**, **Item Responses**, **Notes**, **Treatment Events**, **Treatment Cycles**, and **Metadata** worksheets, with one logical record per row, stable identifiers, and documented relationships.
- An optional **Daily Summary** worksheet may be added as a derived convenience view, including common treatment-event yes/no columns where useful, while normalized **Treatment Events** records remain the source of truth.
- The clinician report should restore a fuller **How to Read This Report** section that explains **Daily Severity Score**, **14-Day Symptom Frequency Score**, and the role of entry coverage and missing check-ins. A concise explanation may remain as a quick reminder, but should not be the only guidance.
- Final clinician-report section names and ordering remain intentionally undecided pending a future design workshop and usability testing.
