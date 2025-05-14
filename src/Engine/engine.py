from Entities.player import Player
from Entities.enemy  import Enemy
from Engine.block    import Block
import pygame as pg
import random

from settings import *

class Level:
    def __init__(self):
        self.surface = pg.display.get_surface()
        self.delta = 0

        self.enemies = []

        #self.visible_sprites = CameraGroup()
        self.visible_sprites = pg.sprite.Group()
        self.active_sprites  = pg.sprite.Group()
        self.collision_list = []

        for i in range(WIDTH):
            self.block = Block((i * SIZE, 0), 'white', [self.visible_sprites], self.delta)
            #self.block = Block((i * SIZE, HEIGHT - SIZE), 'white', [self.visible_sprites], self.delta)
            self.collision_list.append(self.block)

        for i in range(HEIGHT):
            self.block = Block((0, i * SIZE), 'white', [self.visible_sprites], self.delta)
            #self.block = Block((WIDTH - SIZE, i * SIZE), 'white', [self.visible_sprites], self.delta)
            self.collision_list.append(self.block)

        #self.setup_level()
        for i in range(2):
            self.enemies.append(Enemy((random.randint(20, self.surface.get_width() - 32), random.randint(50, self.surface.get_height() - 32)), (32, 32), 'orange', [self.visible_sprites, self.active_sprites], self.delta))
            self.collision_list.append(self.enemies[i])

        self.player = Player((40, 40), [self.visible_sprites, self.active_sprites], self.delta, self.enemies, self.collision_list)
    
    def run(self, delta):
        self.delta = delta
        self.active_sprites.update()
        #self.visible_sprites.custom_draw(self.player) # type: ignore
        self.visible_sprites.draw(self.surface)

class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()

        cam_left = CAMERA_BORDERS["left"]
        cam_top = CAMERA_BORDERS["top"]
        cam_width = self.display_surface.get_size()[0] - (cam_left + CAMERA_BORDERS["right"])
        cam_height = self.display_surface.get_size()[1] - (cam_top + CAMERA_BORDERS["bottom"])

        self.camera_rect = pg.Rect(cam_left, cam_top, cam_width, cam_height)

    def custom_draw(self, player):
        #print(self.camera_rect)

        if player.rect.left < self.camera_rect.left:
            self.camera_rect.left = player.rect.left

        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right
			
        if player.rect.top < self.camera_rect.top:
            self.camera_rect.top = player.rect.top

        if player.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom

        if self.camera_rect.x <= 0:
            self.camera_rect.x = 0 + CAMERA_BORDERS["left"]
        elif self.camera_rect.x >= self.display_surface.get_width():
            self.camera_rect.x = self.display_surface.get_width()

        if self.camera_rect.y <= 0:
            self.camera_rect.y = 0

        elif self.camera_rect.y >= self.display_surface.get_height():
            self.camera_rect.y = self.display_surface.get_height()
        self.offset = pg.math.Vector2(self.camera_rect.left - CAMERA_BORDERS["left"], self.camera_rect.top - CAMERA_BORDERS["top"])

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)