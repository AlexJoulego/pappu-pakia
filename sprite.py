import pygame

# img, rect = load_image("pappu.png")
img = pygame.image.load("pappu_old.png")
img2 = pygame.image.load("pappu.png")
rect = img.get_rect()
rect2 = img2.get_rect()

print("old: ", rect)
print('new: ', rect2)