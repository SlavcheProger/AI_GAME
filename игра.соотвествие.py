from pygame import *
import sys
from textediting import *

init()

screen = display.set_mode((600, 600))


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
    f = font.SysFont(None, 300)
    img = f.render('NO', True, (255, 0, 68))
    screen.blit(img, (100, 100))
    display.update()
    time.delay(700)
    text = EditText(screen, background, 600//2, 600-100)

f = font.SysFont(None, 300)
img = f.render('WIN', True, (0,255,34))
screen.blit(img, (100, 100))
display.update()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False
quit()