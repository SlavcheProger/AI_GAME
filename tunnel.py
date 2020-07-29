from pygame import *
import sys

init()
screen = display.set_mode((600, 600))
display.set_caption('none')

color = (225,0,0)
img0 = image.load('./tunnel2.jpg')
img0 = transform.scale(img0, (600, 600))
screen.blit(img0, (0, 0))
display.flip()

img0.convert()
rect0 = img0.get_rect()
draw.rect(img0, color, rect0, 1)
center = 300, 300
img = img0
rect = img.get_rect()
rect.center = center
angle = 0
scale = 1
for e in event.get():

    if e.type == KEYDOWN:
        if e.type == K_r:
            if e.mod & KMOD_SHIFT:
                angle -= 10
            else:
                angle += 10
            img = transform.rotozoom(img0, angle, scale)
    elif e.type == K_s:
        if e.mod & KMOD_SHIFT:
            scale /= 1.1
        else:
            scale *= 1.1
        img = transform.rotozoom(img0, angle, scale)
    rect = img.get_rect()
    rect.center = center
    img0 = transform.scale(img0, (600, 600))
    screen.blit(img0, (0, 0))
    display.flip()