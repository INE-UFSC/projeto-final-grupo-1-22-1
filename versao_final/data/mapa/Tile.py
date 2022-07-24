from data.Desenhavel import Desenhavel


class Tile(Desenhavel):
    def __init__(self, position, size):
        super().__init__("resources/images/Tijolo.png", position, size)
