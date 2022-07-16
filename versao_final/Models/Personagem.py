from abc import ABC, abstractmethod
from Models.Desenhavel import Desenhavel 
import pygame as pg
from pygame.math import Vector2
 
class Personagem(Desenhavel, ABC):
    @abstractmethod
    def __init__(self, image_path: str, velocidade: int = 1, position : tuple = (0,0)):
        super().__init__(image_path, position)
        self.__sentido_imagem = 'cima'
        self.__velocidade = velocidade
        self.__direcao = Vector2(0,0)

    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    @property 
    def direcao(self):
        return self.__direcao

    def get_dirx(self):
        return self.__direcao.x

    def get_diry(self):
        return self.__direcao.y

    def get_dir(self):
        return self.__direcao
    
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

    

    def __mover_x(self) -> None:
        self.rect.x += self.__direcao.x * self.__velocidade
        self.__direcao.y = 0
    
    def __mover_y(self) -> None:
        self.__direcao.x = 0
        self.rect.y += self.__direcao.y * self.__velocidade
    
    def mover_direita(self) -> None:
        self.__direcao.x = 1
        self.__mover_x()
        self.__girar_imagem('direita')

    def mover_esquerda(self) -> None:
        self.__direcao.x = -1
        self.__mover_x()
        self.__girar_imagem('esquerda')

    def mover_cima(self) -> None:
        self.__direcao.y = -1
        self.__mover_y()
        self.__girar_imagem('cima')

    def mover_baixo(self) -> None:
        self.__direcao.y = 1
        self.__mover_y()
        self.__girar_imagem('baixo')

    def parar(self) -> None:
        self.__direcao.x = 0
        self.__direcao.y = 0

    def get_centerx(self) -> int:
        return self.rect.centerx

    def get_centery(self) -> int:
        return self.rect.centery
    
    def get_coordenadas(self) -> tuple:
        return self.rect.center