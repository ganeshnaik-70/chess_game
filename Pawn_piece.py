# constant values
gap = 75
BLACK = (139, 69, 45)
WHITE = (250, 235, 215)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


# To make a black and white pattern in the board
def make_box(grid):
    for i in range(8):
        for j in range(8):
            if (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0):
                grid[i][j].clr = BLACK
            else:
                grid[i][j].clr = WHITE


# To check for a valid place to move
def check_place(obj):
    if obj.piece is None:
        return True
    else:
        return False


# To check for pawn first move is valid or mot
def check_pawn_first_move(obj):
    if check_place(obj):
        obj.clr = YELLOW
        return True
    else:
        return False


# To eliminate enemy piece
def eliminate(row, col, grid):
    grid[row][col].piece.eliminated = True
    grid[row][col].piece = None


# class for a pawn piece
class Pawn:
    def __init__(self, p_x, p_y, clr, img, grid, win):
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
        self.pawn_img = img
        self.screen = win
        self.piece_name = "pawn"
        self.black_pawn_attacked_spot = []
        self.white_pawn_attacked_spot = []

    # To show a pawn on board
    def show_pawn(self):
        if not self.eliminated:
            self.screen.blit(self.pawn_img, (self.px, self.py))

    # To check for all possible moves
    def check_move(self, row, col, grid):
        if row < 7:
            self.check_diagonal(row, col, grid)
            if self.first_move:
                if check_pawn_first_move(grid[row + 1][col]):
                    if check_place(grid[row + 2][col]):
                        grid[row + 2][col].clr = YELLOW
            else:
                check_pawn_first_move(grid[row + 1][col])

    # To check for diagonal movement
    def check_diagonal(self, row, col, grid):
        if col > 0 and grid[row + 1][col - 1].piece is not None and grid[row + 1][col - 1].piece.clor == WHITE:  # left
            grid[row + 1][col - 1].clr = RED
            self.diagonal_move.append(grid[row + 1][col - 1])
        if col < 7 and grid[row + 1][col + 1].piece is not None and grid[row + 1][col + 1].piece.clor == WHITE:  # right
            grid[row + 1][col + 1].clr = RED
            self.diagonal_move.append(grid[row + 1][col + 1])

    # To move the pawn piece
    def move(self, row, col, grid, collision):
        self.px = col * gap + 10
        self.py = row * gap + 10
        if collision:
            eliminate(row, col, grid)
        grid[row][col].piece = self
        self.first_move = False
        grid[self.row][self.col].piece = None
        self.row = self.py // gap
        self.col = self.px // gap
        make_box(grid)

    def attacked_spot(self, grid):
        if not self.eliminated:
            if 0 <= self.col <= 7:
                self.black_pawn_attacked_spot.clear()
                self.white_pawn_attacked_spot.clear()
                if self.clor == WHITE:
                    if self.row > 0:
                        if self.col != 0:
                            if grid[self.row - 1][self.col - 1].piece is None:
                                self.white_pawn_attacked_spot.append(grid[self.row - 1][self.col - 1])
                            elif grid[self.row - 1][self.col - 1].piece.clor != WHITE:
                                self.white_pawn_attacked_spot.append(grid[self.row - 1][self.col - 1])
                            else:
                                self.white_pawn_attacked_spot.append(grid[self.row - 1][self.col - 1])
                        if self.col != 7:
                            if grid[self.row - 1][self.col + 1].piece is None:
                                self.white_pawn_attacked_spot.append(grid[self.row - 1][self.col + 1])
                            elif grid[self.row - 1][self.col + 1].piece.clor != WHITE:
                                self.white_pawn_attacked_spot.append(grid[self.row - 1][self.col + 1])
                            else:
                                self.white_pawn_attacked_spot.append(grid[self.row - 1][self.col + 1])
                    return self.white_pawn_attacked_spot

                if self.clor == BLACK:
                    if self.row < 7:
                        if self.col != 0:
                            if grid[self.row + 1][self.col - 1].piece is None:
                                self.black_pawn_attacked_spot.append(grid[self.row + 1][self.col - 1])
                            elif grid[self.row + 1][self.col - 1].piece.clor != BLACK:
                                self.black_pawn_attacked_spot.append(grid[self.row + 1][self.col - 1])
                            else:
                                self.black_pawn_attacked_spot.append(grid[self.row + 1][self.col - 1])
                        if self.col != 7:
                            if grid[self.row + 1][self.col + 1].piece is None:
                                self.black_pawn_attacked_spot.append(grid[self.row + 1][self.col + 1])
                            elif grid[self.row + 1][self.col + 1].piece.clor != BLACK:
                                self.black_pawn_attacked_spot.append(grid[self.row + 1][self.col + 1])
                            else:
                                self.black_pawn_attacked_spot.append(grid[self.row + 1][self.col + 1])
                    return self.black_pawn_attacked_spot
        else:
            return []


# class for White pawn
class White_pawn(Pawn):
    # To check for white pawns all possible moves
    def check_move(self, row, col, grid):
        if row > 0:
            self.check_diagonal(row, col, grid)
            if self.first_move:
                if check_pawn_first_move(grid[row - 1][col]):
                    if check_place(grid[row - 2][col]):
                        grid[row - 2][col].clr = YELLOW
            else:
                check_pawn_first_move(grid[row - 1][col])

    # To check for white pawns diagonal movements
    def check_diagonal(self, row, col, grid):
        if col > 0 and grid[row - 1][col - 1].piece is not None and grid[row - 1][col - 1].piece.clor == BLACK:  # left
            grid[row - 1][col - 1].clr = RED
            self.diagonal_move.append(grid[row - 1][col - 1])
        if col < 7 and grid[row - 1][col + 1].piece is not None and grid[row - 1][col + 1].piece.clor == BLACK:  # right
            grid[row - 1][col + 1].clr = RED
            self.diagonal_move.append(grid[row - 1][col + 1])
