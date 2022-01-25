#25.01.2022
#демонстарция использования __slots__
import timeit

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0

class Point2D:
    __slots__ = ('x', 'y')
    z = 500

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0

p1 = Point(1, 2)
p2 = Point2D(1, 2)
print("p1.__dict__ = ", p1.__dict__)
# print(p2.__dict__) отсутствует
#подсчет памяти
print("p1 объем памяти = ", p1.__sizeof__() + p1.__dict__.__sizeof__(), " байт")
print("p2 объем памяти = ", p2.__sizeof__(), " байт")
print("Проверяем скорость работы функицй calc")
t1 = timeit.timeit(p1.calc)
t2 = timeit.timeit(p2.calc)
print("результат без __slots__", t1)
print("результат c  __slots__ ", t2)