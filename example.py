from pygame import *
import sys

red = (255, 0, 0)
blue = (0,0,255)
green = (0,255,0)
init()

screen = display.set_mode((600, 600))

display.set_caption("Turing's jorney")


background = image.load('./продолжить ряд/6.png')
w, h = display.get_surface().get_size()
background = transform.scale(background, (w, h))
rect = background.get_rect()
rect = rect.move((0,0))
screen.blit(background, rect)
display.flip()
z = 40
z1 = 10
z2 = z1// 2
data = []
for i in range(9):
    d = []
    for j in range(9):
        d.append(0)
        if j >= 8 or i >= 8:
            pass
        else:
            if i % 2 == j % 2:
                draw.rect(screen, red,(i*z, j*z, z,z))
            else:
                draw.rect(screen, green, (i * z, j * z, z, z))
        draw.ellipse(screen,blue, (i*z-z2, j*z-z2, z1, z1))

        data.append(d)
display.update()


running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False
        if e.type == MOUSEBUTTONDOWN:
            x, y = mouse.get_pos()
            x = x // z
            y = y // z
            print(x,y)
            #data[x][y] = 1
            #draw.rect(screen, green, (x * z, y * z, z, z))
            display.update()

quit()
