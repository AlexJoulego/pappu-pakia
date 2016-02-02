import pygame

forks = []

class Fork(object):
	def __init__(self):
		self.x = 0
		self.y = 0
		self.w = 0
		self.h = 0
		self.color = (0, 0, 255)

def createRandomForks(canvas, count):
	if len(forks) < count:
		for i in range(count - len(forks)+1):
			fork = Fork()

			if len(forks) > 0 and forks[len(forks)-1] is not None:
				fork.x = forks[len(forks)-1].x
				fork.x += 150
				fork.y = forks[len(forks)-1].y
			else:
				fork.x = i*150
				fork.y = 100

			forks.append(fork)

	index = 0
	for fork in forks:
		if fork.x < 0:
			forks.pop(index)
		fork.x -= 2
		index += 1

		pygame.draw.line(canvas, fork.color, [fork.x, 0], [fork.x, fork.y], 5)

