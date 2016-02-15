import pygame, sys
import forks, branches, pakia, collectibles
from pygame.locals import *
from pappu import Pappu
from configs import *
from utils import *

if not pygame.font:
	print("Warning, fonts disabled")
if not pygame.mixer:
	print("Warning, sound disabled")

pygame.init()

# Set the width and height of the screen
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
window = pygame.display.set_mode(screen_size)
screen = pygame.display.get_surface()

pygame.display.set_caption("Pappu Pakia")

# Data structures and globals

clouds, clouds_rect = load_image("clouds.png")
back_trees, back_trees_rect = load_image("back_trees.png")
front_trees, front_trees_rect = load_image("front_trees.png")
ground, ground_rect = load_image("ground.png")
grass, grass_rect = load_image("grass.png")
log, log_rect = load_image("log.png")
dig, dig_rect = load_image("dig.png")


stand, stand_rect = load_image("stand.png")
stand_pos = (SCREEN_WIDTH - 150, 85)

plank, plank_rect = load_image("plank_top.png")
plank_pos = (SCREEN_WIDTH - 220, 150)
plank_x, plank_y = plank_pos
plank_btm = (plank_x + 160, plank_y + 150)
plank_rect = (plank_x, plank_y, plank_btm[0], plank_btm[1])

dig_pos = (SCREEN_WIDTH - 150, 450)

controls, controls_rect = load_image("controls.png")
controls_pos = (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.6)

# Font
pygame.font.init()
fontObj = pygame.font.Font(font_path, font_size)
creditsFont = pygame.font.Font(font_path, credits_size)
credits2Font = pygame.font.Font(font_path, credits2_size)
startFont = pygame.font.Font(font_path, start_size)

# Score board
scoreFont = pygame.font.Font(font_path, score_size)
score_pos = (SCREEN_WIDTH - 100, 10)

opacity = 0

# Music
pygame.mixer.music.load('data/pappu-pakia2.3.ogg')
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


pappu = Pappu()
if not started:
	pappu.x = 33
	pappu.y = 284
	# pappu.w = 48
	# pappu.h = pappu.rect.width

collided = False


