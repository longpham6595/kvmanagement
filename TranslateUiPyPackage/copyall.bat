for /F %%a in (dir.txt) do (
	xcopy /s py_op %%a
)