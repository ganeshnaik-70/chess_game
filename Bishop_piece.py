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


# class for a Bishop piece
class Bishop:
    def __init__(self, p_x, p_y, clr, img, grid, win):
        self.px = p_x
        self.py = p_y
        self.row = p_y // gap
        self.col = p_x // gap
        grid[self.row][self.col].piece = self
        self.eliminated = False
        self.clor = clr
        self.bishop_img = img
        self.screen = win
        self.piece_name = "bishop"
        self.atk_spot = []
        self.black_bishop_attacked_spot = []
        self.white_bishop_attacked_spot = []

    # To show a bishop on board
    def show_bishop(self):
        if not self.eliminated:
            self.screen.blit(self.bishop_img, (self.px, self.py))

    # To check for possible move
    def check_move(self, row, col, grid):
        self.right_down(row + 1, col + 1, grid)
        self.left_down(row + 1, col - 1, grid)
        self.right_up(row - 1, col + 1, grid)
        self.left_up(row - 1, col - 1, grid)

    # To check for a place to move
    def right_down(self, row, col, grid):
        if 0 <= row <= 7 and 0 <= col <= 7:
            if grid[row][col].piece is None:
                grid[row][col].clr = YELLOW
                self.right_down(row + 1, col + 1, grid)
            elif grid[row][col].piece is not None and self.check_opponent(grid[row][col].piece.clor):
                grid[row][col].clr = RED
        else:
            return

    # To check for a place to move
    def left_down(self, row, col, grid):
        if 0 <= row <= 7 and 0 <= col <= 7:
            if grid[row][col].piece is None:
                grid[row][col].clr = YELLOW
                self.left_down(row + 1, col - 1, grid)
            elif grid[row][col].piece is not None and self.check_opponent(grid[row][col].piece.clor):
                grid[row][col].clr = RED
        else:
            return

    # To check for a place to move
    def right_up(self, row, col, grid):
        if 0 <= row <= 7 and 0 <= col <= 7:
            if grid[row][col].piece is None:
                grid[row][col].clr = YELLOW
                self.right_up(row - 1, col + 1, grid)
            elif grid[row][col].piece is not None and self.check_opponent(grid[row][col].piece.clor):
                grid[row][col].clr = RED
        else:
            return

    # To check for a place to move
    def left_up(self, row, col, grid):
        if 0 <= row <= 7 and 0 <= col <= 7:
            if grid[row][col].piece is None:
                grid[row][col].clr = YELLOW
                self.left_up(row - 1, col - 1, grid)
            elif grid[row][col].piece is not None and self.check_opponent(grid[row][col].piece.clor):
                grid[row][col].clr = RED
        else:
            return

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
            self.atk_spot_bishop(self.row + 1, self.col + 1, grid, "right_d")
            self.atk_spot_bishop(self.row + 1, self.col - 1, grid, "left_d")
            self.atk_spot_bishop(self.row - 1, self.col + 1, grid, "right_u")
            self.atk_spot_bishop(self.row - 1, self.col - 1, grid, "left_u")
            if self.clor == WHITE:
                self.white_bishop_attacked_spot.clear()
                self.white_bishop_attacked_spot = self.atk_spot.copy()
                return self.white_bishop_attacked_spot
            elif self.clor == BLACK:
                self.black_bishop_attacked_spot.clear()
                self.black_bishop_attacked_spot = self.atk_spot.copy()
                return self.black_bishop_attacked_spot
        else:
            return []

    def atk_spot_bishop(self, row, col, grid, dirt):
        if 0 <= row <= 7 and 0 <= col <= 7:
            if grid[row][col].piece is None:
                self.atk_spot.append(grid[row][col])
                if dirt == "right_d":
                    self.atk_spot_bishop(row + 1, col + 1, grid, "right_d")
                elif dirt == "left_d":
                    self.atk_spot_bishop(row + 1, col - 1, grid, "left_d")
                elif dirt == "right_u":
                    self.atk_spot_bishop(row - 1, col + 1, grid, "right_u")
                elif dirt == "left_u":
                    self.atk_spot_bishop(row - 1, col - 1, grid, "left_u")
            elif grid[row][col].piece is not None and self.check_opponent(grid[row][col].piece.clor):
                self.atk_spot.append(grid[row][col])
            else:
                self.atk_spot.append(grid[row][col])
        else:
            return
