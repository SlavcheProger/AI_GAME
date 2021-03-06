from pygame import *
import sys
from textediting import *

init()

def show(screen, display):



    background = image.load('./найти правдивое выражение/1.png')
    screen.blit(background, (0, 0))

    for i in range(1, 6):
        for e in event.get():
            if e.type == QUIT:
                quit()
        time.delay(150)
        background = image.load('./найти правдивое выражение/' + str(i) + '.png')
        w, h = display.get_surface().get_size()
        background = transform.scale(background, (w, h))
        screen.blit(background, (0, 0))
        display.flip()

    text = EditText(screen, background, 600, 650)
    while text != '2':
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


