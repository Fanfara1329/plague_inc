import pygame as pg
import random
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

countries = {'Австралия': ['pictures/Austraalia/australia_0.png', '22 685 143', 0, (172.5, 135.8), (750, 410),
                           [(803, 469), (851, 453), (863, 511)]],
             'Новая Зеландия': ['pictures/New Zealand/New Zealand_0.png', '5 112 300 чел', 0, (87.47, 84.57),
                                (886, 505.5), [(953, 537), (924, 555)]],
             'Новая Гвинея': ['pictures/New Guinea/new guinea_0.png', '8 776 096', 0, (74.501, 51.428), (848, 359),
                              [(873, 378), (898, 394)]],
             'Иднонезия': ['pictures/Indonesia/indonesia_0.png', '271 349 889', 0, (93.569, 65.142), (728, 331.5),
                           [(802, 363), (756, 374)]],
             'Филиппины': ['pictures/Philippines/philippines_0.png', '109 035 343', 0, (47, 42.857), (792, 288.5),
                           [(817, 308)]],
             'Япония': ['pictures/Japan/japan_0.png', '125 552 000 ', 0, (43.902, 71.571), (822.3, 175.4),
                        [(847, 226)]],
             'Ю.-В. Азия': ['pictures/S-E Asia/s-e asia_0.png', '655 298 044', 0, (118.847, 114.857), (717, 259),
                            [(746, 283), (769, 321), (763, 356)]],
             'Индия': ['pictures/India/india_0.png', '1 381 790 000', 0, (82.926, 146.142), (657.5, 199),
                       [(705, 227), (712, 273), (682, 303)]],
             'Гренландия': ['pictures/Greenland/greenland_0.png', '56 770', 0, (177.383, 147.857), (259.6, 22),
                            [(297, 48), (348, 82)]],
             'Канада': ['pictures/Canada/canada_0.png', '38 246 108', 0, (302.882, 194.142), (26, 22),
                        [(106, 95), (165, 147), (271, 120)]],
             'Мадагаскар': ['pictures/Madagascar/madagascar_0.png', '28 427 328', 0, (39.467, 47.571), (570, 402),
                            [(589, 429)]],
             'Карибы': ['pictures/Caribbean_Islands/caribbean_0.png', '42 000 000', 0, (60.753, 29.571), (197.7, 289),
                        [(215, 299), (237, 311)]],
             'Центр. Америка': ['pictures/Central America/central_0.png', '4 745 000', 0, (53.215, 68.571), (165, 288),
                                [(182, 310), (196, 341)]],
             'Мексика': ['pictures/Mexico/mexico_0.png', '128,932,753', 0, (111.549, 85.201), (90, 244),
                         [(130, 270), (146, 292)]],
             'США': ['pictures/USA/usa_0.png', '332 278 200', 0, (205.321, 140.571), (88, 150),
                     [(136, 205), (169, 231), (237, 202)]],
             'Исландия': ['pictures/Iceland/iceland_0.png', '350 000', 0, (44.789, 34.285), (468.7, 56.3), [(486, 73)]],
             'Колумбия': ['pictures/Colombia/colombia_0.png', '50 372 424', 0, (101.552, 71.571), (194.5, 327),
                          [(234, 344), (231, 376)]],
             'Бразилия': ['pictures/Brazil/brazil_0.png', '213 317 639', 0, (145.011, 146.142), (210.5, 310),
                          [(282, 376), (322, 386), (311, 429)]],
             'Перу': ['pictures/Peru/peru_0.png', '34 294 231', 0, (65.188, 48.428), (200, 380),
                      [(219, 399), (248, 416)]],
             'Боливия': ['pictures/Bolivia/bolivia_0.png', '11 639 909', 0, (92.682, 42.857), (226, 416),
                         [(259, 435), (277, 444)]],
             'Аргентина': ['pictures/Argentina/argentina_0.png', '44 938 742', 0, (91.352, 138.428), (233, 430),
                           [(274, 487), (260, 537), (254, 461)]],
             'Южная Африка': ['pictures/South Africa/south_0.png', '60 142 978', 0, (170.731, 123.428), (433, 368),
                              [(501, 420), (512, 449), (543, 446)]],
             'Ботсвана': ['pictures/Botswana/botswana_0.png', '2 380 250', 0, (34.146, 37.285), (510, 408),
                          [(527, 433)]],
             'Зимбабве': ['pictures/Zimbabwe/zimbabwe_0.png', '14 862 927', 0, (71.396, 39.428), (489, 384),
                          [(521, 406)]],
             'Вост. Африка': ['pictures/East Africa/east_0.png', '433 904 943', 0, (113.968, 139.285), (493, 304),
                              [(560, 335), (555, 376), (541, 418)]],
             'Ангола': ['pictures/Angola/angola_0.png', '31 127 674', 0, (79.822, 51.857), (466, 346), [(497, 374)]],
             'Судан': ['pictures/Sudan/sudan_0.png', '44 909 353', 0, (79.379, 92.142), (498, 279),
                       [(545, 301), (525, 337)]],
             'Египет': ['pictures/Egypt/egypt_0.png', '100 223 850', 0, (60.753, 57.428), (494, 258), [(523, 284)]],
             'Ливия': ['pictures/Libya/libya_0.png', '5 700 000', 0, (53.215, 52.285), (473, 259), [(496, 284)]],
             'Цент. Африка': ['pictures/Central Africa/central africa_0.png', '675 920 972', 0, (84.7, 87.428),
                              (453, 286), [(489, 314), (494, 345)]],
             'Запад. Африка': ['pictures/West Africa/west africa_0.png', '347 098 777', 0, (87.361, 75.857),
                               (394, 284), [(432, 310), (458, 328), (434, 343)]],
             'Монако': ['pictures/Monaco/monaco_0.png', '38 350', 0, (59.423, 75.428), (393, 249), [(417, 291)]],
             'Алжир': ['pictures/Algeria/algeria_0.png', '43 910 000', 0, (63.858, 72.429), (423, 239),
                       [(467, 267), (457, 291)]],
             'Китай': ['pictures/China/сhina_0.png', '1 442 965 000', 0, (164.079, 142.285), (682, 145),
                       [(744, 191), (808, 169), (766, 248)]],
             'Корея': ['pictures/Korea/korea_0.png', '25 449 927', 0, (38.137, 42), (787, 204), [(809, 220)]],
             'Россия': ['pictures/Russia/russia_0.png', '145 975 300', 0, (400, 184.285), (508, 22),
                        [(556, 147), (617, 176), (677, 143), (764, 150), (805, 95), (862, 133)]],
             'Финляндия': ['pictures/Finland/finland_0.png', '5 528 737', 0, (24.83, 59.142), (500, 117), [(514, 156)]],
             'Швеция': ['pictures/Sweden/sweden_0.png', '10 409 248', 0, (56.319, 72.428), (465, 115), [(501, 135)]],
             'Норвегия': ['pictures/Norway/norway_0.png', '5 391 369', 0, (41.241, 54), (454, 120), [(486, 139)]],
             'Англия': ['pictures/England/england_0.png', '63 400 000', 0, (45.232, 45), (414.8, 164.5), [(441, 192)]],
             'Испания': ['pictures/Spain/spain_0.png', '47 394 223', 0, (44.345, 36.428), (418, 218), [(442, 240)]],
             'Италия': ['pictures/Italy/italy_0.png', '62 000 000', 0, (52.771, 30), (450, 219), [(490, 239)]],
             'Франция': ['pictures/France/france_0.png', '67 413 000', 0, (64.301, 38.142), (429, 192), [(464, 212)]],
             'Германия': ['pictures/Germany/germany_0.png', '83 190 556', 0, (59.866, 46.285), (459, 173),
                          [(494, 200)]],
             'Балканы': ['pictures/Balkans/balkans_0.png', '55 000 000', 0, (63.414, 40.714), (478, 215), [(521, 224)]],
             'Цент. Европа': ['pictures/Central Europe/central_europe_0.png', '2 000 000', 0, (74.501, 37.714),
                              (490, 200), [(546, 229), (514, 221)]],
             'Турция': ['pictures/Turkey/turkey_0.png', '83 154 997', 0, (50.554, 21.428), (518, 233), [(549, 246)]],
             'Прибалтика': ['pictures/Baltic states/baltic_states_0.png', '6 121 000', 0, (68.736, 77.571), (502, 153),
                            [(529, 178), (526, 201)]],
             'Польша': ['pictures/Poland/poland_0.png', '38 228 100', 0, (83.813, 68.571), (520.7, 160),
                        [(553, 209), (568, 199)]],
             'Украина': ['pictures/Ukraine/ukraine_0.png', '43 200 350', 0, (86.917, 53.142), (555, 164),
                         [(583, 186), (602, 199)]],
             'Сауд. Аравия': ['pictures/Saudi Arabia/saudi_arabia_0.png', '27 345 986', 0, (74.057, 57), (557, 272),
                              [(580, 298), (611, 305)]],
             'Ближ. Восток': ['pictures/Middle East/middle_east_0.png', '312 008 700', 0, (64.301, 33.857), (534, 263),
                              [(562, 281)]],
             'Ирак': ['pictures/Iraq/iraq_0.png', '37 056 169', 0, (66.962, 30), (534, 245), [(563, 260)]],
             'Иран': ['pictures/Iran/iran_0.png', '83 183 741', 0, (64.301, 41.571), (565, 245), [(606, 270)]],
             'Пакистан': ['pictures/Pakistan/pakistan_0.png', '207 774 520', 0, (62.527, 39.857), (605, 253),
                          [(624, 280), (640, 280)]],
             'Афганистан': ['pictures/Afghanistan/afghanistan_0.png', '37 466 414', 0, (86.031, 48.857), (617, 245),
                            [(650, 266), (663, 273)]],
             'Казахстан': ['pictures/Kazakhstan/kazakhstan_0.png', '19 082 467', 0, (110.864, 75), (588, 188),
                           [(673, 213), (628, 218), (638, 236)]],
             'Монголия': ['pictures/Mongolia/mongolia_0.png', '3 353 470', 0, (73.17, 64.285), (624, 202),
                          [(682, 222), (657, 247)]],
             'Цент. Азия': ['pictures/Central Asia/central_asia_0.png', '74 500 000', 0, (83.37, 62.142), (550, 206),
                            [(572, 227), (579, 244), (608, 249)]]}

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
                    app = QApplication(sys.argv)
                    ex = MyWidget()
                    ex.show()
                    app.exec()

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
        for _, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(_, j, QTableWidgetItem(str(val)))
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
                    first = choice_country()
                    countries[first][2] = 1
                    print(countries[first])
                    map_of_world(input_text)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    first = choice_country()
                    map_of_world(input_text)

        keys = pg.key.get_pressed()

        if keys[pg.K_1]:
            need_input = True

        text2 = f2.render(input_text, True, (255, 255, 255))
        pg.display.set_caption('Инициализация')
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

