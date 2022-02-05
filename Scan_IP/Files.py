#31.01.2022
"""
Читает и записывает данные из файлов
"""
from ipaddress import ip_address

try:
    with open("Config.txt") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Файл не найден")

ip_start = ip_finish = 0
try:
    ip_start = ip_address(lines[1].strip())
    ip_finish = ip_address(lines[2].strip())

except ValueError:
    print(f"Один из IP адресов {lines[1].strip()}, {lines[2].strip()} не является корректным")

print("Начинаем с IP адреса", ip_start)
print("Заканчиваем IP адресом", ip_finish)