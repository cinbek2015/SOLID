#25.01.2022

class ExceptPrintAll(Exception):
    "ошибка вывода на печать"
    pass

class ExceptPrintJam(ExceptPrintAll):
    "замятие бумаги"

    def __init__(self, *args):
        self.mesage = args[0] if args else None

    def __str__(self):
        return f"Ошибка, замятие {self.mesage}"

class ExceptPrintNoPaper(ExceptPrintAll):
    "отсутствие бумаги"

    def __init__(self, *args):
        self.mesage = args[0] if args else None

    def __str__(self):
        return f"Ошибка с бумагой {self.mesage}"

class PrintData:

    def print(self, data):
        self.data = data
        self.send_data(data)
        print( f'Идет печать {self.data}')

    def send_data(self, data):
        if self.paper_lotok():
            raise ExceptPrintNoPaper("Отсутствует бумага в лотке")
        if self.paper_manual_feed():
            raise ExceptPrintNoPaper("отсутствует бумага в лотке ручной подачи")
        if self.send_to_jam_fuser():
            raise ExceptPrintJam("в печке")

    def paper_lotok(self):
        return False

    def paper_manual_feed(self):
        return False

    def send_to_jam_fuser(self):
        return True

p1 = PrintData()
p1.send_data("Печать страницы")