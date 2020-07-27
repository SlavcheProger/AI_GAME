from pygame import *
import sys
import math

red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
init()

screen = display.set_mode((320, 320))

display.set_caption("Turing's jorney")

size = 40

data = []
for i in range(8):
    d = []
    for j in range(8):
        d.append(0)
        print(i, j)
        if i % 2 == j % 2:
            draw.rect(screen, black, (i * size,j * size,  size, size))
        else:
            draw.rect(screen, white, (i * size, j * size, size, size))
        draw.ellipse(screen, red, (i * size - 10, j * size - 10, 10, 10))
    data.append(d)
print(data)

display.update()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            x,y = mouse.get_pos()
            x = x // size
            y = y // size
            print(x,y)
            data[y][x] = 1
            draw.rect(screen, red, (x * size, y * size, size, size))
            display.update()
quit()
