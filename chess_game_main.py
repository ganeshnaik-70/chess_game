import pygame
import os
from chess_game_project import Pawn_piece, Rook_piece, Knight_piece, King_piece, Bishop_piece, Queen_piece

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
YELLOW = (255, 255, 0)
piece_list = []
pawn_list = []
bishop_list = []
rook_list = []
knight_list = []
king_list = []
queen_list = []
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
            box = Box(WHITE, j, i, gap)
            grid[i].append(box)
    return grid


# To draw grid lines
def create_board():
    for i in range(9):
        pygame.draw.line(screen, BLACK, (0, i * gap), (WIDTH, i * gap), 3)
        pygame.draw.line(screen, BLACK, (i * gap, 0), (i * gap, WIDTH), 3)


# To make a black and white pattern in the board
def make_box(grid):
    for i in range(8):
        for j in range(8):
            if (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0):
                grid[i][j].clr = BLACK
            else:
                grid[i][j].clr = WHITE


def get_row(position):
    x, y = position
    rows = y // gap
    cols = x // gap
    return rows, cols


grid = create_grid()
make_box(grid)


# To eliminate emeny piece
def eliminate(row, col, grid):
    grid[row][col].piece.eliminated = True
    grid[row][col].piece = None


def check_piece_move(grid, row, col):
    if grid[row][col].piece is not None and (grid[row][col].clr == BLACK or grid[row][col].clr == WHITE):
        if len(piece_list) == 0:
            grid[row][col].piece.check_move(row, col, grid)
            piece_list.append(grid[row][col].piece)
        else:
            piece_list.pop()
            make_box(grid)
            grid[row][col].piece.check_move(row, col, grid)
            piece_list.append(grid[row][col].piece)

    elif grid[row][col].piece is None and grid[row][col].clr == YELLOW:
        # function to move the piece
        piece_list[0].move(row, col, grid, collision=False)

    elif grid[row][col].piece is not None and grid[row][col].clr == RED:
        # function to move the piece and eliminate enemy piece
        piece_list[0].move(row, col, grid, collision=True)

    elif grid[row][col].piece is None and (grid[row][col].clr == BLACK or grid[row][col].clr == WHITE):
        make_box(grid)
        piece_list.clear()


for i in range(8):
    bpp = Pawn_piece.Pawn(10 + i * gap, 85, BLACK, black_pawn, grid, screen)
    wpp = Pawn_piece.White_pawn(10 + i * gap, 460, WHITE, white_pawn, grid, screen)
    pawn_list.append(bpp)
    pawn_list.append(wpp)

brp1 = Rook_piece.Rook(10, 10, BLACK, black_rook, grid, screen)
brp2 = Rook_piece.Rook(10+75*7, 10, BLACK, black_rook, grid, screen)
wrp1 = Rook_piece.Rook(10, 10+75*7, WHITE, white_rook, grid, screen)
wrp2 = Rook_piece.Rook(10+75*7, 10+75*7, WHITE, white_rook, grid, screen)
rook_list.append(brp1)
rook_list.append(brp2)
rook_list.append(wrp1)
rook_list.append(wrp2)

bkp1 = Knight_piece.Knight(10 + 75, 10, BLACK, black_horse, grid, screen)
bkp2 = Knight_piece.Knight(10 + 75 * 6, 10, BLACK, black_horse, grid, screen)
wkp1 = Knight_piece.Knight(10 + 75, 10+75*7, WHITE, white_horse, grid, screen)
wkp2 = Knight_piece.Knight(10 + 75*6, 10+75*7, WHITE, white_horse, grid, screen)
knight_list.append(bkp1)
knight_list.append(bkp2)
knight_list.append(wkp1)
knight_list.append(wkp2)

bbp1 = Bishop_piece.Bishop(10+75*2, 10, BLACK, black_bishop, grid, screen)
bbp2 = Bishop_piece.Bishop(10+75*5, 10, BLACK, black_bishop, grid, screen)
wbp1 = Bishop_piece.Bishop(10+75*2, 10+75*7, WHITE, white_bishop, grid, screen)
wbp2 = Bishop_piece.Bishop(10+75*5, 10+75*7, WHITE, white_bishop, grid, screen)
bishop_list.append(bbp1)
bishop_list.append(bbp2)
bishop_list.append(wbp1)
bishop_list.append(wbp2)

bqp = Queen_piece.Queen(10 + 75 * 3, 10, BLACK, black_queen, grid, screen)
wqp = Queen_piece.Queen(10 + 75 * 3, 10 + 75 * 7, WHITE, white_queen, grid, screen)
queen_list.append(bqp)
queen_list.append(wqp)

bkp = King_piece.King(10+75*4, 10, BLACK, black_king, grid, screen)
wkp = King_piece.King(10+75*4, 10+75*7, WHITE, white_king, grid, screen)
king_list.append(bkp)
king_list.append(wkp)


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
            if pos[1] < 600:
                row, col = get_row(pos)
                check_piece_move(grid, row, col)

    # To create a chess board
    for i in range(8):
        for j in range(8):
            grid[i][j].draw_box()

    for i in range(len(pawn_list)):
        pawn_list[i].show_pawn()

    for i in range(len(rook_list)):
        rook_list[i].show_rook()
        knight_list[i].show_knight()
        bishop_list[i].show_bishop()

    for i in range(len(king_list)):
        king_list[i].show_king()
        queen_list[i].show_queen()

    create_board()

    # update the display screen
    pygame.display.update()
