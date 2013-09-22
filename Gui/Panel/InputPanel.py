#-*- coding: utf-8 -*-

import wx

from Groups import Groups

class InputPanel(wx.Panel):

	def __init__(self, rootPanel):
		wx.Panel.__init__(self, rootPanel, wx.ID_ANY)
		self.groups = Groups()
		self.acount = None
