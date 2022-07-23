from Models.Desenhavel import Desenhavel


class Tile(Desenhavel):
    def __init__(self, position, size):
        super().__init__("Images/Tijolo.png", position, size)
