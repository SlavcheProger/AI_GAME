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
import tunnel
import division_square
import puzzles

init()
screen = display.set_mode((600, 600))

display.set_caption('Support Organization')

#first_slide.show(screen, display)
#intro.show(screen, display)
#first_meet.show(screen, display)

#background = image.load('./background1.jpg')
#screen.blit(background, (0, 0))
#display.flip()
#time.delay(100)
#continue_the_series.show(screen, display)
#screen.blit(background, (0, 0))
#display.flip()
#time.delay(100)

#puzzles.show(screen, display)
#tunnel.show(screen, display)

#second_chess.start(screen, display)

#riddle
#background5 = image.load('./background1.jpg')
#screen.blit(background, (0, 0))
#display.flip()
#time.delay(100)
#find_an_expression.show(screen, display)
#tunnel.show(screen, display)
#third_medicine.show(screen, display)
#screen.blit(background, (0, 0))
#display.flip()
#time.delay(100)
division_square.show(screen, display)
#screen.blit(background, (0, 0))
#display.flip()
#time.delay(100)
#expression.show(screen, display)
#tunnel.show(screen, display)
#fourth_life.show(screen, display)

quit()