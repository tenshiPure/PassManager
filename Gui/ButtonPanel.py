#-*- coding: utf-8 -*-

import wx

class ButtonPanel(wx.Panel):

	def __init__(self, rootPanel, func):
		wx.Panel.__init__(self, rootPanel, wx.ID_ANY)

		buttonInputTwice = wx.Button(self, wx.ID_ANY, 'id / pass')
		buttonInputTwice.Bind(wx.EVT_BUTTON, self.inputTwice)

		buttonInputOnce = wx.Button(self, wx.ID_ANY, 'pass')
		buttonInputOnce.Bind(wx.EVT_BUTTON, self.inputOnce)

		buttonToClipboard = wx.Button(self, wx.ID_ANY, 'clip board')
		buttonToClipboard.Bind(wx.EVT_BUTTON, self.toClipboard)

		buttonExit = wx.Button(self, wx.ID_ANY, 'exit')
		buttonExit.Bind(wx.EVT_BUTTON, func)

		sizer = wx.GridSizer(2, 2)
		sizer.Add(buttonInputTwice, flag = wx.GROW | wx.ALL, border = 3)
		sizer.Add(buttonInputOnce, flag = wx.GROW | wx.ALL, border = 3)
		sizer.Add(buttonToClipboard, flag = wx.GROW | wx.ALL, border = 3)
		sizer.Add(buttonExit, flag = wx.GROW | wx.ALL, border = 3)
		self.SetSizer(sizer)

		rootPanel.addPanel(self)

	def inputTwice(self, event):
		print 'input twice'

	def inputOnce(self, event):
		print 'input once'

	def toClipboard(self, event):
		print 'to clipboard'
