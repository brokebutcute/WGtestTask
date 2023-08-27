import math

from twoDEngine.src.model.shapes.Shape import Shape


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3, color):
        super().__init__((x1 + x2 + x3)/3, (y1 + y2 + y3)/3, color)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def draw(self, canvas):
        super().draw(canvas)
        print(f'Drawing Triangle:({self.x_center}, {self.y_center}) with sides: '
              f'{calculate_distance(self.x1, self.y1, self.x2, self.y2)}, '
              f'{calculate_distance(self.x2, self.y2, self.x3, self.y3)}, '
              f' {calculate_distance(self.x3, self.y3, self.x1, self.y1)} '
              f'and color: R = {self.color.R} G = {self.color.G} B = {self.color.B}')

def calculate_distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)