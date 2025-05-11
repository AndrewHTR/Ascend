import pygame as pg
import math, os
from modules.point_direction import get_angle, get_point_direction, get_point_radius
from .bullet                 import Bullet
from .gun                    import Gun

class Player(pg.sprite.Sprite):
    def __init__(self, pos, group, delta, enemies):
        super().__init__(group)
        self.group = group
        
        # Time variables
        self.delta = delta
        self.start_ticks = 0
        self.seconds_passed = 0
        
        # Sprite variables
        self.angle = 25
        self.image = pg.image.load("./src/Sprites/spr_player_idle.png").convert_alpha()
        self.image_cp = self.image.copy()
        self.rect = self.image.get_rect(topleft = pos)

        # Movement variables
        self.mov = pg.Vector2(0, 0)
        self.spd = 6

        # Collision variables
        self.enemies = enemies

        # Gun variables
        self.fire_rate = 5
        self.inventory = []
        
        path = os.path.dirname("src/Sprites/")
        image1 = os.path.join(path, "spr_basic_gun.png")
        image2 = os.path.join(path, "spr_basic_gun_2.png")

        self.gun1 = Gun((self.rect.centerx + 50, self.rect.centery + 50), image1, 5, self.fire_rate, 5, self.delta, self.group, self.enemies, 1)
        self.gun2 = Gun((self.rect.centerx + 50, self.rect.centery + 50), image2, 5, self.fire_rate, 10, self.delta, self.group, self.enemies, 1.5)
        self.inventory.append(self.gun1)
        self.inventory.append(self.gun2)
        self.gun = self.inventory[0]
        self.gun.add(group)
    
    def change_weapon(self, weapon):
        self.gun.kill()
        self.gun = weapon
        self.gun.add(self.group)

    def movement(self, mouse):
        self.keys = pg.key.get_pressed()
    
        if self.keys[pg.K_w]:
            self.mov[1] = -1 # type: ignore
        elif self.keys[pg.K_s]:
            self.mov[1] = 1 # type: ignore 

        else:
            self.mov[1] = 0

        if self.keys[pg.K_a]:
            self.mov[0] = -1 # type: ignore
        elif self.keys[pg.K_d]:
            self.mov[0] = 1 # type: ignore
    
        else:
            self.mov[0] = 0

        just_p = pg.key.get_just_pressed()

        if just_p[pg.K_r]:
            self.change_weapon(self.inventory[1])

        if just_p[pg.K_e]:
            self.change_weapon(self.inventory[0])

        # Rotates sprite angle having the mouse as a base
        #self.angle = get_angle(self.rect.center, mouse) 
        #self.image = pg.transform.rotate(self.image_cp, self.angle)
        #self.rect  = self.image.get_rect(center = self.rect.center)
        
        self.rect.y += (self.mov[1] * (math.sqrt(2)/2)) * self.spd
        self.rect.x += (self.mov[0] * (math.sqrt(2)/2)) * self.spd
        
        mouse = pg.mouse.get_pos()

        gun_pos = get_point_radius(self.rect.center, mouse)
        self.gun.face_mouse((gun_pos[0], gun_pos[1]))

    def fire(self, mouse):
        self.keys = pg.key.get_just_pressed()

        if self.keys[pg.K_SPACE]:
            self.start_ticks = pg.time.get_ticks()
            self.gun.fire(self.rect.center, mouse)
            #print(self.gun.group)
            
    def input(self):
        mouse = pg.mouse.get_pos()
        self.movement(mouse)
        self.fire(mouse)

    def update(self):
        self.input()
        seconds = (pg.time.get_ticks() - self.start_ticks) / 1000
        self.seconds_passed = seconds

    def draw(self):
        pass
