import pygame
from sys import exit

pygame.init()
screen =  pygame.display.set_mode((1280,720))
pygame.display.set_caption('Farm')
clock = pygame.time.Clock()

screen.fill('coral')

test_surface = pygame.Surface((100,200))
#test_surface.fill('coral')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_surface,(0,0))

    pygame.display.update()
    clock.tick(60)
