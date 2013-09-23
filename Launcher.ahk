!q::
	command := getCommand("text")
	Run, %command%
	return

!w::
	command := getCommand("combo")
	Run, %command%
	return

getCommand(mode) {
	python = python -B 
;	rootDir = D:\MyDocument\Program\PassManager
	rootDir = %A_WorkingDir%
	result = %python% %rootDir%\PassManager.pyw %mode%
	return result
}
