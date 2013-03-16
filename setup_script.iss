; 脚本由 Inno Setup 脚本向导 生成！
; 有关创建 Inno Setup 脚本文件的详细资料请查阅帮助文档！

[Setup]
; 注意: AppId 值用于唯一识别该应用程序。
; 禁止对其他应用程序的安装器使用相同的 AppId 值！
; (若要生成一个新的 GUID，请选择“工具 | 生成 GUID”。)
AppId={{88B330D8-B45E-4CFE-A0FC-DA690A4570B5}
AppName=PtProject
AppVerName=PtProject 开发工具  V1.5
AppPublisher=PtPHP
AppPublisherURL=http://www.ptphp.com/
AppSupportURL=http://www.ptphp.com/
AppUpdatesURL=http://www.ptphp.com/
DefaultDirName={pf}\PtProject
DefaultGroupName=PtProject
AllowNoIcons=yes
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "chinese"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\Dhole\PtProject\PtGUI\PtProject.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\_sqlite3.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\Microsoft.VC90.CRT.manifest"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\MSVCM90.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\MSVCP90.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\MSVCR90.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\PtProject.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\PySide.QtCore.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\PySide.QtGui.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\PySide.QtNetwork.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\PySide.QtWebKit.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\pyside-python2.6.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\python26.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\QtCore4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\QtGui4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\QtNetwork4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\QtWebKit4.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\shiboken-python2.6.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\sqlite3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\w9xpopen.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Dhole\PtProject\PtGUI\imageformats\*"; DestDir: "{app}\imageformats"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\Dhole\PtProject\PtGUI\res\*"; DestDir: "{app}\res"; Flags: ignoreversion recursesubdirs createallsubdirs
; 注意: 不要在任何共享系统文件上使用“Flags: ignoreversion”

[Icons]
Name: "{group}\PtProject"; Filename: "{app}\PtProject.exe"
Name: "{group}\{cm:ProgramOnTheWeb,PtProject}"; Filename: "http://www.ptphp.com/"
Name: "{group}\{cm:UninstallProgram,PtProject}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\PtProject"; Filename: "{app}\PtProject.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\PtProject"; Filename: "{app}\PtProject.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\PtProject.exe"; Description: "{cm:LaunchProgram,PtProject}"; Flags: nowait postinstall skipifsilent

