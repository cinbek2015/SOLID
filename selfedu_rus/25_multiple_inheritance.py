#24.01.2022

class Shop:

    def __init__(self, name, price, weight):
        super().__init__()#инициализация второго класса
        self._name = name
        self._price = price
        self._weight = weight

    def get_shop(self):
        return f'{self._name} : {self._price} Руб, weight = {self._weight}'

class LogSales:
    ID = 0

    def __init__(self):
        print("__init__ LogSales")
        self.ID += 1
        self.id = self.ID

    def get_ID(self):
        return self.ID

class NoteBook(Shop, LogSales):
    pass

n1 = NoteBook("Asus GFT25J17sd", 46324, 17)
print(n1.get_shop(), "log =", n1.get_ID())
print(NoteBook.__mro__)