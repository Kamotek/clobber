# tests/test_heuristics.py

import unittest
from unittest.mock import MagicMock
from game.board import Board
from heuristics.utils import calculate_possible_moves as global_calculate_moves
import heuristics.aggresive_heuristic as aggressive
import heuristics.positional_heuristic as positional
from heuristics.minmax import minimax

class TestHeuristics(unittest.TestCase):

    def setUp(self):
        self.board = Board(size=4)

    def test_global_calculate_possible_moves(self):
        moves_player_1 = global_calculate_moves(self.board, 1)
        self.assertEqual(len(moves_player_1), 24)

        moves_player_2 = global_calculate_moves(self.board, 2)
        self.assertEqual(len(moves_player_2), 24)

    def test_aggressive_heuristic_score(self):
        self.board.grid = [
            [1, 2, 1, 0],
            [2, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.board.current_player = 1
        score = aggressive.calculate_score(self.board)
        self.assertGreater(score, 0)

    def test_positional_heuristic_score(self):
        self.board.grid = [
            [1, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.board.current_player = 1
        score = positional.calculate_score(self.board)
        self.assertLess(score, 0)

    def test_minimax_basic_choice(self):
        self.board.grid = [
            [1, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.board.current_player = 1

        simple_heuristic = lambda b: sum(row.count(1) for row in b.grid)

        _, best_move, _ = minimax(self.board, depth=1, heuristic=simple_heuristic, maximizing_player=True)
        self.assertEqual(best_move, ((0, 0), (0, 1)))

if __name__ == '__main__':
    unittest.main()