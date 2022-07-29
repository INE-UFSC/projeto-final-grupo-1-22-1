import pygame as pg
from pygame import MOUSEBUTTONUP, event
import time


class Button():
    def __init__(self, x, y, default_image, hover_image, scale):
        self.default_image = default_image
        self.hover_image = hover_image
        self.scale = scale
        self.image = self.scale_image(default_image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.hovered = False

    def scale_image(self, image):
        return pg.transform.scale(
            image, (int(image.get_width() * self.scale), int(image.get_height() * self.scale)))

    def draw(self, surface):
        self.image = self.scale_image(
            self.hover_image if self.hovered else self.default_image)
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def read_events(self):
        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.hovered = True
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                time.sleep(0.2)
        else:
            self.hovered = False

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
