#-*- coding: utf-8 -*-

import wx

class RootPanel(wx.Panel):

	def __init__(self, frame):
		wx.Panel.__init__(self, frame, wx.ID_ANY)
		self.sizer = wx.BoxSizer(wx.VERTICAL)

	def addPanel(self, panel):
		self.sizer.Add(panel, flag = wx.GROW, proportion = 1)
		self.SetSizer(self.sizer)
