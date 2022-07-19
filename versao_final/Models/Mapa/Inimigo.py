from re import L
import pygame as pg
from Models.Personagem import Personagem
from random import randint
from Models.Lanterna import Lanterna
import math

class Inimigo(Personagem):
  def __init__(self, velocidade, posicao):
    super().__init__('Images/Cientista.png', velocidade, posicao)
    self.__rotacao = 0
    self.__angulo = 0
    self.__precisa_rotar = 0
    self.__lanterna = Lanterna(self.get_coordenadas(), 50)
    self.imagem = pg.transform.rotate(self.image, self.__rotacao%360) 
    
  def draw(self, window):
    window.blit(self.imagem, self.get_coordenadas())
    #TODO: Arrumar posicao lanterna 
    #window.blit(self.__lanterna.image, self.get_coordenadas())

  def update(self, deslocamento_x, deslocamento_y):
    self.rect.x += deslocamento_x
    self.rect.y += deslocamento_y

  def __girar_imagem(self, c_p, c_i, janela) -> None:
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
        #TODO : Substituir método por self.draw()
        janela.blit(self.imagem, (self.get_coordenadas()[0] - int(self.imagem.get_width()) / 2, self.get_coordenadas()[1] - int(self.imagem.get_height()) / 2))  
  
  def mover_inim(self, c_p, c_i, x, y, janela) -> None:
        if 0 <= self.__precisa_rotar - (self.__rotacao % 360) <= 3 :                                                                              
            self.rect.x += x
            self.rect.y += y
        self.__girar_imagem(c_p, c_i, janela)                     

  def seguir_jogador(self, coordenada: tuple, janela):
    x_atual = self.rect.x
    y_atual = self.rect.y
    x_player = coordenada[0]                                                                                       
    y_player = coordenada[1]

    if y_player < y_atual:
      #Segundo Quadrante
      if x_player < x_atual:                                      #-1, -1
        self.mover_inim((x_player, y_player), (x_atual, y_atual), -self.velocidade, -self.velocidade, janela)
      #Primeiro Quadrante
      elif x_player > x_atual:                                    #1, -1
        self.mover_inim((x_player, y_player), (x_atual, y_atual), self.velocidade, -self.velocidade, janela)
      #Mesma linha, mas encima
      else:                                                       #0, -1
        self.mover_inim((x_player, y_player), (x_atual, y_atual), 0, -self.velocidade, janela)
    elif y_player > y_atual:
      if x_player > x_atual:                                      #1, 1
        self.mover_inim((x_player, y_player), (x_atual, y_atual), self.velocidade, self.velocidade, janela)
      elif x_player < x_atual:                                    #1, 1
        self.mover_inim((x_player, y_player), (x_atual, y_atual), -self.velocidade, self.velocidade, janela)
      else:                                                       #1, 0
        self.mover_inim((x_player, y_player), (x_atual, y_atual), self.velocidade, 0, janela)
    else:
      if x_player > x_atual:                                      #1, 0
        self.mover_inim((x_player, y_player), (x_atual, y_atual), self.velocidade, 0, janela)
      else:                                                       #1, 0
        self.mover_inim((x_player, y_player), (x_atual, y_atual), -self.velocidade, 0, janela)
  
  def pegar_tesouro(self, coordenada):
    pass
