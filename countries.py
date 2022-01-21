import pygame as pg


class Countries(pg.sprite.Sprite):

    def __init__(self, pos, name, im, con_size, *group):
        super().__init__(*group)
        self.name = name
        self.image = pg.transform.scale(pg.image.load(im), con_size)
        self.rect = self.image.get_rect().move(pos)
        self.mask = pg.mask.from_surface(self.image)

    def update(self, *args):
        local_pos = args[0].pos[0] - self.rect.x, args[0].pos[1] - self.rect.y
        if args and args[0].type == pg.MOUSEBUTTONDOWN and args[0].button == 1 and \
                self.rect.collidepoint(args[0].pos):
            if self.mask.get_at(local_pos):
                return self.name


SIZE = (1000, 600)
pg.init()
screen = pg.display.set_mode(SIZE)

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

countries_group = pg.sprite.Group()


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
                        a = _.update(event)
                        b = countries[a][1]
                if 600 < pg.mouse.get_pos()[0] < 660 and 510 < pg.mouse.get_pos()[1] < 570:
                    if a == '':
                        a2 = 'Вы не выбрали страну'
                    else:
                        return a
                        a2 = ''

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


choice_country()
