#-*- coding: utf-8 -*-

import wx

class TextCtrlPanel(wx.Panel):

	def __init__(self, rootPanel):
		wx.Panel.__init__(self, rootPanel, wx.ID_ANY)

		idText = wx.TextCtrl(self, wx.ID_ANY, 'id')
		duplicateText = wx.TextCtrl(self, wx.ID_ANY, 'dup')

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(idText, proportion = 1, flag = wx.GROW | wx.ALL, border = 3)
		sizer.Add(duplicateText, proportion = 1, flag = wx.GROW | wx.ALL, border = 3)
		self.SetSizer(sizer)

		rootPanel.addPanel(self)
