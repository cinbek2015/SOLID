#26.01.2022
#*****************************************************
A = type("Point", (), {"Andru": 46, "Roma": 37})
a = A()
a.Gera = 36
print("Пример простого создания метакласса, Example metaclass create simple")
print(a.__dict__)
print(a.Andru)

#******************************************************
#пример создание метокласса с помощью функции
def metaclass_creator(name, base, attr):
    #как пример можем добавлять по желанию два атрибута
    attr.update({"MAX_COORD": 100, "MIN_COORD": 0})
    return type(name, base, attr)

class MyClass(metaclass=metaclass_creator):
    def myfunc(self):
        return (0, 0)

mycl = MyClass()
print("MyClass example", mycl.myfunc())
#********************************************************
#создаем метакласс
class Meta(type):

    # можно через __new__ вносим изменение в словарь и только потом создаем объект
    def __new__(cls, name, base, atr):
        atr.update({"MAX_COORD": 100, "MIN_COORD": 0})
        return type.__new__(cls, name, base, atr)

    #можно через __init__ мы добавляем атрибуты, потому что объект уже создан
    # def __init__(cls, name, base, atr):
    #     super().__init__(name, base, atr)
    #     cls.MAX_COORD = 100
    #     cls.MIN_COORD = 0

class Point(metaclass=Meta):

    def get_coords(self):
        return (0, 0)

p = Point
print(p.MIN_COORD)
print(p.MAX_COORD)
#****************************************************************