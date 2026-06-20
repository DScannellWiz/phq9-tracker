# \# PHQ-9 Tracker

# 

# A local desktop application for recording PHQ-9 assessments, tracking symptom trends over time, generating clinician discussion reports, and exporting assessment data.

# 

# \## Purpose

# 

# This project was created to provide a private, local-first method of tracking PHQ-9 depression screening results and related treatment events. The application is designed to support discussions with healthcare providers by presenting symptom trends, recent changes, and treatment context in a structured format.

# 

# \## Features

# 

# \* Import PHQ-9 entries from Excel

# \* Store entries in a local SQLite database

# \* Manual daily entry workflow

# \* Display the most recent 14 entries

# \* Calculate PHQ-9 totals and severity categories

# \* Track symptom trends over time

# \* Generate clinician discussion reports

# \* Export data to CSV and Excel

# \* Monitor Question 9 responses

# \* Track treatment events including:

# 

# &#x20; \* Ketamine

# &#x20; \* Therapy

# &#x20; \* Medication Start

# &#x20; \* Medication Stop

# &#x20; \* Medication Dose Increase

# &#x20; \* Medication Dose Decrease

# &#x20; \* Custom treatment events

# \* Support optional note tags:

# 

# &#x20; \* Finances

# &#x20; \* Work

# &#x20; \* Family

# &#x20; \* Health

# &#x20; \* Sleep

# &#x20; \* Relationships

# &#x20; \* Other

# 

# \## Reports

# 

# The clinician discussion report includes:

# 

# \* Clickable table of contents

# \* Question 9 monitoring section

# \* Current clinical status summary

# \* Recent 14-day and 30-day summaries

# \* Most recent symptom responses

# \* Item-level analysis

# \* Ketamine response review

# \* Page numbering

# \* Clinical disclaimers

# 

# Spreadsheet exports are designed as data-only exports and include:

# 

# \* Scores

# \* Severity levels

# \* Notes

# \* Tags

# \* Treatment indicators

# 

# \## Installation

# 

# For packaged releases:

# 

# 1\. Run `Launch PHQ-9 Tracker.bat`

# 2\. Follow the build and deployment instructions in `BUILD\_AND\_RELEASE.md`

# 

# \## Project Structure

# 

# ```text

# src/          Application source code

# packaging/    Installer and packaging files

# docs/         Documentation (future)

# ```

# 

# \## Privacy

# 

# \* This application does not upload data.

# \* Data is stored locally on the user's computer.

# \* Exported reports and spreadsheets are generated only when requested.

# \* If the application folder is stored inside a cloud-synced location, those files may be synchronized by that service.

# 

# \## Disclaimer

# 

# This application is intended to support discussions with licensed healthcare professionals.

# 

# It is not a diagnostic tool and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

# 

