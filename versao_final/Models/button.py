import pygame as pg


class Button():
    def __init__(self, x, y, image1, image2, scale):
        self.image1 = image1
        self.image2 = image2
        self.image = image1
        width = self.image1.get_width()
        height = self.image1.get_height()
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
            self.image = self.image2
            # TODO: remover imagem por baixo
            self.draw(surface)
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False


        return action
