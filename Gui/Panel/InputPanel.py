#-*- coding: utf-8 -*-

import wx

class InputPanel(wx.Panel):

	def __init__(self, rootPanel):
		wx.Panel.__init__(self, rootPanel, wx.ID_ANY)
		self.acount = None
