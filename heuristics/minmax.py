import copy
from .utils import calculate_possible_moves


def minimax(board, depth, heuristic, maximizing_player):
    player_id = board.current_player
    moves = calculate_possible_moves(board, player_id)

    if depth == 0 or not moves:
        return heuristic(board), None, 1

    visited_nodes = 1
    best_move = None

    if maximizing_player:
        max_eval = -float('inf')
        for src, dst in moves:
            board_copy = copy.deepcopy(board)
            board_copy.move_piece(src, dst)
            board_copy.current_player = board_copy.get_opponent(player_id)

            eval_score, _, nodes_from_child = minimax(board_copy, depth - 1, heuristic, False)
            visited_nodes += nodes_from_child

            if eval_score > max_eval:
                max_eval = eval_score
                best_move = (src, dst)
        return max_eval, best_move, visited_nodes
    else:
        min_eval = float('inf')
        for src, dst in moves:
            board_copy = copy.deepcopy(board)
            board_copy.move_piece(src, dst)
            board_copy.current_player = board_copy.get_opponent(player_id)

            eval_score, _, nodes_from_child = minimax(board_copy, depth - 1, heuristic, True)
            visited_nodes += nodes_from_child

            if eval_score < min_eval:
                min_eval = eval_score
                best_move = (src, dst)
        return min_eval, best_move, visited_nodes


def alpha_beta(board, depth, heuristic, maximizing_player, alpha=-float('inf'), beta=float('inf')):
    player_id = board.current_player
    moves = calculate_possible_moves(board, player_id)

    if depth == 0 or not moves:
        return heuristic(board), None, 1

    visited_nodes = 1
    best_move = None

    if maximizing_player:
        value = -float('inf')
        for src, dst in moves:
            board_copy = copy.deepcopy(board)
            board_copy.move_piece(src, dst)
            board_copy.current_player = board_copy.get_opponent(player_id)

            eval_score, _, nodes_from_child = alpha_beta(board_copy, depth - 1, heuristic, False, alpha, beta)
            visited_nodes += nodes_from_child

            if eval_score > value:
                value = eval_score
                best_move = (src, dst)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value, best_move, visited_nodes
    else:
        value = float('inf')
        for src, dst in moves:
            board_copy = copy.deepcopy(board)
            board_copy.move_piece(src, dst)
            board_copy.current_player = board_copy.get_opponent(player_id)

            eval_score, _, nodes_from_child = alpha_beta(board_copy, depth - 1, heuristic, True, alpha, beta)
            visited_nodes += nodes_from_child

            if eval_score < value:
                value = eval_score
                best_move = (src, dst)
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value, best_move, visited_nodes