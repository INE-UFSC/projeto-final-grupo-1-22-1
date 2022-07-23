from Models.Persistencia.DAO import DAO
from Models.Persistencia.Pontuacao import Pontuacao

class JogoDAO(DAO):
    def __init__(self):
        super().__init__('jogo.pkl')

    def add(self, jogo_pontuacao: Pontuacao):
        if isinstance(jogo_pontuacao.pontos, int) and isinstance(jogo_pontuacao.data, str):
            super().add(jogo_pontuacao)
        else:
            print('Não foi')