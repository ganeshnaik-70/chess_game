import pygame

# initialize pygame module
pygame.init()
# set the display screen
screen = pygame.display.set_mode((800, 700))
# set the screen caption
pygame.display.set_caption("Chess Game")
# load the icon image
ico = pygame.image.load("images/horse.png")
# set the icon image for screen
pygame.display.set_icon(ico)

# load all piece images
black_pawn = pygame.image.load("images/black_pawn.png")
black_rook = pygame.image.load("images/black_rook.png")
black_bishop = pygame.image.load("images/black_bishop.png")
black_king = pygame.image.load("images/black_king.png")
black_queen = pygame.image.load("images/black_queen.png")
black_horse = pygame.image.load("images/black_horse.png")
white_pawn = pygame.image.load("images/white_pawn.png")
white_rook = pygame.image.load("images/white_rook.png")
white_bishop = pygame.image.load("images/white_bishop.png")
white_king = pygame.image.load("images/white_king.png")
white_queen = pygame.image.load("images/white_queen.png")
white_horse = pygame.image.load("images/white_horse.png")

# main game loop
running = True
while running:
    # fill the screen with black colour
    screen.fill((255, 255, 255))

    # check for the event happen in pygame
    for event in pygame.event.get():
        # check if exit key is pressed
        if event.type == pygame.QUIT:
            running = False

    # creating a chess board
    for i in range(9):
        pygame.draw.line(screen, (0, 0, 0), (110, 50 + i * 70), (670, 50 + i * 70), 2)
        pygame.draw.line(screen, (0, 0, 0), (110 + i * 70, 50), (110 + i * 70, 610), 2)
    for i in range(8):
        for j in range(8):
            if (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0):
                screen.fill((160, 82, 45), (110 + i * 70, 50 + j * 70, 71, 71))
            else:
                screen.fill((255, 240, 240), (110 + i * 70, 50 + j * 70, 71, 71))

    screen.blit(black_horse, (115 + 70, 195 - 70))

    # update the display screen
    pygame.display.update()
