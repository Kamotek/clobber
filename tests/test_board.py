# tests/test_board.py

import unittest
from game.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board(size=4)

    def test_board_initialization(self):
        self.assertEqual(self.board.size, 4)
        self.assertEqual(self.board.grid[0][0], 1)
        self.assertEqual(self.board.grid[0][1], 2)

    def test_get_opponent(self):
        self.assertEqual(self.board.get_opponent(1), 2)
        self.assertEqual(self.board.get_opponent(2), 1)

    def test_calculate_possible_moves(self):
        moves = self.board.calculate_possible_moves(0, 0)
        self.assertCountEqual(moves, [(0, 1), (1, 0)])

        self.board.grid[0][1] = 0
        moves = self.board.calculate_possible_moves(0, 0)
        self.assertCountEqual(moves, [(1, 0)])

    def test_move_piece(self):
        src, dst = (0, 0), (0, 1)
        player_id = self.board.grid[src[0]][src[1]]

        self.board.move_piece(src, dst)

        self.assertEqual(self.board.grid[dst[0]][dst[1]], player_id)
        self.assertEqual(self.board.grid[src[0]][src[1]], 0)

if __name__ == '__main__':
    unittest.main()