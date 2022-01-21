import pygame as pg
import random
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


def start_screen():
    global screen
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
                elif 390 < pg.mouse.get_pos()[0] < 620 and 290 < pg.mouse.get_pos()[1] < 350:
                    print(screen.get_width(), screen.get_height())
                    app = QApplication(sys.argv)
                    ex = MyWidget()
                    ex.show()
                    app.exec()
                    print(screen.get_width(), screen.get_height())

        pg.display.set_caption('Заставка')
        pg.display.flip()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI1.ui", self)
        self.con = sqlite3.connect("result.db")
        self.pushButton.clicked.connect(self.update_result)
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM point").fetchall()
        self.tableWidget.setRowCount(len(result))

        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}
        self.titles = None

    def update_result(self):
        self.close()


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
    pg.display.set_caption('Нихуя')

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
                elif len(input_text) < 28:
                    input_text += event.unicode
            if event.type == pg.MOUSEBUTTONDOWN:
                if 770 < pg.mouse.get_pos()[0] < 820 and 185 < pg.mouse.get_pos()[1] < 210:
                    map_of_world(input_text)

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


class Countries(pg.sprite.Sprite):

    def __init__(self, pos, name, im, con_size, *group):
        super().__init__(*group)
        self.speed = 0
        self.name = name
        self.image = pg.transform.scale(pg.image.load(im), con_size)
        self.rect = self.image.get_rect().move(pos)
        self.mask = pg.mask.from_surface(self.image)

    def update(self, *args):
        f2 = pg.font.Font(None, 40)
        local_pos = args[0].pos[0] - self.rect.x, args[0].pos[1] - self.rect.y
        text2 = f2.render('', True, (255, 255, 255))
        if args and args[0].type == pg.MOUSEBUTTONDOWN and args[0].button == 1 and \
                self.rect.collidepoint(args[0].pos):
            if self.mask.get_at(local_pos):
                return self.name


class Symptoms(pg.sprite.Sprite):
    neighbors = {'Тошнота': [17],
                 'Рвота': [25, 18, 14],
                 'Диарея': [17, 14, 26],
                 'Дизентерия': [18, 27],
                 'Кашель': [7, 11],
                 'Пневмония': [5, 14, 3],
                 'Отек легких': [17, 18, 7, 5],
                 'Фиброз легких': [14, 2, 7],
                 'Чиханье': [3, 16, 9],
                 'Лихорадка': [11, 9, 21, 22],
                 'Подавление иммунитета': [2, 11, 16],
                 'Сыпь': [21],
                 'Потение': [29, 22, 16],
                 'Поражение кожи': [21, 30, 16],
                 'Некроз': [22, 31],
                 'Бессонница': [20],
                 'Паранойя': [28, 13, 19],
                 'Эпилепсия': [20, 13, 27],
                 'Невменяемость': [19, 26],
                 'Киста': [8, 12],
                 'Аллергия': [4, 13, 6],
                 'Воспаление': [20, 19, 8, 6],
                 'Паралич': [8, 13, 1],
                 'Нарывы': [4, 15, 10],
                 'Опухоли': [12, 10, 24, 23],
                 'Системная инфекция': [12, 15, 1],
                 'Анемия': [24],
                 'Гемофилия': [15, 0, 23],
                 'Внутреннее кровотечение': [15, 24, 31],
                 'Геморрагический шок': [30, 23],
                 'Отказ органов': [1, 9, 5],
                 'Кома': [6, 10, 2]
                 }

    def __init__(self, pos, name, im, num, *group):
        super().__init__(*group)
        self.ind = num
        self.buy = 0
        self.name = name
        self.image = pg.transform.scale(pg.image.load(im), (92, 80))
        self.rect = self.image.get_rect().move(pos)

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            list_of_buy[self.ind] = 1
            for i in self.neighbors[self.name.capitalize()]:
                list_of_buy[i] = 1
                Symptoms(*symptoms[i], symptoms_group)


class Aircraft(pg.sprite.Sprite):
    image = pg.transform.scale(pg.image.load('aircraft_ru.png'), (20, 20))

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


