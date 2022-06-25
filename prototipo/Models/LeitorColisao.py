from pygame.sprite import groupcollide, collide_circle, spritecollide


class LeitorColisao():
  def __init__(self, grupo_jogador, grupo_obstaculos):
    self.__grupo_jogador = grupo_jogador
    self.__grupo_obstaculos = grupo_obstaculos

  def checar_colisao(self, sprite_jogador):
    if spritecollide(sprite_jogador, self.__grupo_obstaculos, False, collide_circle):
      return True

  
