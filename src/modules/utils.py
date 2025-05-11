import pygame as pg

def draw_text(text, color, surface, x, y, size = 32, alpha = 255, origin = "center"):
    font = pg.font.SysFont("Noto Sans", size)
    textobj = font.render(str(text), True, color)
    textobj.set_alpha(alpha)
    textrect = textobj.get_rect()
    match origin:

        case "center":
            textrect.center = (x, y)
        case _:
            textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def display_fps(clock):
    screen = pg.display.get_surface()  
    font = pg.font.SysFont("Noto Sans", 32)
    textobj = font.render(str(int(clock.get_fps())), True, (255, 255, 255))
    textobj.set_alpha(255)
    textrect = textobj.get_rect()
    textrect.topleft = (20, 20)
    screen.blit(textobj, textrect)

def debug_text(text, origin = "nada"):
    draw_text(text, "white", pg.display.get_surface(), 20, 20, origin=origin)