import pygame, random
from configs import *
from utils import *

class Collectible(object):
	''' There will be some collectibles.

	Ones that give 50, 100, 500, 1000 points.
	Those for 50 and 100 points will also prevent pakias
	from coming for a while.

	One to clone pappu, it'll kill all forks, branches, and pakias.
	'''
	def __init__(self):
		self.x = 0
		self.y = 0

		self.w = 0
		self.h = 0

		# self.rect = (self.x, self.y, self.w, self.h)

		self.types = ['point', 'clone']
		self.sub_types = {
			'point': [50, 100, 500, 1000]
		}

	def getBounds(self):
		bounds = {
			'start_x': self.x,
			'start_y': self.y,
			'end_x': self.x + self.w,
			'end_y': self.y + self.h
		}
		return bounds

	def draw(self, canvas):
		pygame.draw.rect(canvas, BLACK, (self.x, self.y, self.w, self.h))

collecs = []
count = 2

def getRandomPos():
	pos = {}	

	if len(collecs) > 0 and collecs[-1] is not None:
		pos['x'] = collecs[-1].x + random.randint(1000, 1500)
	else:
		pos['x'] = random.randint(2000, 3000)

	pos['y'] = random.randint(100, SCREEN_HEIGHT-100)

	# Check positioning with forks
	forks = forks_lst
	if len(forks) > 0:
		for fork in forks:
			if abs(pos['x'] - fork.x) < 300:
				pos['x'] = fork.x + 300

	# Check positioning with branches
	branches = branches_lst
	if len(branches) > 0:
		for branch in branches:
			if abs(pos['x'] - branch.x) < 300:
				pos['x'] = branch.x + 300

	return pos

def create(cnt=count):
	count = cnt - len(collecs)
	collec = {}

	for i in range(count):
		collec = Collectible()
		pos = getRandomPos()

		collec.x = pos['x']
		collec.y = pos['y']

		collec.w = 30
		collec.h = 30

		collecs.append(collec)
		collecs_lst.append(collec)

def draw(canvas):
	create()
	# index = 0
	for collec in collecs:
		if collec.x < 0:
			# Move off the left edge
			pos = getRandomPos()

			collec.x = pos['x']
			collec.y = pos['y']
		collec.x -= (ground_bg_move_speed * 1.6)
		collec.draw(canvas)
	# index += 1

def checkCollision(sprite):
	first_collec = collecs[0]
	sprite_bounds = sprite.getBounds()
	collec_bounds = first_collec.getBounds()

	if intersect(sprite_bounds, collec_bounds):
		# Pappu collected!
		pos = getRandomPos()

		first_collec.x = pos['x']
		first_collec.y = pos['y']

		print('caught a collectible')

def reset():
	global collecs
	collecs = []