@echo off
REM ========================================
REM Script de lancement Namz IA
REM ========================================

echo.
echo ========================================
echo    NAMZ IA - Demarrage
echo ========================================
echo.

REM Vérifier si l'environnement virtuel existe
if not exist ".venv\Scripts\activate.bat" (
    echo [ERREUR] Environnement virtuel non trouve !
    echo.
    echo Creation de l'environnement virtuel...
    python -m venv .venv
    
    if errorlevel 1 (
        echo [ERREUR] Impossible de creer l'environnement virtuel
        pause
        exit /b 1
    )
    
    echo [OK] Environnement virtuel cree
    echo.
    echo Installation des dependances...
    call .venv\Scripts\activate.bat
    pip install -r requirements.txt
    
    if errorlevel 1 (
        echo [ERREUR] Impossible d'installer les dependances
        pause
        exit /b 1
    )
    
    echo [OK] Dependances installees
    echo.
)

REM Activer l'environnement virtuel
echo Activation de l'environnement virtuel...
call .venv\Scripts\activate.bat

if errorlevel 1 (
    echo [ERREUR] Impossible d'activer l'environnement virtuel
    pause
    exit /b 1
)

echo [OK] Environnement virtuel active
echo.

REM Vérifier que Flask est installé
python -c "import flask" 2>nul
if errorlevel 1 (
    echo [ATTENTION] Flask n'est pas installe
    echo Installation des dependances...
    pip install -r requirements.txt
    echo.
)

REM Lancer l'application
echo ========================================
echo    Lancement de Namz IA...
echo ========================================
echo.
echo Application disponible sur :
echo   - http://localhost:5000
echo   - http://127.0.0.1:5000
echo.
echo Appuyez sur Ctrl+C pour arreter l'application
echo.

python wsgi.py

REM Si l'application se ferme
echo.
echo ========================================
echo    Application arretee
echo ========================================
echo.
pause
