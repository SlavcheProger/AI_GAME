from pygame import *
import sys

init()

screen = display.set_mode((600, 600))


display.set_caption('none')


background = image.load('./диалоги/4этап(быт)/1.png')

screen.blit(background, (0, 0))
for i in range(1, 123):
    if i == 25:
        time.delay(25000)
    elif i == 47:
        time.delay(25000)
    elif i == 80:
        time.delay(4000)
    elif i == 102 or i == 121:
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

while 1:
    for i in event.get():
        if i.type == QUIT:

            sys.exit()
