#18.01.2022
class Monster:
    "класс демонстрирующий __new__ и __init__"
    count = 0 #счетчик создания объектов типа Monster

    def __new__(cls, *args, **kwargs):
        cls.count += 1
        print("create new", cls)
        return super().__new__(cls)

    def __init__(self, x, y):
        print("initializations ", self)
        self.x = x
        self.y = y

    def get_attr(self):
        return (self.x, self.y)

    @classmethod
    def get_count(cls):
        return cls.count

t = [i for i in range(15)]
for i in range(15):
    t[i] = Monster(12, 15)
print()
print(t[0].get_count())
print(t[0].__doc__)