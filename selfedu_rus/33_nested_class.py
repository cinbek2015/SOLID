#26.01.2022

class Women:

    order = "атрибут order класса Women"
    foto = "атрибут foto класса women"

    def __init__(self, name, paswd):
        self._name = name
        self. paswd = paswd
        self._data = self.Data(name + "@" + paswd)

    #вложенный класс
    class Data:
        order = ['id']

        def __init__(self, user):
            self._user = user

w = Women("user", "1245")
print(w.__dict__)
print(w._data.__dict__)