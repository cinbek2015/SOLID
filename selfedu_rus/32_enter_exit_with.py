#26.01.2022

class Defender:

    def __init__(self, v):
        self.__v = v

    #создаем объект
    def __enter__(self):
        self._temp = self.__v[:]
        return self._temp

    #при отсутствии исключений копируем результат работы и закрывает объект
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self._temp

        return False

v1 = [1, 2, 3]
v2 = [2, 3, 4]

try:
    with Defender(v1) as df:
        for i, a in enumerate(df):
            df[i] += v2[i]
except:
    print("Ошибка")

print(v1)