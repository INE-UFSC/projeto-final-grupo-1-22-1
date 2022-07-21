from pygame import Vector2
from pygame.sprite import GroupSingle, groupcollide, collide_circle, spritecollide
from Models.Mapa.Tile import Tile
from Models.Personagem import Personagem


class GerenciadorColisao:
    def __init__(self, grupo_jogador, grupo_inimigos, grupo_obstaculos, grupo_armaduras) -> None:
        self.__grupo_jogador = grupo_jogador
        self.__grupo_inimigos = grupo_inimigos
        self.__grupo_obstaculos = grupo_obstaculos
        self.__grupo_armaduras = grupo_armaduras

    def checar_colisao_obstaculo(self, personagem: GroupSingle) -> Tile:
        # jogador = self.__grupo_jogador.sprite()
        for obstaculo in self.__grupo_obstaculos:
            if obstaculo.rect.colliderect(personagem.sprite.rect):
                return obstaculo

    def checar_colisao_inimigo(self):
        jogador = self.__grupo_jogador.sprite
        inimigos_colididos = spritecollide(jogador, self.__grupo_inimigos, False, collide_circle)
        if inimigos_colididos:
            if jogador.armadura:
                jogador.armadura = None
                inimigos_colididos[0].kill()
            else:
                jogador.renascer(jogador.posicao_inicial)
                jogador.diminuir_vida()
            return True


    def checar_colisao_armadura(self):
        sprite_jogador = self.__grupo_jogador.sprite
        for armadura in self.__grupo_armaduras:
            if armadura.rect.colliderect(sprite_jogador.rect):
                return armadura
