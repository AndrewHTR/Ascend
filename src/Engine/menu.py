import pygame as pg
from settings import *
from modules.utils import draw_text, wave_text


def main_menu(game):
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Ascend")

    clock = pg.time.Clock()

    running = True
    delta_time = 0 

    teste = 1

    while running:
        screen.fill("black")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    running = False
                if event.key == pg.K_SPACE:
                    game()

        wave_text("Main Menu", "white", screen, WIDTH//2, HEIGHT//2 - 190, teste, origin="center")
        teste += 0.1
        pg.display.flip()

        clock.tick(60) * 0.001

    pg.quit()

