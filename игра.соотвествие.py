from pygame import *
import sys
from textediting import *

init()

screen = display.set_mode((0, 0), FULLSCREEN)


display.set_caption("Turing's jorney")


background = image.load('./соотвествие/1.png')

screen.blit(background, (0, 0))
for i in range(1, 7):
    background = image.load('./соотвествие/' + str(i) + '.png')
    w, h = display.get_surface().get_size()
    background = transform.scale(background, (w, h))
    screen.blit(background, (0, 0))
    display.flip()

text = EditText(screen, background, 600, 650)
while text != '4':
    f = font.SysFont(None, 700)
    img = f.render('WRONG', True, (255, 0, 68))
    screen.blit(img, (200, 300))
    display.update()
    time.delay(700)
    text = EditText(screen, background, 600, 650)

f = font.SysFont(None, 700)
img = f.render('WIN', True, (0,255,34))
screen.blit(img, (200, 300))
display.update()

running = True
while running:
    for e in event.get():
        if e.type == K_ESCAPE:
            running = False

quit()