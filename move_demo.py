from pygame import *
import sys

red = (255,0,0)
white = (255,255,255)
black = (0,0,0)

init()
screen = display.set_mode((320, 320))
display.set_caption("Turing's jorney")

moving = False

rect = Rect(50, 50, 100,100)

running = True

field = [[1,-1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
rects = [img1,img2]

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(e.pos):
                moving = True
        elif e.type == MOUSEBUTTONUP:
            moving = False
        elif e.type == MOUSEMOTION and moving:
            rect.move_ip(e.rel)
            print("*", e.rel)

        screen.fill(white)
        draw.rect(screen, red, rect)

        if moving:
            draw.rect(screen, black, rect, 4)

    display.flip()
quit()
