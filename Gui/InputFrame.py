#-*- coding: utf-8 -*-

import wx

class InputFrame:

	def __init__(self, func):
		self.application = wx.App()
		self.frame = wx.Frame(None, wx.ID_ANY, 'input mode', style = wx.DEFAULT_FRAME_STYLE & ~wx.SYSTEM_MENU, size=(100, 200), pos = (50, 50))
		self.panel = wx.Panel(self.frame,wx.ID_ANY)

		self.text = wx.TextCtrl(self.panel, wx.ID_ANY, size = (90, 20), pos = (10, 10))

		self.buttonInputTwice = wx.Button(self.panel, wx.ID_ANY, 'id / pass', size = (90, 20), pos = (10, 40))
		self.buttonInputTwice.Bind(wx.EVT_BUTTON, self.inputTwice)

		self.buttonInputOnce = wx.Button(self.panel, wx.ID_ANY, 'pass', size = (90, 20), pos = (10, 70))
		self.buttonInputOnce.Bind(wx.EVT_BUTTON, self.inputOnce)

		self.buttonToClipboard = wx.Button(self.panel, wx.ID_ANY, 'clip board', size = (90, 20), pos = (10, 100))
		self.buttonToClipboard.Bind(wx.EVT_BUTTON, self.toClipboard)

		self.buttonExit = wx.Button(self.panel, wx.ID_ANY, 'exit', size = (90, 20), pos = (10, 130))
		self.buttonExit.Bind(wx.EVT_BUTTON, func)

	def inputTwice(self, event):
		print 'input twice'

	def inputOnce(self, event):
		print 'input once'

	def toClipboard(self, event):
		print 'to clipboard'
