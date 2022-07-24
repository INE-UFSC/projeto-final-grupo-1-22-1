from data.Desenhavel import Desenhavel


class Bau(Desenhavel):
    def __init__(self, position):
        super().__init__("resources/images/Explorador.png", position)
