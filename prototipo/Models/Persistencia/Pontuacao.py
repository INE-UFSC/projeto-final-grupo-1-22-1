from datetime import datetime as dt

class Pontuacao:
    def __init__(self, pontos: int, tempo: int):
        self.__pontos = pontos
        self.__tempo = tempo
        self.__data = f'{dt.now().hour}:{dt.now().minute} - {dt.now().day}/{dt.now().month}/{dt.now().year}'

    @property
    def pontos(self):
        return self.__pontos

    @property
    def tempo(self):
        return self.__tempo

    @property
    def data(self):
        return self.__data