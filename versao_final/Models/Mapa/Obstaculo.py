from Models.Desenhavel import Desenhavel


class Obstaculo(Desenhavel):
    def __init__(self, position, size):
        super().__init__("Images/Tijolo.png", position, size)
