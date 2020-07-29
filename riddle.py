#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sys, os
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
# окно
window = pygame.display.set_mode((0, 0))
background = pygame.image.load('./гиппократ/5.png')
w, h = pygame.display.get_surface().get_size()
action = False

mp = pygame.mouse.get_pos()

n = 4  # количество клеток квадратного поля игры
width = 150  # ширина клетки( и объекта)
height = 150  # высота клетки ( и объекта)

margin = 5  # промежуток между клетками
x = None
y = None
screen = pygame.Surface(((width + margin) * n + margin, (height + margin) * n + margin))  # создаем игровое поле(экран)

all_s = []
orig = []


def drawField():
    for row in range(n):  # рисуем игровое поле
        for column in range(n):
            color = WHITE
            pygame.draw.rect(screen,
                             color,
                             [(margin + width) * column + margin,
                              (margin + height) * row + margin,
                              width,
                              height])

    for i in all_s:  # запись положения объекта в список grid
        i.mesto()

    for i in all_s:
        i.render()
        
class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.image = pygame.image.load(filename)  # создаем рисунок-загрузка из файла
        self.action = False
        self.rect = self.image.get_rect()  # представляем его прямоугольником

        self.w = self.image.get_width()  # ширина
        self.h = self.image.get_height()  # высота
        # all_s.append(self)
        orig.append(self)
        self.row = None
        self.column = None

    def bum(self):  # проверка попадания мышки на объект

        if self.x < mp[0] < self.x + self.w and self.y < mp[1] < self.y + self.h:
            self.action = True  # объект активирован
        else:
            self.action = False  # для избежания случая активации одновременно
            #  двух объектов

    def mouv(self):  # функция перемещения объекта
        a = self.x  # первоначальные координаты объекта
        b = self.y

        if e.key == pygame.K_LEFT:  # если нажата клавиша лево курсора
            if self.x > margin and self.action == True:  # если координ.х больше промежутка и движение разрешено
                self.x -= margin + width  # коорд.х присвоить значение один шаг влево
                self.action = False  # запрет на перемещение
                grid[b // (height + margin)][a // (width + margin)] = 0  # ячейке списка грид предыдущего положения присвоить значение 0

        if e.key == pygame.K_RIGHT:
            if self.x < (width + margin) * (n - 1) and self.action == True:
                self.x += margin + width
                self.action = False
                grid[b // (height + margin)][a // (width + margin)] = 0
        if e.key == pygame.K_UP:
            if self.y > margin and self.action == True:
                self.y -= height + margin
                self.action = False  # запрет на перемещение
                grid[b // (height + margin)][a // (width + margin)] = 0
        if e.key == pygame.K_DOWN:
            if self.y < (height + margin) * (n - 1) and self.action == True:
                self.y += height + margin
                self.action = False  # запрет на перемещение
                grid[b // (height + margin)][a // (width + margin)] = 0
        # проверка не занята ли клетка куда переместили объект
        self.column = self.x // (width + margin)
        self.row = self.y // (height + margin)
        if grid[self.row][self.column] == 1:  # если занята
            # возвращаем объект на прежнее место
            self.x = a
            self.y = b

    def mesto(self):
        self.column = self.x // (width + margin)
        self.row = self.y // (height + margin)
        grid[self.row][self.column] = 1

        '''
        print(grid)
        for r in grid:
            s = ''
            for c in r:
                s = s + str(c) + ' '
            print(s)
        print("*****")
'''
    def render(self):  # отображение обьекта на игровом поле(экране)
        screen.blit(self.image, (self.x, self.y))


hero1 = Sprite(margin, margin, ('1.gif'))
hero2 = Sprite(margin + (width + margin), margin, ('2.gif'))
hero3 = Sprite((width + margin) * 2 + margin, margin, ('3.gif'))
hero4 = Sprite((width + margin) * 3 + margin, margin, ('4.gif'))
hero5 = Sprite(margin, margin + (height + margin), ('5.gif'))
hero6 = Sprite(margin + (width + margin), margin + (height + margin), ('6.gif'))
hero7 = Sprite(margin + (width + margin) * 2, margin + (height + margin), ('7.gif'))
hero8 = Sprite(margin + (width + margin) * 3, margin + (height + margin), ('8.gif'))
hero9 = Sprite(margin, margin + (height + margin) * 2, ('9.gif'))
hero10 = Sprite(margin + (width + margin), margin + (height + margin) * 2, ('10.gif'))
hero11 = Sprite(margin + (width + margin) * 2, margin + (height + margin) * 2, ('11.gif'))
hero12 = Sprite(margin + (width + margin) * 3, margin + (height + margin) * 2, ('12.gif'))
hero13 = Sprite(margin, margin + (height + margin) * 3, ('13.gif'))
hero14 = Sprite(margin + (width + margin), margin + (height + margin) * 3, ('14.gif'))
hero15 = Sprite(margin + (width + margin) * 2, margin + (height + margin) * 3, ('15.gif'))
# создаём список координат клеточек (правильный)
koord = [(margin, margin),
         (margin + (width + margin), margin),
         ((width + margin) * 2 + margin, margin),
         ((width + margin) * 3 + margin, margin),
         (margin, margin + (height + margin)),
         (margin + (width + margin), margin + (height + margin)),
         (margin + (width + margin) * 2, margin + (height + margin)),
         (margin + (width + margin) * 3, margin + (height + margin)),
         (margin, margin + (height + margin) * 2),
         (margin + (width + margin), margin + (height + margin) * 2),
         (margin + (width + margin) * 2, margin + (height + margin) * 2),
         (margin + (width + margin) * 3, margin + (height + margin) * 2),
         (margin, margin + (height + margin) * 3),
         (margin + (width + margin), margin + (height + margin) * 3),
         (margin + (width + margin) * 2, margin + (height + margin) * 3)]

koordin = koord[:]  # копия победных координат
# перемешиваем список координат случайным образом
random.shuffle(koordin)

# пятнашкам присваиваем случайные координаты с перемешанного списка
i = 0
for e in orig:
    e.x, e.y = koordin[i]
    all_s.append(e)
    i += 1
done = True  # некая переменная
grid = []  # список занятых и свободных клеточек
for row in range(n):
    # заполняем пустую матрицу
    # 10 х 10  grid[row,column]
    grid.append([])
    for column in range(n):
        grid[row].append(0)


while done:  # условие существования игрового цикла

    screen.fill((10, 2, 100))
    for e in pygame.event.get():  # для любого события

        if e.type == pygame.QUIT:  # если было закрытие окна
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                sys.exit()
        elif e.type == pygame.K_SPACE:
            random.shuffle(koordin)
            print('koordfhkjsdhfkjsdhkjfhskdjhfkjsdhfkjhsdkjfhskjdhfkjsdhkjhdin', koordin)
            drawField()
            sys.exit()
        else:
            if e.type == pygame.MOUSEBUTTONDOWN:  # если событие мышь
                if pygame.mouse.get_pressed()[0]:  # если  была нажата лкм
                    mp = pygame.mouse.get_pos()


                for i in all_s:  #
                    i.bum()  # выбор объекта

        # Перемещение объекта с помощью курсора
        if e.type == pygame.KEYDOWN:  # если была нажата клавиша
            for i in all_s:
                i.mouv()

    drawField()

    window.blit(screen, (0, 0))  # на окне прорисовываем поле игры

    pygame.display.flip()  # отображаем полностью дисплей(окно)
quit()
