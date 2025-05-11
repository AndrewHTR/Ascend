import pygame as pg
from engine.engine import Level

pg.init()

WIDTH = 800
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Ascend")

clock = pg.time.Clock()

running = True
delta_time = 0 
level = Level()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.K_q:
            running = False

    screen.fill("black")

    level.run(delta_time)

    pg.display.flip()

    delta_time = clock.tick(60) * 0.001

pg.quit()

