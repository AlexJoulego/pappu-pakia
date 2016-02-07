import pygame, random
from configs import *

forks = []
edges = ['top', 'bottom']

fork_img = pygame.image.load('fork_handle.png')

dig_img = pygame.image.load('dig.png')
dig_rect = dig_img.get_rect()


class Fork(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.w = 0
		self.h = 0
		self.dig_x = 0
		self.dig_y = 0
		self.edge = 'bottom'

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
				print(dig_rect[2], dig_rect[3])

				fork.y = 200 + random.randint(0, 100)
			if fork.edge == 'top':
				fork.y = 0 - random.randint(0, 100)

			pos = getRandomForkPos()
			fork.x = pos['x']

			forks.append(fork)

	index = 0	
	for fork in forks:
		if fork.x < 0:
			forks.pop(index)
		fork.x -= ground_bg_move_speed
		index += 1	

		
		canvas.blit(fork_img, (fork.x, fork.y))
		if fork.edge == 'bottom':
			canvas.blit(dig_img, (fork.x - fork.dig_x, fork.dig_y))