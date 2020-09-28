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
YELLOW = (255, 255, 0)
piece_list = []
black_pawn_list = []
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


# To check for a valid place to move
def check_place(obj):
    if obj.piece is None:
        return True
    else:
        return False


def check_pawn_first_move(obj):
    if check_place(obj):
        obj.clr = YELLOW
        return True
    else:
        return False


# class for a pawn piece
class Pawn:
    def __init__(self, p_x, p_y, clr):
        self.px = p_x
        self.py = p_y
        self.row = p_y // gap
        self.col = p_x // gap
        grid[self.row][self.col].piece = self
        self.first_move = True
        self.diagonal_move = []
        self.straight_move = []
        self.eliminated = False
        self.clor = clr

    # To show a pawn on board
    def show_pawn(self):
        if not self.eliminated:
            screen.blit(black_pawn, (self.px, self.py))

    def check_move(self, row, col):
        self.check_diagonal(row, col)
        if self.first_move:
            if check_pawn_first_move(grid[row + 1][col]):
                if check_place(grid[row + 2][col]):
                    grid[row + 2][col].clr = YELLOW
        else:
            check_pawn_first_move(grid[row + 1][col])

    def check_diagonal(self, row, col):
        if col > 0 and grid[row + 1][col - 1].piece is not None and grid[row + 1][col - 1].piece.clor == WHITE:  # left
            grid[row + 1][col - 1].clr = RED
            self.diagonal_move.append(grid[row + 1][col - 1])
        if col < 7 and grid[row + 1][col + 1].piece is not None and grid[row + 1][col + 1].piece.clor == WHITE:  # right
            grid[row + 1][col + 1].clr = RED
            self.diagonal_move.append(grid[row + 1][col + 1])

    def move(self, row, col, collision):
        self.px = col * gap + 10
        self.py = row * gap + 10
        if collision:
            self.eliminate(row, col)
        grid[row][col].piece = self
        self.first_move = False
        grid[self.row][self.col].piece = None
        self.row = self.py // gap
        self.col = self.px // gap
        make_box(grid)

    def eliminate(self, row, col):
        grid[row][col].piece.eliminated = True
        grid[row][col].piece = None


def check_piece_move(grid, row, col):
    if grid[row][col].piece is not None and (grid[row][col].clr == BLACK or grid[row][col].clr == WHITE):
        if len(piece_list) == 0:
            grid[row][col].piece.check_move(row, col)
            piece_list.append(grid[row][col].piece)
        else:
            piece_list.pop()
            make_box(grid)
            grid[row][col].piece.check_move(row, col)
            piece_list.append(grid[row][col].piece)
        print(piece_list)

    elif grid[row][col].piece is None and grid[row][col].clr == YELLOW:
        # function to move the piece
        piece_list[0].move(row, col, collision=False)

    elif grid[row][col].piece is not None and grid[row][col].clr == RED:
        # function to move the piece and eliminate enemy piece
        piece_list[0].move(row, col, collision=True)

    elif grid[row][col].piece is None and (grid[row][col].clr == BLACK or grid[row][col].clr == WHITE):
        make_box(grid)
        piece_list.clear()


for i in range(8):
    p = Pawn(10 + i * gap, 85, BLACK)
    black_pawn_list.append(p)

s = Pawn(10 + 75, 10 + 75 * 2, WHITE)

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

    for i in range(len(black_pawn_list)):
        black_pawn_list[i].show_pawn()

    create_board()
    s.show_pawn()
    # screen.blit(white_pawn, (10 + 75, 10 + 75 * 2))
    # screen.blit(white_pawn, (10 + 75 * 3, 10 + 75 * 2))
    # grid[2][1].piece = white_pawn
    # grid[2][3].piece = white_pawn

    # update the display screen
    pygame.display.update()
