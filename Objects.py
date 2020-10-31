import pygame
from chess_game_project import Pawn_piece, Rook_piece, Knight_piece, King_piece, Bishop_piece, Queen_piece

# constant values
gap = 75
BLACK = (139, 69, 45)
WHITE = (250, 235, 215)

pawn_list = []
bishop_list = []
rook_list = []
knight_list = []
king_list = []
queen_list = []
wkp, bkp = 0, 0

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


def obj_init(grid, screen):
    global wkp, bkp

    for i in range(8):
        bpp = Pawn_piece.Pawn(10 + i * gap, 85, BLACK, black_pawn, grid, screen)
        wpp = Pawn_piece.White_pawn(10 + i * gap, 460, WHITE, white_pawn, grid, screen)
        pawn_list.append(bpp)
        pawn_list.append(wpp)

    brp1 = Rook_piece.Rook(10, 10, BLACK, black_rook, grid, screen)
    brp2 = Rook_piece.Rook(10 + 75 * 7, 10, BLACK, black_rook, grid, screen)
    wrp1 = Rook_piece.Rook(10, 10 + 75 * 7, WHITE, white_rook, grid, screen)
    wrp2 = Rook_piece.Rook(10 + 75 * 7, 10 + 75 * 7, WHITE, white_rook, grid, screen)
    rook_list.append(brp1)
    rook_list.append(brp2)
    rook_list.append(wrp1)
    rook_list.append(wrp2)

    bkp1 = Knight_piece.Knight(10 + 75, 10, BLACK, black_horse, grid, screen)
    bkp2 = Knight_piece.Knight(10 + 75 * 6, 10, BLACK, black_horse, grid, screen)
    wkp1 = Knight_piece.Knight(10 + 75, 10 + 75 * 7, WHITE, white_horse, grid, screen)
    wkp2 = Knight_piece.Knight(10 + 75 * 6, 10 + 75 * 7, WHITE, white_horse, grid, screen)
    knight_list.append(bkp1)
    knight_list.append(bkp2)
    knight_list.append(wkp1)
    knight_list.append(wkp2)

    bbp1 = Bishop_piece.Bishop(10 + 75 * 2, 10, BLACK, black_bishop, grid, screen)
    bbp2 = Bishop_piece.Bishop(10 + 75 * 5, 10, BLACK, black_bishop, grid, screen)
    wbp1 = Bishop_piece.Bishop(10 + 75 * 2, 10 + 75 * 7, WHITE, white_bishop, grid, screen)
    wbp2 = Bishop_piece.Bishop(10 + 75 * 5, 10 + 75 * 7, WHITE, white_bishop, grid, screen)
    bishop_list.append(bbp1)
    bishop_list.append(bbp2)
    bishop_list.append(wbp1)
    bishop_list.append(wbp2)

    bqp = Queen_piece.Queen(10 + 75 * 3, 10, BLACK, black_queen, grid, screen)
    wqp = Queen_piece.Queen(10 + 75 * 3, 10 + 75 * 7, WHITE, white_queen, grid, screen)
    queen_list.append(bqp)
    queen_list.append(wqp)

    bkp = King_piece.King(10 + 75 * 4, 10, BLACK, black_king, grid, screen)
    wkp = King_piece.King(10 + 75 * 4, 10 + 75 * 7, WHITE, white_king, grid, screen)
    king_list.append(bkp)
    king_list.append(wkp)


def get_blk_king_pos(grid):
    bks = king_list[0].attacked_spot(grid)
    return bks


def get_whk_king_pos(grid):
    wks = king_list[1].attacked_spot(grid)
    return wks


def black_atk_spot(grid):
    bps = queen_list[0].attacked_spot(grid) + bishop_list[0].attacked_spot(grid) + bishop_list[1].attacked_spot(grid) + \
          king_list[0].attacked_spot(grid) + knight_list[0].attacked_spot(grid) + knight_list[1].attacked_spot(grid) + \
          rook_list[0].attacked_spot(grid) + rook_list[1].attacked_spot(grid)
    for i in range(len(pawn_list)):
        if i % 2 == 0:
            bps = bps + pawn_list[i].attacked_spot(grid)
    return bps


def blackP_atk_spot(grid):
    bps = queen_list[0].attacked_spot(grid) + bishop_list[0].attacked_spot(grid) + bishop_list[1].attacked_spot(grid) + \
          knight_list[0].attacked_spot(grid) + knight_list[1].attacked_spot(grid) + rook_list[0].attacked_spot(grid) + \
          rook_list[1].attacked_spot(grid)

    return bps


def white_atk_spot(grid):
    bps = queen_list[1].attacked_spot(grid)[:-1] if type(queen_list[1].attacked_spot(grid)[-1]) == type([]) \
        else queen_list[1].attacked_spot(grid) + bishop_list[2].attacked_spot(grid) + bishop_list[3].attacked_spot(
        grid) + king_list[1].attacked_spot(grid) + knight_list[2].attacked_spot(grid) + knight_list[3].attacked_spot(
        grid) + rook_list[2].attacked_spot(grid) + rook_list[3].attacked_spot(grid)
    for i in range(len(pawn_list)):
        if i % 2 != 0:
            bps = bps + pawn_list[i].attacked_spot(grid)
    return bps


def whiteP_atk_spot(grid):
    bps = queen_list[1].attacked_spot(grid) + bishop_list[2].attacked_spot(grid) + bishop_list[3].attacked_spot(grid) + \
          knight_list[2].attacked_spot(grid) + knight_list[3].attacked_spot(grid) + rook_list[2].attacked_spot(grid) + \
          rook_list[3].attacked_spot(grid)

    return bps


def white_spot(grid):
    q_atk_spot = queen_list[1].attacked_spot(grid)[:-1] if type(queen_list[1].attacked_spot(grid)[-1]) == type([]) \
        else queen_list[1].attacked_spot(grid)
    for i in queen_list[1].attacked_spot(grid)[-1]:
        q_atk_spot.append(i)
    bps = q_atk_spot + bishop_list[2].attacked_spot(grid) + bishop_list[3].attacked_spot(
        grid) + king_list[1].attacked_spot(grid) + knight_list[2].attacked_spot(grid) + knight_list[3].attacked_spot(
        grid) + rook_list[2].attacked_spot(grid) + rook_list[3].attacked_spot(grid)
    for i in range(len(pawn_list)):
        if i % 2 != 0:
            bps = bps + pawn_list[i].attacked_spot(grid)
    return bps
