param(
    [string]$Version = "0.3.0-alpha.1"
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Dist = Join-Path $Root "dist"
$Build = Join-Path $Root "build"
$PortableOut = Join-Path $Root "release"
$PythonBase = python -c "import sys; print(sys.base_prefix)"
$TkinterLib = Join-Path $PythonBase "Lib\tkinter"
$TclLib = Join-Path $PythonBase "tcl\tcl8.6"
$TkLib = Join-Path $PythonBase "tcl\tk8.6"
$TclPackages = Join-Path $PythonBase "tcl\tcl8"
$TkinterExtension = Join-Path $PythonBase "DLLs\_tkinter.pyd"
$TclDll = Join-Path $PythonBase "DLLs\tcl86t.dll"
$TkDll = Join-Path $PythonBase "DLLs\tk86t.dll"
$TkRuntimeHook = Join-Path $Root "packaging\pyi_rth_tkinter_portable.py"

python -c "import openpyxl, pandas, PIL, reportlab, pypdf"
if ($LASTEXITCODE -ne 0) {
    throw "Release dependencies are incomplete. Install requirements.txt and PyInstaller in the build environment."
}

$RequiredTkPaths = @(
    $TkinterLib,
    $TclLib,
    $TkLib,
    $TclPackages,
    $TkinterExtension,
    $TclDll,
    $TkDll,
    $TkRuntimeHook
)
foreach ($RequiredPath in $RequiredTkPaths) {
    if (-not (Test-Path -LiteralPath $RequiredPath)) {
        throw "Tk runtime dependency is missing: $RequiredPath"
    }
}

New-Item -ItemType Directory -Force -Path $Dist, $Build, $PortableOut | Out-Null

python -m PyInstaller `
  --noconfirm `
  --clean `
  --onedir `
  --name "PHQ9Tracker" `
  --distpath $Dist `
  --workpath $Build `
  --paths "$Root\src" `
  --icon "$Root\packaging\assets\PHQ9_Tracker.ico" `
  --add-data "$Root\README.md;." `
  --add-data "$TkinterLib;tkinter" `
  --add-data "$TclLib;_tcl_data" `
  --add-data "$TkLib;_tk_data" `
  --add-data "$TclPackages;tcl8" `
  --add-binary "$TkinterExtension;." `
  --add-binary "$TclDll;." `
  --add-binary "$TkDll;." `
  --runtime-hook $TkRuntimeHook `
  --exclude-module pytest `
  --exclude-module unittest `
  --exclude-module IPython `
  --exclude-module notebook `
  "$Root\src\phq9_tracker\app.py"

$PortableDir = Join-Path $PortableOut "PHQ9Tracker-Portable-$Version"
if (Test-Path $PortableDir) {
    Remove-Item -Recurse -Force $PortableDir
}
Copy-Item -Recurse (Join-Path $Dist "PHQ9Tracker") $PortableDir
Set-Content -Path (Join-Path $PortableDir "Launch Portable Mental Health Tracker.bat") -Value @"
@echo off
setlocal
set PHQ9_TRACKER_PORTABLE=1
cd /d "%~dp0"
"%~dp0PHQ9Tracker.exe"
"@

$ZipPath = Join-Path $PortableOut "PHQ9Tracker-Portable-$Version.zip"
if (Test-Path $ZipPath) {
    Remove-Item -Force $ZipPath
}
Compress-Archive -Path "$PortableDir\*" -DestinationPath $ZipPath -CompressionLevel Optimal

Write-Host "Built folder-based app: $Dist\PHQ9Tracker"
Write-Host "Built portable folder: $PortableDir"
Write-Host "Built portable zip: $ZipPath"
Write-Host "Next: compile packaging\PHQ9Tracker.iss with Inno Setup."
