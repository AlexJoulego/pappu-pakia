import pygame
from utils import *
from configs import *

class Pappu(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()

		self.image, self.rect = load_image("pappu.png")

		self.x = 60
		self.y = 60
		self.w = self.rect.width
		self.h = self.rect.height // 8

		self.sprite = []
		self.sprite_num = self.rect.height
		self.sprite_h = self.rect.height // 8
		

		self.fly_frame_count = 0
		self.max_fly_frame_count = 8

		self.flying_up = False

		self.change_per_frame = 1
		self.rotate_angle = 0

		self.sound = load_sound('flap.ogg')
		self.sound.set_volume(0.2)
		

		for frame in range(0, self.sprite_num, self.sprite_h):
			shift = (self.rect.left, self.rect.top + frame, self.rect.width, self.sprite_h)
			for i in range(self.change_per_frame):
				self.sprite.append(self.image.subsurface(shift))
		self.max_fly_frame_count = len(self.sprite)


	def draw(self, canvas):
				
		# print(self.flying_up)
		rotated = pygame.transform.rotate(self.sprite[self.fly_frame_count], self.rotate_angle)
		if self.flying_up:
			self.sound.play()

			if self.rotate_angle > -15:
				self.rotate_angle -= 1.6			
			self.fly_frame_count += 1
			if self.fly_frame_count == self.max_fly_frame_count:
				self.fly_frame_count = 0			
			canvas.blit(rotated, (self.x, self.y))
			# pygame.draw.rect(canvas, BLUE, (self.x, self.y, self.w, self.h))
			# print(self.fly_frame_count)
		else:
			if self.rotate_angle < 30:
				self.rotate_angle += 1.6
			# canvas.blit(self.sprite[0], (self.x, self.y))
			canvas.blit(rotated, (self.x, self.y))
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