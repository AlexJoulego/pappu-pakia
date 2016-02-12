import pygame, random
from utils import *
from configs import *

pakias = []

class Pakia(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

		self.types = ['sad', 'happy', 'angry']

		self.sad_img, self.sad_rect = load_image("sad_pakiya.png")
		self.happy_img, self.happy_rect = load_image("happy_pakiya.png")
		self.angry_img, self.angry_rect = load_image("angry_pakiya.png")

		self.type = 'angry'
		self.x = 0
		self.y = 0
		self.w = 0
		self.h = 0

		self.vx = 0
		self.vy = 0
		self.ax = 0
		self.ay = 0

def reflow(canvas):
	pakia = Pakia()
	pakia.w = pakia.sad_rect.width
	pakia.h = pakia.sad_rect.height

	pakia.x = canvas.get_rect().width/2 + 20
	pakia.y = canvas.get_rect().height

	pakia.ax = -5
	pakia.ay = -1

	pakia.vx = -10
	pakia.vy = (-1) * random.randint(10, 14)

	pakias.append(pakia)

def repaint(canvas):
	pakia = pakias[0]

	pakia.vy += gravity

	pakia.x += pakia.vx
	pakia.y += pakia.vy

	canvas.blit(pakia.sad_img, (pakia.x, pakia.y))