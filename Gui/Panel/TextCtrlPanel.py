#-*- coding: utf-8 -*-

import wx

from InputPanel import InputPanel

class TextCtrlPanel(InputPanel):

	def __init__(self, rootPanel):
		InputPanel.__init__(self, rootPanel)

		self.nameText = wx.TextCtrl(self, wx.ID_ANY, 'input id here', style = wx.TE_PROCESS_ENTER)
		self.nameText.Bind(wx.EVT_TEXT, self.searchAcount)

		self.duplicateComboBox = wx.ComboBox(self, wx.ID_ANY, '...', choices = [])
		self.duplicateComboBox.Bind(wx.EVT_COMBOBOX, self.choiceGroup)

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.nameText, proportion = 1, flag = wx.GROW | wx.ALL, border = 3)
		sizer.Add(self.duplicateComboBox, proportion = 1, flag = wx.GROW | wx.ALL, border = 3)
		self.SetSizer(sizer)

		rootPanel.addPanel(self)

	def searchAcount(self, event):
		name = self.nameText.GetValue()
		self.acounts, self.groupNames = self.groups.searchAcountWithGroupName(name)

		self.setAcountsAndGroupNames(self.acounts, self.groupNames)

	def setAcountsAndGroupNames(self, acounts, groupNames):
		if acounts is None and groupNames is None:
			self.duplicateComboBox.SetItems([])
			self.duplicateComboBox.SetValue('...')
			self.acount = None
			return

		if len(acounts) == 1:
			self.duplicateComboBox.SetValue('non duplicate')
			self.acount = acounts[0]

		else:
			self.duplicateComboBox.SetItems(groupNames)
			self.duplicateComboBox.SetValue('%d hit' % len(acounts))
			self.acount = None

	def choiceGroup(self, event):
		groupNum = event.GetEventObject().GetSelection()
		self.acount = self.acounts[groupNum]
