import pygame as pg
import random


def start_screen():
    background_image = pg.image.load('screensaver.jpeg')
    background_image = pg.transform.scale(background_image, size)
    screen.blit(background_image, (0, 0))

    f1 = pg.font.Font(None, 60)
    text1 = f1.render('Играть', True, (0, 0, 0))
    text2 = f1.render('Как играть', True, 'black')
    text3 = f1.render('Рекорды', True, 'black')

    pg.draw.rect(screen, 'white', (410, 150, 180, 60))
    pg.draw.rect(screen, 'white', (360, 220, 280, 60))
    pg.draw.rect(screen, 'white', (390, 290, 230, 60))

    screen.blit(text1, (430, 160))
    screen.blit(text2, (390, 230))
    screen.blit(text3, (410, 300))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if 410 < pg.mouse.get_pos()[0] < 590 and 150 < pg.mouse.get_pos()[1] < 210:
                    player_name()
                elif 360 < pg.mouse.get_pos()[0] < 640 and 220 < pg.mouse.get_pos()[1] < 280:
                    how_to_play()

        pg.display.set_caption('Заставка')
        pg.display.flip()


def player_name():
    background_image = pg.image.load('player_name.jpg')
    background_image = pg.transform.scale(background_image, size)
    screen.blit(background_image, (0, 0))
    f1 = pg.font.Font(None, 60)
    f2 = pg.font.Font(None, 40)
    text = f1.render('Name your Plague', True, (255, 255, 255))
    text3 = f2.render('GO!', True, 'black')
    screen.blit(text, (300, 48))
    screen.blit(text3, (770, 185))
    pg.display.set_caption('')

    need_input = False
    input_text = ''
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if need_input and event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    need_input = False
                    input_text = ''
                elif event.key == pg.K_BACKSPACE:
                    input_text = input_text[:-1]
                    print(input_text)
                else:
                    input_text += event.unicode
            if event.type == pg.MOUSEBUTTONDOWN:
                if 770 < pg.mouse.get_pos()[0] < 820 and 185 < pg.mouse.get_pos()[1] < 210:
                    map_of_world()

        keys = pg.key.get_pressed()

        if keys[pg.K_1]:
            need_input = True

        text2 = f2.render(input_text, True, (255, 255, 255))
        pg.display.set_caption('Основной экран')
        screen.blit(background_image, (0, 0))
        screen.blit(text, (300, 48))
        screen.blit(text3, (770, 185))
        screen.blit(text2, (300, 188))
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
    pg.draw.rect(screen, 'black', (0, 550, 270, 40))
    f1 = pg.font.Font(None, 26)
    text = f1.render('Вернутся на главный экран', True, (255, 255, 255))
    screen.blit(text, (15, 558))
    pg.draw.rect(screen, 'black', (45, 75, 760, 60))
    pg.draw.rect(screen, 'black', (45, 150, 760, 60))
    pg.draw.rect(screen, 'black', (45, 225, 760, 85))
    pg.draw.rect(screen, 'black', (45, 325, 760, 60))
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
                if 0 < pg.mouse.get_pos()[0] < 270 and 550 < pg.mouse.get_pos()[1] < 590:
                    start_screen()
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


class Aircraft(pg.sprite.Sprite):
    image = pg.transform.scale(pg.image.load('aircraft.png'), (20, 20))

    def __init__(self, pos, *group):
        super().__init__(*group)
        self.pos = pos
        self.image = Aircraft.image
        self.speed = 2
        self.set_target(pos)
        self.rect = self.image.get_rect()

    def set_target(self, pos):
        self.target = pg.Vector2(pos)

    def update(self):
        move = self.target - self.pos
        move_length = move.length()

        if move_length < self.speed:
            self.pos = self.target
        elif move_length != 0:
            move.normalize_ip()
            move = move * self.speed
            self.pos += move

        self.rect.topleft = list(int(v) for v in self.pos)


def map_of_world():
    pg.time.set_timer(aircraft_fly_event, 6000)
    pg.time.set_timer(aircraft_fly_event, 6000)
    background_image = pg.image.load('world_map_without_background.png')
    background_image = pg.transform.scale(background_image, size)
    pg.display.set_caption('Основной экран')
    f1 = pg.font.Font(None, 32)
    text = f1.render('Пути передачи', True, (0, 0, 0))
    pg.display.set_caption('Основной экран')
    pg.display.flip()
    for j in countries:
        Rendering(*j, countries_group)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if 0 < pg.mouse.get_pos()[0] < 200 and 550 < pg.mouse.get_pos()[1] < 590:
                    map_of_symptoms()

            if event.type == aircraft_fly_event:
                print('pop')
                for air in aircraft_group:
                    air.set_target(random.choice(destinations))

        aircraft_group.update()
        screen.fill((30, 30, 100))
        screen.blit(background_image, (0, 0))

        pg.draw.rect(screen, 'grey', (0, 550, 205, 45))
        pg.draw.rect(screen, 'white', (0, 550, 200, 40))
        screen.blit(text, (15, 558))

        countries_group.draw(screen)
        for i in destinations:
            pg.draw.circle(screen, 'red', i, 2)
        aircraft_group.draw(screen)
        pg.display.flip()


