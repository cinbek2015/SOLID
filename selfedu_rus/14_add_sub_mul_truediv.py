#21.01.2022
class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __add__(self, other):
        if not isinstance(other, Point):
            raise ValueError("нельзя складывать разные типы")
        return (self.__x + other.__x, self.__y + other.__y)

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise ValueError("нельзя вычитать разные типы")
        return (self.__x - other.__x, self.__y - other.__y)

    def __mul__(self, other):
        if not isinstance(other, Point):
            raise ValueError("нельзя умножать разные типы")
        return (self.__x * other.__x, self.__y * other.__y)

    def __truediv__(self, other):
        if not isinstance(other, Point):
            raise ValueError("нельзя умножать разные типы")
        return (int(self.__x / other.__x), int(self.__y / other.__y))

p1 = Point(1, 1)
p2 = Point(2, 2)
print(p1 + p2)
print(p2 - p1)
print(p1 * p2)
print(p1 / p2)