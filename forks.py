import pygame

class Fork(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.w = 0
		self.h = 0
		self.color = (0, 0, 0)

def createRandomForks(canvas, count):
	forks = []
	for i in range(count+1):
		fork = Fork()
		fork.x = i*100
		fork.y = i*100

		forks.append(fork)

	for fork in forks:
		pygame.draw.line(canvas, fork.color, [fork.x, 0], [fork.x, fork.y], 5)

