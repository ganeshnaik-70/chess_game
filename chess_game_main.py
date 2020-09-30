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
white_pawn_list = []
black_rook_list = []
white_rook_list = []
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











class White_pawn(Pawn):
    def check_move(self, row, col):
        if row > 0:
            self.check_diagonal(row, col)
            if self.first_move:
                if check_pawn_first_move(grid[row - 1][col]):
                    if check_place(grid[row - 2][col]):
                        grid[row - 2][col].clr = YELLOW
            else:
                check_pawn_first_move(grid[row - 1][col])

    def check_diagonal(self, row, col):
        if col > 0 and grid[row - 1][col - 1].piece is not None and grid[row - 1][col - 1].piece.clor == BLACK:  # left
            grid[row - 1][col - 1].clr = RED
            self.diagonal_move.append(grid[row - 1][col - 1])
        if col < 7 and grid[row - 1][col + 1].piece is not None and grid[row - 1][col + 1].piece.clor == BLACK:  # right
            grid[row - 1][col + 1].clr = RED
            self.diagonal_move.append(grid[row - 1][col + 1])


class Rook:
    def __init__(self, p_x, p_y, clr, img):
        self.px = p_x
        self.py = p_y
        self.row = p_y // gap
        self.col = p_x // gap
        self.front_list = []
        self.back_list = []
        self.left_list = []
        self.right_list = []
        grid[self.row][self.col].piece = self
        self.eliminated = False
        self.clor = clr
        self.rook_img = img

    # To show a rook on board
    def show_rook(self):
        if not self.eliminated:
            screen.blit(self.rook_img, (self.px, self.py))

    def check_move(self, row, col):
        self.front_move(row, col)
        self.back_move(row, col)
        self.left_move(row, col)
        self.right_move(row, col)
        for obj in self.front_list:
            obj.clr = YELLOW
        for obj in self.back_list:
            obj.clr = YELLOW
        for obj in self.left_list:
            obj.clr = YELLOW
        for obj in self.right_list:
            obj.clr = YELLOW
        self.front_list.clear()
        self.back_list.clear()
        self.left_list.clear()
        self.right_list.clear()

    def front_move(self, row, col):
        if row > 6:
            return
        else:
            if grid[row + 1][col].piece is None:
                self.front_list.append(grid[row + 1][col])
                self.front_move(row + 1, col)
            elif grid[row + 1][col].piece is not None and self.check_opponent(grid[row + 1][col].piece.clor):
                grid[row + 1][col].clr = RED
                return
            else:
                return

    def back_move(self, row, col):
        if row < 1:
            return
        else:
            if grid[row - 1][col].piece is None:
                self.back_list.append(grid[row - 1][col])
                self.back_move(row - 1, col)
            elif grid[row - 1][col].piece is not None and self.check_opponent(grid[row - 1][col].piece.clor):
                grid[row - 1][col].clr = RED
                return
            else:
                return

    def left_move(self, row, col):
        if col < 1:
            return
        else:
            if grid[row][col - 1].piece is None:
                self.left_list.append(grid[row][col - 1])
                self.left_move(row, col - 1)
            elif grid[row][col - 1].piece is not None and self.check_opponent(grid[row][col-1].piece.clor):
                grid[row][col - 1].clr = RED
                return
            else:
                return

    def right_move(self, row, col):
        if col > 6:
            return
        else:
            if grid[row][col + 1].piece is None:
                self.right_list.append(grid[row][col + 1])
                self.right_move(row, col + 1)
            elif grid[row][col + 1].piece is not None and self.check_opponent(grid[row][col+1].piece.clor):
                grid[row][col + 1].clr = RED
                return
            else:
                return

    def move(self, row, col, collision):
        self.px = col * gap + 10
        self.py = row * gap + 10
        if collision:
            eliminate(row, col)
        grid[row][col].piece = self
        grid[self.row][self.col].piece = None
        self.row = self.py // gap
        self.col = self.px // gap
        make_box(grid)

    def check_opponent(self, op_clr):
        if (self.clor == BLACK and op_clr == WHITE) or (self.clor == WHITE and op_clr == BLACK):
            return True
        else:
            return False


class White_rook(Rook):
    pass


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

    elif grid[row][col].piece is None and grid[row][col].clr == YELLOW:
        # function to move the piece
        piece_list[0].move(row, col, collision=False)

    elif grid[row][col].piece is not None and grid[row][col].clr == RED:
        # function to move the piece and eliminate enemy piece
        piece_list[0].move(row, col, collision=True)

    elif grid[row][col].piece is None and (grid[row][col].clr == BLACK or grid[row][col].clr == WHITE):
        make_box(grid)
        piece_list.clear()


# for i in range(8):
#    bp = Pawn(10 + i * gap, 85, BLACK, black_pawn)
wp = White_pawn(10 +  gap, 460, WHITE, white_pawn, grid)
#    black_pawn_list.append(bp)
#    white_pawn_list.append(wp)
rp = Rook(10 + 75 * 5, 10 + 75 * 2, BLACK, black_rook)
wp = White_rook(10, 85 + 75, WHITE, white_rook)
wp2 = White_rook(10+75*7, 85 + 75, WHITE, white_rook)


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

    #    for i in range(len(black_pawn_list)):
    #        black_pawn_list[i].show_pawn()
    #        white_pawn_list[i].show_pawn()

    create_board()
    rp.show_rook()
    wp.show_rook()
    wp2.show_rook()

    # update the display screen
    pygame.display.update()
