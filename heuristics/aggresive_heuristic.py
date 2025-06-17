# heuristics/aggressive_heuristic.py
from .utils import calculate_possible_moves
from .minmax import minimax, alpha_beta


def calculate_score(board):

    player_id = board.current_player
    opp_id = board.get_opponent(player_id)

    my_pieces = sum(cell == player_id for row in board.grid for cell in row)
    opp_pieces = sum(cell == opp_id for row in board.grid for cell in row)
    material = my_pieces - opp_pieces

    my_moves = len(calculate_possible_moves(board, player_id))
    opp_moves = len(calculate_possible_moves(board, opp_id))
    mobility = my_moves - opp_moves

    size = board.size
    center = (size - 1) / 2
    pos_score = 0
    for r in range(size):
        for c in range(size):
            if board.grid[r][c] == player_id:
                pos_score += (size - (abs(r - center) + abs(c - center)))

    return material * 10 + mobility * 5 + pos_score


def move(board, player_id, depth, use_alpha_beta=True):

    board.current_player = player_id
    heuristic = calculate_score

    if use_alpha_beta:
        _, best_move, _ = alpha_beta(board, depth, heuristic, True)
    else:
        _, best_move, _ = minimax(board, depth, heuristic, True)

    return best_move

