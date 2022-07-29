from classes.desenhaveis.Desenhavel import Desenhavel

class Bau(Desenhavel):
    def __init__(self, position):
        super().__init__("recursos/imagens/Tesouro.png", position)
