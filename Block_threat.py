lis = []
spot = []
BLACK = (139, 69, 45)
WHITE = (250, 235, 215)


def atk_spot_queen(row, col, grid, dirt):
    global lis
    if 0 <= row <= 7 and 0 <= col <= 7:
        if grid[row][col].piece is None:
            lis.append(grid[row][col])
            if dirt == "right_d":
                atk_spot_queen(row + 1, col + 1, grid, "right_d")
            elif dirt == "left_d":
                atk_spot_queen(row + 1, col - 1, grid, "left_d")
            elif dirt == "right_u":
                atk_spot_queen(row - 1, col + 1, grid, "right_u")
            elif dirt == "left_u":
                atk_spot_queen(row - 1, col - 1, grid, "left_u")
            elif dirt == "front":
                atk_spot_queen(row + 1, col, grid, "front")
            elif dirt == "back":
                atk_spot_queen(row - 1, col, grid, "back")
            elif dirt == "left":
                atk_spot_queen(row, col - 1, grid, "left")
            elif dirt == "right":
                atk_spot_queen(row, col + 1, grid, "right")
            return lis
        elif grid[row][col].piece is not None and grid[row][col].piece.piece_name == "king":
            lis.append(grid[row][col])
            return lis
    else:
        return lis


def atk_spot_rook(row, col, grid, move):
    global lis
    if row > 7 or row < 0 or col < 0 or col > 7:
        return lis
    else:
        if grid[row][col].piece is None:
            lis.append(grid[row][col])
            if move == "front":
                atk_spot_rook(row + 1, col, grid, "front")
            elif move == "back":
                atk_spot_rook(row - 1, col, grid, "back")
            elif move == "left":
                atk_spot_rook(row, col - 1, grid, "left")
            elif move == "right":
                atk_spot_rook(row, col + 1, grid, "right")
            return lis
        else:
            return lis


def atk_spot_bishop(row, col, grid, dirt):
    global lis
    if 0 <= row <= 7 and 0 <= col <= 7:
        if grid[row][col].piece is None:
            lis.append(grid[row][col])
            if dirt == "right_d":
                atk_spot_bishop(row + 1, col + 1, grid, "right_d")
            elif dirt == "left_d":
                atk_spot_bishop(row + 1, col - 1, grid, "left_d")
            elif dirt == "right_u":
                atk_spot_bishop(row - 1, col + 1, grid, "right_u")
            elif dirt == "left_u":
                atk_spot_bishop(row - 1, col - 1, grid, "left_u")
            return lis
        elif grid[row][col].piece is not None and grid[row][col].piece.piece_name == "king":
            lis.append(grid[row][col])
            return lis
    else:
        return lis


def block_threat(grid, piece, king_p):
    global spot
    if piece.piece_name == "bishop":
        if king_p.row > piece.row:
            if king_p.col > piece.col:
                spot = atk_spot_bishop(piece.row + 1, piece.col + 1, grid, "right_d")
            else:
                spot = atk_spot_bishop(piece.row + 1, piece.col - 1, grid, "left_d")
        else:
            if king_p.col > piece.col:
                spot = atk_spot_bishop(piece.row - 1, piece.col + 1, grid, "right_u")
            else:
                spot = atk_spot_bishop(piece.row - 1, piece.col - 1, grid, "left_u")
        return spot

    if piece.piece_name == "rook":
        if king_p.col == piece.col:
            if king_p.row > piece.row:
                spot = atk_spot_rook(piece.row + 1, piece.col, grid, "front")
            else:
                spot = atk_spot_rook(piece.row - 1, piece.col, grid, "back")
        elif king_p.row == piece.row:
            if king_p.col > piece.col:
                spot = atk_spot_rook(piece.row, piece.col + 1, grid, "right")
            else:
                spot = atk_spot_rook(piece.row, piece.col - 1, grid, "left")
        return spot

    if piece.piece_name == "queen":
        if king_p.col == piece.col:
            if king_p.row > piece.row:
                spot = atk_spot_queen(piece.row + 1, piece.col, grid, "front")
            else:
                spot = atk_spot_queen(piece.row - 1, piece.col, grid, "back")
        elif king_p.row == piece.row:
            if king_p.col > piece.col:
                spot = atk_spot_queen(piece.row, piece.col + 1, grid, "right")
            else:
                spot = atk_spot_queen(piece.row, piece.col - 1, grid, "left")
        elif king_p.row > piece.row:
            if king_p.col > piece.col:
                spot = atk_spot_queen(piece.row + 1, piece.col + 1, grid, "right_d")
            else:
                spot = atk_spot_queen(piece.row + 1, piece.col - 1, grid, "left_d")
        else:
            if king_p.col > piece.col:
                spot = atk_spot_queen(piece.row - 1, piece.col + 1, grid, "right_u")
            else:
                spot = atk_spot_queen(piece.row - 1, piece.col - 1, grid, "left_u")
        return spot
