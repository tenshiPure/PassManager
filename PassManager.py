#-*- coding: utf-8 -*-

import wx
import pyauto

from Gui.InputFrame import InputFrame

class PassManager:

	def __init__(self):
		self.running = False
		self.inputFrame = InputFrame(self.hookEnd)

	def hookStart(self):
		self.hook = pyauto.Hook()
		self.hook.keydown = self.onKeyDown
		pyauto.messageLoop()

	def hookEnd(self, event):
		self.hook.destroy()

	def onKeyDown(self, vk, scan):
		if not self.running:
			self.inputFrame.frame.Show()
			self.running = True

if __name__ == '__main__':
	passManager = PassManager()
	passManager.hookStart()
