@echo Please make sure you have python 3.13 installed before continuing
@pause
@set /p "build=1 (File Interpreter) or 2 (Input Interpreter) > "
@if %build%==1 (	
	@python.exe -m pip install --upgrade pip
	@pip install pyinstaller
	@pyinstaller --clean --onefile --icon=.\uwufuckbuild\uwuFuck_FileInterpreter.png .\uwufuckbuild\uwuFuck_FileInterpreter.py
	@del uwuFuck_FileInterpreter.spec
	@echo y|rmdir /s build
	@copy .\dist\uwuFuck_FileInterpreter.exe .\uwuFuck_FileInterpreter.exe
	@echo y|rmdir /s dist
	@pause
)
@if %build%==2 (	
	@python.exe -m pip install --upgrade pip
	@pip install pyinstaller
	@pyinstaller --clean --onefile --icon=.\uwufuckbuild\uwuFuck_InputInterpreter.png .\uwufuckbuild\uwuFuck_InputInterpreter.py
	@del uwuFuck_InputInterpreter.spec
	@y|rmdir /s build
	@copy .\dist\uwuFuck_InputInterpreter.exe .\uwuFuck_InputInterpreter.exe
	@y|rmdir /s dist
	@pause
)