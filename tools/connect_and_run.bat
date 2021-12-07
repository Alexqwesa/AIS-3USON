rem @echo off
SETLOCAL ENABLEEXTENSIONS
SET me=%~n0
SET parent=%~dp0
set SDIR=%1
rem ############################
rem  copy app to %APPDATA%\AIS-3USON
rem ---------------------------
robocopy /mir %SDIR%\AIS-3USON  %APPDATA%\AIS-3USON

FOR /F "usebackq tokens=3 " %%i in (`REG QUERY "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" /v Desktop`) DO SET DESKTOPDIR=%%i
FOR /F "usebackq delims=" %%i in (`ECHO %DESKTOPDIR%`) DO SET DESKTOPDIR=%%i
ECHO %DESKTOPDIR%
xcopy %SDIR%\AIS_3USON.lnk  %DESKTOPDIR%\ /K /D /H /Y

rem ############################
rem  install vcredist_x86
rem  ---------------------------
find /c "app_3uson_installed = 1" %UserProfile%\.config\3uson\3uson.conf
if %errorlevel% EQU 1 goto notfound
    echo vcredist_x86 installed
    goto done
:notfound
    echo installing vcredist_x86
    cd %APPDATA%\AIS-3USON\thirdparty
    vcredist_x86.exe  /install /passive /norestart
    rem msiexec /i  mysql-connector-odbc-8.0.msi  /quiet /qn /norestart
goto done
:done


rem ############################
rem  update mysql_connector
rem  ---------------------------
find /c "mysql_connector = 8020" %UserProfile%\.config\3uson\3uson.conf
if %errorlevel% EQU 1 goto notfound_upd
    echo app installed
    goto done_upd
:notfound_upd
    echo updating mysql_connector
    cd %APPDATA%\AIS-3USON\thirdparty
    msiexec /i  mysql-connector-odbc-8.0.msi /passive
    rem msiexec /i  mysql-connector-odbc-8.0.msi  /quiet /qn /norestart
goto done_upd
:done_upd


rem ############################
rem  start app
rem  ---------------------------
cd %APPDATA%\AIS-3USON
%APPDATA%\AIS-3USON\AIS-3USON.exe
