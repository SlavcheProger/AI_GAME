from pygame import *
import sys

init()

screen = display.set_mode((0, 0), FULLSCREEN)


display.set_caption('none')


background = image.load('./диалоги/0введение/1.png')

screen.blit(background, (0, 0))
for i in range(1, 17):
    if i == 8:
        time.delay(25000)
    else:
        time.delay(100)
    background = image.load('./диалоги/0введение/' + str(i) + '.png')
    w, h = display.get_surface().get_size()
    background = transform.scale(background, (w, h))
    screen.blit(background, (0, 0))
    display.flip()


while 1:
    for i in event.get():
        if i.type == K_ESCAPE:

            sys.exit()