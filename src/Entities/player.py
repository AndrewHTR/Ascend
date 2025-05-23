import pygame as pg
import math, os
from modules.point_direction import get_angle, get_point_direction, get_point_radius
from modules.utils           import debug_text
from .bullet                 import Bullet
from .gun                    import Gun

class Player(pg.sprite.Sprite):
    def __init__(self, pos, group, delta, collision):
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
        self.collision_list = collision

        # Gun variables
        self.fire_rate = 5
        self.inventory = []
        
        path = os.path.dirname("src/Sprites/")
        image1 = os.path.join(path, "spr_basic_gun.png")
        image2 = os.path.join(path, "spr_basic_gun_2.png")

        self.gun1 = Gun((self.rect.centerx + 50, self.rect.centery + 50), image1, 15, 0.5, 5, 1, self.delta, self.group, self.collision_list, 1)
        self.gun2 = Gun((self.rect.centerx + 50, self.rect.centery + 50), image2, 5, 0.2, 3, 2, self.delta, self.group, self.collision_list, 1.5)
        self.inventory.append(self.gun1)
        self.inventory.append(self.gun2)
        self.gun = self.inventory[0]
        self.gun.add(group)
    
    def check_h_collision(self):
        for x in self.collision_list["Block"]:
            print(self.collision_list)
            if x.rect.colliderect(self.rect) and x.alive():
                if self.mov[0] < 0:
                    self.mov[0] = 0
                    self.rect.left = x.rect.right
                if self.mov[0] > 0:
                    self.mov[0] = 0
                    self.rect.right = x.rect.left
    
    def check_v_collision(self):
        self.check_h_collision()
        for y in self.collision_list["Block"]:
            if self.rect.colliderect(y.rect) and y.alive():
                if self.mov[1] < 0:
                    self.mov[1] = 0
                    self.rect.top = y.rect.bottom
                
                if self.mov[1] > 0:
                    self.mov[1] = 0
                    self.rect.bottom = y.rect.top
            
    def check_collision(self):
        self.check_v_collision()

    def change_weapon(self, weapon):
        self.gun.kill()
        self.gun = weapon
        self.gun.add(self.group)

    def movement(self, mouse):
        self.keys = pg.key.get_pressed()
    
        if self.keys[pg.K_w]:
            self.mov[1] = -1 
        elif self.keys[pg.K_s]:
            self.mov[1] = 1  
        else:
            self.mov[1] = 0

        if self.keys[pg.K_a]:
            self.mov[0] = -1 
        elif self.keys[pg.K_d]:
            self.mov[0] = 1 
        else:
            self.mov[0] = 0

        just_p = pg.key.get_just_pressed()

        if just_p[pg.K_1]:
            self.change_weapon(self.inventory[1])

        if just_p[pg.K_2]:
            self.change_weapon(self.inventory[0])

        #self.rotate(mouse)

        self.rect.y += self.mov[1] * self.spd
        self.rect.x += self.mov[0] * self.spd
        self.check_collision()
        
        gun_pos = get_point_radius(self.rect.center, mouse)
        self.gun.face_mouse((gun_pos[0], gun_pos[1]))

    def fire(self, mouse, keys):
        keys = pg.key.get_just_pressed()

        if keys[pg.K_SPACE]:
            self.start_ticks = pg.time.get_ticks()
            self.gun.fire(self.rect.center, mouse)

    def reload(self, keys):
        if keys[pg.K_r]:
            self.gun.reload()
            
    def rotate(self, mouse):
        # Rotates sprite angle having the mouse as a base
        self.angle = get_angle(self.rect.center, mouse) 
        self.image = pg.transform.rotate(self.image_cp, self.angle)
        self.rect  = self.image.get_rect(center = self.rect.center)
    
    def input(self):
        mouse = pg.mouse.get_pos()
        keys = pg.key.get_just_pressed()
        self.movement(mouse)
        #self.check_v_collision()
        #self.check_h_collision()
        self.fire(mouse, keys)
        self.reload(keys)

    def update(self):
        self.input()
        seconds = (pg.time.get_ticks() - self.start_ticks) / 1000
        self.seconds_passed = seconds

    def draw(self):
        pass
