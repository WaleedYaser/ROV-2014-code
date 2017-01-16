import pygame, sys
from pygame.locals import *
import tkFileDialog as msg
pygame.init()
screen = pygame.display.set_mode((1366,748))
pygame.display.set_caption('Future ROV')
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
x = msg.askopenfilename()
y = str(x)
image = pygame.image.load(y) 
screen.blit(image, (0,0))
l = [None]*8
i = 1
lenght = 0
laser = 42.5
font = pygame.font.Font('freesansbold.ttf',20)
msg = 'hello'
blueColor = pygame.Color(0, 0, 255)
whiteColor = pygame.Color(255,255,255)
while True:
    screen.fill(whiteColor)
    screen.blit(image, (0,0))
    msgSurfaceObj = font.render(msg, False, blueColor)
    msgRectObj = msgSurfaceObj.get_rect()
    msgRectObj.topleft = (800,600)
    screen.blit(msgSurfaceObj, msgRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONUP:
            if i == 1:
                l[0], l[1] = event.pos
                msg ='first point of ship: Done' 
                i = 2
            elif i == 2:
                l[2],l[3] = event.pos
                msg ='second point of ship: Done'
                i = 3
            elif i == 3:
                l[4],l[5] = event.pos
                msg ='first point of laser: Done'
                i = 4
            elif i == 4:
                l[6], l[7] = event.pos
                msg ='second point of laser: Done'
                i = 1
            
        
        elif event.type == KEYDOWN:
            if event.key == K_d:
                msg = 'new'
                l = [None]*8
                i = 1

            if event.key == K_a:
                length = ((l[0] - l[2])**2 + (l[1] - l[3])**2)**.5
                laser_length = ((l[4] - l[6])**2 + (l[5] - l[7])**2)**.5
                real_length = (laser * length)/laser_length
                msg = 'length = ' + str(real_length)
    pygame.display.update()
    
