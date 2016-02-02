import pygame, random
from configs import *

forks = []
edges = ['top', 'bottom']

class Fork(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.w = 0
		self.h = 0
		self.edge = 'bottom'
		self.color = BLUE

def getRandomForkPos():
	pos = {}

	if len(forks) > 0 and forks[len(forks)-1] is not None:
		pos['x'] = forks[len(forks)-1].x
		pos['x'] += 200
		pos['y'] = forks[len(forks)-1].y
	else:
		pos['x'] = 200
		pos['y'] = 200
	return pos

def drawForks(canvas, count):
	if len(forks) < count:
		for i in range(count - len(forks)+1):
			fork = Fork()

			pos = getRandomForkPos()

			fork.x = pos['x']
			fork.y = pos['y']

			# Setting a random edge
			fork.edge = edges[random.randint(0, 1)]

			forks.append(fork)

	index = 0
	for fork in forks:
		if fork.x < 0:
			forks.pop(index)
		fork.x -= 3
		index += 1

		line_start = [fork.x, fork.y]
		if fork.edge == 'top':
			line_end = [fork.x, 0]
		elif fork.edge == 'bottom':
			line_end = [fork.x, SCREEN_HEIGHT]
		pygame.draw.line(canvas, fork.color, line_start, line_end, 5)

