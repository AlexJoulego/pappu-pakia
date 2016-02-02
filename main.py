import pygame
import forks, branches, utils
from pygame.locals import *
from configs import *

pygame.init()

# Set the width and height of the screen
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Pappu Pakia")

# Data structures and globals
fork_count = 6
gravity = 0.2


class Pappu(object):
	def __init__(self):
		self.x = 50
		self.y = 10
		self.w = 50
		self.h = 50

	def draw(self, canvas):
		pygame.Surface.fill(canvas, RED, [self.x, self.y, self.w, self.h])

	def hasReachedBoundary(self, canvas_width, canvas_height):
		ctop = (self.y < 0)
		cbtm = (self.y > canvas_height)
		cleft = (self.x < 0)
		crgt = (self.x > canvas_width)

		if (ctop or cbtm or cleft or crgt):
			return True
		return False
		

pappu = Pappu()

# velocity
vx = 0
vy = 0
v_cap = 4

# acceleration
ax = 0
ay = 0

clouds = pygame.image.load("clouds.png").convert_alpha()
back_trees = pygame.image.load("back_trees.png").convert_alpha()
front_trees = pygame.image.load("front_trees.png").convert_alpha()
ground = pygame.image.load("ground.png").convert_alpha()

cloud_bg_move_speed = 1
cloud_bg_vx = 0
backtree_bg_move_speed = 2
backtree_bg_vx = 0
fronttree_bg_move_speed = 3
fronttree_bg_vx = 0
ground_bg_move_speed = 4
ground_bg_vx = 0


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
	# Game over on reaching any boundary
	if pappu.hasReachedBoundary(SCREEN_WIDTH, SCREEN_HEIGHT):
		done = True

	# Velocity
	if (vy < v_cap and ay + gravity > 0) or (vy > -v_cap and ay + gravity < 0):
		vy += ay
		vy += gravity

	pappu.x += vx
	pappu.y += vy

	# --- Screen-clearing code
	screen.fill(WHITE)
	
	# --- Draw animated BACKGROUND
	utils.fill_gradient(screen, GRADIENT_START, GRADIENT_STOP)
	# Clouds
	if -cloud_bg_vx >= SCREEN_WIDTH:
		cloud_bg_vx = 0
	cloud_bg_vx -= cloud_bg_move_speed

	screen.blit(clouds, (cloud_bg_vx, 0))	
	screen.blit(clouds, (SCREEN_WIDTH + cloud_bg_vx, 0))

	# Black Trees
	if -backtree_bg_vx >= SCREEN_WIDTH:
		backtree_bg_vx = 0
	backtree_bg_vx -= backtree_bg_move_speed

	screen.blit(back_trees, (backtree_bg_vx, 0))
	screen.blit(back_trees, (SCREEN_WIDTH + backtree_bg_vx, 0))

	# Front Trees
	if -fronttree_bg_vx >= SCREEN_WIDTH:
		fronttree_bg_vx = 0
	fronttree_bg_vx -= fronttree_bg_move_speed

	screen.blit(front_trees, (fronttree_bg_vx, 0))
	screen.blit(front_trees, (SCREEN_WIDTH + fronttree_bg_vx, 0))

	# Ground
	if -ground_bg_vx >= SCREEN_WIDTH:
		ground_bg_vx = 0
	ground_bg_vx -= ground_bg_move_speed

	screen.blit(ground, (ground_bg_vx, 0))
	screen.blit(ground, (SCREEN_WIDTH + ground_bg_vx, 0))


	# --- Drawing code
	pappu.draw(screen)
	# Draw forks
	forks.drawForks(screen, 6)
	# Draw branches
	branches.drawBranches(screen, 4)
	
	# --- Update the screen
	pygame.display.flip()

	# --- Limit to 80 frames per second
	clock.tick(80)

pygame.quit()