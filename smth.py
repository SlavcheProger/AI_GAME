from pygame import *
import sys

init()

screen = display.set_mode((1890, 1417))


display.set_caption('none')


background = image.load('./продолжить ряд/1.png')

screen.blit(background, (0, 0))
for i in range(1, 17):
    background = image.load('./продолжить ряд/' + str(i) + '.png')
    screen.blit(background, (0, 0))
    display.flip()



while 1:
    for i in event.get():
        if i.type == QUIT:

            sys.exit()




