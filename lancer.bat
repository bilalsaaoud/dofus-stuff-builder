@echo off
cd /d "C:\Users\bilal\Claude\Projects\application  dofus"
echo ================================
echo   Dofus Stuff Builder - Serveur
echo ================================
echo Serveur lance sur http://localhost:8000
echo Laisse cette fenetre ouverte !
echo.
start "" "http://localhost:8000"
python -m http.server 8000
pause
