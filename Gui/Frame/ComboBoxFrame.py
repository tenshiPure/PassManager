#-*- coding: utf-8 -*-

import wx

from RootFrame import RootFrame
from RootPanel import RootPanel
from ComboBoxPanel import ComboBoxPanel
from ButtonPanel import ButtonPanel

class ComboBoxFrame(RootFrame):

	def __init__(self, lastActiveWindowName):
		RootFrame.__init__(self, 'select mode')

		rootPanel = RootPanel(self)

		inputPanel = ComboBoxPanel(rootPanel)
		buttonPanel = ButtonPanel(rootPanel, inputPanel, lastActiveWindowName, self.exitApplication)
