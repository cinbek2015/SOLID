#13.01.2022
class Vector():
    _x = 0
    _y = 0
    _z = 0

    def __init__(self, x, y ,z=0):
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        return "class release metod mathematic"

    #альтернативный конструктор
    #принимает строку в формате "x,y"
    @classmethod
    def init_str(cls, line):
        try:
            return cls(*[int(x) for x in line.split(",")])
        except Exception:
            print("Ошибка неккоректного ввода")
        print(cls._x, cls._y)

    def get_all(self):
        return self._x, self._y, self._z

    def __add__(self, other):
        try:
            if not isinstance(other, Vector):
                raise Exception("Ошибка неккоректного ввода")
        except Exception as exp:  # ловим собственную ошибку
            print(exp)  # выводим "Ошибка неккоректного ввода"
        else:  # блок который выполняется в случае если ошибки не было
            return self._x + other._x, self._y + other._y, self._z + other._z

    def __sub__(self, other):
        try:
            if not isinstance(other, Vector):
                raise Exception("Ошибка неккоректного ввода")
        except Exception as exp:  # ловим собственную ошибку
            print(exp)  # выводим "Ошибка неккоректного ввода"
        else:  # блок который выполняется в случае если ошибки не было
            return self._x - other._x, self._y - other._y, self._z - other._z


    def __mul__(self, other):
        try:
            if not isinstance(other, Vector):
                raise Exception("Ошибка неккоректного ввода")
        except Exception as exp:  # ловим собственную ошибку
            print(exp)  # выводим "Ошибка неккоректного ввода"
        else:  # блок который выполняется в случае если ошибки не было
            return self._x * other._x, self._y * other._y, self._z * other._z

    def __truediv__(self, other):
        try:
            if not isinstance(other, Vector):
                raise Exception("Ошибка неккоректного ввода")
        except Exception as exp:  # ловим собственную ошибку
            print(exp)  # выводим "Ошибка неккоректного ввода"
        else:  # блок который выполняется в случае если ошибки не было
            return self._x / other._x, self._y / other._y, self._z / other._z

    def __floordiv__(self, other):
        try:
            if not isinstance(other, Vector):
                raise Exception("Ошибка неккоректного ввода")
        except Exception as exp:  # ловим собственную ошибку
            print(exp)  # выводим "Ошибка неккоректного ввода"
        else:  # блок который выполняется в случае если ошибки не было
            return self._x // other._x, self._y // other._y, self._z // other._z

    def __mod__(self, other):
        try:
            if not isinstance(other, Vector):
                raise Exception("Ошибка неккоректного ввода")
        except Exception as exp:  # ловим собственную ошибку
            print(exp)  # выводим "Ошибка неккоректного ввода"
        else:  # блок который выполняется в случае если ошибки не было
            return self._x % other._x, self._y % other._y, self._z % other._z

vec1 = Vector(11, 16, 16)
vec2 = Vector.init_str("12,15")
vec3 = Vector(4, 5, 5)
print(vec1.get_all())
# print(vec2.get_all())
print(vec3.get_all())
print("*"*10)
print(vec1 + vec3)
print("*"*10)
print(vec1 - vec3)
print("*"*10)
print(vec1 * vec3)
print("*"*10)
print(vec1 / vec3)
print("*"*10)
print(vec1 // vec3)
print("*"*10)
print(vec1 % vec3)