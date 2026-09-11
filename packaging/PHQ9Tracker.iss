#define MyAppName "Len"
#ifndef MyAppVersion
  #error MyAppVersion must be supplied explicitly. The frozen 0.3.0-alpha.1 version must not be rebuilt from post-rename source.
#endif
#define MyAppPublisher "Local"
#define MyAppExeName "PHQ9Tracker.exe"

[Setup]
AppId={{6E5B9209-9A57-4917-9DC0-2F78F26C3B0A}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\Len
DefaultGroupName=Len
DisableProgramGroupPage=no
OutputDir=..\release
OutputBaseFilename=Len-Setup-{#MyAppVersion}
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
UninstallDisplayIcon={app}\{#MyAppExeName}
SetupIconFile=assets\PHQ9_Tracker.ico
PrivilegesRequired=lowest

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Shortcuts:"

[Files]
Source: "..\dist\PHQ9Tracker\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Len"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\{#MyAppExeName}"
Name: "{group}\Uninstall Len"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Len"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch Len"; Flags: nowait postinstall skipifsilent
