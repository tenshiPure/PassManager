#-*- coding: utf-8 -*-

import sys

import AutoLoader
from TextCtrlFrame import TextCtrlFrame
from ComboBoxFrame import ComboBoxFrame

if __name__ == '__main__':
	frame = {'text' : TextCtrlFrame(), 'combo' : ComboBoxFrame()}[sys.argv[1]]

	frame.Show()
	frame.application.MainLoop()
