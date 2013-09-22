#-*- coding: utf-8 -*-

import wx

from RootFrame import RootFrame
from RootPanel import RootPanel
from ComboBoxPanel import ComboBoxPanel
from ButtonPanel import ButtonPanel

from Groups import Groups

class ComboBoxFrame(RootFrame):

	def __init__(self, func):
		RootFrame.__init__(self, 'select mode')

		rootPanel = RootPanel(self)

		comboBoxPanel = ComboBoxPanel(rootPanel, Groups())
		buttonPanel = ButtonPanel(rootPanel, func)
