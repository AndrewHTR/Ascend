from settings import *
from Engine.engine import Level
from Engine.menu   import main_menu
import pygame as pg

def game():
    pg.init()

    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Ascend")
    
    clock = pg.time.Clock()

    running = True
    level = Level()

    delta_time = 0

    print(f"Starting {pg.display.get_caption()[0]}")

    while running:
        screen.fill("black")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    running = False
                if event.key == pg.K_c:
                    main_menu(game=game)

        level.run(delta_time)

        pg.display.flip()

        delta_time = clock.tick(60) * 0.001

    pg.quit()

#main_menu(game=game)
game()