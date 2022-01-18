#18.01.2022

class Point:
    "данный класс демонстрирует закрытые методы + проверку введенных данных"

    def __init__(self, x, y):
        self._x = self._y = 0
        if self.examination(x) and self.examination(y):
            self._x = x
            self._y = y
            print("данные приняты")
        else:
            raise ValueError ("Ошибочные данные не тот тип, должен быть числовой")

    @classmethod
    def examination(cls, x):
        return type(x) in (int, float)

    def get_point(self):
        return (self._x, self._y)

poi = Point(12.6, 34)
print(poi.get_point())
print(poi.__doc__)