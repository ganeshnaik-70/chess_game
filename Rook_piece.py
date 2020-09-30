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


# To eliminate emeny piece
def eliminate(row, col, grid):
    grid[row][col].piece.eliminated = True
    grid[row][col].piece = None


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

    # To show a rook on board
    def show_rook(self):
        if not self.eliminated:
            self.screen.blit(self.rook_img, (self.px, self.py))

    def check_move(self, row, col, grid):
        self.front_move(row, col, grid)
        self.back_move(row, col, grid)
        self.left_move(row, col, grid)
        self.right_move(row, col, grid)
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

    def front_move(self, row, col, grid):
        if row > 6:
            return
        else:
            if grid[row + 1][col].piece is None:
                self.front_list.append(grid[row + 1][col])
                self.front_move(row + 1, col, grid)
            elif grid[row + 1][col].piece is not None and self.check_opponent(grid[row + 1][col].piece.clor):
                grid[row + 1][col].clr = RED
                return
            else:
                return

    def back_move(self, row, col, grid):
        if row < 1:
            return
        else:
            if grid[row - 1][col].piece is None:
                self.back_list.append(grid[row - 1][col])
                self.back_move(row - 1, col, grid)
            elif grid[row - 1][col].piece is not None and self.check_opponent(grid[row - 1][col].piece.clor):
                grid[row - 1][col].clr = RED
                return
            else:
                return

    def left_move(self, row, col, grid):
        if col < 1:
            return
        else:
            if grid[row][col - 1].piece is None:
                self.left_list.append(grid[row][col - 1])
                self.left_move(row, col - 1, grid)
            elif grid[row][col - 1].piece is not None and self.check_opponent(grid[row][col - 1].piece.clor):
                grid[row][col - 1].clr = RED
                return
            else:
                return

    def right_move(self, row, col, grid):
        if col > 6:
            return
        else:
            if grid[row][col + 1].piece is None:
                self.right_list.append(grid[row][col + 1])
                self.right_move(row, col + 1, grid)
            elif grid[row][col + 1].piece is not None and self.check_opponent(grid[row][col + 1].piece.clor):
                grid[row][col + 1].clr = RED
                return
            else:
                return

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

    def check_opponent(self, op_clr):
        if (self.clor == BLACK and op_clr == WHITE) or (self.clor == WHITE and op_clr == BLACK):
            return True
        else:
            return False
