from classes.persistencia.DAO import DAO
from classes.persistencia.Pontuacao import Pontuacao

class JogoDAO(DAO):
    def __init__(self):
        super().__init__('jogo.pkl')

    def add(self, jogo_pontuacao: Pontuacao):
        if isinstance(jogo_pontuacao.baus, int) and isinstance(jogo_pontuacao.data, str) and isinstance(jogo_pontuacao.mortes, int):
            super().add(jogo_pontuacao)
        else:
            raise TypeError()