#-*- coding: utf-8 -*-

import wx

class InputPanel(wx.Panel):

	def __init__(self, rootPanel):
		wx.Panel.__init__(self, rootPanel, wx.ID_ANY)

		self.idText = wx.TextCtrl(self, wx.ID_ANY, 'id')
		self.duplicateText = wx.TextCtrl(self, wx.ID_ANY, 'dup')

		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.idText, proportion = 1, flag = wx.GROW | wx.ALL, border = 3)
		self.sizer.Add(self.duplicateText, proportion = 1, flag = wx.GROW | wx.ALL, border = 3)
		self.SetSizer(self.sizer)

		rootPanel.addPanel(self)
