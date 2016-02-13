import pygame, random
from threading import Timer
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

		# self.types = ['coin', 'clone', 'invincible']
		# self.sub_types = {
		# 	'coin': [50, 100, 500, 1000]
		# }

		self.type = 'coin'
		self.sub_type = 50


	def getBounds(self):
		bounds = {
			'start_x': self.x,
			'start_y': self.y,
			'end_x': self.x + self.w,
			'end_y': self.y + self.h
		}
		return bounds

	def draw(self, canvas):
		# pygame.draw.rect(canvas, BLACK, (self.x, self.y, self.w, self.h))
		if self.type == 'coin':
			self.drawCoin(canvas)
		elif self.type == 'clone':
			self.drawClone(canvas)
		elif self.type == 'invincible':
			self.drawInvincible(canvas)

	def drawCoin(self, canvas):
		color = getCoinColor(self.sub_type)
		pygame.draw.circle(canvas, color, (int(self.x), self.y), self.w//2)

	def drawClone(self, canvas):
		pygame.draw.rect(canvas, RED, (self.x, self.y, self.w, self.h))

	def drawInvincible(self, canvas):
		pygame.draw.rect(canvas, LIGHTBLUE, (self.x, self.y, self.w, self.h))

collecs = []
count = 2
types = ['coin', 'clone', 'invincible']
sub_types = {
	'coin': [50, 100, 500, 1000],
	'clone': [],
	'invincible': []
}

def getCoinColor(sub_type):
	if sub_type == 50:
		return YELLOW
	elif sub_type == 100:
		return BLUE
	elif sub_type == 500:
		return ORANGE
	elif sub_type == 1000:
		return PURPLE

def getRandomPos():
	pos = {}	

	if len(collecs) > 0 and collecs[-1] is not None:
		pos['x'] = collecs[-1].x + random.randint(1000, 1500)
	else:
		pos['x'] = random.randint(500, 1000)

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
	# collec = {}
	# sub_types = {}
	# pos = {}

	for i in range(count):
		collec = Collectible()
		pos = getRandomPos()

		collec.x = pos['x']
		collec.y = pos['y']

		collec.w = 30
		collec.h = 30

		collec.type = types[random.randint(0, len(types)-1)]
		print(collec.type)

		# Choose subtypes if any
		st = sub_types[collec.type]
		if len(st) > 0:
			collec.sub_type = st[random.randint(0, len(sub_types)-1)]
			print('subtype: ', collec.sub_type)

		collecs.append(collec)
		collecs_lst.append(collec)

def draw(canvas):
	create()
	index = 0
	for collec in collecs:
		if collec.x < 0:
			# Move off the left edge
			# pos = getRandomPos()

			# collec.x = pos['x']
			# collec.y = pos['y']
			collecs.pop(index)
			collecs_lst.pop(index)
		collec.x -= ground_bg_move_speed
		index += 1
		collec.draw(canvas)


def checkCollision(sprite):	
	collec = collecs[0]
	sprite_bounds = sprite.getBounds()
	collec_bounds = collec.getBounds()

	if intersect(sprite_bounds, collec_bounds):
		# Pappu collected!
		# pos = getRandomPos()

		# Determine the type and perform action accordingly
		if collec.type == 'coin':
			sprite.score += collec.sub_type
			print('score + ', collec.sub_type)			
		elif collec.type == 'invincible':
			sprite.invincible = True
			t = Timer(5.0, sprite.undoInvincible)
			t.start()
		print(sprite.score)


		# first_collec.x = pos['x']
		# first_collec.y = pos['y']
		shift = collecs.pop(0)

		print('caught a collectible')

def reset():
	global collecs
	collecs = []