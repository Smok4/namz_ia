@echo off
REM ========================================
REM Script de test Namz IA
REM ========================================

echo.
echo ========================================
echo    NAMZ IA - Tests
echo ========================================
echo.

REM Activer l'environnement virtuel
call .venv\Scripts\activate.bat

if errorlevel 1 (
    echo [ERREUR] Environnement virtuel non trouve
    echo Executez install.bat d'abord
    pause
    exit /b 1
)

echo Test 1: Chargement de l'application...
python -c "from app import create_app; app = create_app(); print('[OK] App chargee')"

if errorlevel 1 (
    echo [ERREUR] Impossible de charger l'application
    pause
    exit /b 1
)

echo.
echo Test 2: Chargement des modules...
python -c "from app.conversation_memory import get_conversation_memory; from app.code_analyzer import get_code_analyzer; from app.proactive_suggester import get_proactive_suggester; from app.multi_file_generator import get_multi_file_generator; print('[OK] Tous les modules charges')"

if errorlevel 1 (
    echo [ERREUR] Erreur lors du chargement des modules
    pause
    exit /b 1
)

echo.
echo Test 3: Test du moteur IA...
python -c "from app.ia_engine import engine; r = engine.analyse('Test'); print('[OK] Moteur IA fonctionnel')"

if errorlevel 1 (
    echo [ERREUR] Erreur du moteur IA
    pause
    exit /b 1
)

echo.
echo ========================================
echo    Tous les tests sont passes !
echo ========================================
echo.
pause
