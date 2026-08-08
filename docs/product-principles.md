# Product Principles

These principles define the stable philosophical core of the Mental Health Tracker. They guide product language, workflows, reports, and future technical decisions.

## Stable Philosophical Core

1. **Summarize without judging.** Present what was recorded without assigning moral value, success, failure, or blame.
2. **Highlight without diagnosing.** Make potentially useful information easier to notice without presenting the application as a diagnostic authority.
3. **Describe patterns without claiming causation.** Events and score changes may be shown on the same timeline, but temporal proximity alone does not prove that one caused the other.
4. **Preserve raw data.** Summaries and reports must not replace the user's underlying records or prevent independent review and export.
5. **Make missed days easy to recover from without guilt.** Support practical catch-up and correction while treating missing days as missing information, not personal failure.
6. **Minimize cognitive burden.** Keep the primary daily task calm, direct, and focused; place optional detail and historical interpretation where users can approach them intentionally.
7. **Maintain privacy and user control.** Prefer local storage and explicit user-directed sharing. Sensitive records should remain under the user's control.
8. **Scores support conversation rather than define the person.** Standardized assessment scores are structured observations, not a complete account of identity, experience, or clinical meaning.
9. **Respect the division of labor.** **The app remembers, the user adds meaning, the clinician interprets.**
10. **Keep the user's words intact.** Do not truncate or summarize a user's own journal entries in clinician reports. Summaries belong to the application's observations; the user's words should remain intact unless the user explicitly requests otherwise.
11. **Make important values directly readable.** Important numerical information should not require precise visual tracing when a direct value affordance, such as a click or hover callout, can be provided.
12. **Be concise without removing necessary understanding.** Explanations should be as concise as practical, but never so compressed that users or clinicians cannot understand how the presented data or scores were derived.

## Adaptable Implementation Layers

The philosophical core should remain stable, but the implementation is expected to evolve. Assessments, supported platforms, charts, journaling features, report formats, and daily or clinical workflows may be extended, replaced, or adapted as needs change.

An implementation change is consistent with the project when it preserves privacy, raw information, user agency, nonjudgmental language, and the boundary between recorded patterns and clinical interpretation. A fork may choose different technical layers while still honoring the same core.
