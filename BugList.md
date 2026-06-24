BUG: Report generation dependency detection



When generating reports or spreadsheets, the application may incorrectly report missing Python dependencies (openpyxl, reportlab, Pillow, pandas) despite a valid Python environment being available.



Investigate:

\- PHQ9\_TRACKER\_BUNDLED\_PYTHON handling

\- Portable mode behavior

\- Installed mode behavior

\- Launcher environment detection

\- Packaging script dependency validation



Expected:

Application automatically locates bundled Python or installed Python environment and generates reports without requiring user configuration.

