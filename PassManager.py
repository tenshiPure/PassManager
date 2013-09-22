#-*- coding: utf-8 -*-

import wx
import pyauto

from Gui.InputFrame import InputFrame
from Gui.SelectFrame import SelectFrame

class PassManager:

	KEY_ALT = 164
	KEY_Q = 81
	KEY_W = 87

	def __init__(self):
		self.running = False
		self.modifier = False
		self.inputFrame = InputFrame(self.hookEnd)
		self.selectFrame = SelectFrame(self.hookEnd)

	def hookStart(self):
		self.hook = pyauto.Hook()
		self.hook.keydown = self.onKeyDown
		self.hook.keyup = self.onKeyUp
		pyauto.messageLoop()

	def hookEnd(self, event):
		self.hook.destroy()

	def onKeyDown(self, vk, scan):
		if self.running:
			return False

		if vk == PassManager.KEY_ALT:
			self.modifier = True

		if self.modifier and vk == PassManager.KEY_Q:
			self.inputFrame.mainFrame.Show()
			self.running = True

		if self.modifier and vk == PassManager.KEY_W:
			self.selectFrame.mainFrame.Show()
			self.running = True

		return True

	def onKeyUp(self, vk, scan):
		if vk == PassManager.KEY_ALT:
			self.modifier = False

		return True

if __name__ == '__main__':
	passManager = PassManager()
	passManager.hookStart()
