threatened = False
start_pos = []
final_pos = []
back = False
kr = 0
BLACK = (139, 69, 45)
WHITE = (250, 235, 215)


def take_back(grid):
    global back
    final_pos[0][2].move(start_pos[0][0], start_pos[0][1], grid, collision=False)
    if final_pos[0][2].piece_name == "pawn" and start_pos[0][2]:
        final_pos[0][2].first_move = True
    back = True


# check for threat in this way
def check_pawn_threat(row, col, grid, p_clr):
    if 0 <= row <= 7 and 0 <= col <= 7:
        if grid[row][col].piece is None:
            return True
        elif grid[row][col].piece is not None:
            if grid[row][col].piece.clor == p_clr:
                return True
            elif grid[row][col].piece.piece_name == "pawn" or grid[row][col].piece.piece_name == "king":
                if grid[row][col].piece.piece_name == "pawn":
                    if kr < row and grid[row][col].piece.clor == BLACK:
                        return True
                    elif kr > row and grid[row][col].piece.clor == WHITE:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return True
    else:
        return True


# check for threat in this way
def right_down(row, col, grid, p_clr):
    if 0 <= row <= 7 and 0 <= col <= 7:
        if grid[row][col].piece is None:
            return right_down(row + 1, col + 1, grid, p_clr)
        elif grid[row][col].piece is not None:
            if grid[row][col].piece.clor == p_clr:
                return True
            elif grid[row][col].piece.piece_name == "bishop" or grid[row][col].piece.piece_name == "queen":
                return False
            else:
                return True
    else:
        return True


# check for threat in this way
def left_down(row, col, grid, p_clr):
    if 0 <= row <= 7 and 0 <= col <= 7:
        if grid[row][col].piece is None:
            return left_down(row + 1, col - 1, grid, p_clr)
        elif grid[row][col].piece is not None:
            if grid[row][col].piece.clor == p_clr:
                return True
            elif grid[row][col].piece.piece_name == "bishop" or grid[row][col].piece.piece_name == "queen":
                return False
            else:
                return True
    else:
        return True


# check for threat in this way
def right_up(row, col, grid, p_clr):
    if 0 <= row <= 7 and 0 <= col <= 7:
        if grid[row][col].piece is None:
            return right_up(row - 1, col + 1, grid, p_clr)
        elif grid[row][col].piece is not None:
            if grid[row][col].piece.clor == p_clr:
                return True
            elif grid[row][col].piece.piece_name == "bishop" or grid[row][col].piece.piece_name == "queen":
                return False
            else:
                return True
    else:
        return True


# check for threat in this way
def left_up(row, col, grid, p_clr):
    if 0 <= row <= 7 and 0 <= col <= 7:
        if grid[row][col].piece is None:
            return left_up(row - 1, col - 1, grid, p_clr)
        elif grid[row][col].piece is not None:
            if grid[row][col].piece.clor == p_clr:
                return True
            elif grid[row][col].piece.piece_name == "bishop" or grid[row][col].piece.piece_name == "queen":
                return False
            else:
                return True
    else:
        return True


# To check for a place to move
def front_move(row, col, grid, p_clr):
    if 0 <= row <= 7 and 0 <= col <= 7:
        if grid[row][col].piece is None:
            return front_move(row + 1, col, grid, p_clr)
        elif grid[row][col].piece is not None:
            if grid[row][col].piece.clor == p_clr:
                return True
            elif grid[row][col].piece.piece_name == "rook" or grid[row][col].piece.piece_name == "queen":
                return False
            else:
                return True
    else:
        return True


# To check for a place to move
def back_move(row, col, grid, p_clr):
    if 0 <= row <= 7 and 0 <= col <= 7:
        if grid[row][col].piece is None:
            return back_move(row - 1, col, grid, p_clr)
        elif grid[row][col].piece is not None:
            if grid[row][col].piece.clor == p_clr:
                return True
            elif grid[row][col].piece.piece_name == "rook" or grid[row][col].piece.piece_name == "queen":
                return False
            else:
                return True
    else:
        return True


