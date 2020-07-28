from pygame import *
import sys

init()
def show(screen, display):

    background = image.load('./шахматы.игра/1.png')

    screen.blit(background, (0, 0))
    for i in range(1, 20):
        background = image.load('./шахматы.игра/' + str(i) + '.png')
        w, h = display.get_surface().get_size()
        background = transform.scale(background, (w, h))
        screen.blit(background, (0, 0))
        display.flip()


    running = True
    while running:
        for e in event.get():
            if e.type == K_ESCAPE:
                running = False

    quit()
