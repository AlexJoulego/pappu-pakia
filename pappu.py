import pygame
from configs import *

class Pappu(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

		self.x = 50
		self.y = 10
		self.w = 50
		self.h = 50

		self.sprite = {}
		self.image = pygame.image.load("pappu.png").convert_alpha()
		self.rect = self.image.get_rect()

	def draw(self, canvas):
		# pygame.Surface.fill(canvas, RED, [self.x, self.y, self.w, self.h])
		canvas.blit(self.image, (self.x, self.y), self.rect)

	def hasReachedBoundary(self, canvas_width, canvas_height):
		ctop = (self.y < 0)
		cbtm = (self.y > canvas_height)
		cleft = (self.x < 0)
		crgt = (self.x > canvas_width)

		if (ctop or cbtm or cleft or crgt):
			return True
		return False