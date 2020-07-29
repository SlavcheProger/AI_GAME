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
display.set_caption('Support Organization')

#first_slide.show(screen, display)
#intro.show(screen, display)
#first_meet.show(screen, display)
background = image.load('./background1.jpg')
screen.blit(background, (0, 0))
display.flip()
time.delay(100)
#continue_the_series.show(screen, display)
screen.blit(background, (0, 0))
display.flip()
time.delay(100)
#puzzles
background2 = image.load('./tunnel.jpg')
screen.blit(background2, (0, 0))
display.flip()
time.delay(100)
second_chess.show(screen, display)
screen.blit(background, (0, 0))
display.flip()
time.delay(100)
#riddle
screen.blit(background, (0, 0))
display.flip()
time.delay(100)
find_an_expression.show(screen, display)
screen.blit(background2, (0, 0))
display.flip()
time.delay(100)
third_medicine.show(screen, display)
screen.blit(background, (0, 0))
display.flip()
time.delay(100)
#division square
screen.blit(background, (0, 0))
display.flip()
time.delay(100)
expression.show(screen, display)
screen.blit(background2, (0, 0))
display.flip()
time.delay(100)
fourth_life.show(screen, display)

quit()