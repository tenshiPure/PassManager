#-*- coding: utf-8 -*-

import wx
import pyauto

class PassManager:

	def __init__(self):
		self.running = False

		self.application = wx.App()
		self.frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300,200))
		self.panel = wx.Panel(self.frame,wx.ID_ANY)
		self.text = wx.TextCtrl(self.panel,wx.ID_ANY)

	def onKeyDown(self, vk, scan):
		if not self.running:
			self.frame.Show()
			self.running = True

if __name__ == '__main__':
	hook = pyauto.Hook()
	passManager = PassManager()
	hook.keydown = passManager.onKeyDown
	pyauto.messageLoop()
