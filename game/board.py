from game.variables import BOARD_SIZE


class Board:
    def __init__(self, size=BOARD_SIZE):
        self.size = size
        self.grid = [[1 if (r + c) % 2 == 0 else 2 for c in range(size)]
                     for r in range(size)]

    def get_opponent(self, player):
        return 2 if player == 1 else 1

    def calculate_possible_moves(self, r, c):
        possible_moves = []
        player = self.grid[r][c]
        opponent = self.get_opponent(player)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.size and 0 <= nc < self.size:
                if self.grid[nr][nc] == opponent:
                    possible_moves.append((nr, nc))
        return possible_moves

    def move_piece(self, src, dst):
        source_row, source_col = src
        dest_row, dest_col = dst
        self.grid[dest_row][dest_col] = self.grid[source_row][source_col]
        self.grid[source_row][source_col] = 0

    def apply_move(self, src, dst):
        source_row, source_col = src
        dest_row, dest_col = dst
        captured = self.grid[dest_row][dest_col]
        self.grid[dest_row][dest_col] = self.grid[source_row][source_col]
        self.grid[source_row][source_col] = 0
        return captured

    def undo_move(self, source, dst, captured):
        source_row, source_col = source;
        dest_row, dest_col = dst
        self.grid[source_row][source_col] = self.grid[dest_row][dest_col]
        self.grid[dest_row][dest_col] = captured
