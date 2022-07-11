from abc import ABC, abstractmethod
from Models.Desenhavel import Desenhavel 
import pygame as pg
 
class Personagem(Desenhavel, ABC):
    @abstractmethod
    def __init__(self, image_path: str, velocidade: int = 1, position : tuple = (0,0)):
        super().__init__(image_path, position)
        self.__sentido_imagem = 'cima'
        self.__velocidade = velocidade

    def __get_angulo_rotacao(self, sentido_final: str) -> int:
        sentidos = {'cima' : 90,
                    'direita': 0,
                    'baixo': 270,
                    'esquerda': 180}
        return sentidos[sentido_final] - sentidos[self.__sentido_imagem]
    
    def __girar_imagem(self, sentido_final: str) -> None:
        if self.__sentido_imagem != sentido_final:
            self.image = pg.transform.rotate(self.image, self.__get_angulo_rotacao(sentido_final))
        self.__sentido_imagem = sentido_final


    def mover_direita(self) -> None:
        self.rect.x += self.__velocidade
        self.__girar_imagem('direita')

    def mover_esquerda(self) -> None:
        self.rect.x -= self.__velocidade
        self.__girar_imagem('esquerda')

    def mover_cima(self) -> None:
        self.rect.y -= self.__velocidade
        self.__girar_imagem('cima')

    def mover_baixo(self) -> None:
        self.rect.y += self.__velocidade
        self.__girar_imagem('baixo')

    def get_coordenadas(self) -> tuple:
        return self.rect.center