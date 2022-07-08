from Models.LeitorEventos import LeitorEventos
from Models.Window import Window
from Models.Tela import Tela

import pygame as pg

class TelaMenu(Tela):
    def __init__(self, leitor_eventos:LeitorEventos, window: Window, fonte):
        super().__init__(leitor_eventos, window, fonte)

    def renderizar_tela(self):
        self.window.surface.fill((54,107,95))
        super().renderizar_texto('main menu', self.fonte, (255, 255, 255), self.window.surface, (self.window.size[0]/2)-100, 20)

        botao1 = pg.Rect((self.window.size[0]/2)-100, 100, 200, 50)
        botao2 = pg.Rect((self.window.size[0]/2)-100, 200, 200, 50)
        pg.draw.rect(self.window.surface, (137, 199, 185), botao1)
        pg.draw.rect(self.window.surface, (137, 199, 185), botao2)

        evento = self.leitor_eventos.ler_evento()
        if  evento == 'CLIQUE':
            posicao_mouse = self.leitor_eventos.posicao_mouse()
            if botao1.collidepoint(posicao_mouse):
                return('OPCAO1')
            elif botao2.collidepoint(posicao_mouse):
                return('OPCAO2')
        elif evento == 'FECHAR':
            self.window.fechar()
            
