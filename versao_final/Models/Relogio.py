import pygame as pg
from pygame.locals import*


class Relogio():
    def __init__(self) -> None:
        self.__comeco_do_jogo = pg.time.get_ticks()
        self.__execucao_do_jogo = 0

    def atualizar_tempo_execucao_jogo(self):
        self.__execucao_do_jogo = (pg.time.get_ticks() - self.__comeco_do_jogo)//1000

    @property
    def execucao_do_jogo(self):
        return (self.__execucao_do_jogo)
