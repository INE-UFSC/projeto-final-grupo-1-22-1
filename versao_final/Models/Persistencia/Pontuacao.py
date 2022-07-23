from datetime import datetime as dt

class Pontuacao:
    def __init__(self, pontos: int):
        self.__data = f'{dt.now().hour}:{dt.now().minute} - {dt.now().day}/{dt.now().month}/{dt.now().year}'
        self.__pontos = pontos

    @property
    def pontos(self):
        return self.__pontos

    @property
    def data(self):
        return self.__data