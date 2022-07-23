
from Models.Desenhavel import Desenhavel


class Armadura(Desenhavel):
    def __init__(self, position):
        super().__init__("Images/ArmaduraOff.png", position)