def choice_country():
    a = ''
    b = ''
    pg.display.set_caption('Выбор страны')
    pg.display.flip()
    f1 = pg.font.Font(None, 32)

    for country in countries.keys():
        con = [countries[country][4], country, countries[country][0], countries[country][3]]
        Countries(*con, countries_group)

    a2 = ''
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                for _ in countries_group:
                    _.update(event)
                    if _.update(event):
                        a = _.update(event)[0]
                        b = countries[a][1]
                if 600 < pg.mouse.get_pos()[0] < 660 and 510 < pg.mouse.get_pos()[1] < 570:
                    if a == '':
                        a2 = 'Вы не выбрали страну'
                    else:
                        return a
                        exit()

        screen.fill((30, 30, 100))
        countries_group.draw(screen)
        text_error = f1.render(a2, True, 'pink')
        if isinstance(a, str):
            text_name = f1.render(a, True, 'white')
            text_count = f1.render(b, True, 'white')
            screen.blit(text_name, (25, 460))
            screen.blit(text_count, (25, 500))
        confirm_text = f1.render('Подтвердить страну', True, 'red')
        screen.blit(text_error, (360, 560))
        screen.blit(confirm_text, (340, 530))
        button = pg.image.load('start.png')
        button = pg.transform.scale(button, (60, 60))
        screen.blit(button, (600, 510))
        pg.display.flip()


