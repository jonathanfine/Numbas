@echo off
REM Batch file for running Rhino on Windows.
java -classpath %RHINO_PATH%\js.jar org.mozilla.javascript.tools.shell.Main %1 %2 %3 %4 %5 %6 %7 %8 %9 
