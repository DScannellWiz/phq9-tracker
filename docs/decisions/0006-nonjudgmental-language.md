Current as of: 2026-08-15
Last substantive update: 2026-08-01

# ADR 0006: Nonjudgmental Language

## Status

Accepted

## Context

Mental health records are personal, and language that labels results as success, failure, good, bad, improvement, or deterioration may imply judgment or clinical certainty. Treatment events and symptom changes can also appear near each other in time without establishing causation.

## Decision

Use neutral, descriptive language throughout the interface, Review summaries, reports, and documentation. Prefer terms such as higher, lower, more often, less often, unchanged, recorded, and insufficient data. Disclose coverage and uncertainty. Do not diagnose, assign blame, recommend treatment, claim causation, or treat a score as a definition of the person.

## Rationale

Neutral language keeps the application within its role as a memory and conversation aid. It respects user agency and leaves lived meaning to the user and clinical interpretation to qualified professionals.

## Consequences

- User-facing language needs review as part of feature validation.
- Deterministic summaries must include explicit non-causal and insufficient-data paths.
- New charts and reports must distinguish observation from interpretation.
- Clinically significant recorded items may be stated factually, but the application must not present them as a diagnosis or current-safety determination.
