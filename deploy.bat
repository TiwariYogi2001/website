@echo off
echo -----------------------------------------
echo   Building and deploying the site...
echo -----------------------------------------

cd /d %~dp0

echo Regenerating pages from build.py...
python build.py
if errorlevel 1 (
  echo Build failed - nothing was pushed.
  pause
  exit /b 1
)

echo Committing changes...
git add -A
git commit -m "Update site" 2>nul

echo Pushing to GitHub...
git push origin main

echo -----------------------------------------
echo   Done. Live in a minute or two at
echo   https://tiwariyogi2001.github.io/website/
echo -----------------------------------------
pause
