import pygame
from configs import *

class Pappu(object):
	def __init__(self):
		self.x = 50
		self.y = 10
		self.w = 50
		self.h = 50

	def draw(self, canvas):
		pygame.Surface.fill(canvas, RED, [self.x, self.y, self.w, self.h])

	def hasReachedBoundary(self, canvas_width, canvas_height):
		ctop = (self.y < 0)
		cbtm = (self.y > canvas_height)
		cleft = (self.x < 0)
		crgt = (self.x > canvas_width)

		if (ctop or cbtm or cleft or crgt):
			return True
		return False