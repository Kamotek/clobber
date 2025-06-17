from .utils import calculate_possible_moves
from .minmax import minimax, alpha_beta


def calculate_score(board):

    player_id = board.current_player
    opp_id = board.get_opponent(player_id)

    my_moves = len(calculate_possible_moves(board, player_id))
    opp_moves = len(calculate_possible_moves(board, opp_id))

    if opp_moves == 0:
        return float('inf')

    if my_moves == 0:
        return -float('inf')

    my_pieces = sum(row.count(player_id) for row in board.grid)
    opp_pieces = sum(row.count(opp_id) for row in board.grid)
    material_advantage = my_pieces - opp_pieces


    return (my_moves * 5) - (opp_moves * 25) + (material_advantage * 2)


def move(board, player_id, depth, use_alpha_beta=True):
    board.current_player = player_id

    heuristic = calculate_score

    if use_alpha_beta:
        _, m, _ = alpha_beta(board, depth, heuristic, True)
    else:
        _, m, _ = minimax(board, depth, heuristic, True)

    return m