from pygame import *
import sys
from textediting import *


init()

screen = display.set_mode((0, 0), FULLSCREEN)

display.set_caption("Turing's jorney")

background = image.load('./продолжить ряд/1.png')
screen.blit(background, (0, 0))

for i in range(1, 17):
    background = image.load('./продолжить ряд/'+str(i)+'.png')
    w, h = display.get_surface().get_size()
    background = transform.scale(background, (w, h))
    screen.blit(background, (0, 0))
    display.flip()

text = EditText(screen, background, 600, 650)
while text != '1':
    f = font.SysFont(None, 700)
    img = f.render('WRONG', True, (255, 0, 68))
    screen.blit(img, (200, 300))
    display.update()
    time.delay(700)
    text = EditText(screen, background, 600, 650)

f = font.SysFont(None, 700)
img = f.render('WIN', True, (0,255,34))
screen.blit(img, (200,300))
display.update()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False

        #if e.type is K_ESCAPE:
         #   if screen.get_flags() & FULLSCREEN:
          #      display.set_mode(size)
           # else:
            #    display.set_mode(size, FULLSCREEN)
quit()


