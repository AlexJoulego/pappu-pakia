import pygame, random
from utils import *
from configs import *

forks = []
edges = ['top', 'bottom']

class Fork(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.x = 0
		self.y = 0
		self.w = 0
		self.h = 0
		self.head_x = 0
		self.head_y = 0
		self.head_w = 0
		self.head_h = 0
		self.dig_x = 0
		self.dig_y = 0
		self.edge = 'bottom'
		self.image, self.rect = load_image('fork_handle.png')
		self.head_image, self.head_rect = load_image('fork_head.png')
		self.dig_image, self.dig_rect = load_image('dig.png')

	def getHandleBounds(self):
		bounds = {
			'start_x': self.x,
			'start_y': self.y,
			'end_x': self.x + self.w,
			'end_y': self.y + self.h
		}		

		return bounds

	def getHeadBounds(self):
		bounds = {
			'start_x': self.head_x,
			'start_y': self.head_y,
			'end_x': self.head_x + self.head_w,
			'end_y': self.head_y + self.head_h
		}
		return bounds
		

def getRandomForkPos(canvas):
	pos = {}

	if len(forks) > 0 and forks[len(forks)-1] is not None:
		pos['x'] = forks[len(forks)-1].x
		pos['x'] += random.randint(300, 600)
		
	else:
		pos['x'] = canvas.get_rect().width/1000 * 800

	for branch in branches_lst:
		if abs(pos['x'] - branch.x) < 300:
			pos['x'] = branch.x + 300
	
	return pos


def draw(canvas, count=forks_cnt):
	if len(forks) < count:
		for i in range(count - len(forks)+1):
			fork = Fork()			

			# Setting a random edge
			fork.edge = edges[random.randint(0, 1)]

			# Setting the dig position
			if fork.edge == 'bottom':
				dig_rand = random.randint(3, 5)
				fork.dig_x = fork.dig_rect[2] / dig_rand
				fork.dig_y = SCREEN_HEIGHT - fork.dig_rect[3]

				fork.y = 200 + random.randint(0, 100)
				fork.y += fork.head_rect[3]
			if fork.edge == 'top':
				fork.y = 0 - random.randint(0, 100)
				fork.y -= fork.head_rect[3]

			pos = getRandomForkPos(canvas)
			fork.x = pos['x']

			fork.w = fork.rect.width
			fork.h = fork.rect.height

			forks.append(fork)
			forks_lst.append(fork)

	index = 0	
	for fork in forks:
		if fork.x < 0:
			forks.pop(index)
			forks_lst.pop(index)
		fork.x -= ground_bg_move_speed
		index += 1	

		
		canvas.blit(fork.image, (fork.x, fork.y))

		# Draw fork head
		if fork.edge == 'top':
			fork.head_x = fork.x - fork.head_rect.width/8
			fork.head_y = fork.y + fork.rect.height

			fork.head_w = fork.head_rect.width
			fork.head_h = fork.head_rect.height

			translate = (fork.x, fork.y + fork.head_rect[3])
			# translate = (fork.x - fork.head_rect[2]/8, fork.y + fork.rect[3])
			fork_head_rotated = pygame.transform.rotate(fork.head_image, 180)			
			translate = (fork.head_x, fork.head_y)

			canvas.blit(fork_head_rotated, translate)
			# pygame.draw.rect(canvas, GREEN, (fork.head_rect.x, fork.head_rect.y, fork.head_rect.w, fork.head_rect.w))
		if fork.edge == 'bottom':
			fork.head_x = fork.x - fork.head_rect.width/8
			fork.head_y = fork.y + fork.rect.height

			fork.head_w = fork.head_rect.width
			fork.head_h = fork.head_rect.height
			canvas.blit(fork.dig_image, (fork.x - fork.dig_x, fork.dig_y))
			
			translate = (fork.x - fork.head_rect[2]/5, fork.y - fork.head_rect[3])
			canvas.blit(fork.head_image, translate)

def checkCollision(sprite):	
	# Get pappu's bounds
	sprite_bounds = sprite.getBounds()

	# Get nearest fork handle's bounds
	fork_bounds = forks[0].getHandleBounds()
	fork_head_bounds = forks[0].getHeadBounds()
	
	if intersect(sprite_bounds, fork_bounds) or slightly_intersect(sprite_bounds, fork_head_bounds):
		return True
	return False

def resetForks():
	global forks
	forks = []
