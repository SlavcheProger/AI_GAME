from pygame import *
import sys
from textediting import *
import math


init()

screen = display.set_mode((0, 0), FULLSCREEN)

display.set_caption("Turing's jorney")

background = image.load('./продолжить ряд/demo.png')
w, h = display.get_surface().get_size()
print("display_size",w,h)

background = transform.scale(background, (w, h))
print("image_size",background.get_width(), background.get_height())
rect = background.get_rect()
rect = rect.move((0, 0))
screen.blit(background, rect)
display.flip()



'''
for i in range(1, 17):
    background = image.load('./продолжить ряд/'+str(i)+'.png')
    w, h = display.get_surface().get_size()
    background = transform.scale(background, (w, h))
<<<<<<< HEAD
    print(w,h)
=======
>>>>>>> 5d9cc48719c4a5ceb25cb3af8853a1b4d8cab70d
    screen.blit(background, (0, 0))
    display.flip()
'''

<<<<<<< HEAD

text = EditText(screen, background, 0, 0)
print("!!!!",text)
=======
text = EditText(screen, background, 600, 650)
>>>>>>> 5d9cc48719c4a5ceb25cb3af8853a1b4d8cab70d
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
<<<<<<< HEAD
        elif e.type == VIDEORESIZE:
            #w, h = display.get_surface().get_size()
            surface = display.get_surface()
            #w = surface.get_width()
            #h = surface.get_height()
            infoObject = display.Info()
            w = infoObject.current_w
            h = infoObject.current_h
            background = transform.scale(background, (w, h))
            print("1",w, h)

            #print("*",windoWidth,windowHeight)
            screen.blit(background, (0, 0))
            display.update()
        elif e.type == VIDEOEXPOSE:  # handles window minimising/maximising
            w, h = display.get_surface().get_size()
            background = transform.scale(background, (w, h))
            print("2",w, h)
            #print("*", windoWidth, windowHeight)
            screen.blit(background, (0, 0))
            display.update()

=======
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False

        #if e.type is K_ESCAPE:
         #   if screen.get_flags() & FULLSCREEN:
          #      display.set_mode(size)
           # else:
            #    display.set_mode(size, FULLSCREEN)
>>>>>>> 5d9cc48719c4a5ceb25cb3af8853a1b4d8cab70d
quit()


