from pygame.sprite import GroupSingle
from Models.Mapa.Tile import Tile
from Models.Personagem import Personagem

class GerenciadorColisao:
    #TODO: inserir inimigos
    # self.__grupo_inimigos = grupo_inimigos
    def __init__(self, grupo_jogador, grupo_obstaculos) -> None:
        self.__grupo_jogador = grupo_jogador
        self.__grupo_obstaculos = grupo_obstaculos

    def checar_colisao_obstaculo(self, personagem: GroupSingle) -> Tile:
        # jogador = self.__grupo_jogador.sprite()
        for obstaculo in self.__grupo_obstaculos:
            if obstaculo.rect.colliderect(personagem.sprite.rect):
                return obstaculo
    
