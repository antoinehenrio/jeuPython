import sys, pygame, time
pygame.init()
 
size = width, height = 640, 480
speed = [30, 30]
white = 255, 255, 255
screen = pygame.display.set_mode(size)
 
dragon = pygame.image.load("./sprites/dragon.png")
dragon = pygame.transform.scale(dragon, (40,40))
dragonRect = dragon.get_rect()
dragonRect.y = height - 40
pygame.key.set_repeat(100,45)
jumpCount = 10

def monte(objetRect):
	for x in range(0,speed[0]):
		objetRect.y -= 1
		time.sleep(0.01)
def descend(objetRect):
	for x in range(0,speed[0]):
		objetRect.y += 1
		time.sleep(0.01)

while 1:
    for event in pygame.event.get():
    	if event.type == pygame.QUIT: sys.exit()
    	if event.type == pygame.KEYDOWN:
    		keys = pygame.key.get_pressed()
    		if keys[pygame.K_RIGHT]:
    			if dragonRect.x + 40 + speed[0] < width:
    				dragonRect = dragonRect.move(speed[0],0)
    			else:
    				dragonRect = dragonRect.move(width - 40 - dragonRect.x,0)
    		if keys[pygame.K_LEFT]:
    			if dragonRect.x > speed[0]:
    				dragonRect = dragonRect.move(-1 * speed[0],0)
    			else:
    				dragonRect = dragonRect.move(-1 * dragonRect.x,0)
    		if keys[pygame.K_SPACE]:
    			# monte(dragonRect)
    			# time.sleep(1)
    			# descend(dragonRect)
    			dragonRect = dragonRect.move(0,-1 * speed[0])
    			dragonRect = dragonRect.move(0,speed[0])
    			for x in range(0,speed[0] + 1):
    				dragonRect = dragonRect.move(0,-1)
    			screen.blit(dragon, dragonRect)
    			for y in range(speed[0],-1,-1):
    				dragonRect = dragonRect.move(0,1)
    screen.fill(white)
    screen.blit(dragon, dragonRect)
    pygame.display.flip()

