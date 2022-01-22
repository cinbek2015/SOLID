#22.01.2022

class Vector:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("сравнивать необходимы эдентичные объекты")
        return self.__x == other.__x and self.__y == other.__y

    def __hash__(self):
        return hash((self.__x, self.__y))

v1 = Vector(1, 2)
v2 = Vector(1, 2)
print(v1 == v2)
print(hash(v1), hash(v2), sep="\n")