import pygame
import os
from chess_game_project import Objects
from chess_game_project import Threat_checking

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (700, 70)
# initialize pygame module
pygame.init()

# set constant values
WIDTH = 600
E_WIDTH = 100
gap = 75
BLACK = (139, 69, 45)
WHITE = (250, 235, 215)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
piece_list = []
white_move = True
black_move = False

# set the display screen
screen = pygame.display.set_mode((WIDTH, WIDTH + E_WIDTH))
# set the screen caption
pygame.display.set_caption("Chess Game")
# load the icon image
ico = pygame.image.load("images/horse.png")
# set the icon image for screen
pygame.display.set_icon(ico)


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


# To get row and col of specific position(tuple)
def get_row(position):
    x, y = position
    rows = y // gap
    cols = x // gap
    return rows, cols


# call created grid function
grid = create_grid()
make_box(grid)


# To eliminate emeny piece
def eliminate(row, col, grid):
    grid[row][col].piece.eliminated = True
    grid[row][col].piece = None


# check for piece to move
def check_piece_move(grid, row, col):
    global white_move, black_move
    if grid[row][col].piece is None and (grid[row][col].clr == BLACK or grid[row][col].clr == WHITE):
        make_box(grid)
        piece_list.clear()

    elif grid[row][col].piece is None and grid[row][col].clr == YELLOW:
        # function to move the piece
        Threat_checking.start_pos.clear()
        Threat_checking.final_pos.clear()
        Threat_checking.start_pos.append(
            [piece_list[0].row, piece_list[0].col, piece_list[0].first_move if piece_list[0].piece_name == "pawn"
                else piece_list[0].row, piece_list[0].col])
        piece_list[0].move(row, col, grid, collision=False)
        Threat_checking.final_pos.append([piece_list[0].row, piece_list[0].col, piece_list[0]])
        if white_move:
            if Threat_checking.check_for_threat(Objects.wkp.row, Objects.wkp.col, WHITE, grid):
                Threat_checking.take_back(grid)
        else:
            if Threat_checking.check_for_threat(Objects.bkp.row, Objects.bkp.col, BLACK, grid):
                Threat_checking.take_back(grid)
        if piece_list[0].clor == WHITE and not Threat_checking.back:
            white_move = False
            black_move = True
        elif piece_list[0].clor == BLACK and not Threat_checking.back:
            white_move = True
            black_move = False
        else:
            Threat_checking.back = False

    elif (grid[row][col].piece.clor == WHITE and white_move) or (grid[row][col].piece.clor == BLACK and black_move):
        if grid[row][col].piece is not None and (grid[row][col].clr == BLACK or grid[row][col].clr == WHITE):
            if len(piece_list) == 0:
                grid[row][col].piece.check_move(row, col, grid)
                piece_list.append(grid[row][col].piece)
            else:
                piece_list.pop()
                make_box(grid)
                grid[row][col].piece.check_move(row, col, grid)
                piece_list.append(grid[row][col].piece)

    elif grid[row][col].piece is not None and grid[row][col].clr == RED:
        # function to move the piece and eliminate enemy piece
        Threat_checking.start_pos.clear()
        Threat_checking.final_pos.clear()
        last_piece = grid[row][col].piece
        Threat_checking.start_pos.append(
            [piece_list[0].row, piece_list[0].col, piece_list[0].first_move if piece_list[0].piece_name == "pawn"
                else piece_list[0].row, piece_list[0].col])
        piece_list[0].move(row, col, grid, collision=True)
        Threat_checking.final_pos.append([piece_list[0].row, piece_list[0].col, piece_list[0]])
        if white_move:
            if Threat_checking.check_for_threat(Objects.wkp.row, Objects.wkp.col, WHITE, grid):
                Threat_checking.take_back(grid)
        else:
            if Threat_checking.check_for_threat(Objects.bkp.row, Objects.bkp.col, BLACK, grid):
                Threat_checking.take_back(grid)
        if piece_list[0].clor == WHITE and not Threat_checking.back:
            white_move = False
            black_move = True
        elif piece_list[0].clor == BLACK and not Threat_checking.back:
            white_move = True
            black_move = False
        else:
            last_piece.eliminated = False
            grid[row][col].piece = last_piece
            Threat_checking.back = False


# initialize objects of all piece class
Objects.obj_init(grid, screen)

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

    for i in range(len(Objects.pawn_list)):
        Objects.pawn_list[i].show_pawn()

    for i in range(len(Objects.rook_list)):
        Objects.rook_list[i].show_rook()
        Objects.knight_list[i].show_knight()
        Objects.bishop_list[i].show_bishop()

    for i in range(len(Objects.king_list)):
        Objects.king_list[i].show_king()
        Objects.queen_list[i].show_queen()

    create_board()

    # update the display screen
    pygame.display.update()
