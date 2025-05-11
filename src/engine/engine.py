import pygame as pg
from Entities.player import Player
from Entities.enemy  import Enemy
import random

class Level:
    def __init__(self):
        self.surface = pg.display.get_surface()
        self.delta = 0

        self.enemies = []

        self.visible_sprites = pg.sprite.Group()
        self.active_sprites  = pg.sprite.Group()

        #self.setup_level()
        for i in range(2):
            self.enemies.append(Enemy((random.randint(20, self.surface.get_width() - 32), random.randint(50, self.surface.get_height() - 32)), (32, 32), 'orange', [self.visible_sprites, self.active_sprites], self.delta))
            
        self.player = Player((20, 20), [self.visible_sprites, self.active_sprites], self.delta, self.enemies)

    def run(self, delta):
        self.delta = delta
        self.active_sprites.update()
        self.visible_sprites.draw(self.surface) # type: ignore
