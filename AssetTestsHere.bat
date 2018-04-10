@echo off
set filePath=%1
echo filePath

rem Get start time:
for /F "tokens=1-4 delims=:.," %%a in ("%time%") do (
   set /A "start=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100"
)


rem AssetTester.exe windows_metadata -id -vf -dir %dir%

pushd "C:\Users\Jackson\Documents\maya\scripts\codeSnippets"mayapy batchExporter.py filePath