# To check for a place to move
def left_move(row, col, grid, p_clr):
    if 0 <= row <= 7 and 0 <= col <= 7:
        if grid[row][col].piece is None:
            return left_move(row, col - 1, grid, p_clr)
        elif grid[row][col].piece is not None:
            if grid[row][col].piece.clor == p_clr:
                return True
            elif grid[row][col].piece.piece_name == "rook" or grid[row][col].piece.piece_name == "queen":
                return False
            else:
                return True
    else:
        return True


# To check for a place to move
def right_move(row, col, grid, p_clr):
    if 0 <= row <= 7 and 0 <= col <= 7:
        if grid[row][col].piece is None:
            return right_move(row, col + 1, grid, p_clr)
        elif grid[row][col].piece is not None:
            if grid[row][col].piece.clor == p_clr:
                return True
            elif grid[row][col].piece.piece_name == "rook" or grid[row][col].piece.piece_name == "queen":
                return False
            else:
                return True
    else:
        return True


# check for threat in this way
def king_side_move(row, col, grid, p_clr):
    if 0 <= row <= 7 and 0 <= col <= 7:
        if grid[row][col].piece is None:
            return True
        elif grid[row][col].piece is not None:
            if grid[row][col].piece.clor == p_clr:
                return True
            elif grid[row][col].piece.piece_name == "king":
                return False
    else:
        return True


# To check for a place to move
def knight_place(row, col, grid, p_clr):
    if 0 <= row <= 7 and 0 <= col <= 7:
        if grid[row][col].piece is None:
            return True
        elif grid[row][col].piece is not None:
            if grid[row][col].piece.clor == p_clr:
                return True
            elif grid[row][col].piece.piece_name == "king":
                return False
    else:
        return True


def now_threatened(row, col, p_clr, grid):
    global kr
    kr = row
    if check_pawn_threat(row - 1, col - 1, grid, p_clr) and check_pawn_threat(row - 1, col + 1, grid, p_clr) \
            and check_pawn_threat(row + 1, col - 1, grid, p_clr) and check_pawn_threat(row + 1, col + 1, grid, p_clr):
        if king_side_move(row + 1, col, grid, p_clr) and king_side_move(row - 1, col, grid, p_clr) \
                and king_side_move(row, col - 1, grid, p_clr) and king_side_move(row, col + 1, grid, p_clr):
            if left_up(row - 1, col - 1, grid, p_clr) and right_up(row - 1, col + 1, grid, p_clr) \
                    and left_down(row + 1, col - 1, grid, p_clr) and right_down(row + 1, col + 1, grid, p_clr):
                if front_move(row + 1, col, grid, p_clr) and back_move(row - 1, col, grid, p_clr) \
                        and left_move(row, col - 1, grid, p_clr) and right_move(row, col + 1, grid, p_clr):
                    if knight_place(row - 2, col - 1, grid, p_clr) and knight_place(row - 2, col + 1, grid, p_clr) \
                            and knight_place(row + 2, col - 1, grid, p_clr) and knight_place(row + 2, col + 1, grid,
                                                                                             p_clr) \
                            and knight_place(row - 1, col - 2, grid, p_clr) and knight_place(row + 1, col - 2, grid,
                                                                                             p_clr) \
                            and knight_place(row - 1, col + 2, grid, p_clr) and knight_place(row + 1, col + 2, grid,
                                                                                             p_clr):
                        return False
                    else:
                        return True
                else:
                    return True
            else:
                return True
        else:
            return True
    else:
        return True


def check_for_threat(row, col, p_clr, grid):
    global threatened
    if (threatened and now_threatened(row, col, p_clr, grid)) or (
            not threatened and now_threatened(row, col, p_clr, grid)):
        # don't allow the piece and take back step
        threatened = True
        return True
    if (threatened and not now_threatened(row, col, p_clr, grid)) or (
            not threatened and not now_threatened(row, col, p_clr, grid)):
        # allow the piece to move
        threatened = False
        return False
