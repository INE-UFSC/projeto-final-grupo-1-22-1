from pygame.sprite import groupcollide, collide_circle, spritecollide, collide_mask


class LeitorColisao():
  def __init__(self, grupo_jogador, grupo_obstaculos, grupo_inimigos):
    self.__grupo_inimigos = grupo_inimigos
    self.__grupo_jogador = grupo_jogador
    self.__grupo_obstaculos = grupo_obstaculos

  def checar_colisao_obstaculo(self, sprite_jogador):
    if spritecollide(sprite_jogador, self.__grupo_obstaculos, False, collide_circle):
      return True

  def checar_colisao_inimigo(self, sprite_jogador):
    if spritecollide(sprite_jogador, self.__grupo_inimigos, False, collide_circle):
      return True

  def checar_colisao_inimigo2(self, sprite_jogador):
    if spritecollide(sprite_jogador, self.__grupo_inimigos, False, collide_mask):
      sprite_jogador.image.fill('red')
      return True

  
