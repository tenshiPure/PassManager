#-*- coding: utf-8 -*-

import sys

import AutoLoader
from TextCtrlFrame import TextCtrlFrame
from ComboBoxFrame import ComboBoxFrame

if __name__ == '__main__':
	mode = sys.argv[1]
	lastActiveWindowName = sys.argv[2]
	frame = {'text' : TextCtrlFrame(lastActiveWindowName), 'combo' : ComboBoxFrame(lastActiveWindowName)}[mode]

	frame.Show()
	frame.application.MainLoop()
