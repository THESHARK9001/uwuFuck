@echo Please make sure you have python 3.13 installed before continuing
@pause
@python.exe -m pip install --upgrade pip
@pip install pyinstaller
@pyinstaller --clean --onefile --icon=.\uwufuckbuild\uwuFuck_Interpreter.png .\uwufuckbuild\uwuFuck_Interpreter.py
@del uwuFuck_FileInterpreter.spec
@echo y|rmdir /s build
@copy .\dist\uwuFuck_Interpreter.exe .\uwuFuck_Interpreter.exe
@echo y|rmdir /s dist
@pause