class DNA(pg.sprite.Sprite):
    image = [pg.transform.scale(pg.image.load('dna.png'), (40, 40)),
             pg.transform.scale(pg.image.load('spiral.png'), (40, 40))]
    price = 2

    def __init__(self, pos, ind, *group):
        super().__init__(*group)
        self.pos = pos
        self.image = DNA.image[ind]
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect().move(pos)

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.kill()
            pg.time.set_timer(DNA_event, 5000, loops=1)


def moves():
    DNA(random.choice(destinations), 0, dna_group)


def map_of_world(a=False):
    con = sqlite3.connect("result.db")
    cur = con.cursor()
    cur.execute("""INSERT INTO point(name) VALUES(?)""", (a,))
    con.commit()
    pg.time.set_timer(aircraft_fly_event, 13000)

    background_image = pg.image.load('world_map_without_background.png')
    background_image = pg.transform.scale(background_image, size)
    pg.display.set_caption('Основной экран')

    f1 = pg.font.Font(None, 32)
    text = f1.render('Пути передачи', True, (0, 0, 0))
    a = ''

    pg.display.set_caption('Основной экран')
    pg.display.flip()

    for j in countries:
        Countries(*j, countries_group)

    while True:
        for event in pg.event.get():
            dna_group.update(event)
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if 0 < pg.mouse.get_pos()[0] < 200 and 550 < pg.mouse.get_pos()[1] < 590:
                    map_of_symptoms()
            if event.type == pg.MOUSEBUTTONDOWN:
                for i in countries_group:
                    i.update(event)
                    if i.update(event):
                        a = i.update(event)

            if event.type == aircraft_fly_event:
                for air in aircraft_group:
                    x = random.choice(destinations)
                    if air.pos[0] > x[0] and air.pos[1] > x[1]:
                        air.image = pg.transform.scale(pg.image.load('aircraft_lu.png'), (20, 20))
                    elif air.pos[0] > x[0] and air.pos[1] < x[1]:
                        air.image = pg.transform.scale(pg.image.load('aircraft_ld.png'), (20, 20))
                    elif air.pos[0] < x[0] and air.pos[1] < x[1]:
                        air.image = pg.transform.scale(pg.image.load('aircraft_rd.png'), (20, 20))
                    elif air.pos[0] < x[0] and air.pos[1] > x[1]:
                        air.image = pg.transform.scale(pg.image.load('aircraft_ru.png'), (20, 20))
                    x = list(x)
                    x[0], x[1] = x[0] - 10, x[1] - 10
                    x = tuple(x)
                    air.set_target(x)

            if event.type == DNA_event:
                moves()

        aircraft_group.update()
        screen.fill((30, 30, 100))
        screen.blit(background_image, (0, 0))
        text_name = f1.render(a, True, (0, 0, 0))
        pg.draw.rect(screen, 'grey', (0, 550, 205, 45))
        pg.draw.rect(screen, 'white', (0, 550, 200, 40))
        screen.blit(text, (15, 558))
        screen.blit(text_name, (0, 0))

        countries_group.draw(screen)
        for i in destinations:
            pg.draw.circle(screen, 'red', i, 2)

        aircraft_group.draw(screen)
        dna_group.draw(screen)
        pg.display.flip()


