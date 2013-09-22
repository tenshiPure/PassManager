#-*- coding: utf-8 -*-

import os
import os.path

from Group import Group
from Acount import Acount

class Groups:

	ACOUNTS_DIR = os.path.abspath(os.path.dirname(__file__) + '/../Acounts').decode('utf-8')

	def __init__(self):
		self.groups = self.parseAcountFiles()
		self.currentGroupNum = 0

	def parseAcountFiles(self):
		Group.init()
		groups = []
		for fileName in os.listdir(self.ACOUNTS_DIR):
			group = Group(fileName)
			for line in open(os.path.join(self.ACOUNTS_DIR, fileName), 'r'):
				acount = Acount(line)
				group.addAcount(acount)

			groups.append(group)

		return groups

	def getGroupNameList(self):
		result = []
		for group in self.groups:
			result.append(group.name)

		return result

	def getAcountDescList(self):
		result = []
		for acount in self.groups[self.currentGroupNum].acounts:
			result.append(acount.desc)

		return result

	def getCurrentGroupName(self):
		return self.groups[self.currentGroupNum].name

	def getAcountByNumFromCurrentGroup(self, id):
		return self.groups[self.currentGroupNum].acounts[id]

	def searchAcountWithGroupName(self, name):
		acounts = []
		groupNames = []
		for group in self.groups:
			for acount in group.acounts:
				if acount.name == name:
					acounts.append(acount)
					groupNames.append(group.name)

		if acounts and groupNames:
			return acounts, groupNames
		else:
			return None, None

	def changeGroup(self, index):
		self.currentGroupNum = index % len(self.groups)

	def prevGroup(self):
		self.currentGroupNum = (self.currentGroupNum - 1) % len(self.groups)

	def nextGroup(self):
		self.currentGroupNum = (self.currentGroupNum + 1) % len(self.groups)

if __name__ == '__main__':
	groups = Groups()
	print groups.getGroupNameList()
	print groups.getAcountDescList()
