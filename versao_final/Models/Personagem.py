from abc import ABC, abstractmethod
from re import X
from Models.Desenhavel import Desenhavel 
import pygame as pg
import math
 
class Personagem(Desenhavel, ABC):
    @abstractmethod
    def __init__(self, image_path: str, velocidade: int = 1, position : tuple = (0,0)):
        super().__init__(image_path, position)
        self.__sentido_imagem = 'cima'
        self.__velocidade = velocidade
        self.__rotacao = 0
        self.__angulo = 0
        self.__precisa_rotar = 0
        self.imagem = pg.transform.rotate(self.image, self.__rotacao%360) 
    
    def get_imagem(self):
        return self.imagem

    @property
    def angulo(self):
        return self.__angulo

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

    def __girar_imagem_inim(self, c_p, c_i) -> None:
        #self.__angulo = 0
        dif_x = c_p[0] - c_i[0]
        dif_y = c_p[1] - c_i[1] 
        distancia = (dif_x**2 + dif_y**2)**(1/2)
        sen = dif_x / distancia 
        self.__angulo = int(math.degrees(math.asin(sen)))

        if self.__angulo > 0:
            if c_p[1] < c_i[1]:
                #if int(self.__angulo) % 360 > self.__rotacao % 360:
                self.__precisa_rotar = 90 - self.__angulo
                #elif int(self.__angulo) % 360 < self.__rotacao % 360:
                    
            else:
                #if self.__angulo % 360 > self.__rotacao % 360:
                #    self.__precisa_rotar 
                #elif self.__angulo % 360 < self.__rotacao % 360:
                self.__precisa_rotar = 270 + self.__angulo

        else:
            if c_p[1] < c_i[1]:
                #if self.__angulo % 360 > self.__rotacao % 360:
                self.__precisa_rotar = 90 + abs(self.__angulo)   
                #elif self.__angulo % 360 < self.__rotacao % 360:
                    
            else:
                self.__precisa_rotar = 180 + (90 + self.__angulo)
                #if self.__angulo % 360 > self.__rotacao % 360:
                    
                #elif self.__angulo % 360 < self.__rotacao % 360:
                    
       # print(self.__precisa_rotar)
        
        if self.__precisa_rotar > self.__rotacao%360:

            if self.__precisa_rotar < self.__rotacao%360 + 180:

                self.__rotacao += 3
            else:

                self.__rotacao -= 3

        elif self.__precisa_rotar < self.__rotacao%360:

            if self.__precisa_rotar > self.__rotacao%360 - 180:

                self.__rotacao -= 3
            else:
                self.__rotacao += 3

        
        """
        print(self.__precisa_rotar)
        if self.__precisa_rotar > self.__rotacao % 360:
            self.__rotacao += 1
        elif self.__precisa_rotar < self.__rotacao % 360:
            self.__rotacao -= 1
        else:
            self.__rotacao = self.__rotacao
        """
        #print(self.__angulo%360, self.__rotacao%360)
        #try:
            #self.__angulo = math.degrees(math.acos((c_p[0] - 600 * c_i[0] - 600 + c_p[1] - 357 * c_i[1] - 357) / (math.sqrt((c_p[0] - 600)**2 + (c_p[1] - 357)**2) * math.sqrt((c_i[0] - 600)**2 + (c_i[1] - 357)**2))))  
            #print(self.__angulo)
        #except:
        #self.__angulo = self.__angulo - math.degrees(math.asin(seno))
        self.imagem = pg.transform.rotate(self.image, self.__rotacao)  

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
    
    def mover_inim(self, c_p, c_i, x, y) -> None:
        if 0 <= self.__precisa_rotar - (self.__rotacao % 360) <= 3 :
            self.rect.x += x
            self.rect.y += y
        self.__girar_imagem_inim(c_p, c_i)

    def get_coordenadas(self) -> tuple:
        return self.rect.center
