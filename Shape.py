#12.01.2022
class Shape():

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

class Triangle(Shape):
    def area(self):
        return int(1/2*(self.get_width()*self.get_height()))


class Rectangle(Shape):
    def area(self):
        return int(self.get_width() * self.get_height())

tr = Triangle(12, 7)
print(tr.area())
rec = Rectangle(12, 7)
print(rec.area())