@echo off
echo -----------------------------------------
echo   🚀 Deploying Your Website to GitHub...
echo -----------------------------------------

cd /d %~dp0

echo Checking for changes...
git add .

git commit -m "Auto-update" 2>nul

echo Pushing to GitHub...
git push origin main

echo -----------------------------------------
echo   ✅ Deployment Complete!
echo -----------------------------------------
pause
