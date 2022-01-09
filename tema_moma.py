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
                elif 360 < pg.mouse.get_pos()[0] < 640 and 220 < pg.mouse.get_pos()[1] < 280:
                    how_to_play()

        pg.display.set_caption('Заставка')
        pg.display.flip()


def how_to_play():
    intro_text = ['', '',
                  '          В начале игры вам нужно выбрать страну зарождения вируса. Лучше выбирать страну ',
                  "          с выходом в море, достаточно большой территорией, с множеством соседей.", "",
                  "          Нельзя заражать страны напрямую, на можно развивать болень. Продумывайте, на ",
                  "          что тратить очки ДНК, и тогда болезнь будет распространяться быстрее.", "",
                  "          Очки ДНК очень важны для развития вируса. Эти очки идут автоматически за ",
                  "          заражение и смерти людей. Их также можно получать, щелкая появляющиеся ",
                  "          красные и желтые пузырьки.", "",
                  "          Наблюдайте за статистикой и процентом заражения. Вы выйграете если все умрут.",
                  "          Не дайте болезни убить всех зараженных, прежде чем заразите всех остальных."]
    background_image = pg.image.load('how_to_play.jpg')
    background_image = pg.transform.scale(background_image, size)
    screen.blit(background_image, (0, 0))
    pg.draw.rect(screen, 'black', (45, 75, 760, 60))
    pg.draw.rect(screen, 'black', (45, 150, 760, 60))
    pg.draw.rect(screen, 'black', (45, 225, 760, 85))
    pg.draw.rect(screen, 'black', (45, 325, 760, 60))
    f1 = pg.font.Font(None, 26)
    text_coord = 30
    for line in intro_text:
        string_rendered = f1.render(line, True, pg.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 7
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                return
            pg.display.set_caption('Как играть')
            pg.display.flip()


class Rendering(pg.sprite.Sprite):
    def __init__(self, pos, name, im, con_size, *group):
        super().__init__(*group)
        self.name = name
        self.image = pg.transform.scale(pg.image.load(im), con_size)
        self.rect = self.image.get_rect().move(pos)


class Symptoms(pg.sprite.Sprite):
    def __init__(self, pos, name, im, *group):
        super().__init__(*group)
        self.name = name
        self.image = pg.transform.scale(pg.image.load(im), (92, 80))
        self.rect = self.image.get_rect().move(pos)


def map_of_world():
    background_image = pg.image.load('world_map.jpg')
    background_image = pg.transform.scale(background_image, size)
    pg.display.set_caption('Основной экран')
    screen.fill('black')
    screen.blit(background_image, (0, 0))
    f1 = pg.font.Font(None, 32)
    text = f1.render('Пути передачи', True, (0, 0, 0))
    screen.blit(text, (15, 558))
    pg.display.flip()
    for j in countries:
        Rendering(*j, countries_group)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    map_of_symptoms()

        pg.display.set_caption('Основной экран')
        countries_group.draw(screen)
        pg.display.flip()


def map_of_symptoms():
    background_image = pg.image.load('map_of_symptoms.jpg')
    background_image = pg.transform.scale(background_image, size)
    for i in symptoms:
        Symptoms(*i, symptoms_group)

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
        symptoms_group.draw(screen)
        pg.display.flip()


pg.init()
size = (1000, 600)
running = True
screen = pg.display.set_mode(size)
symptoms = [[(454, 300), 'кома', 'симптомы/кома.png'],
            [(454, 220), 'отказ органов', 'симптомы/отказ органов.png'],
            [(454, 60), 'кашель', 'симптомы/кашель.png'],
            [(454, 460), 'киста', 'симптомы/киста.png'],

            [(383, 180), 'фиброз', 'симптомы/фиброз легких.png'],
            [(383, 340), 'паралич', 'симптомы/паралич.png'],
            [(383, 100), 'пневмония', 'симптомы/пневмония.png'],
            [(383, 420), 'аллергия', 'симптомы/аллергия.png'],

            [(524, 180), 'подавление иммунитета', 'симптомы/подавление иммунитета.png'],
            [(524, 340), 'системная инфекция', 'симптомы/системная инфекция.png'],
            [(524, 100), 'чихание', 'симптомы/чихание.png'],
            [(524, 420), 'нарывы', 'симптомы/нарывы.png'],

            [(313, 380), 'воспаление', 'симптомы/воспаление.png'],
            [(313, 140), 'отек легких', 'симптомы/отек легких.png'],

            [(594, 380), 'опухоли', 'симптомы/опухоли.png'],
            [(594, 140), 'лихорадка', 'симптомы/лихорадка.png'],

            [(243, 100), 'рвота', 'симптомы/рвота.png'],
            [(243, 180), 'диарея', 'симптомы/диарея.png'],
            [(243, 340), 'эпилепсия', 'симптомы/эпилепсия.png'],
            [(243, 420), 'паранойя', 'симптомы/паранойя.png'],

            [(664, 100), 'потение', 'симптомы/потение.png'],
            [(664, 180), 'поражение кожи', 'симптомы/поражение кожи.png'],
            [(664, 340), 'внутреннее кровотечение', 'симптомы/внутреннее кровотечение.png'],
            [(664, 420), 'гемофилия', 'симптомы/гемофилия.png'],

            [(173, 60), 'тошнота', 'симптомы/тошнота.png'],
            [(173, 220), 'дизентерия', 'симптомы/дизентирия.png'],
            [(173, 300), 'невнимательность', 'симптомы/невнимательность.png'],
            [(173, 460), 'бессонница', 'симптомы/бессоница.png'],

            [(734, 60), 'сыпь', 'симптомы/сыпь.png'],
            [(734, 220), 'некроз', 'симптомы/некроз.png'],
            [(734, 300), 'геморрагический шок', 'симптомы/геморрагический шок.png'],
            [(734, 460), 'анемия', 'симптомы/анемия.png']]

countries = [[(750, 410), 'Австралия', 'pictures/Austraalia/australia_0.png', (172.5, 135.8)],
             [(886, 505.5), 'Новая Зеландия', 'pictures/New Zealand/New Zealand_0.png', (87.47, 84.57)],
             [(848, 359), 'Новая Гвинея', 'pictures/New Guinea/new guinea_0.png', (74.501, 51.428)],
             [(728, 331.5), 'Иднонезия', 'pictures/Indonesia/indonesia_0.png', (93.569, 65.142)],
             [(792, 288.5), 'Филиппины', 'pictures/Philippines/philippines_0.png', (47, 42.857)],
             [(822.3, 175.4), 'Япония', 'pictures/Japan/japan_0.png', (43.902, 71.571)],
             [(717, 259), 'Ю.-В. Азия', 'pictures/S-E Asia/s-e asia_0.png', (118.847, 114.857)],
             [(657.5, 199), 'Индия', 'pictures/India/india_0.png', (82.926, 146.142)],
             [(259.6, 22), 'Гренландия', 'pictures/Greenland/greenland_0.png', (177.383, 147.857)],
             [(26, 22), 'Канада', 'pictures/Canada/canada_0.png', (302.882, 194.142)],
             [(570, 402), 'Мадагаскар', 'pictures/Madagascar/madagascar_0.png', (39.467, 47.571)],
             [(197.7, 289), 'Карибы', 'pictures/Caribbean_Islands/caribbean_0.png', (60.753, 29.571)],
             [(165, 288), 'Центр. Америка', 'pictures/Central America/central_0.png', (53.215, 68.571)],
             [(90, 244), 'Мексика', 'pictures/Mexico/mexico_0.png', (111.549, 85.201)],
             [(88, 150), 'США', 'pictures/USA/usa_0.png', (205.321, 140.571)],
             [(468.7, 56.3), 'Исландия', 'pictures/Iceland/iceland_0.png', (44.789, 34.285)],
             [(194.5, 327), 'Колумбия', 'pictures/Colombia/colombia_0.png', (101.552, 71.571)],
             [(210.5, 310), 'Бразилия', 'pictures/Brazil/brazil_0.png', (145.011, 146.142)],
             [(200, 380), 'Перу', 'pictures/Peru/peru_0.png', (65.188, 48.428)],
             [(226, 416), 'Боливия', 'pictures/Bolivia/bolivia_0.png', (92.682, 42.857)],
             [(233, 430), 'Аргентина', 'pictures/Argentina/argentina_0.png', (91.352, 138.428)],
             [(433, 368), 'Южная Африка', 'pictures/South Africa/south_0.png', (170.731, 123.428)],
             [(510, 408), 'Ботсвана', 'pictures/Botswana/botswana_0.png', (34.146, 37.285)],
             [(489, 384), 'Зимбабве', 'pictures/Zimbabwe/zimbabwe_0.png', (71.396, 39.428)],
             [(493, 304), 'Вост. Африка', 'pictures/East Africa/east_0.png', (113.968, 139.285)]]

countries_group = pg.sprite.Group()
symptoms_group = pg.sprite.Group()
count_people = {'Австралия': '22 685 143', 'Новая Зеландия': '5 112 300 чел', 'Новая Гвинея': '8 776 096',
                'Иднонезия': '271 349 889', 'Филиппины': '109 035 343', 'Япония': '125 552 000 ',
                'Ю.-В. Азия': '655 298 044', 'Индия': '1 381 790 000', 'Гренландия': '56 770', 'Канада': '38 246 108',
                'Мадагаскар': '28 427 328', 'Карибы': '42 000 000', 'Центр. Америка': '4 745 000', 'Мексика': '128,932,753',
                'США': '332 278 200', 'Исландия': '350 000', 'Колумбия': '50 372 424', 'Бразилия': '213 317 639',
                'Перу': '34 294 231', 'Боливия': '11 639 909', 'Аргентина': '44 938 742', 'Южная Африка': '60 142 978 чел',
                'Ботсвана': '2 380 250', 'Зимбабве': '14 862 927', 'Вост. Африка': '433 904 943'}
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
