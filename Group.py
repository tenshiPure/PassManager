#-*- coding: utf-8 -*-

from Acount import Acount

class Group:

	id = 0

	@staticmethod
	def init():
		Group.id = 0

	def __init__(self, name):
		self.id = self.getNextId()
		self.name = name.encode('cp932')
		self.acounts = []

		Acount.init()

	def addAcount(self, acount):
		self.acounts.append(acount)

	def getNextId(self):
		Group.id += 1
		return Group.id

	def dump(self):
		print 'id   : %s' % self.id
		print 'name : %s' % self.name
		for acount in self.acounts:
			acount.dump()
		print ' '
