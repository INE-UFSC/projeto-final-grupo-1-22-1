from classes.desenhaveis.Desenhavel import Desenhavel


class Portal(Desenhavel):
    def __init__(self, position, size):
        super().__init__("recursos/imagens/portal.png", position, size)