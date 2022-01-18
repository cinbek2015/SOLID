#18.01.2022

class Example:

    COORD_MIN = 0
    COORD_MAX = 100

    @classmethod
    def validate(cls, x):
        return cls.COORD_MIN <= x <= cls.COORD_MAX

    @staticmethod
    def dot_cube(x, y):
        return x*x + y*y

    def prius(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_attr(self):
        return self.x, self.y


ex = Example()
ex.prius(12, 34)
print(ex.get_attr())
print(ex.dot_cube(*ex.get_attr()))