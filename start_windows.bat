@echo off
setlocal
cd /d "%~dp0"
echo Starting Streamlit from the project folder...
python -m streamlit run run.py
if errorlevel 1 (
  echo Open Anaconda PowerShell Prompt, activate mynewproject,
  echo install requirements.txt, and try again.
  pause
)
endlocal
