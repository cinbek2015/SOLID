#20.01.2022


class Collaborat:
    "класс работника"

    def __init__(self, fio, age, table):
        self.verification_fio(fio)
        self.set_age(age)
        self.set_table(table)

        self.__fio = fio
        self.age = age
        self.table = table

    def get_users(self):
        return (self.fio, self.age, self.table)

    @property
    def fio(self):
        return self.__fio

    def verification_fio(self, fio):
        if len(fio.split()) != 3 or type(fio) != str or fio.isalpha():
            raise ValueError ("неправильный формат ФИО")
        name = [c for c in fio if c != " "]
        for c in "".join(name):
             if not c.isalpha():
                 raise ValueError ("ФИО должно состоять из букв")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.set_age(age)
        self.__age = age

    def set_age(self, age):
        if type(age) != int  or age <= 17 or age >= 120:
            raise ValueError (f" Возраст {age} выходит за рамки (17, 120)")

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, table):
        self.set_table(table)
        self.__table = table

    def set_table(self, table):
        if type(table) != int:
            raise ValueError("Табельный номер должен быть числом")


Andru = Collaborat("Andru Kovalchuk V", 45, 134676)
print(Andru.get_users())

Andru.table = 526342
Andru.age = 50
print(Andru.get_users())