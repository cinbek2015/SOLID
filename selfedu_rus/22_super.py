#24.01.2022

class Geom:
    "класс демонстрирующий работу  super()"
    def __init__(self, x, y):
        print("__init__ Geom")
        self._x = x
        self._y = y
        self._fill = 0

class Line(Geom):

    def __init__(self, x, y, fill=None):
        super().__init__(x, y)
        print("__init__ Line")
        self._fill = fill

l = Line(12, 24, 666)
print(l.__dict__)
