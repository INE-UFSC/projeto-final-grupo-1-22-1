import pygame
from pygame import event
from pygame.locals import QUIT, KEYUP, K_SPACE, K_ESCAPE

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


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      return('ESQUERDA')
    elif keys[pygame.K_RIGHT]:
      return('DIREITA')
    elif keys[pygame.K_UP]:
      return('CIMA')
    elif keys[pygame.K_DOWN]:
      return('BAIXO')