class Countries(pg.sprite.Sprite):

    def __init__(self, pos, name, im, con_size, *group):
        super().__init__(*group)
        self.speed = 0
        self.infected = 0
        self.name = name
        self.image = pg.transform.scale(pg.image.load(im), con_size)
        self.rect = self.image.get_rect().move(pos)
        self.mask = pg.mask.from_surface(self.image)

    def update(self, *args):
        local_pos = args[0].pos[0] - self.rect.x, args[0].pos[1] - self.rect.y
        if args and args[0].type == pg.MOUSEBUTTONDOWN and args[0].button == 1 and \
                self.rect.collidepoint(args[0].pos):
            if self.mask.get_at(local_pos):
                return self.name, self.infected


class Symptoms(pg.sprite.Sprite):
    neighbors = {'Тошнота': [17, 0, 3],
                 'Рвота': [25, 18, 14, 0, 4],
                 'Диарея': [17, 14, 26, 0, 5],
                 'Дизентерия': [18, 27, 0, 8],
                 'Кашель': [7, 11, 0, 3],
                 'Пневмония': [5, 14, 3, 0, 4],
                 'Отек легких': [17, 18, 7, 5, 0, 5],
                 'Фиброз легких': [14, 2, 7, 0, 7],
                 'Чиханье': [3, 16, 9, 0, 4],
                 'Лихорадка': [11, 9, 21, 22, 0, 5],
                 'Подавление иммунитета': [2, 11, 16, 0, 7],
                 'Сыпь': [21, 0, 3],
                 'Потение': [29, 22, 16, 0, 4],
                 'Поражение кожи': [21, 30, 16, 0, 5],
                 'Некроз': [22, 31, 0, 8],
                 'Бессонница': [20, 0, 3],
                 'Паранойя': [28, 13, 19, 0, 4],
                 'Эпилепсия': [20, 13, 27, 0, 5],
                 'Невменяемость': [19, 26, 0, 9],
                 'Киста': [8, 12, 0, 4],
                 'Аллергия': [4, 13, 6, 0, 4],
                 'Воспаление': [20, 19, 8, 6, 0, 5],
                 'Паралич': [8, 13, 1, 0, 8],
                 'Нарывы': [4, 15, 10, 0, 4],
                 'Опухоли': [12, 10, 24, 23, 0, 5],
                 'Системная инфекция': [12, 15, 1, 0, 7],
                 'Анемия': [24, 0, 3],
                 'Гемофилия': [15, 0, 23, 0, 4],
                 'Внутреннее кровотечение': [15, 24, 31, 0, 5],
                 'Геморрагический шок': [30, 23, 0, 9],
                 'Отказ органов': [1, 9, 5, 0, 10],
                 'Кома': [6, 10, 2, 0, 10]
                 }

    def __init__(self, pos, name, im, num, *group):
        super().__init__(*group)
        self.ind = num
        self.buy = 0
        self.name = name
        self.im = im
        self.image = pg.transform.scale(pg.image.load(im), (92, 80))
        self.rect = self.image.get_rect().move(pos)
        self.buy = False

    def update(self, *args):
        f1 = pg.font.Font(None, 70)
        f2 = pg.font.Font(None, 45)
        dog_surf = pg.image.load('dna_one.png')
        flip = pg.transform.scale(
            dog_surf, (100, 100))
        if args and args[0].type == pg.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            pg.draw.rect(screen, 'black', (785, 200, 200, 200))
            text = f1.render(f'-{str(self.neighbors[self.name.capitalize()][-1])}', True, 'white')
            screen.blit(flip, (800, 240))
            screen.blit(text, (890, 260))
            pg.draw.rect(screen, 'white', (800, 350, 170, 40))
            text2 = f2.render('Купить', True, 'black')
            screen.blit(text2, (830, 357))
            self.buy = True
        if args and args[0].type == pg.MOUSEBUTTONDOWN and self.buy:
            print(self.im)
            if 785 < pg.mouse.get_pos()[0] < 985 and 200 < pg.mouse.get_pos()[1] < 400:
                self.im = self.im[:-4] + '_1' + self.im[-4:]
                self.image = pg.transform.scale(pg.image.load(self.im), (92, 80))
                list_of_buy[self.ind] = 1
                pg.draw.rect(screen, 'black', (785, 200, 200, 200))
                for _ in self.neighbors[self.name.capitalize()][:-2]:
                    list_of_buy[_] = 1
                    Symptoms(*symptoms[_], symptoms_group)


