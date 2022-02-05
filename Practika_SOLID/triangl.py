#28.01.2022
"""
Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.
"""
class TriangleChecker:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def istringle(self, x, y, z):
        if ((x+y>z) and (x+z>y) and (y+z>x)):
            return True
        return False

    def is_triangle(self):
        if not( isinstance(self._x, int) and isinstance(self._y, int) and isinstance(self._z, int)):
            raise ValueError("Нужно вводить только числа!")
        if not (self._x >= 0 and self._y >= 0 and self._z >= 0):
            raise ValueError("С отрицательными числами ничего не выйдет!")
        if self.istringle(self._x, self._y, self._z):
            print("Ура, можно построить треугольник!")
        else:
            print("Жаль, но из этого треугольник не сделать.")



#Test
# s = TriangleChecker("2", 3, 2)
# s.is_triangle()
# a = TriangleChecker(-2, 3, 4)
# a.is_triangle()
t = TriangleChecker(3, 1, 3)
t.is_triangle()

# Тесты
triangle1 = TriangleChecker(2, 3, 4)
print(triangle1.is_triangle())
triangle2 = TriangleChecker(77, 3, 4)
print(triangle2.is_triangle())
triangle3 = TriangleChecker(77, 3, 'Сторона3')
print(triangle3.is_triangle())
triangle4 = TriangleChecker(77, -3, 4)
print(triangle4.is_triangle())