import pygame, sys
from pygame.locals import *

pygame.init()

screen_width = 3200
screen_height = 2000
screen = pygame.display.set_mode((screen_width, screen_height))

red = (255, 0, 0) 
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (165, 42, 42)
green = (0, 255, 0)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
orange = (255, 165, 0)
purple = (128, 0, 128)
pink = (255, 192, 203)
light_blue = (173, 216, 230)
dark_green = (0, 100, 0)
gray = (128, 128, 128)

while True:
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()




    pygame.display.update()

    pygame.time.Clock().tick(60)
