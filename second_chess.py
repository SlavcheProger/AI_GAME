from pygame import *
import sys

init()

def show(screen, display):

    background = image.load('./диалоги/2этап(шахматы)/1.png')

    screen.blit(background, (0, 0))
    for i in range(1, 83):
        if i == 15:
            time.delay(25000)
        elif 51 <= i <= 57:
            time.delay(150)
        elif i == 77:
            time.delay(4000)
        else:
            time.delay(250)
        background = image.load('./диалоги/2этап(шахматы)/' + str(i) + '.png')
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