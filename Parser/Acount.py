#-*- coding: utf-8 -*-

class Acount:

	id = 0

	@staticmethod
	def init():
		Acount.id = 0

	def __init__(self, line):
		splited = line.decode('utf-8').encode('cp932').rstrip('\r\n').split(',')

		self.id   = self.getNextId()
		self.desc = splited[0]
		self.name = splited[1]
		self.pswd = splited[2]

	def getNextId(self):
		Acount.id += 1
		return Acount.id

	def dump(self):
		print '\tid   : %s' % self.id
		print '\tdesc : %s' % self.desc
		print '\tname : %s' % self.name
		print '\tpswd : %s' % self.pswd
		print ' '
