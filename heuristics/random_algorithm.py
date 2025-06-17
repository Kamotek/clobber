import random
from .utils import calculate_possible_moves

def move(board,player_id,depth=None,use_alpha_beta=False):
    mv=calculate_possible_moves(board,player_id)
    return random.choice(mv) if mv else None
