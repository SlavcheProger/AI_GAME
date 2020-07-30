from pygame import *
import sys
import math
from textediting import *



def show(screen, display):
    background = image.load('./разделение квадрата.быт/1.png')
    red = (255, 0, 0)
    screen.blit(background, (0, 0))
    size = 80
    data = []

    for i in range(1, 16):
        for e in event.get():
            if e.type == QUIT:
                quit()

        background = image.load('./разделение квадрата.быт/' + str(i) + '.png')
        w, h = display.get_surface().get_size()
        background = transform.scale(background, (w, h))
        screen.blit(background, (0, 0))
        display.flip()
    for i in range(5):
        d = []
        for j in range(5):
            for e in event.get():
                if e.type == QUIT:
                    quit()
            d.append(0)
            draw.ellipse(screen, red, ((i * (size-13) - 10)+180, (j * size - 60)+210, 10, 10))
        data.append(d)

    display.update()
    running = True
    z = 0
    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
            if z < 1:
                if e.type == MOUSEBUTTONDOWN:
                    if mouse.get_pos() == (177, 156) or mouse.get_pos() == (243,156) or mouse.get_pos() == (243,156) or mouse.get_pos() ==(310,155) or mouse.get_pos() == (377,156) or mouse.get_pos() == (422,155) or mouse.get_pos() == (422,236) or mouse.get_pos() == (423,315) or mouse.get_pos() == (443,396) or mouse.get_pos() == (443, 475) or mouse.get_pos() == (376, 235) or mouse.get_pos() == (377, 315):
                        print(mouse.get_pos())
                        x, y = mouse.get_pos()
                        x = x // size
                        y = y // size
                        print(x, y)
                        display.update()
                        z += 1
                    else:
                        continue
            elif z < 2:
                if e.type == MOUSEBUTTONDOWN:
                    if mouse.get_pos() == (177, 156) or mouse.get_pos() == (243,156) or mouse.get_pos() == (243,156) or mouse.get_pos() ==(310,155) or mouse.get_pos() == (377,156) or mouse.get_pos() == (422,155) or mouse.get_pos() == (422,236) or mouse.get_pos() == (423,315) or mouse.get_pos() == (443,396) or mouse.get_pos() == (443, 475) or mouse.get_pos() == (376, 235) or mouse.get_pos() == (377, 315):

                        x1, y1 = mouse.get_pos()
                        x1 = x1 // size
                        y1 = y1 // size
                        print(x1, y1)
                        display.update()
                        z += 1
                    else:
                        continue
            else:
                z = 0
                draw.line(screen, (255, 0, 0), [x, y],[x1, y1], 3)
                display.update()

    text = EditText(screen, background, 600, 650)
    while text != '6':
        f = font.SysFont(None, 300)
        img = f.render('NO', True, (255, 0, 68))
        screen.blit(img, (100, 100))
        display.update()
        time.delay(700)
        text = EditText(screen, background, 600 // 2, 600 - 100)

    f = font.SysFont(None, 300)
    img = f.render('WIN', True, (0, 255, 34))
    screen.blit(img, (100, 100))
    display.update()
    time.delay(700)

