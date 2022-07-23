from Models.Desenhavel import Desenhavel


class Bau(Desenhavel):
    def __init__(self, position):
        super().__init__("Images/Explorador.png", position)
