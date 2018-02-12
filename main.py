import pygame, sys

from panels.point import Point
from panels.widgets import CloseButton
from panels.window import Window
from panels.container import Container, RootWindow

pygame.init()

windowSurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello, World!")

win = Window(Point(100, 100), Point(128, 90))
win.add(CloseButton())

root = RootWindow(windowSurface, Point(0, 0), Point(800, 600))
root.background = (0, 230, 230)
root.add(win)
root.draw(Point(0, 0))

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = Point(*event.pos)
            root.click(pos)
            print(event.button)
            root.draw(Point(0, 0))
