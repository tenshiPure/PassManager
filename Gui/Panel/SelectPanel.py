#-*- coding: utf-8 -*-

import wx

class SelectPanel(wx.Panel):

	def __init__(self, rootPanel, groups, acounts):
		wx.Panel.__init__(self, rootPanel, wx.ID_ANY)

		comboboxGroup = wx.ComboBox(self, wx.ID_ANY, choices = groups)
		comboboxAcounts = wx.ComboBox(self, wx.ID_ANY, choices = acounts)

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(comboboxGroup, proportion = 1, flag = wx.GROW | wx.ALL, border = 3)
		sizer.Add(comboboxAcounts, proportion = 1, flag = wx.GROW | wx.ALL, border = 3)
		self.SetSizer(sizer)

		rootPanel.addPanel(self)
