#-*- coding: utf-8 -*-

import wx

class RootFrame(wx.Frame):

	def __init__(self, windowName):
		self.application = wx.App()
		wx.Frame.__init__(self, None, wx.ID_ANY, windowName, style = wx.DEFAULT_FRAME_STYLE & ~wx.SYSTEM_MENU, size=(180, 150), pos = (50, 50))

	def exitApplication(self):
		self.application.Exit()
