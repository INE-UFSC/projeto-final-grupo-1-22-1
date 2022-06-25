
import pygame as pg
from pygame.locals import *
from sys import exit

from pygame.sprite import Group, GroupSingle

from Models.Jogador import Jogador
from Models.Desenhavel import Desenhavel
from Models.LeitorEventos import LeitorEventos
from Models.ControladorMovimentos import ControladorMovimentos
from Models.Obstaculo import Obstaculo
from Models.SpriteObstaculo import SpriteObstaculo
from Models.Inimigo import Inimigo



def draw_cenario(size, width, high):
    door = 40

    #Desenho de retangulos, que recebe "window" = tela em que vai ser desenhado, (45,84,60) = Cor em RGB, [] = coordenadas dos pontos da diagonal principal, 0 = Tamanho da borda do retangulo
    pg.draw.rect(window, (45, 84, 60),[0, 0, width-size, size], 0)
    pg.draw.rect(window, (45, 84, 60),[width-size, 0, width, high/5], 0)
    pg.draw.rect(window, (45, 84, 60),[width-size, (high/5)+door , width, (high*(4/5))-(door+size)], 0)
    pg.draw.rect(window, (45, 84, 60),[size, high-size, width, high], 0)
    pg.draw.rect(window, (45, 84, 60),[0, size, size, high-size], 0)
    # pg.draw.circle(window, (45, 84, 60),[width/4, high/4], 40)
    # pg.draw.circle(window, (45, 84, 60),[width*3/4, high/4], 40)
    # pg.draw.circle(window, (45, 84, 60),[width/4, high*3/4], 40)
    # pg.draw.circle(window, (45, 84, 60),[width*3/4, high*3/4], 40)

def draw_luz():
    points = [(width*7/15, high*10/12), (width*8/15, high*10/12), (width*5/8,30), (width*3/8,30)]
    pg.draw.polygon(window, (174, 207, 136), points)



wall_size = 30

timer = pg.time.Clock()

width = 640
high = 480


x = width*3/4
y = high/2
speed = 5
preto = (20,20,20)
vermelho = (168, 101, 34)
cor = preto

pg.init()

#Setando tamanho da tela

window = pg.display.set_mode(
    size=(width, high),
    flags=0,
    depth=0,
    display=0,
    vsync=0 #tira sincronização do tipo raster
)

pg.display.set_caption('Cooper Temple - Alfa')





jogador = Jogador()
inimigo = Inimigo()

grupo_jogador = GroupSingle(jogador.sprite)
grupo_obstaculos = Group(SpriteObstaculo(width/4, high/4),
                         SpriteObstaculo(width*3/4, high/4),
                         SpriteObstaculo(width/4, high*3/4),
                         SpriteObstaculo(width*3/4, high*3/4))

grupo_inimigos = GroupSingle(inimigo.sprite)


leitor_eventos = LeitorEventos()
controlador_movimentos = ControladorMovimentos(jogador, grupo_jogador, grupo_obstaculos)

while True:
    timer.tick(30)
    
    # for event in pg.event.get():
    #     if event.type == QUIT:
    #         pg.quit()
    #         exit()

#Chamada dos desenhos
    #Define a cor da tela no padrão RGB
    window.fill((54,107,95))

    #Desenha o circulo do personagem
    luz = draw_luz()
    personagem = pg.draw.circle(window, (cor),[x, y], 10)

    #Detecta tecla pressionada
    keys = pg.key.get_pressed()

    # #Se a tecla for pressionada, então:
    # if keys[pg.K_DOWN]:
    #     #Se a tecla de seta para baixo for pressionada, acrescenta o valor de speed na variavel y
    #     y += speed
    # if keys[pg.K_UP]:
    #     y -= speed
    # if keys[pg.K_LEFT]:
    #     x -= speed
    # if keys[pg.K_RIGHT]:
    #     x += speed

    #Desenhando os grupos a cada ciclo de clock
    grupo_jogador.draw(window)
    grupo_obstaculos.draw(window)
    grupo_inimigos.draw(window)

    evento = leitor_eventos.ler_evento()
    controlador_movimentos.mover_personagem(evento, jogador)


    grupo_jogador.update()
    grupo_obstaculos.update()

    draw_cenario(wall_size, width, high)

    pg.display.flip() #Precisa estar no final do algoritmo