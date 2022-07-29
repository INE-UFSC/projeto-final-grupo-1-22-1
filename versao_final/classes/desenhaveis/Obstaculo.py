from classes.desenhaveis.Desenhavel import Desenhavel


class Obstaculo(Desenhavel):
    def __init__(self, position, size):
        super().__init__("recursos/imagens/Tijolo.png", position, size)
