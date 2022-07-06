
import pygame as pg
from pygame.locals import *
from sys import exit
from pygame import font

from pygame.sprite import Group, GroupSingle

from Models.Jogador import Jogador
from Models.Desenhavel import Desenhavel
from Models.LeitorEventos import LeitorEventos
from Models.Controlador import Controlador
from Models.Obstaculo import Obstaculo
from Models.Inimigo import Inimigo
from Models.SpriteImage import SpriteImage
from Models.SpriteObstaculo import SpriteObstaculo
from Models.Vida import Vida

from Models.Window import Window
from Models.TelaCreditos import TelaCreditos
from Models.TelaMenu import TelaMenu

from Models.Configuracoes import Configuracoes

configuracoes = Configuracoes()

fonte = configuracoes.fonte

wall_size = 30

timer = pg.time.Clock()

width = 640
height = 480

pg.init()

vida = Vida()
jogador = Jogador()
inimigo = Inimigo()

grupo_jogador = GroupSingle(jogador.sprite)
grupo_obstaculos = Group(SpriteObstaculo(width/4, height/4),
                         SpriteObstaculo(width*3/4, height/4),
                         SpriteObstaculo(width/4, height*3/4),
                         SpriteObstaculo(width*3/4, height*3/4))

grupo_inimigos = GroupSingle(inimigo.sprite)

window = Window((width, height), "Cooper Temple - Alfa")
window_surface = window.surface

leitor_eventos = LeitorEventos()
controlador = Controlador(jogador, inimigo, grupo_jogador, grupo_obstaculos, grupo_inimigos)


#Na entrega final, essa lógica estará implementada usando OO

def draw_luz():
    points = [(width*7/15, height*10/12), (width*8/15, height*10/12), (width*5/8,30), (width*3/8,30)]
    pg.draw.polygon(window_surface, (174, 207, 136), points)

def draw_text(text, fonte, color, surface, x, y):
    textobj = fonte.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False

menu_principal = TelaMenu(leitor_eventos, window, fonte)

def main_menu():
    while True:
        escolha = menu_principal.renderizar_tela()
        # window_surface.fill((54,107,95))
        # draw_text('main menu', fonte, (255, 255, 255), window_surface, (width/2)-100, 20)
 
        # mx, my = pg.mouse.get_pos()
 
        # button_1 = pg.Rect((width/2)-100, 100, 200, 50)
        # button_2 = pg.Rect((width/2)-100, 200, 200, 50)
        # if button_1.collidepoint((mx, my)):
        #     if click:
        #         #Chamada do jogo
        #         game()
        # if button_2.collidepoint((mx, my)):
        #     if click:
        #         #chamada da segunda tela
        #         tela_creditos = TelaCreditos(leitor_eventos, window, fonte)
        #         tela_creditos.renderizar_tela()
        # pg.draw.rect(window_surface, (137, 199, 185), button_1)
        # pg.draw.rect(window_surface, (137, 199, 185), button_2)

        if escolha == 'OPCAO1':
            game()
        elif escolha == 'OPCAO2':
            tela_creditos = TelaCreditos(leitor_eventos, window, fonte)
            tela_creditos.renderizar_tela()
        
        click = False
        for event in pg.event.get():
            if event.type == QUIT:
                window.fechar()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    window.fechar()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pg.display.update()
        timer.tick(30)
    

def draw_cenario(size, width, height):
        door = 40
        #Desenho de retangulos, que recebe "window" = tela em que vai ser desenhado, (45,84,60) = Cor em RGB, [] = coordenadas dos pontos da diagonal principal, 0 = Tamanho da borda do retangulo
        pg.draw.rect(window_surface, (45, 84, 60),[0, 0, width-size, size], 0)
        pg.draw.rect(window_surface, (45, 84, 60),[width-size, 0, width, height/5], 0)
        pg.draw.rect(window_surface, (45, 84, 60),[width-size, (height/5)+door , width, (height*(4/5))-(door+size)], 0)
        pg.draw.rect(window_surface, (45, 84, 60),[size, height-size, width, height], 0)
        pg.draw.rect(window_surface, (45, 84, 60),[0, size, size, height-size], 0)

def game():
    x = width*3/4
    y = height/2
    speed = 5
    preto = (20,20,20)
    vermelho = (168, 101, 34)
    cor = preto
    counter = 0
    while True:
        timer.tick(30)

        counter += 1
        if counter % 120 == 0:
            controlador.gerar_coordenada()

        controlador.mover_inimigo()
        controlador.morte_jogador()

        # for event in pg.event.get():
        #     if event.type == QUIT:
        #         pg.quit()
        #         exit()

    #Chamada dos desenhos
        #Define a cor da tela no padrão RGB
        window_surface.fill((54,107,95))

        luz = draw_luz()

        #Detecta tecla pressionada
        # keys = pg.key.get_pressed()

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
        grupo_jogador.draw(window_surface)
        grupo_obstaculos.draw(window_surface)
        grupo_inimigos.draw(window_surface)

        evento = leitor_eventos.ler_evento()
        controlador.mover_personagem(evento, jogador)


        grupo_jogador.update()
        grupo_obstaculos.update()

        draw_cenario(30,width, height)

        vida.atualizar_vida(jogador.vida, window_surface)

        pg.display.flip() #Precisa estar no final do algoritmo

main_menu()