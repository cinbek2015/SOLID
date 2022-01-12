#12.01.2022
class Mother():
    def __str__(self):
        return "class Mother"

    def __repr__(self):
        return self.__class__

class Daughtres(Mother):

    def __str__(self):
        return "class Daughtres"

class Rob():
    pass

mother = Mother()
print(mother)
daug = Daughtres()
print(daug)