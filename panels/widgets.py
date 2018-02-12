from pygame import Rect
import panels
from panels.point import Point


class Widget:
    def __init__(self):
        self._size = Point(0, 0)
        self.position = Point(0, 0)
        self.parent = None

    def draw(self, origin): pass

    def get_surface(self):
        curr = self
        while not isinstance(curr, panels.container.RootWindow):
            curr = curr.parent
        return curr.surface

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value: Point):
        newsize = self.limit_size(value)
        self._size = newsize

    def limit_size(self, value) -> Point:
        return value

    def inside(self, point: Point) -> bool:
        return not(point.x < self.position.x or
                   point.y < self.position.y or
                   point.x >= self.size.x+self.position.x or
                   point.y >= self.size.y+self.position.y)

    def global_to_local(self, point: Point) -> Point:
        return Point(point.x-self.position.x,
                     point.y-self.position.y)

    def click(self, global_point: Point): pass


class Button(Widget): pass


class CloseButton(Button):
    def __init__(self):
        super(CloseButton, self).__init__()
        self.position = Point(16 - 10, 16 - 10)
        self.size = Point(16, 16)

    def draw(self, origin):
        pos = origin + self.position
        self.get_surface().blit(self.parent.texture, pos.tuple, Rect(96, 0, 16, 16))

    def click(self, point):
        window = self.parent
        window.parent.remove(window)