def map_of_symptoms():
    background_image = pg.image.load('map_of_symptoms.jpg')
    background_image = pg.transform.scale(background_image, size)
    screen.blit(background_image, (0, 0))
    pg.draw.rect(screen, 'grey', (0, 550, 155, 45))
    pg.draw.rect(screen, 'white', (0, 550, 150, 40))
    pg.draw.rect(screen, 'black', (785, 20, 200, 540))
    f1 = pg.font.Font(None, 32)
    text = f1.render('Карта мира', True, (0, 0, 0))
    screen.blit(text, (15, 558))
    for i in symptoms:
        Symptoms(*i, symptoms_group)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if 0 < pg.mouse.get_pos()[0] < 150 and 550 < pg.mouse.get_pos()[1] < 590:
                    map_of_world()

        pg.display.set_caption('Симптомы')
        symptoms_group.draw(screen)
        pg.display.flip()


pg.init()
size = (1000, 600)
running = True
screen = pg.display.set_mode(size)
symptoms = [[(384, 300), 'кома', 'симптомы/кома.png'],
            [(384, 220), 'отказ органов', 'симптомы/отказ органов.png'],
            [(384, 60), 'кашель', 'симптомы/кашель.png'],
            [(384, 460), 'киста', 'симптомы/киста.png'],

            [(313, 180), 'фиброз', 'симптомы/фиброз легких.png'],
            [(313, 340), 'паралич', 'симптомы/паралич.png'],
            [(313, 100), 'пневмония', 'симптомы/пневмония.png'],
            [(313, 420), 'аллергия', 'симптомы/аллергия.png'],

            [(454, 180), 'подавление иммунитета', 'симптомы/подавление иммунитета.png'],
            [(454, 340), 'системная инфекция', 'симптомы/системная инфекция.png'],
            [(454, 100), 'чихание', 'симптомы/чихание.png'],
            [(454, 420), 'нарывы', 'симптомы/нарывы.png'],

            [(243, 380), 'воспаление', 'симптомы/воспаление.png'],
            [(243, 140), 'отек легких', 'симптомы/отек легких.png'],

            [(524, 380), 'опухоли', 'симптомы/опухоли.png'],
            [(524, 140), 'лихорадка', 'симптомы/лихорадка.png'],

            [(173, 100), 'рвота', 'симптомы/рвота.png'],
            [(173, 180), 'диарея', 'симптомы/диарея.png'],
            [(173, 340), 'эпилепсия', 'симптомы/эпилепсия.png'],
            [(173, 420), 'паранойя', 'симптомы/паранойя.png'],

            [(594, 100), 'потение', 'симптомы/потение.png'],
            [(594, 180), 'поражение кожи', 'симптомы/поражение кожи.png'],
            [(594, 340), 'внутреннее кровотечение', 'симптомы/внутреннее кровотечение.png'],
            [(594, 420), 'гемофилия', 'симптомы/гемофилия.png'],

            [(103, 60), 'тошнота', 'симптомы/тошнота.png'],
            [(103, 220), 'дизентерия', 'симптомы/дизентирия.png'],
            [(103, 300), 'невнимательность', 'симптомы/невнимательность.png'],
            [(103, 460), 'бессонница', 'симптомы/бессоница.png'],

            [(664, 60), 'сыпь', 'симптомы/сыпь.png'],
            [(664, 220), 'некроз', 'симптомы/некроз.png'],
            [(664, 300), 'геморрагический шок', 'симптомы/геморрагический шок.png'],
            [(664, 460), 'анемия', 'симптомы/анемия.png']]
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
             [(493, 304), 'Вост. Африка', 'pictures/East Africa/east_0.png', (113.968, 139.285)],
             [(466, 346), 'Ангола', 'pictures/Angola/angola_0.png', (79.822, 51.857)],
             [(498, 279), 'Судан', 'pictures/Sudan/sudan_0.png', (79.379, 92.142)],
             [(494, 258), 'Египет', 'pictures/Egypt/egypt_0.png', (60.753, 57.428)],
             [(473, 259), 'Ливия', 'pictures/Libya/libya_0.png', (53.215, 52.285)],
             [(453, 286), 'Цент. Африка', 'pictures/Central Africa/central africa_0.png', (84.7, 87.428)],
             [(394, 284), 'Запад. Африка', 'pictures/West Africa/west africa_0.png', (87.361, 75.857)],
             [(393, 249), 'Монако', 'pictures/Monaco/monaco_0.png', (59.423, 75.428)],
             [(423, 239), 'Алжир', 'pictures/Algeria/algeria_0.png', (63.858, 72.429)],
             [(682, 145), 'Китай', 'pictures/China/сhina_0.png', (164.079, 142.285)],
             [(787, 204), 'Корея', 'pictures/Korea/korea_0.png', (38.137, 42)],
             [(508, 22), 'Россия', 'pictures/Russia/russia_0.png', (400, 184.285)],
             [(500, 117), 'Финляндия', 'pictures/Finland/finland_0.png', (24.83, 59.142)],
             [(465, 115), 'Швеция', 'pictures/Sweden/sweden_0.png', (56.319, 72.428)],
             [(454, 120), 'Норвегия', 'pictures/Norway/norway_0.png', (41.241, 54)],
             [(414.8, 164.5), 'Англия', 'pictures/England/england_0.png', (45.232, 45)],
             [(418, 218), 'Испания', 'pictures/Spain/spain_0.png', (44.345, 36.428)],
             [(450, 219), 'Италия', 'pictures/Italy/italy_0.png', (52.771, 30)],
             [(429, 192), 'Франция', 'pictures/France/france_0.png', (64.301, 38.142)],
             [(459, 173), 'Германия', 'pictures/Germany/germany_0.png', (59.866, 46.285)],
             [(478, 215), 'Балканы', 'pictures/Balkans/balkans_0.png', (63.414, 40.714)],
             [(490, 200), 'Цент. Европа', 'pictures/Central Europe/central_europe_0.png', (74.501, 37.714)],
             [(518, 233), 'Турция', 'pictures/Turkey/turkey_0.png', (50.554, 21.428)],
             [(502, 153), 'Прибалтика', 'pictures/Baltic states/baltic_states_0.png', (68.736, 77.571)],
             [(520.7, 160), 'Польша', 'pictures/Poland/poland_0.png', (83.813, 68.571)],
             [(555, 164), 'Украина', 'pictures/Ukraine/ukraine_0.png', (86.917, 53.142)],
             [(557, 272), 'Сауд. Аравия', 'pictures/Saudi Arabia/saudi_arabia_0.png', (74.057, 57)]]

