#-*- coding: utf-8 -*-

import wx
import os

import AutoLoader

class ButtonPanel(wx.Panel):

	def __init__(self, rootPanel, inputPanel):
		wx.Panel.__init__(self, rootPanel, wx.ID_ANY)

		self.inputPanel = inputPanel

		buttonInputTwice = wx.Button(self, wx.ID_ANY, 'id / pass')
		buttonInputTwice.Bind(wx.EVT_BUTTON, self.inputIdAndPass)

		buttonInputOnce = wx.Button(self, wx.ID_ANY, 'pass')
		buttonInputOnce.Bind(wx.EVT_BUTTON, self.inputPass)

		buttonToClipboard = wx.Button(self, wx.ID_ANY, 'clip board')
		buttonToClipboard.Bind(wx.EVT_BUTTON, self.toClipboard)

		buttonExit = wx.Button(self, wx.ID_ANY, 'exit')
		buttonExit.Bind(wx.EVT_BUTTON, self.exit)

		sizer = wx.GridSizer(2, 2)
		sizer.Add(buttonInputTwice, flag = wx.GROW | wx.ALL, border = 3)
		sizer.Add(buttonInputOnce, flag = wx.GROW | wx.ALL, border = 3)
		sizer.Add(buttonToClipboard, flag = wx.GROW | wx.ALL, border = 3)
		sizer.Add(buttonExit, flag = wx.GROW | wx.ALL, border = 3)
		self.SetSizer(sizer)

		rootPanel.addPanel(self)

	def inputIdAndPass(self, event):
		print self.getId()
		print self.getPass()

	def inputPass(self, event):
		print self.getPass()

	def toClipboard(self, event):
		script = self.getScriptPath('ToClipBoard.exe')
		password = self.getPass()
		os.system('%s %s' % (script, password))

	def exit(self, event):
		print 'exit'

	def getId(self):
		acount = self.inputPanel.acount
		return acount.name if acount is not None else None

	def getPass(self):
		acount = self.inputPanel.acount
		return acount.pswd if acount is not None else None

	def getScriptPath(self, scriptName):
		scriptPash = os.path.abspath(AutoLoader.ROOT_PATH + '/Gui/Button')
		return os.path.join(scriptPash, scriptName)
