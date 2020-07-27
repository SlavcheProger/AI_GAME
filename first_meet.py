from pygame import *
import sys

def show(screen, display):
    background = image.load('./диалоги/1этап(встреча)/1.png')

    screen.blit(background, (0, 0))
    for i in range(1, 131):
        for e in event.get():
            if e.type == QUIT:
                quit()

        if i == 8:
            continue
        elif 1 <= i <= 4 or 115 <= i <= 123:
            time.delay(50)
        elif i == 6:
            time.delay(4500)
        elif i == 91 or i == 52 or i == 73 or i == 126:
            time.delay(3500)
        time.delay(250)
        background = image.load('./диалоги/1этап(встреча)/' + str(i) + '.png')
        w, h = display.get_surface().get_size()
        background = transform.scale(background, (w, h))
        screen.blit(background, (0, 0))
        display.flip()
