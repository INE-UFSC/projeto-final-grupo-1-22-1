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