import pytest

from twoDEngine.src.model.Color import Color
from twoDEngine.src.model.Canvas import Canvas


class Engine2D:

    def __init__(self, canvas=None, color=None):
        self.current_color = Color(0, 0, 0) if color is None else color
        self.current_canvas = Canvas(100, 100) if canvas is None else canvas
        print('instance of 2d engine created')


    def draw(self, canvas):
        print('Starting draw all shapes')
        for shape in self.current_canvas.get_shapes_list():
            shape.draw(self, canvas)
        print('All figures are drawn, now clearing canvas')
        self.current_canvas.clear_canvas()

    def set_color(self, new_color):
        self.current_color = new_color
