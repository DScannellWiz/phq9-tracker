param(
    [string]$BaseZip = "",
    [string]$Version = "0.3.0-alpha.1",
    [string]$ArtifactRevision = "redistribution.1",
    [string]$Python = ""
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$ReleaseRoot = Join-Path $Root "release"
$WorkRoot = Join-Path $Root "work"
$ExpectedBaseHash = "76DE3678AF9BF5C61CC0C0A318347E0F5E1C7F471A6112FE9431DA9A304F4C47"
$ExpectedBaseEntries = 1836

if ([string]::IsNullOrWhiteSpace($BaseZip)) {
    $BaseZip = Join-Path $ReleaseRoot "PHQ9Tracker-Portable-0.3.0-alpha.1.zip"
}
if ([string]::IsNullOrWhiteSpace($Python)) {
    $RepositoryPython = Join-Path $Root ".venv\Scripts\python.exe"
    $Python = if (Test-Path -LiteralPath $RepositoryPython) { $RepositoryPython } else { "python" }
}

function Assert-ChildPath([string]$Path, [string]$Parent, [string]$Purpose) {
    $ResolvedPath = [IO.Path]::GetFullPath($Path)
    $ResolvedParent = [IO.Path]::GetFullPath($Parent).TrimEnd('\') + '\'
    if (-not $ResolvedPath.StartsWith($ResolvedParent, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing $Purpose outside $ResolvedParent`: $ResolvedPath"
    }
}

if (-not (Test-Path -LiteralPath $BaseZip -PathType Leaf)) {
    throw "Base ZIP not found: $BaseZip"
}
$BaseHash = (Get-FileHash -LiteralPath $BaseZip -Algorithm SHA256).Hash
if ($BaseHash -ne $ExpectedBaseHash) {
    throw "Base ZIP hash mismatch. Expected $ExpectedBaseHash, found $BaseHash"
}

Add-Type -AssemblyName System.IO.Compression.FileSystem
$Archive = [IO.Compression.ZipFile]::OpenRead($BaseZip)
try {
    if ($Archive.Entries.Count -ne $ExpectedBaseEntries) {
        throw "Base ZIP entry-count mismatch. Expected $ExpectedBaseEntries, found $($Archive.Entries.Count)"
    }
    $PrivateEntries = @(
        $Archive.Entries | Where-Object {
            $_.FullName -match '(?i)(^|/)(data|reports|exports|screenshots?)(/|$)' -or
            $_.FullName -match '(?i)\.(sqlite3?|db|csv|xlsx?|pdf|log)$'
        }
    )
    if ($PrivateEntries.Count -gt 0) {
        throw "Base ZIP contains forbidden private/generated paths: $($PrivateEntries.FullName -join ', ')"
    }
} finally {
    $Archive.Dispose()
}

& $Python (Join-Path $PSScriptRoot "verify_release_licenses.py") --notice-only
if ($LASTEXITCODE -ne 0) {
    throw "Committed release notice verification failed."
}

$ArtifactLabel = if ([string]::IsNullOrWhiteSpace($ArtifactRevision)) {
    $Version
} else {
    "$Version-$ArtifactRevision"
}
$PortableDir = Join-Path $ReleaseRoot "PHQ9Tracker-Portable-$ArtifactLabel"
$ZipPath = Join-Path $ReleaseRoot "PHQ9Tracker-Portable-$ArtifactLabel.zip"
if ((Test-Path -LiteralPath $PortableDir) -or (Test-Path -LiteralPath $ZipPath)) {
    throw "Refusing to overwrite existing redistribution output: $ArtifactLabel"
}

$StageRoot = Join-Path $WorkRoot ("repackage-" + [guid]::NewGuid().ToString("N"))
Assert-ChildPath $StageRoot $WorkRoot "temporary extraction"
New-Item -ItemType Directory -Path $StageRoot | Out-Null
try {
    Expand-Archive -LiteralPath $BaseZip -DestinationPath $StageRoot
    Copy-Item -LiteralPath (Join-Path $Root "LICENSE") -Destination (Join-Path $StageRoot "LICENSE")
    Copy-Item -Recurse -LiteralPath (Join-Path $Root "THIRD_PARTY_NOTICES") -Destination (Join-Path $StageRoot "THIRD_PARTY_NOTICES")

    $FixedTimestamp = [DateTime]::SpecifyKind([DateTime]::Parse("2026-09-07T00:00:00"), [DateTimeKind]::Utc)
    Get-ChildItem -LiteralPath (Join-Path $StageRoot "THIRD_PARTY_NOTICES") -Recurse | ForEach-Object {
        $_.LastWriteTimeUtc = $FixedTimestamp
    }
    (Get-Item -LiteralPath (Join-Path $StageRoot "LICENSE")).LastWriteTimeUtc = $FixedTimestamp

    Copy-Item -Recurse -LiteralPath $StageRoot -Destination $PortableDir
    Compress-Archive -Path "$StageRoot\*" -DestinationPath $ZipPath -CompressionLevel Optimal
} finally {
    if (Test-Path -LiteralPath $StageRoot) {
        Assert-ChildPath $StageRoot $WorkRoot "temporary cleanup"
        Remove-Item -LiteralPath $StageRoot -Recurse -Force
    }
}

$FinalHash = (Get-FileHash -LiteralPath $ZipPath -Algorithm SHA256).Hash
$FinalArchive = [IO.Compression.ZipFile]::OpenRead($ZipPath)
try {
    $FinalEntries = $FinalArchive.Entries.Count
} finally {
    $FinalArchive.Dispose()
}

Write-Host "Verified base ZIP: $BaseZip"
Write-Host "Base SHA-256: $BaseHash"
Write-Host "Built redistribution folder: $PortableDir"
Write-Host "Built redistribution ZIP: $ZipPath"
Write-Host "Redistribution ZIP entries: $FinalEntries"
Write-Host "Redistribution ZIP SHA-256: $FinalHash"
