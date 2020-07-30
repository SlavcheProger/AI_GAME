from pygame import *
import sys

init()

def show(screen, display):


    background = image.load('./диалоги/4этап(быт)/1.png')

    screen.blit(background, (0, 0))
    for i in range(1, 124):
        for e in event.get():
            if e.type == QUIT:
                quit()

        if i == 25:
            time.delay(25000)
        elif i == 47:
            time.delay(25000)
        elif i == 80:
            time.delay(4000)
        elif i == 102 or i == 122:
            time.delay(4000)
        elif i == 6 or i == 15 or i == 39:
            time.delay(4000)
        else:
            time.delay(150)
        background = image.load('./диалоги/4этап(быт)/' + str(i) + '.png')
        w, h = display.get_surface().get_size()
        background = transform.scale(background, (w, h))
        screen.blit(background, (0, 0))
        display.flip()

   