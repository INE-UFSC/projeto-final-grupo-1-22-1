class Mapa:
    def __init__(self, largura_paredes: int, comprimento_tela: int, altura_tela: int):
        self.__largura_paredes = largura_paredes
        self.__comprimento_tela = comprimento_tela
        self.__altura_tela = altura_tela


    def __desenhar_paredes(tamanho, comprimento, high):
        door = 40
        #Desenho de retangulos, que recebe "window" = tela em que vai ser desenhado, (45,84,60) = Cor em RGB, [] = coordenadas dos pontos da diagonal principal, 0 = Tamanho da borda do retangulo
        pg.draw.rect(window, (45, 84, 60),[0, 0, comprimento-tamanho, tamanho], 0)
        pg.draw.rect(window, (45, 84, 60),[comprimento-tamanho, 0, comprimento, high/5], 0)
        pg.draw.rect(window, (45, 84, 60),[comprimento-tamanho, (high/5)+door , comprimento, (high*(4/5))-(door+tamanho)], 0)
        pg.draw.rect(window, (45, 84, 60),[tamanho, high-tamanho, comprimento, high], 0)
        pg.draw.rect(window, (45, 84, 60),[0, tamanho, tamanho, high-tamanho], 0)