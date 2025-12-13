@echo off
cd /d "%~dp0"

set REPO_URL=https://github.com/lotsofnames/clone.git
set TEMP_DIR=_temp_clone
set MAIN_FILE=audio.py

echo === Kontrola Pythonu ===
python --version >nul 2>&1
if errorlevel 1 (
    echo Python nie je nainstalovany!
    echo Nainstaluj z: https://www.python.org/downloads/
    pause
    exit /b
)

echo === Kontrola GIT ===
git --version >nul 2>&1
if errorlevel 1 (
    echo GIT nie je nainstalovany!
    echo https://git-scm.com/download/win
    pause
    exit /b
)

echo === Klonujem repo (docasne) ===
if exist "%TEMP_DIR%" rmdir /s /q "%TEMP_DIR%"
git clone %REPO_URL% "%TEMP_DIR%"

echo === Kopirujem subory (bez .git a requirements.txt) ===
for /d %%D in ("%TEMP_DIR%\*") do (
    if /I not "%%~nxD"==".git" (
        xcopy "%%D" "%%~nxD" /E /I /Y >nul
    )
)

for %%F in ("%TEMP_DIR%\*") do (
    if /I not "%%~nxF"=="requirements.txt" (
        copy "%%F" . >nul
    )
)

echo === Mazem docasny priecinok ===
rmdir /s /q "%TEMP_DIR%"

if not exist "%MAIN_FILE%" (
    echo CHYBA: %MAIN_FILE% sa nenasiel!
    pause
    exit /b
)

echo === Spustam program ===
python %MAIN_FILE%

pause
