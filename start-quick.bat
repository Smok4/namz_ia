@echo off
REM ========================================
REM Script de lancement rapide Namz IA
REM (Version sans verifications)
REM ========================================

title Namz IA

REM Activer l'environnement virtuel et lancer
call .venv\Scripts\activate.bat && python wsgi.py
