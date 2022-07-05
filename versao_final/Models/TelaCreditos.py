import pygame as pg

from Models.Tela import Tela
from Models.LeitorEventos import LeitorEventos
from Models.Window import Window


class TelaCreditos(Tela):
  def __init__(self, leitor_eventos:LeitorEventos, window: Window, fonte):
    super().__init__(leitor_eventos, window, fonte)

  def renderizar_tela(self):
    running = True
    while running:
        self.window.surface.fill((0,0,0))
 
        super().renderizar_texto('creditos', self.fonte, (255, 255, 255), self.window.surface, 20, 20)
        
        evento = self.leitor_eventos.ler_evento()
        if  evento == 'FECHAR':
            self.window.fechar()
        elif evento == 'ESCAPE':
                running = False

        self.window.update()
        pg.time.Clock().tick(30)