\# Current Development Priorities



\## Primary Goal



Build professional-quality, privacy-first software while learning software engineering through AI-assisted development.



\---



\## Current Priorities



1\. Complete the multi-assessment framework.

2\. Integrate GAD-7.

3\. Improve reporting.

4\. Implement security features.

5\. Improve packaging and releases.

6\. Preserve stable record IDs when editing historical data and make destructive actions explicit and confirmed.



\---



\## Security Philosophy



User mental health data should remain under the user's control.



Design toward:



\* Local-first storage.

\* Optional encryption.

\* Optional application password.

\* Password-protected reports.

\* Secure backups.

\* No cloud dependency unless explicitly requested by the user.



Security should be optional but easy to enable.



\---



\## Development Principles



\* One primary feature per iteration.

\* Update documentation alongside code.

\* Add tests for business logic.

\* Preserve backward compatibility whenever practical.

\* Explain architectural decisions.

\* Never commit private user data.

\* Treat daily notes as one synchronized day-level value even while legacy assessment tables remain compatible.

\* Make repeated daily submission idempotent; use an explicit action for another legitimate treatment event.

\* Use the user-facing labels Daily Severity Score and 14-Day Symptom Frequency Score without renaming stable internal database fields unnecessarily.

\* Do not copy or autofill prior symptom responses; mindful reflection is an intentional data-quality feature.



\---



\## Long-Term Vision



Create an open-source mental health assessment platform that is:



\* Local-first

\* Privacy-first

\* Extensible

\* Well documented

\* Easy to contribute to

\* Helpful to both patients and clinicians

\* Built with professional software engineering practices



\---



\## Development Narrative and Decision Records



For every substantial future iteration:



\* Update `DEVELOPMENT_JOURNAL.md` with the context, decisions, meaningful rejected or deferred alternatives, validation, consequences, and lessons learned.

\* Add a new record under `docs/decisions/` when a significant product or architectural decision is accepted.

\* Amend an existing architecture decision record when the decision is refined without being replaced.

\* Mark a superseded decision explicitly and link the replacement record rather than silently rewriting project history.

\* Keep implementation details consistent with `docs/product-principles.md`, or document why a deliberate change to those principles is warranted.



