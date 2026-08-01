# ADR 0002: Reusable Assessment Framework

## Status

Accepted

## Context

The project began as a PHQ-9 tracker. Adding GAD-7 showed that hard-coding every workflow around one instrument would limit extensibility, while replacing the original storage contract could put existing PHQ-9 records and behavior at risk.

## Decision

Represent supported instruments through reusable assessment definitions and a generic assessment-entry model. Preserve the legacy PHQ-9 path for backward compatibility while new and shared workflows use the reusable framework. Add future instruments only after confirming their items, scoring rules, presentation needs, and whether shared calculations are appropriate.

## Rationale

An additive framework supports multiple assessments without forcing a destructive migration or pretending that every instrument has identical scoring and interpretation.

## Consequences

- Existing PHQ-9 data and established interfaces remain supported.
- Shared UI, storage, reports, and exports can reuse common assessment metadata.
- Some compatibility code remains until a separately approved migration is justified.
- Each new assessment requires explicit validation rather than registry-only configuration by assumption.
