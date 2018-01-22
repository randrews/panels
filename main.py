import pygame, sys

from panels.point import Point
from panels.widgets import CloseButton
from panels.window import Window

pygame.init()

windowSurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello, World!")

windowSurface.fill((0, 230, 230))
win = Window(windowSurface)
win.position = Point(100, 100)
win.size = (128, 96)
win.add(CloseButton())
win.draw()

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
