#-*- coding: utf-8 -*-

import wx

from InputPanel import InputPanel

class ComboBoxPanel(InputPanel):

	KEY_LEFT  = 314
	KEY_UP    = 315
	KEY_RIGHT = 316
	KEY_DOWN  = 317

	def __init__(self, rootPanel):
		InputPanel.__init__(self, rootPanel)

		self.acountNum = 0
		self.acount = self.groups.getAcountByNumFromCurrentGroup(self.acountNum)

		groupNameList = self.groups.getGroupNameList()
		self.groupComboBox = wx.ComboBox(self, wx.ID_ANY, groupNameList[0], choices = groupNameList)
		self.groupComboBox.Bind(wx.EVT_COMBOBOX, self.changeGroup)
		self.groupComboBox.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)

		acountDescList = self.groups.getAcountDescList()
		self.acountsComboBox = wx.ComboBox(self, wx.ID_ANY, acountDescList[0], choices = acountDescList)
		self.acountsComboBox.Bind(wx.EVT_COMBOBOX, self.selectAcount)
		self.groupComboBox.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.groupComboBox, proportion = 1, flag = wx.GROW | wx.ALL, border = 3)
		sizer.Add(self.acountsComboBox, proportion = 1, flag = wx.GROW | wx.ALL, border = 3)
		self.SetSizer(sizer)

		rootPanel.addPanel(self)

	def changeGroup(self, event):
		groupNum = event.GetEventObject().GetSelection()
		self.groups.changeGroup(groupNum)

		self._update()

	def selectAcount(self, event):
		self.acountNum = event.GetEventObject().GetSelection()
		self.acount = self.groups.getAcountByNumFromCurrentGroup(self.acountNum)

	def onKeyDown(self, event):
		keyCode = event.GetKeyCode()
		if keyCode == self.KEY_LEFT:
			self.groups.prevGroup()
			self._update()

		if keyCode == self.KEY_RIGHT:
			self.groups.nextGroup()
			self._update()

		if keyCode == self.KEY_UP:
			self.acountNum += 1
			self.acount = self.groups.getAcountByNumFromCurrentGroup(self.acountNum)
			#丸め
			#表記

		if keyCode == self.KEY_DOWN:
			self.acountNum -= 1
			self.acount = self.groups.getAcountByNumFromCurrentGroup(self.acountNum)

	def _update(self):
		acountDescList = self.groups.getAcountDescList()
		self.acountsComboBox.SetItems(acountDescList)
		self.acountsComboBox.SetValue(acountDescList[0])

		self.groupComboBox.SetValue(self.groups.getCurrentGroupName())

		self.acount = self.groups.getAcountByNumFromCurrentGroup(0)
