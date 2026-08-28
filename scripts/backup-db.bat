@echo off
rem Wrapper for Task Scheduler - calls the bash backup script.
rem Uses Hermes' bundled git-bash (found on this machine).
set BASH="C:\Users\user\AppData\Local\hermes\git\usr\bin\bash.exe"
if not exist %BASH% set BASH="C:\Program Files\Git\bin\bash.exe"
if not exist %BASH% (
  echo ERROR: bash.exe not found. 1>&2
  exit /b 1
)
rem Ensure docker is on PATH for the child bash.
set "PATH=C:\Program Files\Docker\Docker\resources\bin;%PATH%"
"%BASH%" -lc "cd '/c/Users/user/Downloads/reactive-resume-main/reactive-resume-main' && ./scripts/backup-db.sh --keep 14"
exit /b %ERRORLEVEL%
