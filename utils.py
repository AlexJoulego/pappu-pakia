import pygame

def load_image(name):
	try:
		image = pygame.image.load(name)
	except pygame.error as message:
		print('Cannot load image:', name)
		raise SystemExit(message)
	image = image.convert_alpha()
	return image, image.get_rect()

def load_sound(name):
	class NoneSound:
		def play(self):
			pass
	if not pygame.mixer:
		return NoneSound()
	try:
		sound = pygame.mixer.Sound(name)
	except pygame.error as message:
		print('Cannot load sound:', name)
		raise SystemExit(message)
	return sound

def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
	''' Fill a surface with a gradient pattern
	color -> starting color
	gradient -> final color
	rect -> area to fill; default is surface's rect

	Pygame recipe: http://www.pygame.org/wiki/GradientCode
	'''
	if rect is None:
		rect = surface.get_rect()
	x1, x2 = rect.left, rect.right
	y1, y2 = rect.top, rect.bottom
	
	if vertical:
		h = y2 - y1
	else:
		h = x2 - x1

	if forward:
		a, b = color, gradient
	else:
		b, a = color, gradient

	rate = (
		float(b[0]-a[0])/h,
		float(b[1]-a[1])/h,
		float(b[2]-a[2])/h)
	fn_line = pygame.draw.line

	if vertical:
		for line in range(y1, y2):
			color = (
				min(max(a[0] + (rate[0] * (line-y1)), 0), 255),
				min(max(a[1] + (rate[1] * (line-y1)), 0), 255),
				min(max(a[2] + (rate[2] * (line-y1)), 0), 255))
			fn_line(surface, color, (x1, line), (x2, line))
	else:
		for col in range(x1, x2):
			color = (
				min(max(a[0] + (rate[0] * (col-x1)), 0), 255),
				min(max(a[1] + (rate[1] * (col-x1)), 0), 255),
				min(max(a[2] + (rate[2] * (col-x1)), 0), 255))
			fn_line(surface, color, (col, y1), (col, y2))

def blit_alpha(target, source, location, opacity):
	''' Blits image with transparency at lower opacity
	Special thanks to Blake
	http://www.nerdparadise.com/tech/python/pygame/blitopacity
	'''
	x = location[0]
	y = location[1]
	temp = pygame.Surface((source.get_width(), source.get_height())).convert()
	temp.blit(target, (-x, -y))
	temp.blit(source, (0, 0))
	temp.set_alpha(opacity)
	target.blit(temp, location)

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

def intersect(bounds1, bounds2):
	return not (bounds1['end_x'] < bounds2['start_x'] or
		bounds2['end_x'] < bounds1['start_x'] or
		bounds1['end_y'] < bounds2['start_y'] or
		bounds2['end_y'] < bounds1['start_y'])

def slightly_intersect(bounds1, bounds2):
	return (bounds1['end_x'] > bounds2['start_x']+20 and
		bounds2['end_x']-20 > bounds1['start_x'] and
		bounds1['end_y'] > bounds2['start_y']+20 and
		bounds2['end_y']-20 > bounds1['start_y'])