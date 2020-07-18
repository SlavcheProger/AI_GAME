from pygame import *
import sys

init()

screen = display.set_mode((1890, 1417))

display.set_caption("Turing's jorney")

background = image.load('./продолжить ряд/1.png')
screen.blit(background, (0, 0))

for i in range(1, 17):
    background = image.load('./продолжить ряд/'+str(i)+'.png')
    screen.blit(background, (0, 0))
    display.flip()

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

pygame.quit()
