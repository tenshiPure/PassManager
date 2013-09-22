#-*- coding: utf-8 -*-

import wx

from RootFrame import RootFrame
from RootPanel import RootPanel
from SelectPanel import SelectPanel
from ButtonPanel import ButtonPanel

from Groups import Groups

class SelectFrame(RootFrame):

	def __init__(self, func):
		RootFrame.__init__(self, 'select mode')

		rootPanel = RootPanel(self)

		groups = Groups()
		groupNameList = groups.getGroupNameList()
		acountDescList = groups.getAcountDescList()


		selectPanel = SelectPanel(rootPanel, groupNameList, acountDescList)
		buttonPanel = ButtonPanel(rootPanel, func)
