#18.01.2022

class Point:

    def __init__(self, x, y):
        print("create ", self)
        self.x = x
        self.y = y

    def __del__(self):
        print("delete ", self)

    def set_attr(self, x, y):
        self.x = x
        self.y = y

    def get_attr(self):
        return self.x, self.y

pt = Point(1, 2)
print(pt.get_attr())
pt.set_attr(3, 4)
print(pt.get_attr())