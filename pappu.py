import pygame
import utils
from configs import *

class Pappu(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

		self.x = 50
		self.y = 10
		self.w = 50
		self.h = 50

		self.sprite = []
		self.sprite_num = 288
		self.sprite_w = 48
		self.image = pygame.image.load("pappu.png").convert_alpha()
		self.rect = self.image.get_rect()

		self.fly_frame_count = 0
		self.max_fly_frame_count = 6

		self.flying_up = False

		self.change_per_frame = 10

		for frame in range(0, self.sprite_num, self.sprite_w):
			shift = (self.rect.left + frame, self.rect.top, self.rect.width // 6, self.rect.height)
			for i in range(self.change_per_frame):
				self.sprite.append(self.image.subsurface(shift))
		self.max_fly_frame_count = len(self.sprite)


	def draw(self, canvas):
				
		# print(self.flying_up)
		if self.flying_up:
			self.fly_frame_count += 1
			if self.fly_frame_count == self.max_fly_frame_count:
				self.fly_frame_count = 0
			canvas.blit(self.sprite[self.fly_frame_count], (self.x, self.y))
			# print(self.fly_frame_count)
		else:
			canvas.blit(self.sprite[0], (self.x, self.y))
		self.flying_up = False

	def drawStatic(self, canvas):
		canvas.blit(self.sprite[0], (self.x, self.y))


	def hasReachedBoundary(self, canvas_width, canvas_height):
		ctop = (self.y < 0)
		cbtm = (self.y > canvas_height)
		cleft = (self.x < 0)
		crgt = (self.x > canvas_width)

		if (ctop or cbtm or cleft or crgt):
			return True
		return False