from pygame import *
import sys

init()

def show(screen, display):


    background = image.load('./диалоги/3этап(медицина)/1.png')

    screen.blit(background, (0, 0))
    for i in range(1, 69):
        if i == 14:
            time.delay(25000)
        elif i == 25 or i == 33 or i == 42 or i == 50 or i == 63:
            time.delay(4000)
        else:
            time.delay(250)
        background = image.load('./диалоги/3этап(медицина)/' + str(i) + '.png')
        w, h = display.get_surface().get_size()
        background = transform.scale(background, (w, h))
        screen.blit(background, (0, 0))
        display.flip()

    running = True
    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    running = False

    quit()