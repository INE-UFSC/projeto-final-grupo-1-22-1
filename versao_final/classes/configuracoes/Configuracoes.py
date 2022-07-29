from pygame import font

from classes.configuracoes.Singleton import Singleton

class Configuracoes(Singleton):
    def init(self):
        font.init()
        self.__fonte = font.SysFont('comicsans', 20)
        self.__fonte_titulo = font.SysFont('comicsans', 60)
        self.__largura_tela = 720
        self.__altura_tela = 540
        self.__velocidade_jogador = 3
        self.__velocidade_inimigo = 1
        self.__vidas_jogador = 3
        self.__cor_fundo = (54, 107, 95)
        self.__vol_control = 1
        self.__dificuldade = 1
        self.__music_control = 0
        self.__dificuldades = {
                               1: {"velocidade": 1, "acres_velo": 10, "baus_nesc": 3}, 
                               2: {"velocidade": 2, "acres_velo": 5, "baus_nesc": 5}, 
                               3: {"velocidade": 3, "acres_velo": 7, "baus_nesc": 7}
                               }


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

    @property
    def fonte_titulo(self):
        return self.__fonte_titulo
    
    @property
    def vol_control(self):
        return self.__vol_control

    @property
    def music_control(self):
        return self.__music_control

    @property
    def dificuldade(self):
        return self.__dificuldade
    
    @property
    def vidas_jogador(self):
        return self.__vidas_jogador

    @velocidade_inimigo.setter
    def velocidade_inimigo(self, velocidade_inimigo):
        self.__velocidade_inimigo = velocidade_inimigo

    @vol_control.setter
    def vol_control(self, new_volum):
        self.__vol_control = new_volum

    @music_control.setter
    def music_control(self, new_music):
        self.__music_control = new_music

    @dificuldade.setter
    def dificuldade(self, new_dif):
        self.__dificuldade = new_dif

    def gerar_dados(self):
        return self.__dificuldades[self.__dificuldade]