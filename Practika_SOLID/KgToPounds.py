#29.01.2022
"""
Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм, а
с помощью метода to_pounds() они переводятся в фунты.Чтобы закрыть доступ к переменной “kg” она реализовала
методы set_kg() - для задания нового значения килограммов, get_kg() - для вывода текущего значения кг.Из - за
этого возникло неудобство: нам нужно теперь использовать  эти 2 метода для задания и вывода значений.Помогите
ей переделать класс с использованием функции property() и свойств - декораторов.Код приведен ниже.
"""

class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205
    @property
    def kg(self):
        return self.__kg
    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

kg = KgToPounds(85)
print(kg.kg, "кг это", kg.to_pounds(), "фунтов")
kg.kg = 95
print(kg.kg, "кг это", kg.to_pounds(), "фунтов")

# Тесты
weight = KgToPounds(12)
print(weight.to_pounds())
print(weight.kg)
weight.kg = 41
print(weight.kg)
# weight.kg = 'десять'