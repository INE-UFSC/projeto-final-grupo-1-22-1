import pygame as pg
import time
from pygame.sprite import GroupSingle
from classes.states.State import State
from classes.configuracoes.Configuracoes import Configuracoes
from classes.mapa.Mapa import Mapa
from classes.desenhaveis.Inimigo import Inimigo
from classes.jogo.ControladorJogo import ControladorJogo


class JogoState(State):
    def __init__(self, window, transition_to) -> None:
        super().__init__(window, transition_to)
        self.__window_surface = self.window.surface
        self.__timer = pg.time.Clock()
        self.__controlador_jogo = ControladorJogo(self.__window_surface)


    def renderizar(self) -> None:
        controlador_jogo = self.__controlador_jogo
        while True:
            self.__timer.tick(60)
            
            self.__window_surface.fill(self.configuracoes.cor_fundo)

            controlador_jogo.iniciar()
            
            if controlador_jogo.checar_vitoria_jogo():
                self.transicionar("VitoriaState")
                break

            if controlador_jogo.checar_derrota_jogo():
                self.transicionar("GameOverState")
                break
            
            
            self.window.update()
            self.window.flip()
