from pygame import *
import sys

init()

screen = display.set_mode((1890, 1417))


display.set_caption('none')


background = image.load('./диалоги/1этап(встреча)/1.png')

screen.blit(background, (0, 131))
for i in range(1, 83):
    if i == 8:
        continue
    time.delay(400)
    background = image.load('./диалоги/1этап(встреча)/' + str(i) + '.png')
    screen.blit(background, (0, 0))
    display.flip()



while 1:
    for i in event.get():
        if i.type == QUIT:

            sys.exit()
