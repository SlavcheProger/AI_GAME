from pygame import *
import sys

init()

screen = display.set_mode((1890, 1417))


display.set_caption('none')


background = image.load('./диалоги/3этап(медицина)/1.png')

screen.blit(background, (0, 0))
for i in range(1, 69):
    if 9 <= i <= 17:
        time.delay(2500)

    else:
        time.delay(400)
    background = image.load('./диалоги/3этап(медицина)/' + str(i) + '.png')
    screen.blit(background, (0, 0))
    display.flip()



while 1:
    for i in event.get():
        if i.type == QUIT:

            sys.exit()
