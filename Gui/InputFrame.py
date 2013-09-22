#-*- coding: utf-8 -*-

import wx

from RootPanel import RootPanel
from InputPanel import InputPanel
from ButtonPanel import ButtonPanel

class InputFrame:

	def __init__(self, func):
		self.application = wx.App()
		self.mainFrame = wx.Frame(None, wx.ID_ANY, 'input mode', style = wx.DEFAULT_FRAME_STYLE & ~wx.SYSTEM_MENU, size=(180, 150), pos = (50, 50))

		self.rootPanel = RootPanel(self.mainFrame)

		self.inputPanel = InputPanel(self.rootPanel)
		self.buttonPanel = ButtonPanel(self.rootPanel, func)
