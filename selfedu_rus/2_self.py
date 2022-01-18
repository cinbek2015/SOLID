#18.01.22
class Point:

    color = "red"

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return(self.x, self.y)

pt = Point()
pt.set_point(1, 2)
print(pt.get_point())

ft = getattr(pt, "get_point")
print(ft)
print(ft())