#12.01.2022

class Animal():
    __name = ""
    __old = 0

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_name(self):
        return self.__name

    def get_old(self):
        return self.__old

class Zebra(Animal):
    __description = ""
    __info = ""

    def __init__(self, name, old):
        super().__init__(name, old)

    def set_description(self, desc):
        self.__description = desc
    def set_info(self, info):
        self.__info = info
    def get_description(self):
        return self.__description
    def get_info(self):
        return self.__info

class Dolphin(Animal):
    __description = ""
    __info = ""

    def __init__(self, name, old):
        super().__init__(name, old)

    def set_description(self, desc):
        self.__description = desc
    def set_info(self, info):
        self.__info = info
    def get_description(self):
        return self.__description
    def get_info(self):
        return self.__info

zeb1 = Zebra("Lili", 3)
zeb1.set_description("Zebra tailed animal")
zeb1.set_info("Zebra")
print(zeb1.get_info(), zeb1.get_name(), zeb1.get_old(), "year", zeb1.get_description())

dol1 = Dolphin("Scot", 2)
dol1.set_description("Dolphin big fish")
dol1.set_info("Dolphin")
print(dol1.get_info(), dol1.get_name(), dol1.get_old(), dol1.get_description())