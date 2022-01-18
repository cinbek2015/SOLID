#18.01.2022
class Monster:

    def __new__(cls, *args, **kwargs):
        print("create new", cls)
        return super().__new__(cls)

    def __init__(self, x, y):
        print("initializations ", self)
        self.x = x
        self.y = y

    def get_attr(self):
        return (self.x, self.y)

mn = Monster(12, 15)
print(mn.get_attr())