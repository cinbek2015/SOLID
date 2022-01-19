#19.01.2021
class Threading:

    bd_users = {
        "user": "",
        "year": 34,
        "id" : 12
    }

    def __init__(self):
        self.__dict__ = self.bd_users

th1 = Threading()
th2 = Threading()