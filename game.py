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

init()
screen = display.set_mode((600, 600))
<<<<<<< HEAD
display.set_caption('none')
'''
first_slide.show(screen, display)
intro.show(screen, display)
first_meet.show(screen, display)

background = image.load('./background1.jpg')
continue_the_series.show(screen, display)
background2 = image.load('./background1.jpg')
'''
#puzzles

background3 = image.load('./tunnel.jpg')
second_chess.start(screen, display)
background4 = image.load('./background1.jpg')
=======
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

#puzzles
#tunnel.show(screen, display)
second_chess.start(screen, display)
>>>>>>> 69fc2a91c18108b72dcf3c10a049824d872ca7bb
#riddle
background5 = image.load('./background1.jpg')
screen.blit(background, (0, 0))
display.flip()
time.delay(100)
find_an_expression.show(screen, display)
tunnel.show(screen, display)
third_medicine.show(screen, display)
screen.blit(background, (0, 0))
display.flip()
time.delay(100)
#division square
screen.blit(background, (0, 0))
display.flip()
time.delay(100)
expression.show(screen, display)
tunnel.show(screen, display)
fourth_life.show(screen, display)

quit()