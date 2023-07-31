import pygame
import sys

window_size = (1280, 720)

pygame.init()

window = pygame.display.set_mode(window_size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
