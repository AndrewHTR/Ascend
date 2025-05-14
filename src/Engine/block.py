import pygame as pg

from settings import *

class Block(pg.sprite.Sprite):
    def __init__(self, pos, color, group, delta):
        super().__init__(group)
        
        self.image = pg.Surface((SIZE, SIZE))
        self.image.fill(color)
        self.group = group
        self.direction = (0, 0)

        self.rect = self.image.get_rect(topleft = pos)

    def update(self):
        pass

    def draw(self):
        pass
