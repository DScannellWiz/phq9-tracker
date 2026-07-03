@echo off
setlocal
cd /d "%~dp0"
set PYTHONPATH=%~dp0src
python -m phq9_tracker --launch
