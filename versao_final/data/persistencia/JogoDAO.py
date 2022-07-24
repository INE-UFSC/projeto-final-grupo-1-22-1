from data.persistencia.DAO import DAO
from data.persistencia.Pontuacao import Pontuacao

class JogoDAO(DAO):
    def __init__(self):
        super().__init__('jogo.pkl')

    def add(self, jogo_pontuacao: Pontuacao):
        if isinstance(jogo_pontuacao.tempo, int) and isinstance(jogo_pontuacao.data, str) and isinstance(jogo_pontuacao.tempo, int):
            super().add(jogo_pontuacao)
        else:
            print('Não foi')