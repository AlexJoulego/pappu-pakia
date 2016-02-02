import pygame, forks
from pygame.locals import *

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen
SCREEN_WIDTH = 740
SCREEN_HEIGHT = 480
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Pappu Pakia")

# Data structures and globals
fork_count = 6
gravity = 0.2

class Pappu(object):
	def __init__(self):
		self.x = 10
		self.y = 10
		self.w = 10
		self.h = 10

	def draw(self, canvas):
		pygame.Surface.fill(canvas, BLACK, [self.x, self.y, self.w, self.h])
		

pappu = Pappu()

# velocity
vx = 0
vy = 0
v_cap = 4

# acceleration
ax = 0
ay = 0


# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# --------------- Main Program Loop ---------------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
			done = True
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				ax = -0.1
			if event.key == K_RIGHT:
				ax = 0.1
			if event.key == K_UP:
				ay = -0.4
			if event.key == K_DOWN:
				ay = 0.1
		if event.type == KEYUP:
			ax = 0
			ay = 0

	# --- Game logic
	# Game over on reaching ground
	if pappu.y >= SCREEN_HEIGHT:
		done = True

	# Velocity
	if (vy < v_cap and ay + gravity > 0) or (vy > -v_cap and ay + gravity < 0):
		vy += ay
		vy += gravity

	pappu.x += vx
	pappu.y += vy

	# --- Screen-clearing code
	screen.fill(WHITE)

	# --- Drawing code
	pappu.draw(screen)
	# Draw forks
	forks.createRandomForks(screen, 6)
	
	# --- Update the screen
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

pygame.quit()