#23.01.2022

class Student:

    def __init__(self, name, marks):
        self.__name = name
        self.__marks = list(marks)

    def __getitem__(self, value):
        if not 0 <= value < len(self.__marks):
            raise IndexError("нет такого элемента в списке")
        else:
            return self.__marks[value]

    def __setitem__(self, key, value):
        if not isinstance(key, int) and key > 0:
            raise IndexError("Ключ должен быть целым значением")

        #если оценка должна быть записана за пределы размера списка
        if key > len(self.__marks):
            tm = key + 1 - len(self.__marks)
            self.__marks.extend([None] * tm)#раширяем список

        self.__marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise IndexError("Ключ должен быть целым значением")

        del self.__marks[key]

    def get_marks(self):
        return self.__marks

s1 = Student("Mark", [5, 5, 3, 4, 3])
print(s1[0])
s1[10] = 3
print(s1.get_marks())
del s1[4]
print(s1.get_marks())