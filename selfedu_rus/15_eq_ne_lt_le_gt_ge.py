#21.01.2022

class Integer:

    def __init__(self, x):
        self.__x = x

    def __eq__(self, other):
        if not isinstance(other, Integer):
            raise ValueError("нельзя сравнивать разные объекты")
        return self.__x == other.__x

    def __gt__(self, other):
        if not isinstance(other, Integer):
            raise ValueError ("нельзя сравнивать разные объекты")
        return self.__x > other.__x

i1 = Integer(500)
i2 = Integer(200)
print(i1 == i2)
print(i1 != i2) #Python сам переворачивает not(i1 == i2)
print(i1 > i2)
print(i1 < i2) #Python сам переворачивает not(i2 > i1)