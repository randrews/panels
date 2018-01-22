from pygame import Rect
from panels.point import Point


class Widget:
    _parent = None
    surface = None

    def draw(self, origin): pass

    @property
    def parent(self): return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent
        self.surface = self._parent.surface


class Button(Widget): pass


class CloseButton(Button):
    position = Point(16 - 9, 16 - 9)

    def draw(self, origin):
        pos = origin + self.position
        self.surface.blit(self.parent.texture, pos.tuple, Rect(96, 0, 18, 18))