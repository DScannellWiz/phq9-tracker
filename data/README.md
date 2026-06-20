# Private Data Directory

Store real local PHQ-9 databases here.

Do not commit real health records, PHI, PII, spreadsheets, notes, logs, exports, or generated reports to GitHub.

The default local database path for source runs is:

```text
data/phq9_tracker.sqlite
```

The `.gitignore` keeps database contents out of version control while preserving this folder with `.gitkeep`.
