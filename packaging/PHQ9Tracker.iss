#define MyAppName "PHQ-9 Tracker"
#define MyAppVersion "0.2.0"
#define MyAppPublisher "Local"
#define MyAppExeName "PHQ9Tracker.exe"

[Setup]
AppId={{6E5B9209-9A57-4917-9DC0-2F78F26C3B0A}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\PHQ-9 Tracker
DefaultGroupName=PHQ-9 Tracker
DisableProgramGroupPage=no
OutputDir=..\release
OutputBaseFilename=PHQ9Tracker-Setup-{#MyAppVersion}
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
UninstallDisplayIcon={app}\{#MyAppExeName}
PrivilegesRequired=lowest

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional shortcuts:"; Flags: unchecked

[Files]
Source: "..\dist\PHQ9Tracker\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\PHQ-9 Tracker"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\Uninstall PHQ-9 Tracker"; Filename: "{uninstallexe}"
Name: "{autodesktop}\PHQ-9 Tracker"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch PHQ-9 Tracker"; Flags: nowait postinstall skipifsilent
