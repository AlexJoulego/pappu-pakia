import pygame

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

def sprite_sheet(size, file, pos=(0,0)):
	len_sprt_x, len_sprt_y = size
	sprt_rect_x, sprt_rect_y = pos

	# sheet = pygame.image.load(file).convert_alpha()
	sheet = file
	sheet_rect = sheet.get_rect()
	sprites = []
	print(sheet_rect.height, sheet_rect.width)

	for i in range(0, sheet_rect.height-len_sprt_y, size[1]):
		print("row")
		for i in range(0, sheet_rect.width-len_sprt_x, size[0]):
			print("column")
			sheet.set_clip(pygame.Rect(sprt_rect_x, sprt_rect_y, len_sprt_x, len_sprt_y))
			sprite = sheet.subsurface(sheet.get_clip())
			sprites.append(sprite)
			sprt_rect_x += len_sprt_x

		sprt_rect_y += len_sprt_y
		sprt_rect_x = 0

	print(sprites)
	return sprites