class Aircraft(pg.sprite.Sprite):
    image = pg.transform.scale(pg.image.load('aircraft_ru.png'), (20, 20))

    def __init__(self, pos, *group):
        super().__init__(*group)
        self.begin = ''
        self.end = ''
        self.pos = pos
        self.image = Aircraft.image
        self.speed = 3
        self.set_target(pos)
        self.rect = self.image.get_rect()

    def set_target(self, pos):
        self.target = pg.Vector2(pos)

    def update(self):
        move = self.target - self.pos
        move_length = move.length()

        if move_length < self.speed:
            self.pos = self.target
            self.kill()
            infection(self.begin, self.end)

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
            pg.time.set_timer(DNA_event, 10000, loops=1)
            return 1


def moves():
    ex = random.choice(list(countries.keys()))
    v = random.choice(countries[ex][-1])
    v = list(v)
    v[0], v[1] = v[0] - 20, v[1] - 20
    v = tuple(v)
    DNA(v, 0, dna_group)


def make_new_fly():
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    choice = random.choice(lis)
    if choice < 40:
        begin, end = random.sample(countries.keys(), 2)
        air_beg = random.choice(countries[begin][-1])
        air_end = random.choice(countries[end][-1])
        air = Aircraft(air_beg, aircraft_group)
        air.begin, air.end = begin, end

        if air_beg[0] > air_end[0] and air_beg[1] > air_end[1]:
            air.image = pg.transform.scale(pg.image.load('aircraft_lu.png'), (20, 20))
        elif air_beg[0] > air_end[0] and air_beg[1] < air_end[1]:
            air.image = pg.transform.scale(pg.image.load('aircraft_ld.png'), (20, 20))
        elif air.pos[0] < air_end[0] and air_beg[1] < air_end[1]:
            air.image = pg.transform.scale(pg.image.load('aircraft_rd.png'), (20, 20))
        elif air_beg[0] < air_end[0] and air_beg[1] > air_end[1]:
            air.image = pg.transform.scale(pg.image.load('aircraft_ru.png'), (20, 20))

        air_end = list(air_end)
        air_end[0], air_end[1] = air_end[0] - 10, air_end[1] - 10
        air_end = tuple(air_end)
        air.set_target(air_end)


