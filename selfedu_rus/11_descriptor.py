#20.01.2022
class Integer:
    """Дескриптор данных"""
    @classmethod
    def examination_value(cls, value):
        if type(value) != int:
            raise TypeError("Тип данных точек должен быить целочисленный")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
        # return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.examination_value(value)
        setattr(instance, self.name, value)
        # instance.__dict__[self.name] = value

class Point3D:
    "создаем три объекта Дескриптора"
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

pt = Point3D(1, 2, 3)
print(pt.__dict__, pt.z)