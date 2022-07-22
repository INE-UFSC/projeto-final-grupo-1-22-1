import pygame as pg
from pygame.sprite import GroupSingle
from Models.States.State import State
from Models.Configuracoes import Configuracoes
from Models.Inimigo import Inimigo
from Models.ControladorJogo import ControladorJogo
from Models.Paused import Paused


class JogoState(State):
    def __init__(self, window, transition_to):
        super().__init__(transition_to)
        self.__configuracoes = Configuracoes()
        self.__window = window
        self.__window_surface = self.__window.surface
        self.__largura_tela = self.__configuracoes.largura_tela
        self.__altura_tela = self.__configuracoes.altura_tela
        self.__timer = pg.time.Clock()
        self.__controlador_jogo = ControladorJogo(self.__window_surface)
        self.__mapa_bg_img = pg.transform.scale(
            pg.image.load("Images/Mapa.png"), (self.__largura_tela, self.__altura_tela))
        self.__paused_game = False
        

    def renderizar(self):
        controlador_jogo = self.__controlador_jogo
        while True:
            if self.__paused_game:
                Paused.renderizar()
            else:
                self.__timer.tick(60)

                self.__window_surface.blit(self.__mapa_bg_img, (0, 0))

                controlador_jogo.iniciar()

                if controlador_jogo.game_over():
                    self.transicionar("GameOverState")
                    break
            #self.__paused_game = controlador_
            pg.display.update()
            pg.display.flip()
