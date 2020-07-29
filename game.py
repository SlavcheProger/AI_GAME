from pygame import *
import sys
import intro
import first_meet
import first_slide
import continue_the_series
import second_chess
import find_an_expression
import third_medicine
import expression
import fourth_life

init()
screen = display.set_mode((600, 600))
display.set_caption('none')

first_slide.show(screen, display)
intro.show(screen, display)
first_meet.show(screen, display)

background = image.load('./background1.jpg')
continue_the_series.show(screen, display)
background2 = image.load('./background1.jpg')

#puzzles
background3 = image.load('./tunnel.jpg')
second_chess.show(screen, display)
background4 = image.load('./background1.jpg')
#riddle
background5 = image.load('./background1.jpg')
find_an_expression.show(screen, display)
background6 = image.load('./tunnel.jpg')
third_medicine.show(screen, display)
background7 = image.load('./background1.jpg')
#division square
background8 = image.load('./background1.jpg')
expression.show(screen, display)
background9 = image.load('./tunnel.jpg')
fourth_life.show(screen, display)

quit()