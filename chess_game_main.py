import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
running = True
while running:

    # fill the screen with black colour
    screen.fill((0, 0, 0))

    # check for the event happen in pygame
    for event in pygame.event.get():

        # check if exit key is pressed
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()