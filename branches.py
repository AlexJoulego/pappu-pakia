import pygame, random
from configs import *

class Branch(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.color = GREEN

	def draw(self, canvas):
		pass

branches = []

def getRandomBranchPos():
	pos = {}

	if len(branches) > 0 and branches[len(branches)-1] is not None:
		pos['x'] = branches[len(branches)-1].x
		pos['x'] += 250
		pos['y'] = branches[len(branches)-1].y
	else:
		pos['x'] = 200
		pos['y'] = 200
	return pos

def drawBranches(canvas, count):
	if len(branches) < count:
		for i in range(count - len(branches)+1):
			branch = Branch()

			pos = getRandomBranchPos()

			branch.x = pos['x']
			branch.y = pos['y']			

			branches.append(branch)

	index = 0
	for branch in branches:
		if branch.x < 0:
			branches.pop(index)
		branch.x -= 3
		index += 1

		line_start = [branch.x, branch.y]
		line_end = [branch.x, 0]
		pygame.draw.line(canvas, branch.color, line_start, line_end, 5)