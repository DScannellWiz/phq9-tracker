# ADR 0001: Local-First Storage

## Status

Accepted

## Context

The application stores standardized mental health assessment responses, notes, treatment events, reports, and exports. These records may contain sensitive personal information. The project began as a personal spreadsheet and then a desktop application, so a network service is not required for its core purpose.

## Decision

Store application records locally by default. Keep databases in the local data boundary and generate reports and exports as local files. Do not introduce cloud storage, automatic synchronization, or automatic clinician sharing unless a future decision explicitly adds an opt-in capability with an appropriate privacy design.

## Rationale

Local-first storage minimizes unnecessary disclosure, keeps the user in control of sharing, supports offline use, and fits the project's privacy-first purpose.

## Consequences

- Users control the device, backups, and copies on which their records reside.
- Reports and exports must be treated as sensitive local files.
- Git must exclude real databases, reports, exports, screenshots, logs, PHI, and PII.
- Backup, encryption, and cross-device use require deliberate future design rather than being inherited from a cloud platform.