def infection(b, e):
    begin_inf, end_inf = countries[b][2], countries[e][2]
    if begin_inf and not end_inf:
        DNA(e, 0, dna_group)
        countries[e][2] = 1
    print(b, e)
    print(begin_inf, end_inf)


def map_of_world(a=False):
    con = sqlite3.connect("result.db")
    cur = con.cursor()
    # cur.execute("""INSERT INTO point(name) VALUES(?)""", (a,))
    con.commit()
    pg.time.set_timer(aircraft_fly_event, 12000)

    background_image = pg.image.load('world_map_without_background.png')
    background_image = pg.transform.scale(background_image, size)
    pg.display.set_caption('Основной экран')

    f1 = pg.font.Font(None, 26)
    f3 = pg.font.Font(None, 32)
    text = f3.render('Пути передачи', True, (0, 0, 0))
    a = ''
    b = ''
    c = ''

    pg.display.set_caption('Основной экран')
    pg.display.flip()

    for country in countries.keys():
        con = [countries[country][4], country, countries[country][0], countries[country][3]]
        Countries(*con, countries_group)

    count = 0
    while True:
        for event in pg.event.get():
            for i in dna_group:
                i.update(event)
                if i.update(event):
                    a = i.update(event)
                    count += 1
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if 0 < pg.mouse.get_pos()[0] < 200 and 550 < pg.mouse.get_pos()[1] < 590:
                    map_of_symptoms(count)
            if event.type == pg.MOUSEBUTTONDOWN:
                for _ in countries_group:
                    _.update(event)
                    if _.update(event):
                        a = _.update(event)[0]
                        c = str(_.update(event)[1])
                        b = countries[a][1]

            if event.type == aircraft_fly_event:
                make_new_fly()

            if event.type == DNA_event:
                moves()

        aircraft_group.update()
        screen.fill((30, 30, 100))
        screen.blit(background_image, (0, 0))
        if isinstance(a, str):
            text_name = f1.render(a, True, 'white')
            text_count = f1.render(b, True, 'white')
            text_infected = f1.render(c, True, 'red')
            screen.blit(text_name, (450, 576))
            screen.blit(text_count, (600, 576))
            screen.blit(text_infected, (330, 576))
        text_dna = f1.render(str(count), True, 'red')
        pg.draw.rect(screen, 'grey', (0, 550, 205, 45))
        pg.draw.rect(screen, 'white', (0, 550, 200, 40))
        screen.blit(text, (15, 558))

        screen.blit(text_dna, (850, 576))

        countries_group.draw(screen)
        for _ in airports:
            pg.draw.circle(screen, 'red', _, 2)

        aircraft_group.draw(screen)
        dna_group.draw(screen)
        pg.display.flip()


