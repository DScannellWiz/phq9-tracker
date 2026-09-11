@echo off
setlocal
cd /d "%~dp0"
set PYTHONPATH=%~dp0src
set "TRACKER_PYTHON=python"
if exist "%~dp0.venv\Scripts\python.exe" set "TRACKER_PYTHON=%~dp0.venv\Scripts\python.exe"
if exist "%~dp0venv\Scripts\python.exe" set "TRACKER_PYTHON=%~dp0venv\Scripts\python.exe"
"%TRACKER_PYTHON%" -m phq9_tracker --launch
