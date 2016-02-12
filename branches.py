import pygame, random
from utils import *
from configs import *

class Branch(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.x = 0
		self.y = 0
		self.w = 0
		self.h = 0
		self.escape_x = 0
		self.escape_y = 0
		self.escape_w = 0
		self.escape_h = 0
		self.col = 64
		self.image, self.rect = load_image('branch.png')

	def getBounds(self):
		bounds = {
			'start_x': self.x,
			'start_y': self.y,
			'end_x': self.x + self.w,
			'end_y': self.y + self.h
		}

		return bounds

	def getEscapeBounds(self):
		bounds = {
			'start_x': self.escape_x,
			'start_y': self.escape_y,
			'end_x': self.escape_x + self.escape_w,
			'end_y': self.escape_y + self.escape_h
		}

		return bounds

branches = []


def getRandomBranchPos():
	pos = {}

	if len(branches) > 0 and branches[len(branches)-1] is not None:
		pos['x'] = branches[len(branches)-1].x
		pos['x'] += random.randint(500, 2000)
	else:
		# first
		pos['x'] = random.randint(2000, 2500)

	# last_fork = forks_lst[-1]

	# if abs(pos['x'] - last_fork.x) < 300:
	# 	pos['x'] = last_fork.x + 300

	for fork in forks_lst:
		if abs(pos['x'] - fork.x) < 400:
			pos['x'] = fork.x + 500

	return pos

def draw(canvas, count=branches_cnt):
	if len(branches) < count:
		for i in range(count - len(branches)+1):
			branch = Branch()

			pos = getRandomBranchPos()

			branch.x = pos['x']
			branch.y = 0

			branch.w = branch.rect.width
			branch.h = branch.rect.height

			# Escape positions
			branch.escape_x = branch.x
			branch.escape_y = branch.y + random.randint(0, branch.rect[3]-150)

			# Escape area width/height
			branch.escape_w = branch.rect.width
			branch.escape_h = 150

			branches.append(branch)
			branches_lst.append(branch)

	index = 0
	for branch in branches:
		if branch.x < 0:
			branches.pop(index)
			branches_lst.pop(index)
		branch.x -= ground_bg_move_speed
		index += 1

		branch.escape_x = branch.x		

		hole_rect = (branch.escape_x, branch.escape_y, branch.escape_w, branch.escape_h)		
		
		canvas.blit(branch.image, (branch.x, branch.y))

		if branch.col == 254:
			branch.col = 64
		canvas.fill((branch.col, 204, 244, 0), hole_rect)	
		branch.col += 5

def checkCollision(sprite):
	sprite_bounds = sprite.getBounds()

	branch_bounds = branches[0].getBounds()

	if intersect(sprite_bounds, branch_bounds):
		# If the escape area intersect then pappu can escape
		escape_bounds = branches[0].getEscapeBounds()

		if not intersect(sprite_bounds, escape_bounds):
			return True
	return False

def resetBranches():
	global branches
	branches = []
	print('branches reset')