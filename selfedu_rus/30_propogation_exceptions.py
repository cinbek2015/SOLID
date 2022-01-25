#25.01.2022
#демонстрация разделения формирования исключений и их обработка в
#пользовательском приложении
def Hp9040(x, y):
    if True:
        try:
            st = x / y
        except ZeroDivisionError:
            return "Отсутствует бумага"

    if True:
        try:
            st = y / x
        except ZeroDivisionError:
            return "Замятие в третьем лотке"



def GUI1():
    print(Hp9040(1, 0))
def GUI2():
    print(Hp9040(0, 1))

GUI1()
print()
GUI2()