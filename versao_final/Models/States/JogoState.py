import pygame as pg
from pygame.sprite import GroupSingle
from Models.States.State import State
from Models.Configuracoes import Configuracoes
from Models.Mapa.Mapa import Mapa
from Models.Mapa.Inimigo import Inimigo
from Models.ControladorJogo import ControladorJogo


class JogoState(State):
    def __init__(self, window, transition_to):
        super().__init__(transition_to)
        self.__configuracoes = Configuracoes()
        self.__window = window
        self.__window_surface = self.__window.surface
        self.__timer = pg.time.Clock()
        self.__controlador_jogo = ControladorJogo(self.__window_surface)
        

    def renderizar(self):
        controlador_jogo = self.__controlador_jogo
        while True:
            self.__timer.tick(60)

            self.__window_surface.fill((54, 107, 95))

            controlador_jogo.iniciar()

            if controlador_jogo.game_over():
                self.transicionar("GameOverState")
                break

            pg.display.update()
            pg.display.flip()
