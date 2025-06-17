from abc import ABC, abstractmethod
import random
from heuristics.aggresive_heuristic import move as aggressive_move
from heuristics.defensive_heuristic import move as defensive_move
from heuristics.positional_heuristic import move as positional_move
from heuristics.random_algorithm import move as random_move

class Player(ABC):
    def __init__(self,id): self.id=id
    @abstractmethod
    def is_human(self): pass

class HumanPlayer(Player):
    def __init__(self,id): super().__init__(id); self.selected=None; self.valid_moves=[]
    def is_human(self): return True
    def handle_click(self,pos,board):
        r,c=pos
        if not self.selected:
            if board.grid[r][c]==self.id:
                mv=board.calculate_possible_moves(r,c)
                if mv: self.selected=(r,c); self.valid_moves=mv
            return None
        if pos in self.valid_moves:
            mv=(self.selected,pos); self.selected=None; self.valid_moves=[]; return mv
        self.selected=None; self.valid_moves=[]; return None

class AIPlayer(Player):
    def __init__(self,id,htype,algo,depth):
        super().__init__(id)
        self.htype=htype
        self.algo=algo
        self.depth=depth
    def is_human(self): return False
    def get_move(self,board):
        if self.htype=='aggressive': return aggressive_move(board,self.id,self.depth,self.algo=='alpha_beta')
        if self.htype=='defensive': return defensive_move(board,self.id,self.depth,self.algo=='alpha_beta')
        if self.htype=='positional': return positional_move(board,self.id,self.depth,self.algo=='alpha_beta')
        return random_move(board,self.id)
