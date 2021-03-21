dir /b ui_ip > dir.txt

set "file=dir.txt"
set /A i=0

break>list.txt

SETLOCAL enabledelayedexpansion
for /F %%a in (dir.txt) do (
	if NOT %%a==pyuic5.exe (
		set x=%%a
		set k=ui_ip\
		set h=!k!!x!
		set t=!x:~0,-3!
		set y=.py
		set c=!t!!y!
		set l=py_op\
		set m=!l!!c!
		set space= 
		set ip=!h!!space!!m!
		echo !ip!>>"list.txt"
	)
)
for /F "tokens=1,2" %%i in (list.txt) do (
		call pyuic5 -x %%i -o %%j
		
)
ENDLOCAL