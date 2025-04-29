@echo off
if not exist build mkdir build
xcopy /E /I templates build\templates
xcopy /E /I static build\static
copy app.py build\
copy requirements.txt build\
copy runtime.txt build\