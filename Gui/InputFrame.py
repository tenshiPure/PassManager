#-*- coding: utf-8 -*-

import wx

from RootFrame import RootFrame

from RootPanel import RootPanel
from InputPanel import InputPanel
from ButtonPanel import ButtonPanel

class InputFrame(RootFrame):

	def __init__(self, func):
		RootFrame.__init__(self, 'input mode')

		rootPanel = RootPanel(self)

		inputPanel = InputPanel(rootPanel)
		buttonPanel = ButtonPanel(rootPanel, func)
