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


# class for a King piece
class King:
    def __init__(self, p_x, p_y, clr, img, grid, win):
        self.px = p_x
        self.py = p_y
        self.row = p_y // gap
        self.col = p_x // gap
        grid[self.row][self.col].piece = self
        self.eliminated = False
        self.clor = clr
        self.king_img = img
        self.screen = win
        self.piece_name = "king"

    # To show a king on board
    def show_king(self):
        if not self.eliminated:
            self.screen.blit(self.king_img, (self.px, self.py))

    # To check for possible move
    def check_move(self, row, col, grid):
        self.place(row + 1, col, grid)
        self.place(row - 1, col, grid)
        self.place(row, col + 1, grid)
        self.place(row, col - 1, grid)
        self.place(row + 1, col+1, grid)
        self.place(row +1, col-1, grid)
        self.place(row-1, col + 1, grid)
        self.place(row-1, col - 1, grid)

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
