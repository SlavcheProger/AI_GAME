from pygame import *
import sys

init()

screen = display.set_mode((1890, 1417))


display.set_caption('none')


background = image.load('./диалоги/4этап(быт)/1.png')

screen.blit(background, (0, 0))
for i in range(1, 123):
    if 22 <= i <= 27:
        time.delay(2500)
    elif 45 <= i <= 50:
        time.delay(2500)
    elif 78 <= i <= 83:
        time.delay(1500)
    elif 85 <= i <= 93:
        time.delay(300)
    elif 64 <= i <= 77:
        time.delay(300)
    else:
        time.delay(400)
    background = image.load('./диалоги/4этап(быт)/' + str(i) + '.png')
    screen.blit(background, (0, 0))
    display.flip()



while 1:
    for i in event.get():
        if i.type == QUIT:

            sys.exit()
