#20.01.2022

class Functions:

    def __init__(self):
        self.counter = 0

    def __call__(self, *args, **kwargs):
        print("__call__")
        self.counter += 1
        return self.counter


f = Functions()
#используем экземпляр класса как ф-цию
f()
f()
f()
print(f.counter)