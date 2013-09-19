#-*- coding: utf-8 -*-

import os
import os.path

from Group import Group
from Acount import Acount

groups = []
Group.init()

dirName = u'./Acounts'
for fileName in os.listdir(dirName):
	group = Group(fileName)
	for line in open(os.path.join(dirName, fileName), 'r'):
		acount = Acount(line.rstrip('\r\n'))
		group.addAcount(acount)

	groups.append(group)

for group in groups:
	group.dump()
