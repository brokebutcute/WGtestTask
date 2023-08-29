from twoDEngine.src.model.shapes.Shape import Shape


class Circle(Shape):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self, canvas):
        super().draw(canvas)
        print(f'Drawing Circle:({self.x_center}, {self.y_center}) with radius {self.radius} '
              f'and color: R = {self.color.R} G = {self.color.G} B = {self.color.B}')
