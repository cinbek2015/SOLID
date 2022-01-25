#25.01.2022

def abnormaly(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деления на ноль"


try:
    x, y = map(int, input().split())
    res = abnormaly(x, y)
except ValueError:
    print("Введены не корректные данные")
else:
    print("Выполняется если блок try был завершен без ошибок", res)
    print(res)
finally:
    print("Блок finally выполняется всегда")
