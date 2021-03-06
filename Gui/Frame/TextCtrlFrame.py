#-*- coding: utf-8 -*-

import wx

from RootFrame import RootFrame
from RootPanel import RootPanel
from TextCtrlPanel import TextCtrlPanel
from ButtonPanel import ButtonPanel

class TextCtrlFrame(RootFrame):

	def __init__(self, lastActiveWindowName):
		RootFrame.__init__(self, 'input mode')

		rootPanel = RootPanel(self)

		inputPanel = TextCtrlPanel(rootPanel)
		buttonPanel = ButtonPanel(rootPanel, inputPanel, lastActiveWindowName, self.exitApplication)
