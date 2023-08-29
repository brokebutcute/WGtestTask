from abc import ABC


class Shape(ABC):
    def __init__(self, x, y, color):
        self.x_center = x
        self.y_center = y
        self.color = color

    def draw(self, canvas):
        canvas.add_shape(canvas)
