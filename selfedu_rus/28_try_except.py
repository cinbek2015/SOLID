#25.01.2022

try:
    x, y = map(int, input().split())
    num = x / y
    print(int(num))
except ValueError:
    print("Ошибка ввода данных")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")

print("Продолжение выполнения программы")