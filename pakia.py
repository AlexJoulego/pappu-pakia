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
			'sad': load_image('sad_pakiya.png')[0],
			'happy': load_image('happy_pakiya.png')[0],
			'angry': load_image('angry_pakiya.png')[0]
		}

		self.rect = {
			'sad': load_image('sad_pakiya.png')[1],
			'happy': load_image('happy_pakiya.png')[1],
			'angry': load_image('angry_pakiya.png')[1]
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

	def draw(self, canvas):
		canvas.blit(self.img[self.type], (self.x, self.y))

	def generateRandomPos(self, canvas):
		self.x = canvas.get_rect().width/2 + 200
		self.y = canvas.get_rect().height

	def generateRandomVelocity(self):
		self.vx = -15
		self.vy = random.randint(-25, -16)

def createPakias(canvas):
	for emo in ['sad', 'happy', 'angry']:
		pakia = Pakia()
		pakia.w = pakia.rect['sad'].width
		pakia.h = pakia.rect['sad'].height

		pakia.generateRandomPos(canvas)
		pakia.generateRandomVelocity()
		pakia.type = emo
		pakias.append(pakia)

def reflow(canvas):
	global cur_pakia
	if not cur_pakia:
		cur_pakia = pakias[random.randint(0,2)]
	cur_pakia.vy += gravity

	cur_pakia.x += cur_pakia.vx
	cur_pakia.y += cur_pakia.vy

	# Reset positions
	if (cur_pakia.x + cur_pakia.w < 0):
		cur_pakia.generateRandomPos(canvas)
		cur_pakia.generateRandomVelocity()
		cur_pakia = False

def repaint(canvas):
	if cur_pakia:
		cur_pakia.draw(canvas)

def render(canvas, score=score):
	if len(pakias) == 0:
		createPakias(canvas)
	if round(score, 2) % 10 == 0 or cur_pakia:
		reflow(canvas)
		repaint(canvas)