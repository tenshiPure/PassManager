#-*- coding: utf-8 -*-

class Acount:

	id = 0

	@staticmethod
	def init():
		Acount.id = 0

	def __init__(self, line):
		parsed = self.parse(line)

		self.id   = self.getNextId()
		self.desc = parsed[0]
		self.name = parsed[1]
		self.pswd = parsed[2]

	def parse(self, line):
		splited = line.split(',')

		return splited[0], splited[1], splited[2]

	def getNextId(self):
		Acount.id += 1
		return Acount.id

	def dump(self):
		print '\tid   : %s' % self.id
		print '\tdesc : %s' % self.desc
		print '\tname : %s' % self.name
		print '\tpswd : %s' % self.pswd
		print ' '
