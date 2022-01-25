#25.01.2022

class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D1(Point):
    pass

class Point3D2(Point):
    __slots__ = 'z',

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

class Point3D3(Point):
    __slots__ = ()#накладывает ограничение с базового класса

p3d1 = Point3D1(1, 2)
p3d1.z = 20
print(p3d1.z, p3d1.__dict__)
print()
p3d2 = Point3D2(10, 20, 30)
print(p3d2.x, p3d2.y, p3d2.z)
p3d3 = Point3D3(100, 200)
# p3d3.z = 34 ошибка создавать данный атрибут нельзя