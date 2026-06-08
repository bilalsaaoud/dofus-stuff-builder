@echo off
echo ========================================
echo   Dofus Stuff Builder - Deploy GitHub
echo ========================================
echo.

:: Verifier que git est installe
git --version >nul 2>&1
if errorlevel 1 (
    echo ERREUR: Git n'est pas installe. Telecharge-le sur https://git-scm.com
    pause
    exit /b
)

:: Initialiser git si pas deja fait
if not exist ".git" (
    echo Initialisation du depot Git...
    git init
    git branch -m main
)

:: Ajouter tous les fichiers
echo Ajout des fichiers...
git add .

:: Commit
set /p MSG="Message du commit (Entree pour 'Update build'): "
if "%MSG%"=="" set MSG=Update build
git commit -m "%MSG%"

:: Demander l'URL du depot si pas configuree
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo.
    echo Entre l'URL de ton depot GitHub (ex: https://github.com/ton-user/dofus-stuff-builder.git)
    set /p REMOTE="URL: "
    git remote add origin !REMOTE!
)

:: Push
echo.
echo Push vers GitHub...
git push -u origin main

echo.
echo ========================================
echo   DONE! Ton site sera visible sur:
echo   https://[ton-user].github.io/[repo]/
echo ========================================
echo   Active GitHub Pages dans:
echo   Settings > Pages > Source: GitHub Actions
echo ========================================
pause
