import sys
import pygame
import time
pygame.init()

size = width, height = 640, 480
speed = [30, 30]
white = 255, 255, 255
screen = pygame.display.set_mode(size)
isJump = False
jumpCount = 10
vel = 20

dragon = pygame.image.load("./sprites/dragon.png")
dragon = pygame.transform.scale(dragon, (40, 40))
y = height - 40
x = 0
while 1:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel

    if keys[pygame.K_RIGHT] and x < width - vel - 40:  
        x += vel

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    screen.fill(white)
    screen.blit(dragon,(x,y))
    pygame.display.flip()
