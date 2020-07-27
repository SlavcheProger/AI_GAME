from pygame import *
import sys
import intro
import first_meet

init()
screen = display.set_mode((600, 600))
display.set_caption('none')

intro.show(screen, display)
first_meet.show(screen, display)
background = image.load('sdfsdfs')

quit()