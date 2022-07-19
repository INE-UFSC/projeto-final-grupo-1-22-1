import pygame as pg
from pygame.sprite import GroupSingle
from Models.States.State import State
from Models.Configuracoes import Configuracoes
from Models.Mapa.Mapa import Mapa
from Models.Inimigo import Inimigo


class JogoState(State):
    def __init__(self, window, transition_to):
        super().__init__(transition_to)
        self.__configuracoes = Configuracoes()
        self.__window = window
        self.__window_surface = self.__window.surface
        self.__timer = pg.time.Clock()
        self.__mapa = Mapa(self.__configuracoes.mapa, self.__window_surface)

    def renderizar(self):
        while True:
            self.__timer.tick(60)

            self.__window_surface.fill((54, 107, 95))

            self.__mapa.run()

            pg.display.update()
            pg.display.flip()
