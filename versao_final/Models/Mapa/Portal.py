from Models.Desenhavel import Desenhavel


class Portal(Desenhavel):
    def __init__(self, position, size):
        super().__init__("Images/portal.png", position, size)