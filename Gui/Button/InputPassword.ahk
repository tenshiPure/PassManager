windowName = %1%
WinActivate, %windowName%

Send, ^a
Send, {DELETE}

password = %2%
Send, %password%
