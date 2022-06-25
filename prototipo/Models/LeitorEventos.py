import pygame
from pygame import event
from pygame.locals import QUIT, KEYUP, K_SPACE, K_LEFT

class LeitorEventos():
  def __init__(self):
    pass
  
  def ler_evento(self):
    for evento in event.get(): #Retorna uma lista de events
      if evento.type ==  QUIT:
        return ("fechar")

      if evento.type == KEYUP:
        if evento.key == K_SPACE:
          return ("atacar")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      return('mover-esq')
    elif keys[pygame.K_RIGHT]:
      return('mover-dir')
    elif keys[pygame.K_UP]:
      return('mover-up')
    elif keys[pygame.K_DOWN]:
      return('mover-down')