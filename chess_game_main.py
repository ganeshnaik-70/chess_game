import pygame

pygame.init()
screen = pygame.display.set_mode((800, 700))
running = True
while running:
    # fill the screen with black colour
    screen.fill((255, 255, 255))

    # check for the event happen in pygame
    for event in pygame.event.get():
        # check if exit key is pressed
        if event.type == pygame.QUIT:
            running = False

    for i in range(9):
        pygame.draw.line(screen, (0, 0, 0), (110, 50 + i * 70), (670, 50 + i * 70), 2)
        pygame.draw.line(screen, (0, 0, 0), (110 + i * 70, 50), (110 + i * 70, 610), 2)
    for i in range(8):
        for j in range(8):
            if (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0):
                screen.fill((160, 82, 45), (110 + i * 70, 50 + j * 70, 71, 71))
            else:
                screen.fill((255, 240, 240), (110 + i * 70, 50 + j * 70, 71, 71))

    pygame.display.update()
