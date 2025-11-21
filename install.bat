@echo off
REM ========================================
REM Script d'installation Namz IA
REM ========================================

echo.
echo ========================================
echo    NAMZ IA - Installation
echo ========================================
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe ou pas dans le PATH
    echo.
    echo Veuillez installer Python 3.8+ depuis https://www.python.org/
    pause
    exit /b 1
)

echo [OK] Python detecte :
python --version
echo.

REM Créer l'environnement virtuel
echo Creation de l'environnement virtuel...
if exist ".venv" (
    echo [INFO] Environnement virtuel existe deja
    echo Voulez-vous le recreer ? (O/N)
    set /p choice="> "
    if /i "%choice%"=="O" (
        echo Suppression de l'ancien environnement...
        rmdir /s /q .venv
        python -m venv .venv
    )
) else (
    python -m venv .venv
)

if errorlevel 1 (
    echo [ERREUR] Impossible de creer l'environnement virtuel
    pause
    exit /b 1
)

echo [OK] Environnement virtuel cree
echo.

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

REM Mettre à jour pip
echo Mise a jour de pip...
python -m pip install --upgrade pip
echo.

REM Installer les dépendances
echo Installation des dependances depuis requirements.txt...
pip install -r requirements.txt

if errorlevel 1 (
    echo [ERREUR] Impossible d'installer les dependances
    pause
    exit /b 1
)

echo.
echo ========================================
echo    Installation terminee !
echo ========================================
echo.
echo Pour lancer Namz IA :
echo   1. Double-cliquez sur start.bat
echo   2. Ou executez : start-quick.bat
echo.
echo L'application sera disponible sur :
echo   http://localhost:5000
echo.
pause