def map_of_symptoms(a):
    f1 = pg.font.Font(None, 60)
    text_dna = f1.render(f'-{a}', True, 'blue')
    background_image = pg.image.load('map_of_symptoms.jpg')
    background_image = pg.transform.scale(background_image, size)
    screen.blit(background_image, (0, 0))
    screen.blit(text_dna, (60, 17))
    pg.draw.rect(screen, 'grey', (0, 550, 155, 45))
    pg.draw.rect(screen, 'white', (0, 550, 150, 40))
    pg.draw.rect(screen, 'black', (785, 200, 200, 200))
    f1 = pg.font.Font(None, 32)
    f2 = pg.font.SysFont('impact', 22)
    f3 = pg.font.Font(None, 22)
    text = f1.render('Карта мира', True, (0, 0, 0))
    text2 = f2.render('Выберите симптом', True, 'white')
    text3 = f3.render('Используйте очки ДНК,', True, 'white')
    text4 = f3.render('чтобы менять симптомы', True, 'white')
    text5 = f3.render('болезни!', True, 'white')
    screen.blit(text2, (787, 200))
    screen.blit(text, (15, 558))
    screen.blit(text3, (787, 240))
    screen.blit(text4, (787, 265))
    screen.blit(text5, (787, 290))
    for _ in symptoms:
        if list_of_buy[_[3]] == 1:
            Symptoms(*_, symptoms_group)

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


airports = []
for key in countries.keys():
    cic = countries[key][-1]
    for i in cic:
        airports.append(i)

list_of_buy = [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0]
countries_group = pg.sprite.Group()
symptoms_group = pg.sprite.Group()
dna_group = pg.sprite.Group(DNA(random.choice(airports), 1), DNA(random.choice(airports), 0))

aircraft_group = pg.sprite.Group()

aircraft_fly_event = pg.USEREVENT + 1
DNA_event = pg.USEREVENT + 1
start_screen()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill('black')
    pg.display.flip()
