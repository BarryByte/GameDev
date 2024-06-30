import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('SST')
x1 = 0  
y1 = 0
x2 = 1080
y2 = 0
velocity = 10
block = pygame.Rect(500,500,100,100)
image  = pygame.image.load('johnwick.jpg')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP] and y1 > 0:
        y1 -= velocity
    if keys[pygame.K_s] or keys[pygame.K_DOWN]and y1 < 620: 
        y1 += velocity
    if keys[pygame.K_a] and x1 > 0:
        x1 -= velocity
    if keys[pygame.K_d] and x1 < 1180:
        x1 += velocity
    if keys[pygame.K_i]:
        y2 -= velocity
    if keys[pygame.K_k]:
        y2 += velocity
    if keys[pygame.K_j]:
        x2 -= velocity
    if keys[pygame.K_l]:
        x2 += velocity

    screen.fill((5, 45, 5))

    pygame.draw.rect(screen, (255, 0, 0), (x1, y1, 100, 100))
    pygame.draw.rect(screen, (0, 255, 0), (x2, y2, 100, 100))
    screen.blit(image, (x1,y1))
    pygame.display.update()

    pygame.time.Clock().tick(60)