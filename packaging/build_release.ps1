param(
    [string]$Version = "0.2.0"
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Dist = Join-Path $Root "dist"
$Build = Join-Path $Root "build"
$PortableOut = Join-Path $Root "release"

New-Item -ItemType Directory -Force -Path $Dist, $Build, $PortableOut | Out-Null

python -m PyInstaller `
  --noconfirm `
  --clean `
  --onedir `
  --name "PHQ9Tracker" `
  --distpath $Dist `
  --workpath $Build `
  --paths "$Root\src" `
  --add-data "$Root\README.md;." `
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
Set-Content -Path (Join-Path $PortableDir "Launch Portable PHQ-9 Tracker.bat") -Value @"
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
