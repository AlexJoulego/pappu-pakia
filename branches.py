import pygame, random
from configs import *

class Branch(object):
	def __init__(self):
		self.x = 0
		self.y = 0

branches = []
branch_img = pygame.image.load('branch.png')

def getRandomBranchPos():
	pos = {}

	if len(branches) > 0 and branches[len(branches)-1] is not None:
		pos['x'] = branches[len(branches)-1].x
		pos['x'] += random.randint(500, 2000)
	else:
		# first
		pos['x'] = random.randint(2000, 2500)
	return pos

def draw(canvas, count):
	if len(branches) < count:
		for i in range(count - len(branches)+1):
			branch = Branch()

			pos = getRandomBranchPos()

			branch.x = pos['x']
			branch.y = 0			

			branches.append(branch)

	index = 0
	for branch in branches:
		if branch.x < 0:
			branches.pop(index)
		branch.x -= ground_bg_move_speed
		index += 1
		
		canvas.blit(branch_img, (branch.x, branch.y))