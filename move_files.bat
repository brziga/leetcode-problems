@echo off
setlocal enabledelayedexpansion

REM Check if the folder name is provided as an argument
if "%~1"=="" (
    echo Usage: %0 ^<target_folder^>
    exit /b 1
)

set "TARGET_FOLDER=%~1"
set "TEMPLATE_FOLDER=template"

REM Create the target folder if it doesn't exist
if not exist "%TARGET_FOLDER%" (
    echo Creating target folder: %TARGET_FOLDER%
    mkdir "%TARGET_FOLDER%"
)

REM Move solution.py and testcases.txt from the current directory to the target folder
for %%f in (solution.py testcases.txt) do (
    if exist "%%f" (
        echo Moving %%f to %TARGET_FOLDER%
        move "%%f" "%TARGET_FOLDER%"
    ) else (
        echo %%f does not exist in the current directory.
    )
)

REM Copy solution.py and testcases.txt from the template folder to the current working directory
for %%f in (solution.py testcases.txt) do (
    set "SOURCE_FILE=%TEMPLATE_FOLDER%\%%f"
    if exist "!SOURCE_FILE!" (
        echo Copying !SOURCE_FILE! to the current working directory
        copy "!SOURCE_FILE!" "."
    ) else (
        echo !SOURCE_FILE! does not exist in the template folder.
    )
)

echo Operation completed.


:: Set the constant to subtract
:: This is the number of extra non-problem directories
:: (since checking the names and counting only numeric ones doesn't seem to want to happen...)
set SUBTRACT_CONSTANT=3

:: Output file path
set output_file=num_solved_problems.txt

:: Initialize counter
set count=0

:: Loop through all directories in the current folder
for /d %%d in (*) do (
    set /a count+=1
)

:: Subtract the constant from the count
set /a result=count-%SUBTRACT_CONSTANT%

:: Write the result to the output file, overwriting if it exists
echo %result% > %output_file%

echo Count has been written to %output_file%

endlocal
