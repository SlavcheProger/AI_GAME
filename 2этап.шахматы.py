from pygame import *
import sys

init()

screen = display.set_mode((0, 0), FULLSCREEN)


display.set_caption('none')


background = image.load('./диалоги/2этап(шахматы)/1.png')

screen.blit(background, (0, 0))
for i in range(1, 83):
    if i == 15:
        time.delay(25000)
    elif 51 <= i <= 57:
        time.delay(150)
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
        if e.type == K_ESCAPE:
            running = False

quit()