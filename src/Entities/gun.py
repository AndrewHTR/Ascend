from modules.point_direction import get_angle, get_point_radius
from modules.utils           import debug_text
from .bullet                 import Bullet
import pygame as pg


class Gun(pg.sprite.Sprite):
    def __init__(self, pos, ammo, fire_rate, reload, delta, group, enemies):
        super().__init__()
        self.group = group

        self.start_ticks = 0
        self.seconds_passed = 0
        self.delta = delta

        self.image = pg.image.load("./src/Sprites/spr_basic_gun.png")
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 1.5, self.image.get_height() * 1.5))
        self.image_cp = self.image.copy()
        self.rect = self.image.get_rect(center = pos)

        self.direction = (0, 0)
        self.radius = 20

        self.ammo = ammo
        self.fire_rate = fire_rate
        self.reload = reload

        self.enemies = enemies

    def fire(self, pos_player, pos_mouse):
        bullet = Bullet((10, 10), 'red', self.delta, self.enemies)
        bullet.add(self.group)
        gun_pos = get_point_radius(pos_player, pos_mouse, 0.9) # Get a point in a radius of the player to place the gun.
        bullet.fire((gun_pos[0], gun_pos[1] - 4), pos_mouse)
        #print(self.direction)

    def face_mouse(self, pos_player):
        mouse = pg.mouse.get_pos()
        self.angle = get_angle(self.rect.center, mouse) 
        self.image = pg.transform.rotate(self.image_cp, self.angle + 90)
        self.rect  = self.image.get_rect(center = pos_player)

        if self.angle >= 0:
            #debug_text("Positive angle", origin="sla")
            image_flip = pg.transform.flip(self.image_cp, False, True)
            self.image = pg.transform.rotate(image_flip, self.angle + 90)
            

    def update(self):
        #self.rect.centerx += self.direction[0] * self.spd 
        #self.rect.centery += self.direction[1] * self.spd 

        #self.face_mouse()
        debug_text(f"Weapon: {self.reload}")

    def draw(self):
        pass
