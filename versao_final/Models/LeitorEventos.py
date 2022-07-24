import pygame as pg
from pygame import event
from pygame.locals import QUIT, KEYUP, K_SPACE, K_ESCAPE, MOUSEBUTTONDOWN

class LeitorEventos():
  def __init__(self):
    pass

  def ler_evento(self):
    for evento in event.get(): #Retorna uma lista de events
      if evento.type ==  QUIT:
        return ("FECHAR")

      if evento.type == KEYUP:
        if evento.key == K_SPACE:
          return ("ESPACO")
        if evento.key == K_ESCAPE:
          return ('ESCAPE')
    
      if evento.type == MOUSEBUTTONDOWN:
        print('clique')
        return ('CLIQUE')

      if evento.type == pg.KEYUP:
          if evento.key == pg.K_p:
            print('Pausado')

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
      return('ESQUERDA')
    elif keys[pg.K_RIGHT]:
      return('DIREITA')
    elif keys[pg.K_UP]:
      return('CIMA')
    elif keys[pg.K_DOWN]:
      return('BAIXO')

  def posicao_mouse(self):
    return pg.mouse.get_pos()