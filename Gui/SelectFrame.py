#-*- coding: utf-8 -*-

import wx

from RootFrame import RootFrame

from RootPanel import RootPanel
from SelectPanel import SelectPanel
from ButtonPanel import ButtonPanel

class SelectFrame(RootFrame):

	def __init__(self, func):
		RootFrame.__init__(self, 'select mode')

		rootPanel = RootPanel(self)

		groups = ['slf', 'soms']
		acounts = ['nrz', 'nlz', 'nyb']

		selectPanel = SelectPanel(rootPanel, groups, acounts)
		buttonPanel = ButtonPanel(rootPanel, func)
