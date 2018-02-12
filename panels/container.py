from panels.point import Point
from panels.widgets import Widget


class Container(Widget):
    def __init__(self, position: Point, size: Point):
        super(Container, self).__init__()
        self.children = []
        self.position = position
        self.size = size

    def add(self, child):
        self.children.append(child)
        child.parent = self

    def remove(self, child):
        self.children.remove(child)

    def draw(self, origin: Point):
        for child in self.children: child.draw(origin + self.position)

    def click(self, global_point: Point):
        if self.inside(global_point):
            local_point = self.global_to_local(global_point)
            for child in self.children:
                if child.inside(local_point):
                    child.click(local_point)


class RootWindow(Container):
    def __init__(self, surface, position: Point, size: Point):
        super(RootWindow, self).__init__(position, size)
        self.surface = surface
        self.background = (0, 0, 0)

    def draw(self, origin: Point):
        self.surface.fill(self.background)
        super(RootWindow, self).draw(origin)