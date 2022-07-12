from pygame.sprite import groupcollide, collide_circle, spritecollide, collide_mask
from pygame import Rect


class GerenciadorColisao():
  def __init__(self, tiles_list, grupo_jogador, grupo_obstaculos, grupo_inimigos):
    self.__tiles_list = tiles_list
    self.__grupo_inimigos = grupo_inimigos
    self.__grupo_jogador = grupo_jogador
    self.__grupo_obstaculos = grupo_obstaculos

  def checar_colisao_obstaculo(self, rect_personagem):
    for tile_sprite in self.__tiles_list:
      if Rect.colliderect(tile_sprite.rect, rect_personagem):
        return tile_sprite
    # if spritecollide(sprite_jogador, self.__grupo_obstaculos, False, collide_circle):
    #   return True

  def checar_colisao_inimigo(self, sprite_jogador):
    if spritecollide(sprite_jogador, self.__grupo_inimigos, False, collide_circle):
      return True

  def checar_colisao_inimigo2(self, sprite_jogador):
    if spritecollide(sprite_jogador, self.__grupo_inimigos, False, collide_mask):
      return True


  
