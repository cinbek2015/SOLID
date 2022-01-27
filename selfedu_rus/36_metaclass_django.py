#27.01.2022
#создаем метакласс
class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, val in self.class_attrs.items():
            self.__dict__[key] = val

    def __init__(cls, name, base, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs

class Women(metaclass=Meta):
    name = "Анджелина Джоли"
    foto = "путь к фото"
    family = "Семейное положение"

class Men(metaclass=Meta):
    name = "Энтони Хопкинс"
    foto = "путь к фото"
    family = "Семейное положение"

w1 = Women()
print(w1.__dict__)
m1 = Men()
print(m1.__dict__)