#-*- coding: utf-8 -*-

import wx

class ButtonPanel(wx.Panel):

	def __init__(self, rootPanel, func):
		wx.Panel.__init__(self, rootPanel, wx.ID_ANY)

		self.buttonInputTwice = wx.Button(self, wx.ID_ANY, 'id / pass')
		self.buttonInputTwice.Bind(wx.EVT_BUTTON, self.inputTwice)

		self.buttonInputOnce = wx.Button(self, wx.ID_ANY, 'pass')
		self.buttonInputOnce.Bind(wx.EVT_BUTTON, self.inputOnce)

		self.buttonToClipboard = wx.Button(self, wx.ID_ANY, 'clip board')
		self.buttonToClipboard.Bind(wx.EVT_BUTTON, self.toClipboard)

		self.buttonExit = wx.Button(self, wx.ID_ANY, 'exit')
		self.buttonExit.Bind(wx.EVT_BUTTON, func)

		self.sizer = wx.GridSizer(2, 2)
		self.sizer.Add(self.buttonInputTwice, flag = wx.GROW | wx.ALL, border = 3)
		self.sizer.Add(self.buttonInputOnce, flag = wx.GROW | wx.ALL, border = 3)
		self.sizer.Add(self.buttonToClipboard, flag = wx.GROW | wx.ALL, border = 3)
		self.sizer.Add(self.buttonExit, flag = wx.GROW | wx.ALL, border = 3)
		self.SetSizer(self.sizer)

	def inputTwice(self, event):
		print 'input twice'

	def inputOnce(self, event):
		print 'input once'

	def toClipboard(self, event):
		print 'to clipboard'
