import pygame
import os
from chess_game_project import Objects
from chess_game_project import Threat_checking
from chess_game_project import Block_threat

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
black_check = False
white_check = False
running = True

# set the display screen
screen = pygame.display.set_mode((WIDTH, WIDTH + E_WIDTH))
# set the screen caption
pygame.display.set_caption("Chess Game")
# load the icon image
ico = pygame.image.load("images/horse.png")
# set the icon image for screen
pygame.display.set_icon(ico)
font = pygame.font.Font("freesansbold.ttf", 35)
Num_font = pygame.font.Font("freesansbold.ttf", 30)
chk_font = pygame.font.Font("freesansbold.ttf", 30)
move = "white move"
pis = " "
black_crown = pygame.image.load("images/black_crown.png")
white_crown = pygame.image.load("images/white_crown.png")


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


def king_escape(grid, piece):
    c = 0
    if piece == "white":
        BPAS = Objects.black_spot(grid)
        wkp = Objects.get_whk_king_pos(grid)
        for i in wkp:
            if i in BPAS:
                c += 1
                if c == len(wkp):
                    return False
            else:
                return True
    if piece == "black":
        WPAS = Objects.white_spot(grid)
        bkp = Objects.get_blk_king_pos(grid)
        for i in bkp:
            if i in WPAS:
                c += 1
                if c == len(bkp):
                    return False
            else:
                return True


def check_for_capturing(grid, pis):
    piece = piece_list[0]
    r, c = piece.row, piece.col
    if pis == "white":
        if grid[r][c] not in Objects.white_atk_spot(grid):
            return True
        else:
            return False
    if pis == "black":
        if grid[r][c] not in Objects.black_atk_spot(grid):
            return True
        else:
            return False


def block_threaten(grid, pis):
    piece = piece_list[0]
    c = 0
    if piece.piece_name == "rook" or piece.piece_name == "bishop" or piece.piece_name == "queen":
        if pis == "white":
            lis = Block_threat.block_threat(grid, piece, Objects.wkp)
            WPAS = Objects.whiteP_atk_spot(grid)
            for i in lis:
                if i not in WPAS:
                    c += 1
                    if c == len(lis):
                        return True
                else:
                    return False
        if pis == "black":
            lis = Block_threat.block_threat(grid, piece, Objects.bkp)
            BPAS = Objects.blackP_atk_spot(grid)
            for i in lis:
                if i not in BPAS:
                    c += 1
                    if c == len(lis):
                        return True
                else:
                    return False
    else:
        return True


# check for piece to move
def check_piece_move(grid, row, col):
    global running, move, pis
    global white_move, black_move, black_check, white_check
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
                white_check = False
                pis = " "
            if not Threat_checking.back and Threat_checking.check_for_threat(Objects.bkp.row, Objects.bkp.col, BLACK,
                                                                             grid):
                black_check = True
                pis = "black"
                if not king_escape(grid, "black"):
                    if check_for_capturing(grid, "black"):
                        if block_threaten(grid, "black"):
                            running = False
        else:
            if Threat_checking.check_for_threat(Objects.bkp.row, Objects.bkp.col, BLACK, grid):
                Threat_checking.take_back(grid)
            else:
                black_check = False
                pis = " "
            if not Threat_checking.back and Threat_checking.check_for_threat(Objects.wkp.row, Objects.wkp.col, WHITE,
                                                                             grid):
                white_check = True
                pis = "white"
                if not king_escape(grid, "white"):
                    if check_for_capturing(grid, "white"):
                        if block_threaten(grid, "white"):
                            running = False

        if piece_list[0].clor == WHITE and not Threat_checking.back:
            white_move = False
            black_move = True
            move = "black move"
        elif piece_list[0].clor == BLACK and not Threat_checking.back:
            white_move = True
            black_move = False
            move = "white move"
        else:
            Threat_checking.back = False

    elif (grid[row][col].piece.clor == WHITE and white_move) or (grid[row][col].piece.clor == BLACK and black_move):
        if grid[row][col].piece is not None and (grid[row][col].clr == BLACK or grid[row][col].clr == WHITE):
            if len(piece_list) == 0:
                grid[row][col].piece.check_move(row, col, grid)
                grid[row][col].piece.attacked_spot(grid)
                piece_list.append(grid[row][col].piece)
            else:
                piece_list.pop()
                make_box(grid)
                grid[row][col].piece.check_move(row, col, grid)
                grid[row][col].piece.attacked_spot(grid)
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
                white_check = False
                pis = " "
            if not Threat_checking.back and Threat_checking.check_for_threat(Objects.bkp.row, Objects.bkp.col, BLACK,
                                                                             grid):
                black_check = True
                pis = "black"
                if not king_escape(grid, "black"):
                    if check_for_capturing(grid, "black"):
                        if block_threaten(grid, "black"):
                            running = False
        else:
            if Threat_checking.check_for_threat(Objects.bkp.row, Objects.bkp.col, BLACK, grid):
                Threat_checking.take_back(grid)
            else:
                black_check = False
                pis = " "
            if not Threat_checking.back and Threat_checking.check_for_threat(Objects.wkp.row, Objects.wkp.col, WHITE,
                                                                             grid):
                white_check = True
                pis = "white"
                if not king_escape(grid, "white"):
                    if check_for_capturing(grid, "white"):
                        if block_threaten(grid, "white"):
                            running = False

        if piece_list[0].clor == WHITE and not Threat_checking.back:
            white_move = False
            black_move = True
            move = "black move"
        elif piece_list[0].clor == BLACK and not Threat_checking.back:
            white_move = True
            black_move = False
            move = "white move"
        else:
            last_piece.eliminated = False
            grid[row][col].piece = last_piece
            Threat_checking.back = False


# initialize objects of all piece class
Objects.obj_init(grid, screen)


def show_eliminated_piece():
    c = 0
    e = 0
    for obj in Objects.white_piece:
        if obj.eliminated:
            c += 1
    screen.blit(white_crown, (460, 610))
    ele_wp = Num_font.render(str(c), True, (0, 0, 0))
    screen.blit(ele_wp, (490, 610))
    for obj in Objects.black_piece:
        if obj.eliminated:
            e += 1
    screen.blit(black_crown, (530, 610))
    ele_bp = Num_font.render(str(e), True, (0, 0, 0))
    screen.blit(ele_bp, (560, 610))


# main game loop
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
    mv_font = font.render(move, True, (125, 55, 200))
    screen.blit(mv_font, (200, 605))
    pygame.draw.line(screen, BLACK, (0, 650), (WIDTH, 650), 4)
    ck_font = chk_font.render("check for "+pis+" king", True, (255, 0, 0))
    if pis != " ":
        screen.blit(ck_font, (150, 660))
    show_eliminated_piece()

    # update the display screen
    pygame.display.update()
