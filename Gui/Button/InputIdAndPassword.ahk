windowName = %1%
WinActivate, %windowName%

Send, ^a
Send, {DELETE}

id = %2%
Send, %id%

Send, {TAB}
Send, ^a
Send, {DELETE}

password = %3%
Send, %password%
