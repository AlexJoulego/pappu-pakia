import pygame, random
from utils import *
from configs import *

class Branch(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.x = 0
		self.y = 0
		self.escape_x = 0
		self.escape_y = 0

branches = []
branch_img = pygame.image.load('branch.png')
branch_rect = branch_img.get_rect()


def getRandomBranchPos():
	pos = {}

	if len(branches) > 0 and branches[len(branches)-1] is not None:
		pos['x'] = branches[len(branches)-1].x
		pos['x'] += random.randint(100, 2000)
	else:
		# first
		pos['x'] = random.randint(500, 2500)
	return pos

def draw(canvas, count):
	if len(branches) < count:
		for i in range(count - len(branches)+1):
			branch = Branch()

			pos = getRandomBranchPos()

			branch.x = pos['x']
			branch.y = 0

			# Escape positions
			branch.escape_x = branch.x
			branch.escape_y = branch.y + random.randint(0, branch_rect[3]-150)

			branches.append(branch)

	index = 0
	for branch in branches:
		if branch.x < 0:
			branches.pop(index)
		branch.x -= ground_bg_move_speed
		index += 1

		branch.escape_x = branch.x
		
		branch_img.convert_alpha()

		hole_rect = (branch.escape_x, branch.escape_y, branch_rect[2], 150)
		
		canvas.blit(branch_img, (branch.x, branch.y))
		canvas.fill(GRADIENT_MID, hole_rect)
