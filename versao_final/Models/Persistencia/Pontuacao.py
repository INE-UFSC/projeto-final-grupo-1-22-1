from datetime import datetime as dt

class Pontuacao:
    def __init__(self, baus: int, mortes:int):
        self.__data = f'{dt.now().hour}:{dt.now().minute} - {dt.now().day}/{dt.now().month}/{dt.now().year}'
        self.__baus = baus
        self.__mortes = mortes

    @property
    def mortes(self):
        return self.__mortes

    @property
    def baus(self):
        return self.__baus

    @property
    def data(self):
        return self.__data