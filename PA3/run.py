import pygame
import sys
import random

import scene
from scene import Ground
# settings
FPS = 60
TITLE = 'Chrome Dino'
BACKGROUND_COLOR = (235, 235, 235)
SCREENSIZE = (700, 300)
IMAGE_PATHS = {
    'ground': 'resources/images/G.png',
    'cloud': 'resources/images/C.png',
}
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)

image_ground = pygame.image.load(IMAGE_PATHS['ground'])
ground = Ground(image_ground, (0, SCREENSIZE[1]))

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)




    ground.update()

    ground.draw(screen)
    pygame.display.update()
    clock.tick(FPS)