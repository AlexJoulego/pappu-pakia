import pygame, random
from utils import *
from configs import *

pakias = []
cur_pakia = False

class Pakia(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

		self.types = ['sad', 'happy', 'angry']

		self.img = {
			'sad': load_image('sad_pakia.png')[0],
			'happy': load_image('happy_pakia.png')[0],
			'angry': load_image('angry_pakia.png')[0]
		}

		self.rect = {
			'sad': load_image('sad_pakia.png')[1],
			'happy': load_image('happy_pakia.png')[1],
			'angry': load_image('angry_pakia.png')[1]
		}

		self.sounds = {
			'angry': load_sound('data/jump1.ogg'),
			'sad': load_sound('data/jump2.ogg'),
			'happy': load_sound('data/jump3.ogg')
		}

		self.type = 'angry'
		self.x = 0
		self.y = 0
		self.w = 0
		self.h = 0

		self.vx = 0
		self.vy = 0
		self.ax = 0
		self.ay = 0

		# Cheating on a bit with the physics
		# can't have the same gravity for pappu and pakias
		self.gravity = 0.3
		self.has_stuck = False

	def draw(self, canvas):
		canvas.blit(self.img[self.type], (self.x, self.y))

	def play(self):
		self.sounds[self.type].play()

	def generateRandomPos(self, canvas):
		self.x = canvas.get_rect().width/2 + 200
		self.y = canvas.get_rect().height

	def generateRandomVelocity(self):
		self.vx = -12
		self.vy = random.randint(-18, -10)

	def getBounds(self):
		bounds = {
			'start_x': self.x,
			'start_y': self.y,
			'end_x': self.x + self.w,
			'end_y': self.y + self.h
		}

		return bounds

def createPakias(canvas):
	for emo in ['sad', 'happy', 'angry']:
		pakia = Pakia()
		pakia.w = pakia.rect['sad'].width
		pakia.h = pakia.rect['sad'].height

		pakia.generateRandomPos(canvas)
		pakia.generateRandomVelocity()
		pakia.type = emo
		pakias.append(pakia)
		pakias_lst.append(pakia)

def reflow(canvas):
	global cur_pakia
	if not cur_pakia:
		cur_pakia = pakias[random.randint(0,2)]
	cur_pakia.vy += cur_pakia.gravity

	cur_pakia.x += cur_pakia.vx
	cur_pakia.y += cur_pakia.vy

	# Reset positions
	if (cur_pakia.x + cur_pakia.w < 0 or cur_pakia.y > canvas.get_rect().width):
		cur_pakia.generateRandomPos(canvas)
		cur_pakia.generateRandomVelocity()
		cur_pakia = False

def repaint(canvas):
	if cur_pakia:
		cur_pakia.draw(canvas)

def render(canvas, score):
	if len(pakias) == 0:
		createPakias(canvas)
	if round(score, 2) % 50 == 0 or cur_pakia:
		reflow(canvas)
		repaint(canvas)
	if round(score, 2) % 50 == 0 and cur_pakia:
		cur_pakia.play()

def checkCollision(sprite):
	if cur_pakia:
		sprite_bounds = sprite.getBounds()
		pakia_bounds = cur_pakia.getBounds()

		if slightly_intersect(sprite_bounds, pakia_bounds):
			# Depends upon the pakia's type
			if cur_pakia.type == 'angry':
				# kill
				return True
			elif cur_pakia.type == 'sad':
				# pull
				if cur_pakia.has_stuck:
					sprite.vy += 20
					cur_pakia.y += 20
					cur_pakia.vx = 0
				cur_pakia.has_stuck = True
			elif cur_pakia.type == 'happy':
				# push
				if cur_pakia.vy < 0:
					sprite.vy -= 10
				else:
					sprite.vy += 10

	return False

def resetPakias():
	global pakias, cur_pakia
	pakias = []
	cur_pakia = False
