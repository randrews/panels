from math import ceil
import pygame
from panels.point import Point
from pygame import Rect


class Window:
    texture = pygame.image.load('window.png')

    def __init__(self, surface):
        self.surface = surface
        self._size = (64, 64)
        self.position = Point(0, 0)
        self.children = []

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        w, h = value
        w = ceil(w / 32)
        h = ceil(h / 32)
        self._size = Point(w*32, h*32)

    def add(self, child):
        self.children.append(child)
        child.parent = self

    def draw(self):
        w, h = self.size.tuple
        for y in range(0, int(h/32)):
            for x in range(0, int(w/32)):
                pos = (self.position + Point(x*32, y*32)).tuple
                if y == 0:
                    if x == 0:
                        self.surface.blit(self.texture, pos, Rect(0,0,32,32))
                    elif x == w/32-1:
                        self.surface.blit(self.texture, pos, Rect(64,0,32,32))
                    else:
                        self.surface.blit(self.texture, pos, Rect(32,0,32,32))
                elif y == h/32-1:
                    if x == 0:
                        self.surface.blit(self.texture, pos, Rect(0,64,32,32))
                    elif x == w/32-1:
                        self.surface.blit(self.texture, pos, Rect(64,64,32,32))
                    else:
                        self.surface.blit(self.texture, pos, Rect(32,64,32,32))
                else:
                    if x == 0:
                        self.surface.blit(self.texture, pos, Rect(0,32,32,32))
                    elif x == w/32-1:
                        self.surface.blit(self.texture, pos, Rect(64,32,32,32))
                    else:
                        self.surface.blit(self.texture, pos, Rect(32,32,32,32))

        for child in self.children: child.draw(self.position)
