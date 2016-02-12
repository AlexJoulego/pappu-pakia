SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TRANSPARENT = (255, 255, 255, 10)

TITLE = (148, 84, 48)
CREDITS = WHITE
MY_CREDITS = (255, 238, 170)
SCORE = BLACK
START = (200, 200, 200)
STARTED = WHITE

start_color = START

GRADIENT_START = (6, 196, 244)
GRADIENT_STOP = (123, 212, 246)
GRADIENT_MID = (64, 204, 244, 0)

# Font
font_path = "./fonts/happy_sans-webfont.ttf"
font_size = 63
credits_size = 36
credits2_size = 28
score_size = 30
start_size = 40

fork_count = 6

# velocity
vx = 0
vy = 0

# acceleration
ax = 0
ay = 0

gravity = 0.5
v_cap = 7
v_vel = 1.0

score = 0

cloud_bg_move_speed = 2
cloud_bg_vx = 0
backtree_bg_move_speed = 3
backtree_bg_vx = 0
fronttree_bg_move_speed = 4
fronttree_bg_vx = 0
ground_bg_move_speed = 6
ground_bg_vx = 0
grass_bg_move_speed = 6
grass_bg_vs = 0

started = False
first_start = True
game_over = True
start_btn_click = 0

forks_cnt = 6
branches_cnt = 4