from pygame import Vector2
from pygame.sprite import GroupSingle, groupcollide, collide_circle, spritecollide
from Models.Mapa.Tile import Tile
from Models.Personagem import Personagem

class GerenciadorColisao:
    #TODO: inserir inimigos
    def __init__(self, grupo_jogador, grupo_inimigos, grupo_obstaculos) -> None:
        self.__grupo_jogador = grupo_jogador
        self.__grupo_inimigos = grupo_inimigos
        self.__grupo_obstaculos = grupo_obstaculos

    def checar_colisao_obstaculo(self, personagem: GroupSingle) -> Tile:
        # jogador = self.__grupo_jogador.sprite()
        for obstaculo in self.__grupo_obstaculos:
            if obstaculo.rect.colliderect(personagem.sprite.rect):
                return obstaculo

    def checar_colisao_inimigo(self):
        jogador = self.__grupo_jogador.sprite
        if spritecollide(jogador, self.__grupo_inimigos, False, collide_circle):
            #TODO: inserir lógica para o estado do jogador (com ou sem armadura)
            return True
