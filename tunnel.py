from pygame import *
import sys

init()
screen = display.set_mode((600, 600))
display.set_caption('none')

background = image.load('./tunnel_3.jpg')
screen.blit(background, (0, 0))
display.flip()
size = 600

angle = 0
scale = 1

for a in range(0,100,10):
    img = transform.rotozoom(background, a, scale)
    rect = img.get_rect()
    rect.center = (300,300)
    print(a)
    screen.blit(img, rect)
    display.flip()
    scale *= 1.1
    print(scale)