import pygame
pygame.init()

#Window Setup
resolution = (1280, 720)
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Insert List")
WHITE = ( 255, 255, 255)

#Loop Setup
condition = True
fps = pygame.time.Clock()

while condition:
    #For loop handles all events, do NOT duplicate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            condition = False

    #Game Logic Here
    
    #Drawing code
    
    #Clear Screen
    screen.fill(WHITE)

    #Frame Update
    pygame.display.flip()
    fps.tick(60)

pygame.quit()
