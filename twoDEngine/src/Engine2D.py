from twoDEngine.src.model.Color import Color
from twoDEngine.src.model.shapes.Circle import Circle
from twoDEngine.src.model.Canvas import Canvas


class Engine2D:
    current_color = Color(0, 0, 0)
    shapes_to_draw_list = []
    current_canvas = Canvas(100, 100)

    def __init__(self):
        print('instance of 2d engine created')

    def draw(self, canvas):
        print('Starting draw all shapes')
        for shape in self.shapes_to_draw_list:
            shape.draw(self, canvas)
        print('All figures are drawn, now clearing canvas')

    def set_color(self, new_color):
        self.current_color = new_color

    def test_null_canvas(self):
        new_colorr = Color(1, 2, 4)
        self.set_color(self, new_colorr)
        circle = Circle(0, 0, 54, self.current_color)
        circle.draw(Canvas)

    def test_positive(self):
        new_colorr = Color(1, 2, 4)
        self.set_color(self, new_colorr)
        circle = Circle(0, 0, 54, self.current_color)
        circle.draw(self.current_canvas)



