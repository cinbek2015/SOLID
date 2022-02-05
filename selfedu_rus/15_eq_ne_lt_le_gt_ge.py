#21.01.2022

class Integer:

    def __init__(self, x):
        self._x = x

    @classmethod
    def check_Integer(cls, other):
        if not isinstance(other, cls):
            raise ValueError("нельзя сравнивать разные объекты")
        return True

    def __eq__(self, other):
        if self.check_Integer(other):
            return self._x == other._x

    def __gt__(self, other):
        if self.check_Integer(other):
            return self._x > other._x



i1 = Integer(500)
i2 = Integer(200)
print(i1 == i2)
print(i1 != i2) #Python сам переворачивает not(i1 == i2)
print(i1 > i2)
print(i1 < i2) #Python сам переворачивает not(i2 > i1)