import pygame as pg


def start_screen():
    background_image = pg.image.load('screensaver.jpeg')
    background_image = pg.transform.scale(background_image, size)
    screen.blit(background_image, (0, 0))

    f1 = pg.font.Font(None, 60)
    text1 = f1.render('Играть', True, (0, 0, 0))
    text2 = f1.render('Как играть', True, 'black')
    text3 = f1.render('Прохождение', True, 'black')

    pg.draw.rect(screen, 'white', (410, 150, 180, 60))
    pg.draw.rect(screen, 'white', (360, 220, 280, 60))
    pg.draw.rect(screen, 'white', (335, 290, 330, 60))

    screen.blit(text1, (430, 160))
    screen.blit(text2, (390, 230))
    screen.blit(text3, (355, 300))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if 410 < pg.mouse.get_pos()[0] < 590 and 150 < pg.mouse.get_pos()[1] < 210:
                    map_of_world()
        pg.display.set_caption('Заставка')
        pg.display.flip()


def rendering_countries():
    aus = pg.image.load("pictures/Austraalia/australia_0.png")
    aus = pg.transform.scale(aus, (172.5, 135.8))
    zeal = pg.image.load("pictures/New Zealand/New Zealand_0.png")
    zeal = pg.transform.scale(zeal, (87.47, 84.57))
    guin = pg.image.load("pictures/New Guinea/new guinea_0.png")
    guin = pg.transform.scale(guin, (74.501, 51.428))
    indo = pg.image.load("pictures/Indonesia/indonesia_0.png")
    indo = pg.transform.scale(indo, (93.569, 65.142))
    phil = pg.image.load("pictures/Philippines/philippines_0.png")
    phil = pg.transform.scale(phil, (47, 42.857))
    japan = pg.image.load("pictures/Japan/japan_0.png")
    japan = pg.transform.scale(japan, (43.902, 71.571))
    s_e = pg.image.load("pictures/S-E Asia/s-e asia_0.png")
    s_e = pg.transform.scale(s_e, (118.847, 114.857))
    ind = pg.image.load("pictures/India/india_0.png")
    ind = pg.transform.scale(ind, (82.926, 146.142))
    green = pg.image.load("pictures/Greenland/greenland_0.png")
    green = pg.transform.scale(green, (177.383, 147.857))

    screen.blit(aus, (750, 410))
    screen.blit(zeal, (886, 505.5))
    screen.blit(guin, (848, 359))
    screen.blit(indo, (728, 331.5))
    screen.blit(phil, (792, 288.5))
    screen.blit(japan, (822.3, 175.4))
    screen.blit(s_e, (717, 259))
    screen.blit(ind, (657.5, 199))
    screen.blit(green, (259.6, 22))


def map_of_world():
    background_image = pg.image.load('world_map.jpg')
    background_image = pg.transform.scale(background_image, size)
    pg.display.set_caption('Основной экран')
    screen.fill('black')
    screen.blit(background_image, (0, 0))
    pg.display.flip()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    map_of_symptoms()

        pg.display.set_caption('Основной экран')
        pg.display.flip()


def map_of_symptoms():
    background_image = pg.image.load('map_of_symptoms.jpg')
    background_image = pg.transform.scale(background_image, size)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    map_of_world()

        pg.display.set_caption('Симптомы')
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
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                map_of_symptoms()
            elif event.key == pg.K_s:
                map_of_world()
    screen.fill('black')
    pg.display.flip()
