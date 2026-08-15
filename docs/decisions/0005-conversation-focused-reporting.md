Current as of: 2026-08-15
Last substantive update: 2026-08-15

# ADR 0005: Conversation-Focused Reporting

## Status

Accepted

## Context

Earlier clinician reports accumulated repeated raw tables and detail that made the main discussion aid long and difficult to scan. Users and clinicians still need access to underlying records, but the primary report serves a different purpose from a complete data export.

## Decision

Make the primary clinician report a compact, local conversation aid focused on scoring context, overall patterns, symptom highlights, treatment context, complete user-authored journal entries, entry coverage, and neutral discussion prompts. Keep detailed raw records available through CSV/XLSX exports instead of repeating them throughout the PDF.

## Rationale

A concise report is easier to use during a limited clinical conversation. Separating summary presentation from raw-data access preserves both usability and transparency.

## Consequences

- Report summaries must be traceable to deterministic calculations and recorded data.
- Detailed exports remain part of the product, not an optional substitute for preserved raw information.
- Report length and rendered layout require validation with synthetic data.
- The report supports discussion but does not diagnose, recommend treatment, or replace professional judgment.
- Compactness must not truncate or summarize user-authored journal text. Reports may grow when narrative length requires it.
- The separate analysis workbook uses normalized records and documented relationships; its derived Daily Summary is a convenience view, not the source of truth.

## Iteration 007.2 Implementation

- The analysis-ready workbook uses **Daily Assessments**, **Item Responses**, **Notes**, **Treatment Events**, **Treatment Cycles**, **Metadata**, and a derived **Daily Summary**.
- The clinician report begins with **How to Read This Report**, then uses **Recorded Period Overview**, **Recorded Symptom Trends**, **Treatment Context**, **Journal and Event Context**, and **Conversation Starters**.
- The early explanation distinguishes **Daily Severity Score** from **14-Day Symptom Frequency Score** and explicitly addresses coverage and missing check-ins.
