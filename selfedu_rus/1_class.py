#17.01.2022
#видимость действия атрибутов класса
class Point:
    color = "red"
    circle = 2

a = Point()
b = Point()

a.x = 2
a.y = 5
a.z = 7
b.x = 20
b.y = 40
b.z = 2

print(a.__dict__, b.__dict__)
for i in ([a.__dict__, b.__dict__]):
    for s in i:
        print(s, "=", i[s])
    print()