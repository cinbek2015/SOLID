#19.01.2022

class Fon:
    "пример декоратора property"
    def __init__(self, color, depth):
        self.__color = color
        self.__depth = depth

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @color.deleter
    def color(self):
        del self.__color

f = Fon("red", 24)
print(f.color)
f.color = "blue"
print(f.color)