#-*- coding: utf-8 -*-

import wx

class InputFrame:

	def __init__(self, func):
		self.application = wx.App()
		self.mainFrame = wx.Frame(None, wx.ID_ANY, 'input mode', style = wx.DEFAULT_FRAME_STYLE & ~wx.SYSTEM_MENU, size=(180, 150), pos = (50, 50))
		self.rootPanel = wx.Panel(self.mainFrame, wx.ID_ANY)

		self.inputPanel = wx.Panel(self.rootPanel,wx.ID_ANY)

		self.idText = wx.TextCtrl(self.inputPanel, wx.ID_ANY, 'id')
		self.duplicateText = wx.TextCtrl(self.inputPanel, wx.ID_ANY, 'dup')

		self.inputSizer = wx.BoxSizer(wx.VERTICAL)
		self.inputSizer.Add(self.idText, proportion = 1, flag = wx.GROW | wx.ALL, border = 3)
		self.inputSizer.Add(self.duplicateText, proportion = 1, flag = wx.GROW | wx.ALL, border = 3)
		self.inputPanel.SetSizer(self.inputSizer)

		self.buttonPanel = wx.Panel(self.rootPanel,wx.ID_ANY)

		self.buttonInputTwice = wx.Button(self.buttonPanel, wx.ID_ANY, 'id / pass')
		self.buttonInputTwice.Bind(wx.EVT_BUTTON, self.inputTwice)

		self.buttonInputOnce = wx.Button(self.buttonPanel, wx.ID_ANY, 'pass')
		self.buttonInputOnce.Bind(wx.EVT_BUTTON, self.inputOnce)

		self.buttonToClipboard = wx.Button(self.buttonPanel, wx.ID_ANY, 'clip board')
		self.buttonToClipboard.Bind(wx.EVT_BUTTON, self.toClipboard)

		self.buttonExit = wx.Button(self.buttonPanel, wx.ID_ANY, 'exit')
		self.buttonExit.Bind(wx.EVT_BUTTON, func)

		self.buttonSizer = wx.GridSizer(2, 2)
		self.buttonSizer.Add(self.buttonInputTwice, flag = wx.GROW | wx.ALL, border = 3)
		self.buttonSizer.Add(self.buttonInputOnce, flag = wx.GROW | wx.ALL, border = 3)
		self.buttonSizer.Add(self.buttonToClipboard, flag = wx.GROW | wx.ALL, border = 3)
		self.buttonSizer.Add(self.buttonExit, flag = wx.GROW | wx.ALL, border = 3)
		self.buttonPanel.SetSizer(self.buttonSizer)

		self.panelSizer = wx.BoxSizer(wx.VERTICAL)
		self.panelSizer.Add(self.inputPanel, flag = wx.GROW, proportion = 1)
		self.panelSizer.Add(self.buttonPanel, flag = wx.GROW, proportion = 1)
		self.rootPanel.SetSizer(self.panelSizer)

	def inputTwice(self, event):
		print 'input twice'

	def inputOnce(self, event):
		print 'input once'

	def toClipboard(self, event):
		print 'to clipboard'
