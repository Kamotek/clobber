# heuristics/utils.py (ulepszona wersja)

def calculate_possible_moves(board, player_id):
    moves = []
    size = board.size

    for r in range(size):
        for c in range(size):
            if board.grid[r][c] == player_id:
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < size and 0 <= nc < size:
                        if board.grid[nr][nc] not in [0, player_id]:
                            moves.append(((r, c), (nr, nc)))
    return moves