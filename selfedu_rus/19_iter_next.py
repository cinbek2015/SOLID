#23.01.2022

class Iterator_my:
    "пример написания итерированных объектов"
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self._start = start
        self._stop = stop
        self._step = step


    def __iter__(self):
        self._value = self._start - self._step
        return self

    def __next__(self):
        if self._value + self._step < self._stop:
            self._value += self._step
            return self._value
        else:
            raise StopIteration

class IterRow:
    "класс использующий итератор класса Iterator_my"
    def __init__(self, start=0.0, stop=0.0, step=1.0, row=5):
        self.__row = row
        self.__itr = Iterator_my(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.__row:
            self.value += 1
            return iter(self.__itr)
        else:
            raise StopIteration

it = IterRow(0.0, 2.0, 0.5)
for row in it:
    for line in row:
        print(line, end=" * ")
    print()