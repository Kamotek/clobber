# heuristics/positional_heuristic.py

from .utils import calculate_possible_moves
from .minmax import minimax, alpha_beta


def calculate_score(board):
    player_id = board.current_player
    opp_id = board.get_opponent(player_id)

    my_positional_score = 0
    opp_positional_score = 0

    CORNER_PENALTY = -50
    WALL_PENALTY = -10

    size = board.size
    rows, cols = size, size

    corners = [(0, 0), (0, cols - 1), (rows - 1, 0), (rows - 1, cols - 1)]

    for r in range(rows):
        for c in range(cols):
            if board.grid[r][c] == player_id:
                if (r, c) in corners:
                    my_positional_score += CORNER_PENALTY
                elif r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    my_positional_score += WALL_PENALTY
            elif board.grid[r][c] == opp_id:
                if (r, c) in corners:
                    opp_positional_score += CORNER_PENALTY
                elif r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    opp_positional_score += WALL_PENALTY

    positional_advantage = my_positional_score - opp_positional_score

    my_moves = len(calculate_possible_moves(board, player_id))
    opp_moves = len(calculate_possible_moves(board, opp_id))
    mobility_advantage = my_moves - opp_moves

    return positional_advantage + mobility_advantage * 15


def move(board, player_id, depth, use_alpha_beta=True):
    board.current_player = player_id
    heuristic = calculate_score

    if use_alpha_beta:
        _, best_move, _ = alpha_beta(board, depth, heuristic, True)
    else:
        _, best_move, _ = minimax(board, depth, heuristic, True)

    return best_move