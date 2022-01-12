#12.01.2022
class Life():
    def lif(self):
        print("class life")

class ciliates(Life):
    def piri(self):
        print("class cili")

class slipper(Life):
    def piri(self):
        print("class slipper")

class People(ciliates, slipper):
    def pip(self):
        print("class People")

Andru = People()
Andru.pip()
Andru.piri()
Andru.lif()
print(Andru.__repr__())