from abc import abstractmethod
from twoDEngine.src.model.Color import Color


class Canvas:

    def __init__(self, x, y, color=None):
        self.__x = x
        self.__y = y
        self.__shapes_list = []
        self.__color = Color(255, 255, 255) if color is None else color
        print(f'\nCanvas with size {self.__x} : {self.__y} was initialized')

    def clear_canvas(self):
        self.__shapes_list = []
        print('canvas clean')

    def get_size(self):
        return self.__x, self.__y

    def get_color(self):
        return self.__color

    def add_shape(self, Shape):
        self.__shapes_list.append(Shape)

    def get_shapes_list(self):
        return self.__shapes_list

    @abstractmethod
    def run(self):
        raise NotImplementedError