def map_of_symptoms():
    background_image = pg.image.load('map_of_symptoms.jpg')
    background_image = pg.transform.scale(background_image, size)
    screen.blit(background_image, (0, 0))
    pg.draw.rect(screen, 'grey', (0, 550, 155, 45))
    pg.draw.rect(screen, 'white', (0, 550, 150, 40))
    pg.draw.rect(screen, 'black', (785, 20, 200, 540))
    f1 = pg.font.Font(None, 32)
    f2 = pg.font.SysFont('impact', 22)
    f3 = pg.font.Font(None, 22)
    text = f1.render('Карта мира', True, (0, 0, 0))
    text2 = f2.render('Выберите симптом', True, 'white')
    text3 = f3.render('Используйте очки ДНК,'
                      'чтобы менять симптомы болезьни!', True, 'white')
    screen.blit(text2, (787, 30))
    screen.blit(text, (15, 558))
    screen.blit(text3, (787, 90))
    for i in symptoms:
        if list_of_buy[i[3]] == 1:
            Symptoms(*i, symptoms_group)

    while True:
        for event in pg.event.get():
            symptoms_group.update(event)
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
symptoms = [[(664, 460), 'анемия', 'симптомы/анемия.png', 0],
            [(384, 300), 'кома', 'симптомы/кома.png', 1],
            [(384, 220), 'отказ органов', 'симптомы/отказ органов.png', 2],
            [(384, 60), 'кашель', 'симптомы/кашель.png', 3],
            [(384, 460), 'киста', 'симптомы/киста.png', 4],

            [(313, 180), 'фиброз легких', 'симптомы/фиброз легких.png', 5],
            [(313, 340), 'паралич', 'симптомы/паралич.png', 6],
            [(313, 100), 'пневмония', 'симптомы/пневмония.png', 7],
            [(313, 420), 'аллергия', 'симптомы/аллергия.png', 8],

            [(454, 180), 'подавление иммунитета', 'симптомы/подавление иммунитета.png', 9],
            [(454, 340), 'системная инфекция', 'симптомы/системная инфекция.png', 10],
            [(454, 100), 'чиханье', 'симптомы/чихание.png', 11],
            [(454, 420), 'нарывы', 'симптомы/нарывы.png', 12],

            [(243, 380), 'воспаление', 'симптомы/воспаление.png', 13],
            [(243, 140), 'отек легких', 'симптомы/отек легких.png', 14],

            [(524, 380), 'опухоли', 'симптомы/опухоли.png', 15],
            [(524, 140), 'лихорадка', 'симптомы/лихорадка.png', 16],

            [(173, 100), 'рвота', 'симптомы/рвота.png', 17],
            [(173, 180), 'диарея', 'симптомы/диарея.png', 18],
            [(173, 340), 'эпилепсия', 'симптомы/эпилепсия.png', 19],
            [(173, 420), 'паранойя', 'симптомы/паранойя.png', 20],

            [(594, 100), 'потение', 'симптомы/потение.png', 21],
            [(594, 180), 'поражение кожи', 'симптомы/поражение кожи.png', 22],
            [(594, 340), 'внутреннее кровотечение', 'симптомы/внутреннее кровотечение.png', 23],
            [(594, 420), 'гемофилия', 'симптомы/гемофилия.png', 24],

            [(103, 60), 'тошнота', 'симптомы/тошнота.png', 25],
            [(103, 220), 'дизентерия', 'симптомы/дизентирия.png', 26],
            [(103, 300), 'невменяемость', 'симптомы/невменяемость.png', 27],
            [(103, 460), 'бессонница', 'симптомы/бессоница.png', 28],

            [(664, 60), 'сыпь', 'симптомы/сыпь.png', 29],
            [(664, 220), 'некроз', 'симптомы/некроз.png', 30],
            [(664, 300), 'геморрагический шок', 'симптомы/геморрагический шок.png', 31]]

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
             [(557, 272), 'Сауд. Аравия', 'pictures/Saudi Arabia/saudi_arabia_0.png', (74.057, 57)],
             [(534, 263), 'Ближ. Восток', 'pictures/Middle East/middle_east_0.png', (64.301, 33.857)],
             [(534, 245), 'Ирак', 'pictures/Iraq/iraq_0.png', (66.962, 30)],
             [(565, 245), 'Иран', 'pictures/Iran/iran_0.png', (64.301, 41.571)],
             [(605, 253), 'Пакистан', 'pictures/Pakistan/pakistan_0.png', (62.527, 39.857)],
             [(617, 245), 'Афганистан', 'pictures/Afghanistan/afghanistan_0.png', (86.031, 48.857)],
             [(588, 188), 'Казахстан', 'pictures/Kazakhstan/kazakhstan_0.png', (110.864, 75)],
             [(624, 202), 'Монголия', 'pictures/Mongolia/mongolia_0.png', (73.17, 64.285)],
             [(550, 206), 'Цент. Азия', 'pictures/Central Asia/central_asia_0.png', (83.37, 62.142)]]
