class Point:
    color = "red"
    circle = 2

print(getattr(Point, 'a', "Error "))

a = Point()