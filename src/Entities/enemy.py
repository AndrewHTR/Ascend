import pygame as pg
import math
from modules.point_direction import get_point_direction
from .bullet import Bullet

class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, size, color, group, delta):
        super().__init__(group)
        
        self.start_ticks = 0
        self.seconds_passed = 0

        self.delta = delta

        self.image = pg.image.load("./src/Sprites/spr_enemy_idle.png").convert_alpha()
        #self.image.fill(color)
        self.group = group
        self.direction = (0, 0)

        self.rect = self.image.get_rect(topleft = pos)
        self.radius = 20

        self.mov = pg.Vector2(0, 0)

        self.spd = 6


    def movement(self, pos_player):
        pos = get_point_direction(self.rect.center, pos_player)
        self.direction = pg.Vector2(pos[0] * self.radius, pos[1] * self.radius)
        #print(self.direction)

    def update(self):
        self.rect.centerx += self.direction[0] * self.spd 
        self.rect.centery += self.direction[1] * self.spd 

        seconds = (pg.time.get_ticks() - self.start_ticks) / 1000
        self.seconds_passed = seconds

    def draw(self):
        pass
