import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Hello World!')


space = pygame.transform.scale(pygame.image.load('space.png'),(600,600))
red = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('redship.png'),(50,50)),90)
yellow = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('yellowship.png'),(50,50)),-90)

border = pygame.Rect(290,0,20,600)

redrect = pygame.Rect(50,300,50,50)
yellowrect = pygame.Rect(500,300,50,50)


def movement():
    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_w] and redrect.top>0:
        redrect.y = redrect.y-2
    if keypress[pygame.K_s]and redrect.bottom<600:
        redrect.y = redrect.y+2
    if keypress[pygame.K_a] and redrect.left>0:
        redrect.x = redrect.x-2
    if keypress[pygame.K_d]and redrect.right<290:
        redrect.x = redrect.x+2
        
    if keypress[pygame.K_UP]and yellowrect.top>0:
        yellowrect.y = yellowrect.y-2
    if keypress[pygame.K_DOWN]and yellowrect.bottom<600:
        yellowrect.y = yellowrect.y+2
    if keypress[pygame.K_LEFT]and yellowrect.left>310:
        yellowrect.x = yellowrect.x-2
    if keypress[pygame.K_RIGHT] and yellowrect.right<600:
        yellowrect.x = yellowrect.x+2

def loadscreen():
    screen.blit(space,(0,0))
    screen.blit(red,(redrect.x,redrect.y))
    screen.blit(yellow,(yellowrect.x,yellowrect.y))
    pygame.draw.rect(screen,'white',border)

delay = pygame.time.Clock()


while True:
    delay.tick(60)
    loadscreen()
    movement()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
         
    pygame.display.update()