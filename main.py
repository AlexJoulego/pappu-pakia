import pygame, sys
import forks, branches, utils
from pygame.locals import *
from pappu import Pappu
from configs import *
from utils import *

pygame.init()

# Set the width and height of the screen
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
window = pygame.display.set_mode(screen_size)
screen = pygame.display.get_surface()

pygame.display.set_caption("Pappu Pakia")

# Data structures and globals


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
grass = pygame.image.load("grass.png").convert_alpha()
log = pygame.image.load("log.png").convert_alpha()
log_x = 30
dig = pygame.image.load("dig.png").convert_alpha()



stand = pygame.image.load("stand.png").convert_alpha()
stand_rect = stand.get_rect()
stand_pos = (SCREEN_WIDTH - 150, 85)

plank = pygame.image.load("plank_top.png").convert_alpha()
plank_pos = (SCREEN_WIDTH - 220, 150)
plank_x, plank_y = plank_pos
plank_btm = (plank_x + 160, plank_y + 150)
plank_rect = (plank_x, plank_y, plank_btm[0], plank_btm[1])

dig_pos = (SCREEN_WIDTH - 150, 450)

controls = pygame.image.load("controls.png").convert_alpha()
controls_pos = (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.6)

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

opacity = 0


# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

started = False
first_start = True
game_over = True
start_btn_click = 0

pappu = Pappu()
if not started:
	pappu.x = 38
	pappu.y = 284

title = fontObj.render("Pappu Pakia", 0, TITLE)
title_pos = (SCREEN_WIDTH // 3 - 30, 20)
credits = creditsFont.render("by Kushagra and Rishabha", 0, CREDITS)
credits_pos = (SCREEN_WIDTH // 3 - 70, 80)
credits2 = credits2Font.render("implemented in Python by Alexander Joulego", 0, MY_CREDITS)
credits2_pos = (SCREEN_WIDTH // 3 - 130, 120)

# start_button = startFont.render(start_text, 0, start_color)
start_pos = (SCREEN_WIDTH - 173, 160)


def intro(fade=0):
	global opacity


	if fade == 1:
		opacity -= 10		
	else:
		opacity += 5
	
	blit_alpha(screen, title, title_pos, opacity)	
	blit_alpha(screen, credits, credits_pos, opacity)	
	blit_alpha(screen, credits2, credits2_pos, opacity)

	blit_alpha(screen, dig, dig_pos, opacity)	
	blit_alpha(screen, stand, stand_pos, opacity)	
	blit_alpha(screen, plank, plank_pos, opacity)
	if first_start:
		start_text = "Start"
	else:
		start_text = "Restart"
	
	start_button = startFont.render(start_text, 0, start_color)
	blit_alpha(screen, start_button, start_pos, opacity)
	
	blit_alpha(screen, controls, controls_pos, opacity)

	if opacity >= 255:
		opacity = 255		
	elif opacity <= 0:
		opacity = 0
	

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
			# if event.key == K_LEFT:
			# 	ax = -0.1
			# if event.key == K_RIGHT:
			# 	ax = 0.1
			if event.key == K_UP:
				if game_over:
					game_over = False
				ay = -v_vel
				flying_up = True
			if event.key == K_DOWN:
				ay = 0.4
		if event.type == KEYUP:
			ax = 0
			ay = 0
			flying_up = False

		# Game play on mouse clicks, too!
		if event.type == MOUSEBUTTONDOWN and start_btn_click == 0:
			mouse = pygame.mouse.get_pos()
			if pressed(mouse, plank_rect):
				started = True
				if game_over:
					score = 0
				start_btn_click += 1					
			
		
		elif event.type == MOUSEBUTTONDOWN and start_btn_click == 1:
			if event.button == 1:
				game_over = False
				ay = -v_vel
				flying_up = True
			if event.button == 3:
				ay = 0.4

		if event.type == MOUSEBUTTONUP:
			ax = 0
			ay = 0
			flying_up = False

		if event.type == MOUSEMOTION:
			mouse = pygame.mouse.get_pos()
			if not started and pressed(mouse, plank_rect):
				start_color = WHITE
			else:
				start_color = START


	# --- Game logic
	# Game over on reaching any boundary
	if pappu.hasReachedBoundary(SCREEN_WIDTH, SCREEN_HEIGHT):
		# done = True
		first_start = False
		started = False
		game_over = True
		start_btn_click = 0
		pappu.x = 38
		pappu.y = 284
	
	if started and not game_over:
		# game_over = False
		# Velocity
		if (vy < v_cap and ay + gravity > 0) or (vy > -v_cap and ay + gravity < 0):
			vy += ay
			vy += gravity

		pappu.x += vx
		pappu.y += vy

	# --- Screen-clearing code
	screen.fill(WHITE)
	
	# --- Draw animated BACKGROUND
	background = fill_gradient(screen, GRADIENT_START, GRADIENT_STOP)	
	# print(background)
	# Clouds
	if -cloud_bg_vx >= SCREEN_WIDTH:
		cloud_bg_vx = 0
	cloud_bg_vx -= cloud_bg_move_speed
	if started and not game_over:		
		opacity = 0

	screen.blit(clouds, (cloud_bg_vx, 0))	
	screen.blit(clouds, (SCREEN_WIDTH + cloud_bg_vx, 0))

	# Black Trees
	if -backtree_bg_vx >= SCREEN_WIDTH:
		backtree_bg_vx = 0
	if started and not game_over:
		backtree_bg_vx -= backtree_bg_move_speed

	screen.blit(back_trees, (backtree_bg_vx, 0))
	screen.blit(back_trees, (SCREEN_WIDTH + backtree_bg_vx, 0))

	# Front Trees
	if -fronttree_bg_vx >= SCREEN_WIDTH:
		fronttree_bg_vx = 0
	if started and not game_over:
		fronttree_bg_vx -= fronttree_bg_move_speed

	screen.blit(front_trees, (fronttree_bg_vx, 0))
	screen.blit(front_trees, (SCREEN_WIDTH + fronttree_bg_vx, 0))

	# Ground
	if -ground_bg_vx >= SCREEN_WIDTH:
		ground_bg_vx = 0
	if started and not game_over:
		ground_bg_vx -= ground_bg_move_speed

	screen.blit(ground, (ground_bg_vx, 0))
	screen.blit(ground, (SCREEN_WIDTH + ground_bg_vx, 0))

	# Grass
	if -grass_bg_vs >= SCREEN_WIDTH:
		grass_bg_vs = 0
	if started and not game_over:
		grass_bg_vs -= grass_bg_move_speed


	screen.blit(grass, (grass_bg_vs, 0))
	screen.blit(grass, (SCREEN_WIDTH + grass_bg_vs, 0))


	# --- Drawing code
	if not started:
		intro()
	else:
		intro(1)
	

	score_text = scoreFont.render(str(int(score)), 0, SCORE)
	screen.blit(score_text, score_pos)	
	

	if started and not game_over:
		# Draw forks
		forks.draw(screen, 6)
		# Draw branches
		branches.draw(screen, 4)

	if flying_up:
		pappu.flying_up = True
	if started and not game_over:
		pappu.draw(screen)
	else:
		pappu.drawStatic(screen)
	
	

	screen.blit(log, (log_x, SCREEN_HEIGHT - 164))
	if started and not game_over:
		log_x -= grass_bg_move_speed
	else:
		log_x = 30	

	# Update score
	if started and not game_over:
		score += 0.2

	
	# --- Update the screen
	pygame.display.update()

	# --- Limit to 80 frames per second
	clock.tick(80)
