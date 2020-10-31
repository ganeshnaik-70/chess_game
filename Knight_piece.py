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


# To eliminate enemy piece
def eliminate(row, col, grid):
    grid[row][col].piece.eliminated = True
    grid[row][col].piece = None


# class for a knight piece
class Knight:
    def __init__(self, p_x, p_y, clr, img, grid, win):
        self.px = p_x
        self.py = p_y
        self.row = p_y // gap
        self.col = p_x // gap
        grid[self.row][self.col].piece = self
        self.eliminated = False
        self.clor = clr
        self.knight_img = img
        self.screen = win
        self.piece_name = "knight"
        self.atk_spot = []
        self.black_knight_attacked_spot = []
        self.white_knight_attacked_spot = []

    # To show a pawn on board
    def show_knight(self):
        if not self.eliminated:
            self.screen.blit(self.knight_img, (self.px, self.py))

    # To check for possible move
    def check_move(self, row, col, grid):
        self.place(row - 2, col - 1, grid)
        self.place(row - 2, col + 1, grid)
        self.place(row + 2, col - 1, grid)
        self.place(row + 2, col + 1, grid)
        self.place(row - 1, col - 2, grid)
        self.place(row + 1, col - 2, grid)
        self.place(row - 1, col + 2, grid)
        self.place(row + 1, col + 2, grid)

    # To check for a place to move
    def place(self, row, col, grid):
        if 0 <= row <= 7 and 0 <= col <= 7:
            if grid[row][col].piece is None:
                grid[row][col].clr = YELLOW
            elif grid[row][col].piece is not None and self.check_opponent(grid[row][col].piece.clor):
                grid[row][col].clr = RED

    # To move the place
    def move(self, row, col, grid, collision):
        self.px = col * gap + 10
        self.py = row * gap + 10
        if collision:
            eliminate(row, col, grid)
        grid[row][col].piece = self
        grid[self.row][self.col].piece = None
        self.row = self.py // gap
        self.col = self.px // gap
        make_box(grid)

    # To check for opponent piece
    def check_opponent(self, op_clr):
        if (self.clor == BLACK and op_clr == WHITE) or (self.clor == WHITE and op_clr == BLACK):
            return True
        else:
            return False

    def attacked_spot(self, grid):
        if not self.eliminated:
            self.atk_spot.clear()
            self.atk_spot_knight(self.row - 2, self.col - 1, grid)
            self.atk_spot_knight(self.row - 2, self.col + 1, grid)
            self.atk_spot_knight(self.row + 2, self.col - 1, grid)
            self.atk_spot_knight(self.row + 2, self.col + 1, grid)
            self.atk_spot_knight(self.row - 1, self.col - 2, grid)
            self.atk_spot_knight(self.row + 1, self.col - 2, grid)
            self.atk_spot_knight(self.row - 1, self.col + 2, grid)
            self.atk_spot_knight(self.row + 1, self.col + 2, grid)
            if self.clor == WHITE:
                self.white_knight_attacked_spot.clear()
                self.white_knight_attacked_spot = self.atk_spot.copy()
                return self.white_knight_attacked_spot
            elif self.clor == BLACK:
                self.black_knight_attacked_spot.clear()
                self.black_knight_attacked_spot = self.atk_spot.copy()
                return self.black_knight_attacked_spot
        else:
            return []

    def atk_spot_knight(self, row, col, grid):
        if 0 <= row <= 7 and 0 <= col <= 7:
            if grid[row][col].piece is None:
                self.atk_spot.append(grid[row][col])
            elif grid[row][col].piece is not None and self.check_opponent(grid[row][col].piece.clor):
                self.atk_spot.append(grid[row][col])
        else:
            return
