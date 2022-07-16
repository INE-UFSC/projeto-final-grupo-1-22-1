import pygame as pg


class Button():
    def __init__(self, x, y, image_off, image_on, scale):
        self.image_off = image_off
        self.image_on = image_on
        self.image = image_off
        width = self.image_off.get_width()
        height = self.image_off.get_height()
        self.image = pg.transform.scale(
            self.image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def clique(self, surface):
        action = False

        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.image = self.image_on
            # TODO: remover imagem por baixo
            self.draw(surface)
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
