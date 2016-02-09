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
		self.col = 64
		self.image, self.rect = load_image('branch.png')

branches = []
# branch_img = pygame.image.load('branch.png')
# branch.rect = branch_img.get_rect()

# branch_col = 64


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

			# Escape positions
			branch.escape_x = branch.x
			branch.escape_y = branch.y + random.randint(0, branch.rect[3]-150)

			branches.append(branch)
			print(branch.rect)

	index = 0
	for branch in branches:
		if branch.x < 0:
			branches.pop(index)
		branch.x -= ground_bg_move_speed
		index += 1

		branch.escape_x = branch.x		

		hole_rect = (branch.escape_x, branch.escape_y, branch.rect[2], 150)		
		
		canvas.blit(branch.image, (branch.x, branch.y))

		if branch.col == 254:
			branch.col = 64
		canvas.fill((branch.col, 204, 244, 0), hole_rect)	
		branch.col += 5