title = fontObj.render("Pappu Pakia", 0, TITLE)
title_pos = (SCREEN_WIDTH // 3 - 30, 20)
credits = creditsFont.render("by Kushagra and Rishabha", 0, CREDITS)
credits_pos = (SCREEN_WIDTH // 3 - 70, 80)
credits2 = credits2Font.render("implemented in Python by Alexander Joulego", 0, MY_CREDITS)
credits2_pos = (SCREEN_WIDTH // 3 - 130, 120)

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
while True:
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
				pappu.ay = -pappu.v_vel
				flying_up = True
			if event.key == K_DOWN:
				pappu.ay = 0.4
		if event.type == KEYUP:
			pappu.ax = 0
			pappu.ay = 0
			flying_up = False

		# Game play on mouse clicks, too!
		if event.type == MOUSEBUTTONDOWN and start_btn_click == 0:
			forks.resetForks()
			branches.resetBranches()
			pakia.resetPakias()
			collectibles.reset()
			pappu.resetClones()
			mouse = pygame.mouse.get_pos()
			if pressed(mouse, plank_rect):
				started = True
				collided = False
				if game_over:
					pappu.score = 0
				start_btn_click += 1					
			
		
		elif event.type == MOUSEBUTTONDOWN and start_btn_click == 1:
			if event.button == 1:
				game_over = False
				pappu.ay = -pappu.v_vel
				flying_up = True
			if event.button == 3:
				pappu.ay = 0.4

		if event.type == MOUSEBUTTONUP:
			pappu.ax = 0
			pappu.ay = 0
			flying_up = False

		if event.type == MOUSEMOTION:
			mouse = pygame.mouse.get_pos()
			if not started and pressed(mouse, plank_rect):
				start_color = WHITE
			else:
				start_color = START


	# --- Game logic
	if collided:
		first_start = False
		started = False
		game_over = True
		start_btn_click = 0
		pappu.x = 33
		pappu.y = 284
		pappu.undoInvincible()
	# Game over on reaching any boundary
	if pappu.hasReachedBoundary(screen):
		collided = True
	
	if started and not game_over:
		# Velocity
		if (pappu.vy < pappu.v_cap and pappu.ay + pappu.gravity > 0) or (pappu.vy > -pappu.v_cap and pappu.ay + pappu.gravity < 0):
			pappu.vy += pappu.ay
			pappu.vy += pappu.gravity

		pappu.x += pappu.vx
		pappu.y += pappu.vy

		if pappu.vy > pappu.v_cap:
			pappu.vy = pappu.v_cap


	# --- Draw animated BACKGROUND
	background = fill_gradient(screen, GRADIENT_START, GRADIENT_STOP)	
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
		backtree_bg_vx -= backtree_bg_move_speed * common_bg_speed

	screen.blit(back_trees, (backtree_bg_vx, 0))
	screen.blit(back_trees, (SCREEN_WIDTH + backtree_bg_vx, 0))

	# Front Trees
	if -fronttree_bg_vx >= SCREEN_WIDTH:
		fronttree_bg_vx = 0
	if started and not game_over:
		fronttree_bg_vx -= fronttree_bg_move_speed * common_bg_speed

	screen.blit(front_trees, (fronttree_bg_vx, 0))
	screen.blit(front_trees, (SCREEN_WIDTH + fronttree_bg_vx, 0))

	# Ground
	if -ground_bg_vx >= SCREEN_WIDTH:
		ground_bg_vx = 0
	if started and not game_over:
		ground_bg_vx -= ground_bg_move_speed * common_bg_speed

	screen.blit(ground, (ground_bg_vx, 0))
	screen.blit(ground, (SCREEN_WIDTH + ground_bg_vx, 0))

	# Grass
	if -grass_bg_vs >= SCREEN_WIDTH:
		grass_bg_vs = 0
	if started and not game_over:
		grass_bg_vs -= grass_bg_move_speed * common_bg_speed


	screen.blit(grass, (grass_bg_vs, 0))
	screen.blit(grass, (SCREEN_WIDTH + grass_bg_vs, 0))


	# --- Drawing code
	if not started:
		intro()
	else:
		intro(1)
	

	score_text = scoreFont.render(str(int(pappu.score)), 0, SCORE)
	screen.blit(score_text, score_pos)

	# Draw the stuff
	if started and not game_over:
		# Draw forks
		forks.draw(screen)
		# Draw branches
		branches.draw(screen)
		# Check collisions with pappu
		if not pappu.invincible:
			if forks.checkCollision(pappu):
				collided = True
			if branches.checkCollision(pappu):
				collided = True

		# Send over pakias
		if pappu.score > 199:
			pakia.render(screen, pappu.score)
		if not pappu.invincible:
			if pakia.checkCollision(pappu):
				collided = True

		# Draw collectibles
		collectibles.draw(screen)
		collectibles.checkCollision(pappu)
		# Draw clones
		pappu.drawClones(screen)
		pappu.checkCloneCollision()


	if flying_up:
		pappu.flying_up = True
		# pappu.sound.play()
	if started and not game_over:
		pappu.draw(screen)
	elif started and game_over:
		flying_up = True
		pappu.draw(screen)
	else:
		pappu.drawStatic(screen)
	

	screen.blit(log, (log_x, SCREEN_HEIGHT - 164))
	if started and not game_over:
		log_x -= grass_bg_move_speed * common_bg_speed
	else:
		log_x = 30	

	# Update score
	if started and not game_over:
		pappu.score += 0.4

	
	# --- Update the screen
	pygame.display.update()

	# --- Limit a number of frames per second
	clock.tick(game_speed)
