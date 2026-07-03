#define MyAppName "Mental Health Tracker"
#define MyAppVersion "0.2.0"
#define MyAppPublisher "Local"
#define MyAppExeName "PHQ9Tracker.exe"

[Setup]
AppId={{6E5B9209-9A57-4917-9DC0-2F78F26C3B0A}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\Mental Health Tracker
DefaultGroupName=Mental Health Tracker
DisableProgramGroupPage=no
OutputDir=..\release
OutputBaseFilename=PHQ9Tracker-Setup-{#MyAppVersion}
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
UninstallDisplayIcon={app}\{#MyAppExeName}
SetupIconFile=assets\PHQ9_Tracker.ico
PrivilegesRequired=lowest

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional shortcuts:"; Flags: unchecked

[Files]
Source: "..\dist\PHQ9Tracker\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Mental Health Tracker"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\Uninstall Mental Health Tracker"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Mental Health Tracker"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch Mental Health Tracker"; Flags: nowait postinstall skipifsilent
