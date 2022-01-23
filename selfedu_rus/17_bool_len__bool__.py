#23.01.2022

class Point:
    """ Принцип работы метода __bool__ если есть ф-ция __len__ она принмиается вначале
        а вот если есть ф-ция __bool__ то она первоочередная"""

    def __init__(self,x, y):
        self.__x = x
        self.__y = y

    def __len__(self):
        print("__len__")
        return self.__x * self.__x + self.__y * self.__y

    def __bool__(self):
        print("__bool__")
        return self.__x == self.__y

p = Point(12, 1)

if p:
    print("объект p возвращает True")
else:
    print("Объект p возращает False")