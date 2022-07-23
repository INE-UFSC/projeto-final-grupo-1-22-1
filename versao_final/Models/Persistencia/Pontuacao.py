from datetime import datetime as dt

class Pontuacao:
    def __init__(self, baus: int, tempo:int):
        self.__data = f'{dt.now().hour}:{dt.now().minute} - {dt.now().day}/{dt.now().month}/{dt.now().year}'
        self.__baus = baus
        self.__tempo = tempo

    @property
    def tempo(self):
        return self.__tempo

    @property
    def baus(self):
        return self.__baus

    @property
    def data(self):
        return self.__data