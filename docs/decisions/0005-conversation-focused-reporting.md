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
