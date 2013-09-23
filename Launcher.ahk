!q::
	windowName := getActiveWindowName()
	command := getCommand("text", windowName)
	Run, %command%
	return

!w::
	windowName := getActiveWindowName()
	command := getCommand("combo", windowName)
	Run, %command%
	return

getCommand(mode, windowName) {
	python = python -B 
;	rootDir = D:\MyDocument\Program\PassManager
	rootDir = %A_WorkingDir%
	result = %python% %rootDir%\PassManager.pyw %mode% %windowName%
	return result
}

getActiveWindowName() {
	WinGetTitle, windowName, A
	return windowName
}
