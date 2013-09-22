#-*- coding: utf-8 -*-

import os
import os.path
import sys

ROOT_PATH = os.path.dirname(__file__)

def getDir(currentRoot):
	for path in os.listdir(currentRoot):
		if path == '.git':
			continue

		fullPath = os.path.join(currentRoot, path)
		if os.path.isdir(fullPath):
			sys.path.append(fullPath)
			getDir(fullPath)

getDir(ROOT_PATH)
sys.path = list(set(sys.path))
