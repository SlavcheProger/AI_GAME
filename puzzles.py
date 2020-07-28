#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import pygame
def show(screen, display):
WHITE = (255, 255, 255)
pygame.init()
n = 8  # количество клеток квадратного поля игры
width = 80  # ширина клетки( и объекта)
height = 80  # высота клетки ( и объекта)

margin = 1  # промежуток между клетками
screen = pygame.Surface(((width + margin) * n + margin, (height + margin) * n + margin))

koo = []  # список нач. координат до перемещения
all_s = []  # список всех объектов

koor = []  # список координат разницы между обьуктом и мышкой
grid = []  # список занятых и свободных клеток

for row in range(n):

    grid.append([])
    for column in range(n):
        grid[row].append(0)


class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        all_s.append(self)
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.action = False
        self.column = self.x // (width + margin)
        self.row = self.y // (height + margin)
        grid[self.row][self.column] = 1

    def bum(self):  # проверка попадания мышки на объект
        if self.x < mp[0] < self.x + self.w and self.y < mp[1] < self.y + self.h:
            a = mp[0] - self.x
            b = mp[1] - self.y
            koor.append(a)
            koor.append(b)
            self.action = True
            c = self.x
            d = self.y
            koo.append(c)
            koo.append(d)

    def funtion(self):  # функция движения точно в клетку
        mp = pygame.mouse.get_pos()
        self.x = (mp[0] // (width + margin)) * (width + margin) + margin
        self.y = (mp[1] // (height + margin)) * (height + margin) + margin
        self.column = self.x // (width + margin)
        self.row = self.y // (height + margin)
        grid[koo[1] // (height + margin)][koo[0] // (width + margin)] = 0  # старой клетке = 0
        if grid[self.row][self.column] == 1:  # если клетка куда переместили занята
            self.x = koo[0]  # откат на обратные координаты
            self.y = koo[1]

    def render(self):  # отображение обьекта на игровом поле(экране)
        screen.blit(self.image, (self.x, self.y))

    def mouv(self):  # движение объекта с мышкой

        pos = pygame.mouse.get_pos()

        # Теперь  игрок имеет координаты мышки с учетом разницы координат
        self.x = pos[0] - koor[0]
        self.y = pos[1] - koor[1]
        # условие границ поля

        if self.x < 0:
            self.x = koo[0]
            self.y = koo[1]
            self.action = False
        if self.x + width > ((margin + width) * n + 10 + margin):
            self.x = koo[0]
            self.y = koo[1]
            self.action = False
        if self.y < 0:
            self.x = koo[0]
            self.y = koo[1]
            self.action = False
        if self.y + height > ((margin + height) * n + 10 + margin):
            self.x = koo[0]
            self.y = koo[1]
            self.action = False

    def mesto(self):  # запись положения объектов в список грид
        self.column = self.x // (width + margin)
        self.row = self.y // (height + margin)
        grid[self.row][self.column] = 1


hero1 = Sprite((width +margin)*(0)+margin,margin+(height +margin)*(0), ('./пазлы/1.png'))
hero2 = Sprite(margin+(width +margin)*(n-8),margin+(height +margin)*(3), ('./пазлы/2.png'))
hero3 = Sprite((width +margin)*(1)+margin,margin+(height +margin)*(0), ('./пазлы/3.png'))
hero4 = Sprite((width +margin)*(3)+margin,margin+(height +margin)*(n-8), ('./пазлы/4.png'))
hero5 = Sprite((width +margin)*(6)+margin,margin+(height +margin)*(n-8), ('./пазлы/5.png'))
hero6 = Sprite((width +margin)*(7)+margin,margin+(height +margin)*(1), ('./пазлы/6.png'))
hero7 = Sprite((width +margin)*(7)+margin,margin+(height +margin)*(0), ('./пазлы/7.png'))
hero8 = Sprite((width +margin)*(1)+margin,margin+(height +margin)*(1), ('./пазлы/8.png'))
hero9 = Sprite((width +margin)*(1)+margin,margin+(height +margin)*(2), ('./пазлы/9.png'))
hero10 = Sprite((width +margin)*(1)+margin,margin+(height +margin)*(6), ('./пазлы/10.png'))
hero11 = Sprite(margin+(width +margin)*(n-8),margin+(height +margin)*(7), ('./пазлы/11.png'))
hero12 = Sprite((width +margin)*(7)+margin,margin+(height +margin)*(6), ('./пазлы/12.png'))
<<<<<<< HEAD
hero13 = Sprite(0, 0, './пазлы/13.png')
=======
hero13 = Sprite(0, 0, ('./пазлы/13.png'))

>>>>>>> 4e0c7e800c836cde8042d7ae3a2a15d304455183
dum = True
while dum:
    screen.fill((10, 10, 100))
    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            sys.exit()

    # захват объекта лкм и перемещение при удержании кнопки
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:

            mp = pygame.mouse.get_pos()
            for i in all_s:  # захват объекта
                i.bum()

        if e.type == pygame.MOUSEBUTTONUP and e.button == 1:  # если отпущена лкм

<<<<<<< HEAD
            for i in all_s:
                if i.action == True:
                    i.funtion()  # перемещение объекта точно в клетку
            for i in all_s:
                i.action = False

            for i in all_s:  # запись положения объекта в список grid
                i.mesto()
            koor = []
            koo = []
=======
        for i in all_s:
            if i.action == True:
                i.funtion()  # перемещение объекта точно в клетку
                i.action = False
                i.mesto()

        koor = []
        koo = []

>>>>>>> 4e0c7e800c836cde8042d7ae3a2a15d304455183
    for i in all_s:
        if i.action == True:
            i.mouv()  # перемещение объекта мышкой

    for i in all_s:
        i.render()

    window.blit(screen, (0, 0))

    pygame.display.flip()

    for r in grid:
        s = ''
        for c in r:
            s = s + str(c) + ' '
        print(s)

    print("**********")
