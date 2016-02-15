import pygame, random
import branches, forks, pakia
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

		# velocity
		self.vx = 0
		self.vy = 0

		# acceleration
		self.ax = 0
		self.ay = 0

		self.gravity = 0.7
		self.v_cap = 7.5
		self.v_vel = 1.7

		self.invincible = False
		self.clones = []

		self.score = 0

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
		opacity = 255
		rotated = pygame.transform.rotate(self.sprite[self.fly_frame_count], self.rotate_angle)
		if self.invincible:
			opacity = 255 * 0.4
		if self.flying_up:
			# self.sound.play()

			if self.rotate_angle > -15:
				self.rotate_angle -= 1.6			
			self.fly_frame_count += 1
			if self.fly_frame_count == self.max_fly_frame_count:
				self.fly_frame_count = 0			
			blit_alpha(canvas, rotated, (self.x, self.y), opacity)
		else:
			if self.rotate_angle < 30:
				self.rotate_angle += 1.6
			blit_alpha(canvas, rotated, (self.x, self.y), opacity)
		self.flying_up = False

	def drawStatic(self, canvas):
		canvas.blit(self.sprite[0], (self.x, self.y))

	def undoInvincible(self):
		self.invincible = False


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

	def createClones(self, count):
		for i in range(count):
			pappu_clone = Pappu()
			pappu_clone.x = self.x
			pappu_clone.y = self.y
			self.clones.append(pappu_clone)

	def drawClones(self, canvas):
		index = 0
		for clone in self.clones:
			if clone.x > canvas.get_rect().width or clone.y < 0 or clone.y > canvas.get_rect().height:
				self.clones.pop(index)
			index += 1

			clone.x += random.randint(5, 10)
			clone.y += random.randint(-20, 20)

			clone.draw(canvas)

	def checkCloneCollision(self):
		branchs = branches.branches
		frks = forks.forks
		pks = pakia.pakias

		index = 0
		for branch in branchs:
			branch_bound = branch.getBounds()
			for clone in self.clones:
				clone_bound = clone.getBounds()
				if intersect(branch_bound, clone_bound):
					if index < len(branchs):
						branchs.pop(index)
						branches_lst.pop(index)
			index += 1

		index = 0
		for fork in frks:
			fork_head_bound = fork.getHeadBounds()
			fork_handle_bound = fork.getHandleBounds()

			for clone in self.clones:
				clone_bound = clone.getBounds()
				if intersect(fork_head_bound, clone_bound):
					if index < len(frks):
						frks.pop(index)
						forks_lst.pop(index)
				if intersect(fork_handle_bound, clone_bound):					
					if index < len(frks):
						frks.pop(index)
						forks_lst.pop(index)
				index += 1

			index = 0
			for paki in pks:
				pakia_bound = paki.getBounds()
				for clone in self.clones:
					clone_bound = clone.getBounds()
					if intersect(pakia_bound, clone_bound):
						pakia.cur_pakia = False
				index += 1

	def resetClones(self):
		self.clones = []