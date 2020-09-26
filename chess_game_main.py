import pygame
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (700, 70)
# initialize pygame module
pygame.init()
# set some constant values
WIDTH = 600
E_WIDTH = 100
gap = 75
BLACK = (139, 69, 45)
WHITE = (250, 235, 215)
RED = (255, 0, 0)

# set the display screen
screen = pygame.display.set_mode((WIDTH, WIDTH + E_WIDTH))
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


# class for box in chess board
class Box:
    def __init__(self, clr, row, col, width):
        self.clr = clr
        self.x = row * width
        self.y = col * width
        self.width = width
        self.piece = None

    # function to draw each box
    def draw_box(self):
        pygame.draw.rect(screen, self.clr, (self.x, self.y, self.width, self.width))


# To create grid of box
def create_grid():
    grid = []
    for i in range(8):
        grid.append([])
        for j in range(8):
            box = Box(WHITE, i, j, gap)
            grid[i].append(box)
    return grid


# To draw grid lines
def create_board():
    for i in range(9):
        pygame.draw.line(screen, BLACK, (0, i * gap), (WIDTH, i * gap))
        pygame.draw.line(screen, BLACK, (i * gap, 0), (i * gap, WIDTH))


# To make a black and white pattern in the board
def make_box(grid):
    for i in range(8):
        for j in range(8):
            if (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0):
                grid[i][j].clr = BLACK
            else:
                grid[i][j].clr = WHITE
            #grid[i][j].draw_box()
    create_board()


def get_row(pos):
    x, y = pos
    row = y // gap
    col = x // gap
    return row, col


grid = create_grid()
make_box(grid)

# class for a pawn piece
class Pawn:
    def __init__(self, p_x, p_y):
        self.px = p_x
        self.py = p_y
        self.row = p_y // gap
        self.col = p_x // gap
        grid[self.row][self.col].piece = self
        self.first_move = True

    # To show a pawn on board
    def show_pawn(self):
        screen.blit(black_pawn, (self.px, self.py))

    def check_move(self, row, col):
        if self.first_move:
            grid[row][col+1].clr = RED
            grid[row][col+2].clr = RED
        else:
            grid[row][col+1].clr = RED
        grid[self.row + 1][self.col].draw_box()


p = Pawn(10, 85)
p1 = Pawn(85, 85)
p2 = Pawn(85+75, 85)
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
        # check if mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[1]< 600:
                row, col = get_row(pos)
            if grid[row][col].piece is None:
                make_box(grid)
            else:
                grid[row][col].piece.check_move(col,row)

    # To create a chess board
    for i in range(8):
        for j in range(8):
            grid[i][j].draw_box()
    p.show_pawn()
    p1.show_pawn()
    p2.show_pawn()

    # update the display screen
    pygame.display.update()
