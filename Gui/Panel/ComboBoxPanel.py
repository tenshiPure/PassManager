#-*- coding: utf-8 -*-

import wx

from InputPanel import InputPanel

class ComboBoxPanel(InputPanel):

	def __init__(self, rootPanel):
		InputPanel.__init__(self, rootPanel)

		self.acount = self.groups.getAcount(0)

		groupNameList = self.groups.getGroupNameList()
		self.groupComboBox = wx.ComboBox(self, wx.ID_ANY, groupNameList[0], choices = groupNameList)
		self.groupComboBox.Bind(wx.EVT_COMBOBOX, self.changeGroup)

		acountDescList = self.groups.getAcountDescList()
		self.acountsComboBox = wx.ComboBox(self, wx.ID_ANY, acountDescList[0], choices = acountDescList)
		self.acountsComboBox.Bind(wx.EVT_COMBOBOX, self.selectAcount)

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.groupComboBox, proportion = 1, flag = wx.GROW | wx.ALL, border = 3)
		sizer.Add(self.acountsComboBox, proportion = 1, flag = wx.GROW | wx.ALL, border = 3)
		self.SetSizer(sizer)

		rootPanel.addPanel(self)

	def changeGroup(self, event):
		groupNum = event.GetEventObject().GetSelection()
		self.groups.changeGroup(groupNum)

		acountDescList = self.groups.getAcountDescList()
		self.acountsComboBox.SetItems(acountDescList)
		self.acountsComboBox.SetValue(acountDescList[0])

		self.acount = self.groups.getAcount(0)

	def selectAcount(self, event):
		acountNum = event.GetEventObject().GetSelection()
		self.acount = self.groups.getAcount(acountNum)
