import pygame as pg


def start_screen():
    background_image = pg.image.load('screensaver.jpeg')
    background_image = pg.transform.scale(background_image, size)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                return

        screen.fill('black')
        screen.blit(background_image, (0, 0))
        pg.display.flip()


def map_of_world():
    background_image = pg.image.load('world_map.jpg')
    background_image = pg.transform.scale(background_image, size)

    screen.fill('black')
    screen.blit(background_image, (0, 0))
    pg.display.flip()


pg.init()
size = (1000, 600)
running = True
screen = pg.display.set_mode(size)

start_screen()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    map_of_world()
    pg.display.flip()
