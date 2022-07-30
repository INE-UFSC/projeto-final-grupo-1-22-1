from abc import ABC, abstractmethod
import pygame as pg
from pygame.sprite import Sprite
from pygame.image import load


class Desenhavel(Sprite, ABC):
    @abstractmethod
    def __init__(self, image_path: str, position: tuple = (0, 0), size=None):
        super().__init__()
        loaded_image = load(image_path)
        self.__image = pg.transform.scale(
            loaded_image, (size, size)) if size else loaded_image
        self.__rect = self.__image.get_rect(topleft=position)
        self.__position = position

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        self.__image = image

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    @property
    def position(self):
        return self.__position

    def set_rect_left(self, valor): self.__rect.left = valor

    def set_rect_right(self, valor): self.__rect.right = valor

    def set_rect_top(self, valor): self.__rect.top = valor

    def set_rect_bottom(self, valor): self.__rect.bottom = valor

    def get_rect_left(self):
        return self.__rect.left

    def get_rect_right(self):
        return self.__rect.right

    def get_rect_top(self):
        return self.__rect.top

    def get_rect_bottom(self):
        return self.__rect.bottom

    def update(self, deslocamento_x):
        self.__rect.x += deslocamento_x