import sys, pygame
pygame.init()
 
size = width, height = 640, 480
speed = [30, 30]
white = 255, 255, 255
 
screen = pygame.display.set_mode(size)
 
dragon = pygame.image.load("./sprites/dragon.png")
dragon = pygame.transform.scale(dragon, (40,40))
dragonRect = dragon.get_rect()
# ballrect = ball.get_rect()
 
while 1:
    for event in pygame.event.get():
    	if event.type == pygame.QUIT: sys.exit()
    	if event.type == pygame.KEYDOWN:
    		keys = pygame.key.get_pressed()
    		if keys[pygame.K_RIGHT]:
    			dragonRect = dragonRect.move(20,0)
    		if keys[pygame.K_LEFT]:
    			dragonRect = dragonRect.move(-20,0)
    		if keys[pygame.K_UP]:
    			dragonRect = dragonRect.move(0,-20)
    		if keys[pygame.K_DOWN]:
    			dragonRect = dragonRect.move(0,20)

    screen.fill(white)
    screen.blit(dragon, dragonRect)
    pygame.display.flip()

