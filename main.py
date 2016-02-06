import pygame, sys
import forks, branches, utils
from pygame.locals import *
from pappu import Pappu
from configs import *

pygame.init()

# Set the width and height of the screen
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Pappu Pakia")

# Data structures and globals


pappu = Pappu()


# velocity
vx = 0
vy = 0
v_cap = 4

# acceleration
ax = 0
ay = 0

# flying up?
flying_up = False

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

stand = pygame.image.load("stand.png").convert_alpha()
stand_rect = stand.get_rect()
stand_pos = (SCREEN_WIDTH - 150, 85)

plank = pygame.image.load("plank_top.png").convert_alpha()
plank_pos = (SCREEN_WIDTH - 220, 150)
plank_x, plank_y = plank_pos
plank_btm = (plank_x + 160, plank_y + 150)
plank_rect = (plank_x, plank_y, plank_btm[0], plank_btm[1])
print(plank_x, plank_y, plank_btm)

# button = Button()
# button.setCoords(SCREEN_WIDTH - 220, 150)


# Font
pygame.font.init()
fontObj = pygame.font.Font(font_path, font_size)
creditsFont = pygame.font.Font(font_path, credits_size)
credits2Font = pygame.font.Font(font_path, credits2_size)
startFont = pygame.font.Font(font_path, start_size)

# Score board
score = 0
scoreFont = pygame.font.Font(font_path, score_size)
score_pos = (SCREEN_WIDTH - 100, 10)

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

started = False

def pressed(mouse, rect):
	if mouse[0] > rect[0]:
		if mouse[1] > rect[1]:
			if mouse[0] < rect[2]:
				if mouse[1] < rect[3]:
					return True
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False

def intro():
	title = fontObj.render("Pappu Pakia", 0, TITLE)
	title_pos = (SCREEN_WIDTH // 3, 20)
	screen.blit(title, title_pos)

	credits = creditsFont.render("by Kushagra and Rishabha", 0, CREDITS)
	credits_pos = (SCREEN_WIDTH // 3 - 70, 80)
	screen.blit(credits, credits_pos)

	credits2 = credits2Font.render("implemented in Python by Alexander Joulego", 0, MY_CREDITS)
	credits2_pos = (SCREEN_WIDTH // 3 - 130, 120)
	screen.blit(credits2, credits2_pos)

	screen.blit(stand, stand_pos)
	screen.blit(plank, plank_pos)	

	start_button = startFont.render("Start", 0, start_color)
	start_pos = (SCREEN_WIDTH - 173, 160)
	screen.blit(start_button, start_pos)
	

def terminate():
	pygame.quit()
	sys.exit()

# --------------- Main Program Loop ---------------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
			terminate()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				ax = -0.1
			if event.key == K_RIGHT:
				ax = 0.1
			if event.key == K_UP:
				ay = -0.4
				flying_up = True
			if event.key == K_DOWN:
				ay = 0.1
		if event.type == KEYUP:
			ax = 0
			ay = 0
			flying_up = False

		# Game play on mouse clicks, too!
		if event.type == MOUSEBUTTONDOWN:
			mouse = pygame.mouse.get_pos()
			if pressed(mouse, plank_rect):
				started = True
			
			ay = -0.4
			flying_up = True
		if event.type == MOUSEBUTTONUP:
			ax = 0
			ay = 0
			flying_up = False

		if event.type == MOUSEMOTION:
			mouse = pygame.mouse.get_pos()
			if pressed(mouse, plank_rect):
				start_color = WHITE
			else:
				start_color = START

	# --- Game logic
	# Game over on reaching any boundary
	if pappu.hasReachedBoundary(SCREEN_WIDTH, SCREEN_HEIGHT):
		# done = True
		pass

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
	if not started:
		intro()

	score_text = scoreFont.render(str(score), 0, SCORE)
	screen.blit(score_text, score_pos)
	score += 1
	

	if flying_up:
		pappu.flying_up = True
	pappu.draw(screen)
	# Draw forks
	# forks.drawForks(screen, 6)
	# Draw branches
	# branches.drawBranches(screen, 4)

	
	
	# --- Update the screen
	pygame.display.flip()

	# --- Limit to 80 frames per second
	clock.tick(80)
