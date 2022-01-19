#19.01.2022

class Getterible:
    MAX_COREDR = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def set_corder(cls, value):
        cls.MAX_COREDR = value

    def get_corder(self):
        return self.MAX_COREDR

    def __getattribute__(self, item):
        #авт зан при обращении к атрибутам класса
        if item == "x":
            raise ValueError ("Дотсуп запрещен")
        else:
            return object.__getattribute__(self, item)

    def __getattr__(self, item):
        #обращение не к существующему атрибуту
        # print("К сожалению вы обратились не к существующей перменной")
        return False

    def __setattr__(self, key, value):
        #при изменений атрибутов класса
        print("__setattr__", key, "=", value)
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == "x":
            raise ValueError("запрет на удаление данного атрибута", item)
        else:
            object.__delattr__(self, item)

child = Getterible(12, 14)
del child.y
print(child.__dict__)
# print(child.x)
# print(child.z)
