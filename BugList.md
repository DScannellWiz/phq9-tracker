BUG: Report generation dependency detection



When generating reports or spreadsheets, the application may incorrectly report missing Python dependencies (openpyxl, reportlab, Pillow, pandas) despite a valid Python environment being available.



Investigate:

\- PHQ9\_TRACKER\_BUNDLED\_PYTHON handling

\- Portable mode behavior

\- Installed mode behavior

\- Launcher environment detection

\- Packaging script dependency validation

\- Why is my 14 day average not calculating correctly?  It is supposed to take each day that has a non-zero score and give it a single point and then assign a value of 0, 1, 2, or 3 depending on how many points are tallied for each item.  There shouldn't be an average.



Expected:

Application automatically locates bundled Python or installed Python environment and generates reports without requiring user configuration.

