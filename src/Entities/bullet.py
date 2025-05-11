from modules.point_direction import get_point_direction
import pygame as pg
import math


class Bullet(pg.sprite.Sprite):
    def __init__(self, size, color, delta, enemies):
        super().__init__()
        self.image = pg.Surface(size)
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.direction = (0, 0)

        self.start_ticks = 0
        self.seconds_passed = 0

        self.shot = 0

        self.spd = 0.5
        self.radius = 20
        self.delta = delta

        self.enemies = enemies

    # A bullet pega a posição do player e mouse, calcula a direção de vetor e normaliza ela
    # para que consigamos lançar a bala em uma direção
    
    def check_collision_enemy(self):
        for enemy in self.enemies:
            #print(self.rect.colliderect(enemy.rect))
            if self.rect.colliderect(enemy.rect):
                enemy.kill()

    def fire(self, pos_player, pos_mouse):
        self.start_ticks = pg.time.get_ticks()
        self.rect.center = pos_player
        
        pos = get_point_direction((pos_player[0], pos_player[1]), pos_mouse)
        #print(self.rect.centerx + 2 * math.degrees(pos[0]))
        self.direction = pg.Vector2(pos[0] * self.radius, pos[1] * self.radius)
        #print(self.direction)

    def update(self):
        self.rect.centerx += self.direction[0] * self.spd 
        self.rect.centery += self.direction[1] * self.spd 

        seconds = (pg.time.get_ticks() - self.start_ticks) / 1000
        self.seconds_passed = seconds
        if self.seconds_passed >= 1:
            self.seconds_passed = 0
            self.kill()
            
        self.check_collision_enemy()
        


    def draw(self):
        pass
