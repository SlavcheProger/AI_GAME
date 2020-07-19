from pygame import *
import sys

init()

screen = display.set_mode((1890, 1417))


display.set_caption('none')


background = image.load('./первый слайд/1.png')

screen.blit(background, (0, 0))
for i in range(1, 14):
    if 5 <= i <= 9:
        time.delay(3500)
    else:
        time.delay(300)
    background = image.load('./первый слайд/' + str(i) + '.png')
    screen.blit(background, (0, 0))
    display.flip()



while 1:
    for i in event.get():
        if i.type == QUIT:

            sys.exit()
