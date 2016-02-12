import pygame
from utils import *
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
		self.image, self.rect = load_image("pappu.png")

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
			# pygame.draw.rect(canvas, BLUE, (self.x, self.y, self.w, self.h))
			# print(self.fly_frame_count)
		else:
			canvas.blit(self.sprite[0], (self.x, self.y))
			# pygame.draw.rect(canvas, BLUE, (self.x, self.y, self.w, self.h))
		self.flying_up = False

	def drawStatic(self, canvas):
		canvas.blit(self.sprite[0], (self.x, self.y))


	def hasReachedBoundary(self, canvas):
		ctop = (self.y < 0)
		cbtm = (self.y > canvas.get_rect().height)
		cleft = (self.x < 0)
		crgt = (self.x > canvas.get_rect().width)

		if (ctop or cbtm or cleft or crgt):
			return True
		return False

	def getBounds(self):
		bounds = {
			'start_x': self.x,
			'start_y': self.y,
			'end_x': self.x + self.w,
			'end_y': self.y + self.h
		}		

		return bounds