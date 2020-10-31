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


# class for Rook piece
class Rook:
    def __init__(self, p_x, p_y, clr, img, grid, win):
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
        self.screen = win
        self.piece_name = "rook"
        self.atk_spot = []
        self.black_rook_attacked_spot = []
        self.white_rook_attacked_spot = []

    # To show a rook on board
    def show_rook(self):
        if not self.eliminated:
            self.screen.blit(self.rook_img, (self.px, self.py))

    # to check for all possible moves
    def check_move(self, row, col, grid):
        self.front_move(row, col, grid)
        self.back_move(row, col, grid)
        self.left_move(row, col, grid)
        self.right_move(row, col, grid)

    # To check for rooks front moves
    def front_move(self, row, col, grid):
        if row > 6:
            return
        else:
            if grid[row + 1][col].piece is None:
                grid[row + 1][col].clr = YELLOW
                self.front_move(row + 1, col, grid)
            elif grid[row + 1][col].piece is not None and self.check_opponent(grid[row + 1][col].piece.clor):
                grid[row + 1][col].clr = RED
                return
            else:
                return

    # To check for rooks back moves
    def back_move(self, row, col, grid):
        if row < 1:
            return
        else:
            if grid[row - 1][col].piece is None:
                grid[row - 1][col].clr = YELLOW
                self.back_move(row - 1, col, grid)
            elif grid[row - 1][col].piece is not None and self.check_opponent(grid[row - 1][col].piece.clor):
                grid[row - 1][col].clr = RED
                return
            else:
                return

    # To check for rooks left moves
    def left_move(self, row, col, grid):
        if col < 1:
            return
        else:
            if grid[row][col - 1].piece is None:
                grid[row][col - 1].clr = YELLOW
                self.left_move(row, col - 1, grid)
            elif grid[row][col - 1].piece is not None and self.check_opponent(grid[row][col - 1].piece.clor):
                grid[row][col - 1].clr = RED
                return
            else:
                return

    # To check for rooks right moves
    def right_move(self, row, col, grid):
        if col > 6:
            return
        else:
            if grid[row][col + 1].piece is None:
                grid[row][col + 1].clr = YELLOW
                self.right_move(row, col + 1, grid)
            elif grid[row][col + 1].piece is not None and self.check_opponent(grid[row][col + 1].piece.clor):
                grid[row][col + 1].clr = RED
                return
            else:
                return

    # To move the Rook piece to given position
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
            self.atk_spot_rook(self.row + 1, self.col, grid, "front")
            self.atk_spot_rook(self.row - 1, self.col, grid, "back")
            self.atk_spot_rook(self.row, self.col - 1, grid, "left")
            self.atk_spot_rook(self.row, self.col + 1, grid, "right")
            if self.clor == WHITE:
                self.white_rook_attacked_spot.clear()
                self.white_rook_attacked_spot = self.atk_spot.copy()
                return self.white_rook_attacked_spot
            elif self.clor == BLACK:
                self.black_rook_attacked_spot.clear()
                self.black_rook_attacked_spot = self.atk_spot.copy()
                return self.black_rook_attacked_spot
        else:
            return []

    def atk_spot_rook(self, row, col, grid, move):
        if row > 7 or row < 0 or col < 0 or col > 7:
            return
        else:
            if grid[row][col].piece is None:
                self.atk_spot.append(grid[row][col])
                if move == "front":
                    self.atk_spot_rook(row + 1, col, grid, "front")
                elif move == "back":
                    self.atk_spot_rook(row - 1, col, grid, "back")
                elif move == "left":
                    self.atk_spot_rook(row, col - 1, grid, "left")
                elif move == "right":
                    self.atk_spot_rook(row, col + 1, grid, "right")
            elif grid[row][col].piece is not None and self.check_opponent(grid[row][col].piece.clor):
                self.atk_spot.append(grid[row][col])
                return
            else:
                return
