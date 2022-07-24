
from data.Desenhavel import Desenhavel


class Armadura(Desenhavel):
    def __init__(self, position):
        super().__init__("resources/images/ArmaduraOff.png", position)
