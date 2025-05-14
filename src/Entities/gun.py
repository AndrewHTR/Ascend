from modules.point_direction import get_angle, get_point_radius
from modules.utils           import debug_text, wave_text, draw_text
from .bullet                 import Bullet
import pygame as pg
import re, math

class Gun(pg.sprite.Sprite):
    def __init__(self, pos, image, capacity, fire_rate, reload, distance, delta, group, collision, resize = 1):
        super().__init__()
        self.group = group
        self.weapon_name = re.search("(spr).*png$", image)[0]

        self.start_ticks = 0
        self.seconds_passed = 0
        self.delta = delta

        self.image = pg.image.load(image)
        self.image = pg.transform.scale(self.image, (self.image.get_width() * resize, self.image.get_height() * resize))
        self.image_cp = self.image.copy()
        self.rect = self.image.get_rect(center = pos)

        self.direction = (0, 0)
        self.radius = 20

        self.start_ticks = 0
        
        self.seconds_passed = 0

        self.capacity = capacity
        self.ammo = capacity
        self.fire_rate = fire_rate
        self.reload_spd = reload
        self.distance = distance

        self.collision_list = collision

        self.teste = 1

    def reload(self):
        if self.ammo <= 0 and self.reload_spd < self.seconds_passed:
            self.ammo = self.capacity

    def fire(self, pos_player, pos_mouse):
        if self.ammo > 0 and self.fire_rate < self.seconds_passed:
            bullet = Bullet((10, 10), 'red', self.delta, self.collision_list, self.distance)
            bullet.add(self.group)
            gun_pos = get_point_radius(pos_player, pos_mouse, 0.9) # Get a point in a radius of the player to place the gun.
            bullet.fire((gun_pos[0], gun_pos[1] - 4), pos_mouse)
            self.ammo -= 1
            self.start_ticks = pg.time.get_ticks()

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
        seconds = (pg.time.get_ticks() - self.start_ticks) / 1000
        self.seconds_passed = seconds
        self.reload()
        #self.face_mouse()
        #debug_text(f"Sprite: {self.weapon_name}")
        #wave_text("Teste", "white", pg.display.get_surface(), pg.display.get_surface().get_width()//2, 100, self.teste)
        draw_text(f"Ammo: {self.ammo}", 'white', pg.display.get_surface(), 36, 32, origin="topleft")
        wave = (math.sin(self.teste))
        #print(wave)
        self.teste += 0.1

    def draw(self):
        pass
