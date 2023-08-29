from twoDEngine.src.model.shapes.Shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y, length, wight, color):
        super().__init__(x, y, color)
        self.lenght = length
        self.wight = wight

    def draw(self, canvas):
        super().draw(canvas)
        print(f'Drawing Rectangle:({self.x_center}, {self.y_center}) with length =  {self.lenght} '
              f'wight = {self.wight}'
              f'and color: R = {self.color.R} G = {self.color.G} B = {self.color.B}')
