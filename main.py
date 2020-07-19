from pygame import *
import sys
from textediting import *

init()

screen = display.set_mode((1890, 1417))

display.set_caption("Turing's jorney")

background = image.load('./продолжить ряд/1.png')
screen.blit(background, (0, 0))

for i in range(1, 17):
    background = image.load('./продолжить ряд/'+str(i)+'.png')
    screen.blit(background, (0, 0))
    display.flip()

text = EditText(screen, background, 600, 650)
print("!!!!",text)
while text != '1':
    f = font.SysFont(None, 48)
    img = f.render('No!!!!', True, (255, 0, 0))
    screen.blit(img, (0, 0))
    display.update()
    text = EditText(screen, background, 600, 650)

print("WIN!")

f = font.SysFont(None, 48)
img = f.render('WIN!!!!', True, (255,0,0))
screen.blit(img, (0,0))
display.update()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

quit()