countries_group = pg.sprite.Group()
symptoms_group = pg.sprite.Group()
aircraft_group = pg.sprite.Group(Aircraft((10, 10)), Aircraft((600, 500)))
count_people = {'Австралия': '22 685 143', 'Новая Зеландия': '5 112 300 чел', 'Новая Гвинея': '8 776 096',
                'Иднонезия': '271 349 889', 'Филиппины': '109 035 343', 'Япония': '125 552 000 ',
                'Ю.-В. Азия': '655 298 044', 'Индия': '1 381 790 000', 'Гренландия': '56 770', 'Канада': '38 246 108',
                'Мадагаскар': '28 427 328', 'Карибы': '42 000 000', 'Центр. Америка': '4 745 000',
                'Мексика': '128,932,753',
                'США': '332 278 200', 'Исландия': '350 000', 'Колумбия': '50 372 424', 'Бразилия': '213 317 639',
                'Перу': '34 294 231', 'Боливия': '11 639 909', 'Аргентина': '44 938 742',
                'Южная Африка': '60 142 978 чел',
                'Ботсвана': '2 380 250', 'Зимбабве': '14 862 927', 'Вост. Африка': '433 904 943'}

destinations = [(98, 80), (273, 168), (167, 147), (201, 75), (213, 53), (294, 49), (349, 120), (336, 385), (268, 436),
                (255, 465), (257, 523), (491, 72), (503, 434), (528, 430),
                (202, 247), (269, 199), (120, 269), (151, 305), (194, 340), (215, 301), (230, 370), (273, 394),
                (522, 404), (554, 414), (559, 355), (529, 326), (492, 328), (135, 204),
                (496, 281), (524, 284), (535, 313), (593, 422), (688, 308), (708, 233), (692, 301), (756, 296),
                (759, 372), (803, 365), (884, 382), (821, 455), (875, 486), (947, 534)]
aircraft_fly_event = pg.USEREVENT + 1
start_screen()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill('black')
    pg.display.flip()
