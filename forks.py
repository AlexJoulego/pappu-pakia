import pygame, random
from utils import *
from configs import *

forks = []
edges = ['top', 'bottom']

# Images
fork_head_img = pygame.image.load('fork_head.png')
fork_head_rect = fork_head_img.get_rect()
dig_img = pygame.image.load('dig.png')
dig_rect = dig_img.get_rect()


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
		

def getRandomForkPos():
	pos = {}

	if len(forks) > 0 and forks[len(forks)-1] is not None:
		pos['x'] = forks[len(forks)-1].x
		pos['x'] += 300	
	else:
		pos['x'] = 200
	return pos

def draw(canvas, count):
	if len(forks) < count:
		for i in range(count - len(forks)+1):
			fork = Fork()			

			# Setting a random edge
			fork.edge = edges[random.randint(0, 1)]

			# Setting the dig position
			if fork.edge == 'bottom':
				dig_rand = random.randint(3, 5)
				fork.dig_x = dig_rect[2] / dig_rand
				fork.dig_y = SCREEN_HEIGHT - dig_rect[3]

				fork.y = 200 + random.randint(0, 100)
				fork.y += fork_head_rect[3]
			if fork.edge == 'top':
				fork.y = 0 - random.randint(0, 100)
				fork.y -= fork_head_rect[3]

			pos = getRandomForkPos()
			fork.x = pos['x']

			fork.w = fork.rect.width
			fork.h = fork.rect.height

			forks.append(fork)

	index = 0	
	for fork in forks:
		if fork.x < 0:
			forks.pop(index)
		fork.x -= ground_bg_move_speed
		index += 1	

		
		canvas.blit(fork.image, (fork.x, fork.y))
		# pygame.draw.rect(canvas, WHITE, (fork.x, fork.y, fork.w, fork.y))

		# Draw fork head
		if fork.edge == 'top':
			fork.head_x = fork.x - fork_head_rect.width/8
			fork.head_y = fork.y + fork.rect.height

			fork.head_w = fork_head_rect.width
			fork.head_h = fork_head_rect.height

			translate = (fork.x, fork.y + fork_head_rect[3])
			# translate = (fork.x - fork_head_rect[2]/8, fork.y + fork.rect[3])
			fork_head_rotated = pygame.transform.rotate(fork_head_img, 180)			
			translate = (fork.head_x, fork.head_y)

			canvas.blit(fork_head_rotated, translate)
			# pygame.draw.rect(canvas, GREEN, (fork_head_rect.x, fork_head_rect.y, fork_head_rect.w, fork_head_rect.w))
		if fork.edge == 'bottom':
			fork.head_x = fork.x - fork_head_rect.width/8
			fork.head_y = fork.y + fork.rect.height

			fork.head_w = fork_head_rect.width
			fork.head_h = fork_head_rect.height
			canvas.blit(dig_img, (fork.x - fork.dig_x, fork.dig_y))
			
			translate = (fork.x - fork_head_rect[2]/5, fork.y - fork_head_rect[3])
			canvas.blit(fork_head_img, translate)

def checkCollision(sprite):	
	# Get pappu's bounds
	sprite_bounds = sprite.getBounds()

	# Get nearest fork handle's bounds
	fork_bounds = forks[0].getHandleBounds()
	# print(sprite_bounds, fork_bounds)
	# print(sprite_bounds['start_x'])

	# Check whether pappu collided with the fork
	# if sprite_bounds['end_x'] > fork_bounds['start_x'] and \
	# 	sprite_bounds['end_x'] < fork_bounds['end_x'] and \
	# 	sprite_bounds['start_y'] > fork_bounds['start_y'] and \
	# 	sprite_bounds['end_y'] < fork_bounds['end_y']:
	# 	return True
	if intersect(sprite_bounds, fork_bounds):
		return True
	return False
