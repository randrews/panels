from math import ceil
import pygame

from panels.container import Container
from panels.point import Point
from pygame import Rect


class Window(Container):
    texture = pygame.image.load('window.png')

    def __init__(self, position: Point, size: Point):
        super(Window, self).__init__(position, size)

    def limit_size(self, value):
        w = ceil(value.x / 32)
        h = ceil(value.y / 32)
        return Point(w*32, h*32)

    def draw(self, origin: Point):
        w, h = self.size.tuple
        surface = self.get_surface()
        for y in range(0, int(h/32)):
            for x in range(0, int(w/32)):
                pos = (origin + self.position + Point(x*32, y*32)).tuple
                if y == 0:
                    if x == 0:
                        surface.blit(self.texture, pos, Rect(0,0,32,32))
                    elif x == w/32-1:
                        surface.blit(self.texture, pos, Rect(64,0,32,32))
                    else:
                        surface.blit(self.texture, pos, Rect(32,0,32,32))
                elif y == h/32-1:
                    if x == 0:
                        surface.blit(self.texture, pos, Rect(0,64,32,32))
                    elif x == w/32-1:
                        surface.blit(self.texture, pos, Rect(64,64,32,32))
                    else:
                        surface.blit(self.texture, pos, Rect(32,64,32,32))
                else:
                    if x == 0:
                        surface.blit(self.texture, pos, Rect(0,32,32,32))
                    elif x == w/32-1:
                        surface.blit(self.texture, pos, Rect(64,32,32,32))
                    else:
                        surface.blit(self.texture, pos, Rect(32,32,32,32))
        super().draw(origin)
