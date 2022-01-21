#21.01.2022

class Cat:

    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return f"{self.__class__} : {self.__name}"

    def __str__(self):
        return self.__name


cat = Cat("Васька")
print(cat)

class Point:

    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))

p = Point(1, 2, -13)
print("Количество точек", len(p))
print(abs(p))