list_of_buy = [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0]
countries_group = pg.sprite.Group()
symptoms_group = pg.sprite.Group()
dna_group = pg.sprite.Group(DNA((100, 100), 1), DNA((500, 200), 0))

count_people = {'Австралия': ['22 685 143'], 'Новая Зеландия': ['5 112 300 чел'], 'Новая Гвинея': ['8 776 096'],
                'Иднонезия': ['271 349 889'], 'Филиппины': ['109 035 343'], 'Япония': ['125 552 000 '],
                'Ю.-В. Азия': ['655 298 044'], 'Индия': ['1 381 790 000'], 'Гренландия': ['56 770'],
                'Канада': ['38 246 108'],
                'Мадагаскар': ['28 427 328'], 'Карибы': ['42 000 000'], 'Центр. Америка': ['4 745 000'],
                'Мексика': ['128,932,753'],
                'США': ['332 278 200'], 'Исландия': ['350 000'], 'Колумбия': ['50 372 424'],
                'Бразилия': ['213 317 639'],
                'Перу': ['34 294 231'], 'Боливия': ['11 639 909'], 'Аргентина': ['44 938 742'],
                'Южная Африка': ['60 142 978'],
                'Ботсвана': ['2 380 250'], 'Зимбабве': ['14 862 927'], 'Вост. Африка': ['433 904 943'],
                'Ангола': ['31 127 674'],
                'Судан': ['44 909 353'], 'Египет': ['100 223 850'], 'Ливия': ['5 700 000'],
                'Цент. Африка': ['675 920 972'], 'Запад. Африка': ['347 098 777'],
                'Монако': ['38 350'], 'Алжир': ['43 910 000'], 'Китай': ['1 442 965 000'], 'Корея': ['25 449 927'],
                'Россия': ['145 975 300'], 'Финляндия': ['5 528 737'],
                'Швеция': ['10 409 248'], 'Норвегия': ['5 391 369'], 'Англия': ['63 400 000'],
                'Испания': ['47 394 223'], 'Италия': ['62 000 000'], 'Франция': ['67 413 000'],
                'Германия': ['83 190 556'], 'Балканы': ['55 000 000'], 'Цент. Европа': ['2 000 000'],
                'Турция': ['83 154 997'], 'Прибалтика': ['6 121 000'],
                'Польша': ['38 228 100'],
                'Украина': ['43 200 350'], 'Сауд. Аравия': ['27 345 986'], 'Ближ. Восток': ['312 008 700'],
                'Ирак': ['37 056 169'], 'Иран': ['83 183 741'],
                'Пакистан': ['207 774 520'], 'Афганистан': ['37 466 414'],
                'Казахстан': ['19 082 467'], 'Монголия': ['3 353 470'], 'Цент. Азия': ['74 500 000']}
destinations = [(98, 80), (273, 168), (167, 147), (201, 75), (213, 53), (294, 49), (349, 120), (336, 385), (268, 436),
                (255, 465), (257, 523), (491, 72), (503, 434), (528, 430), (202, 247), (269, 199), (120, 269),
                (151, 305), (194, 340), (215, 301), (230, 370), (273, 394), (522, 404), (554, 414), (559, 355),
                (529, 326), (492, 328), (135, 204), (496, 281), (524, 284), (535, 313), (593, 422), (688, 308),
                (708, 233), (692, 301), (756, 296), (759, 372), (803, 365), (884, 382), (821, 455), (875, 486),
                (947, 534), (415, 284), (495, 370), (439, 327), (456, 276), (559, 276), (581, 292), (558, 279),
                (553, 253), (591, 265), (630, 275), (660, 263), (668, 233), (631, 220), (585, 238), (464, 209),
                (485, 197), (457, 212), (527, 184), (558, 203), (589, 192), (489, 163), (507, 153), (538, 152),
                (605, 174), (655, 139), (764, 165), (660, 102), (825, 73), (852, 133), (845, 222), (732, 197),
                (773, 251)]

aircraft_group = pg.sprite.Group(Aircraft(random.choice(destinations)), Aircraft(random.choice(destinations)))

aircraft_fly_event = pg.USEREVENT + 1
DNA_event = pg.USEREVENT + 1
start_screen()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill('black')
    pg.display.flip()
