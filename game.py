import pygame, sys, random
from pygame.locals import *

class Block:
    def __init__(self, x, y):
        self.width = 50
        self.height = 30
        self.rect = pygame.Rect(x, y, self.width, self.height)

class Bullet:
    def __init__(self,x,y):
        self.width = 20
        self.height = 30
        self.rect = pygame.Rect(x, y, self.width, self.height)

class Explosion:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load('explosion.png'), (100, 100))
        self.rect = self.image.get_rect(center=(x, y))
        self.timer = 20  # Display explosion for 60 frames



pygame.init()
# screen = pygame.display.set_mode((3200, 2000))
screen = pygame.display.set_mode((3200, 2000), pygame.HWSURFACE | pygame.DOUBLEBUF)

pygame.display.set_caption('invaders')

red = (255, 0, 0) 
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (165, 42, 42)

player_x = 1600
player_y = 1800
velocity = 30

bullets = []
blocks = []
explosions = []

for i in range(1000):
    block_x = random.randint(100, 3100)
    block_y = random.randint(50, 1500)
    block = Block(block_x, block_y)
    blocks.append(block)

while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player_x,player_y-20))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]  or keys[pygame.K_LEFT]  and player_x > 0 and player_x < 3000:
        player_x -= 5
    if keys[pygame.K_d] or keys[pygame.K_RIGHT] and player_y < 3000 and player_x > 0:
        player_x += 5
    
    screen.fill(white)
    
    for bullet in bullets:
        for block in blocks:
            if bullet.rect.colliderect(block.rect):
                if bullets.count(bullet) == 1:
                    bullets.remove(bullet)
                blocks.remove(block)
                explosions.append(Explosion(block.rect.x, block.rect.y))
                break


    for block in blocks:
        pygame.draw.rect(screen, black, block.rect)

    for explosion in explosions:
        explosion.timer -= 1
        if explosion.timer <= 0:
            explosions.remove(explosion)
            print(explosion.rect.x)
        else:
            screen.blit(explosion.image, explosion.rect)

                

    

    for bullet in bullets:
        bullet.rect.y -= velocity
        pygame.draw.rect(screen, brown, bullet.rect)

    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 100, 100))
   
    pygame.display.update()

    pygame.time.Clock().tick(60)