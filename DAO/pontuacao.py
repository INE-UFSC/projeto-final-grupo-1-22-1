from datetime import date

class Pontuacao:
    def __init__(self, pontos, tempo):
        self.__pontos = pontos
        self.__tempo = tempo
        self.__data = f'{}:{} - {date.today().day}/{date.today().month}/{date.today().year}'

    @property
    def data(self):
        return self.__data

a = Pontuacao(10, 23)

print(a.data)