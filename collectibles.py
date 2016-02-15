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
		
		self.type = 'clone'
		self.sub_type = 50

		self.sound = load_sound('ting.ogg')
		self.sound.set_volume(0.35)

		self.clone_img = pygame.image.load('berries.png').convert_alpha()
		self.invincible_img = pygame.image.load('apple.png').convert_alpha()
		self.coin_img = pygame.image.load('coins.png').convert_alpha()


	def getBounds(self):
		bounds = {
			'start_x': self.x,
			'start_y': self.y,
			'end_x': self.x + self.w,
			'end_y': self.y + self.h
		}
		return bounds

	def draw(self, canvas):
		if self.type == 'coin':
			self.drawCoin(canvas)
		elif self.type == 'clone':
			self.drawClone(canvas)
		elif self.type == 'invincible':
			self.drawInvincible(canvas)

	def drawCoin(self, canvas):
		pos = getCoinSpritePos(self.sub_type)
		canvas.blit(self.coin_img, (self.x, self.y), (pos['x'], pos['y'], 38, 38))

	def drawClone(self, canvas):
		canvas.blit(self.clone_img, (self.x, self.y))

	def drawInvincible(self, canvas):
		canvas.blit(self.invincible_img, (self.x, self.y))		

collecs = []
count = 2
types = ['coin', 'clone', 'invincible']
sub_types = {
	'coin': [50, 100, 500, 1000],
	'clone': [],
	'invincible': []
}

def getCoinSpritePos(sub_type):
	if sub_type == 50:
		return {'x': 38, 'y': 0}
	elif sub_type == 100:
		return {'x': 76, 'y': 0}
	elif sub_type == 500:
		return {'x': 114, 'y': 0}
	elif sub_type == 1000:
		return {'x': 152, 'y': 0}

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
		collec.sound.play()

		# Determine the type and perform action accordingly
		if collec.type == 'coin':
			sprite.score += collec.sub_type
			print('score + ', collec.sub_type)			
		elif collec.type == 'invincible':
			sprite.invincible = True
			t = Timer(5.0, sprite.undoInvincible)
			t.start()
		elif collec.type == 'clone':
			sprite.createClones(3)
		print(sprite.score)
		
		shift = collecs.pop(0)

		print('caught a collectible')

def reset():
	global collecs
	collecs = []