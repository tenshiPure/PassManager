#-*- coding: utf-8 -*-

import wx

from RootFrame import RootFrame
from RootPanel import RootPanel
from ComboBoxPanel import ComboBoxPanel
from ButtonPanel import ButtonPanel

class ComboBoxFrame(RootFrame):

	def __init__(self, exitFunction):
		RootFrame.__init__(self, 'select mode')

		rootPanel = RootPanel(self)

		comboBoxPanel = ComboBoxPanel(rootPanel)
		buttonPanel = ButtonPanel(rootPanel, comboBoxPanel, exitFunction)
