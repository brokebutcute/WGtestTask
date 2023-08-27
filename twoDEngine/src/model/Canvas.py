from abc import abstractmethod


class Canvas:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__shapes_list = []
        print(f'Canvas with size {self.__x} : {self.__y} was initialized')

    def clear_canvas(self):
        self.__shapes_list = []
        print('canvas clean')

    def add_shape(self, Shape):
        self.__shapes_list.append(Shape)

    @abstractmethod
    def run(self):
        raise NotImplementedError
