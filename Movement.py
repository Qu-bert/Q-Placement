__author__ = 'RobertM'
# By Robert, designed for Python 2.7.9
# Version 1.00
# To do list: Make rect smaller, collision is too far away from actual sprite
import pygame

# Player Setup


class Player(pygame.sprite.Sprite):
    def __init__(self, name_input, x, y):
        super(Player, self).__init__()
        self.image = pygame.image.load("Sprites\character1.png").convert()
        self.name = name_input
        # Handler for cords
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Variables for new cords
        self.newX = x
        self.newY = y

        # Set transparent colour
        self.image.set_colorkey(RED)


    def update(self):
        self.rect.x += self.newRect.x
        self.rect.y += self.newRect.y


class Interact(pygame.sprite.Sprite):
    def __init__(self, name_input, x, y):
        super(Interact, self).__init__()
        self.image = pygame.image.load("Sprites\character3.png").convert()
        self.name = name_input
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.set_colorkey(RED)

pygame.init()

# Window Setup
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
resolution = screen.get_size()
pygame.display.set_caption("Player Movement Test - Q-Bert")
WHITE = (255, 255, 255)
RED = (237, 28, 36)

# Loop Setup
condition = True
fps = pygame.time.Clock()

# Background Setup
background = pygame.image.load("Background\LectureHall.png").convert()
background = pygame.transform.scale(background, resolution)

# Initialise objects
spritesList = pygame.sprite.Group()
defaultPlayer = Player("defaultPlayer", 800, 800)
npc = Interact("interact", 1700, 800)
spritesList.add(defaultPlayer)
spritesList.add(npc)


while condition:
    # Clear Screen
    screen.fill(WHITE)
    # For loop handles all events, do NOT duplicate for loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            condition = False

        # Mouse Input
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            defaultPlayer.newX = mousePos[0]
            if mousePos[1] > 750:
                defaultPlayer.newY = mousePos[1]

        # Keyboard Input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                condition = False

    if pygame.sprite.collide_rect(defaultPlayer, npc):
        print("Collision detected")
        defaultPlayer.newX = defaultPlayer.rect.centerx - 1
        defaultPlayer.newY = defaultPlayer.rect.centery - 1

    # Movement
    if defaultPlayer.rect.centerx < defaultPlayer.newX:
        defaultPlayer.rect.x += 1
    if defaultPlayer.rect.centerx > defaultPlayer.newX:
        defaultPlayer.rect.x -= 1
    if defaultPlayer.rect.centery < defaultPlayer.newY:
        defaultPlayer.rect.y += 1
    if defaultPlayer.rect.centery > defaultPlayer.newY:
        defaultPlayer.rect.y -= 1

    # Draw Update
    screen.blit(background, [0, 0])
    spritesList.draw(screen)

    # Frame Update
    pygame.display.flip()
    fps.tick(200)

pygame.quit()
