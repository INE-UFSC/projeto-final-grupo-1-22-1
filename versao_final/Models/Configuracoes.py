from pygame import font

from Models.Singleton import Singleton


class Configuracoes(Singleton):
    def init(self):
        font.init()
        self.__fonte = font.SysFont('comicsans', 20)
        self.__largura_tela = 720
        self.__altura_tela = 540
        self.__velocidade_jogador = 3
        self.__velocidade_inimigo = 1
        self.__cor_fundo = (54, 107, 95)

    @property
    def fonte(self):
        return self.__fonte 

    @property
    def largura_tela(self):
        return self.__largura_tela

    @property
    def altura_tela(self):
        return self.__altura_tela

    @property
    def velocidade_jogador(self):
        return self.__velocidade_jogador

    @property
    def velocidade_inimigo(self):
        return self.__velocidade_inimigo

    @property
    def cor_fundo(self):
        return self.__cor_fundo

    @velocidade_inimigo.setter
    def velocidade_inimigo(self, velocidade_inimigo):
        self.__velocidade_inimigo = velocidade_inimigo
