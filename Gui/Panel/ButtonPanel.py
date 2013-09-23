#-*- coding: utf-8 -*-

import wx
import Tkinter

class ButtonPanel(wx.Panel):

	def __init__(self, rootPanel, inputPanel, exitFunction):
		wx.Panel.__init__(self, rootPanel, wx.ID_ANY)

		self.inputPanel = inputPanel

		buttonInputTwice = wx.Button(self, wx.ID_ANY, 'id / pass')
		buttonInputTwice.Bind(wx.EVT_BUTTON, self.inputTwice)

		buttonInputOnce = wx.Button(self, wx.ID_ANY, 'pass')
		buttonInputOnce.Bind(wx.EVT_BUTTON, self.inputOnce)

		buttonToClipboard = wx.Button(self, wx.ID_ANY, 'clip board')
		buttonToClipboard.Bind(wx.EVT_BUTTON, self.toClipboard)

		buttonExit = wx.Button(self, wx.ID_ANY, 'exit')
		buttonExit.Bind(wx.EVT_BUTTON, exitFunction)

		sizer = wx.GridSizer(2, 2)
		sizer.Add(buttonInputTwice, flag = wx.GROW | wx.ALL, border = 3)
		sizer.Add(buttonInputOnce, flag = wx.GROW | wx.ALL, border = 3)
		sizer.Add(buttonToClipboard, flag = wx.GROW | wx.ALL, border = 3)
		sizer.Add(buttonExit, flag = wx.GROW | wx.ALL, border = 3)
		self.SetSizer(sizer)

		rootPanel.addPanel(self)

	def inputTwice(self, event):
		print self.inputPanel.acount.name
		print self.inputPanel.acount.pswd

	def inputOnce(self, event):
		print self.inputPanel.acount.pswd

	def toClipboard(self, event):
		Tkinter.Text().clipboard_clear()
		Tkinter.Text().clipboard_append(self.inputPanel.acount.pswd)
