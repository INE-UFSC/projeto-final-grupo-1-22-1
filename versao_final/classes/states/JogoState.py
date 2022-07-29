import pygame as pg
import time
from pygame.sprite import GroupSingle
from classes.states.State import State
from classes.configuracoes.Configuracoes import Configuracoes
from classes.mapa.Mapa import Mapa
from classes.desenhaveis.Inimigo import Inimigo
from classes.jogo.ControladorJogo import ControladorJogo


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
            
            self.__window_surface.fill(self.__configuracoes.cor_fundo)

            controlador_jogo.iniciar()
            
            if controlador_jogo.checar_vitoria_jogo():
                self.transicionar("VitoriaState")
                break

            if controlador_jogo.checar_derrota_jogo():
                self.transicionar("GameOverState")
                break
            
            
            pg.display.update()
            pg.display.flip()
