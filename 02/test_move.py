from move import (load_moves, encode_moves,
                  normalize_index, move,
                  alternate_move)
import unittest

class TestMove(unittest.TestCase):
    def setUp(self):
        self.moves = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']    

    def test_load_moves(self):
        assert load_moves('example.txt') == self.moves

    def test_encode_moves(self):
        assert encode_moves(self.moves) == '1985'

    def test_normalize_index(self):
        assert normalize_index(3) == 2
        assert normalize_index(2) == 2
        assert normalize_index(1) == 1
        assert normalize_index(0) == 0
        assert normalize_index(-1) == 0

    def test_move(self):
        assert move(5, 'U') == 2
        assert move(8, 'D') == 8
        assert move(7, 'L') == 7
        assert move(7, 'D') == 7
        assert move(2, 'R') == 3
        assert move(1, 'L') == 1

    def test_encode_alternate_moves(self):
        assert encode_moves(self.moves, use_alternate=True) == '5DB3'

    def test_alternate_move(self):
        assert alternate_move(5, 'U') == 5
        assert alternate_move(5, 'L') == 5
        assert alternate_move(7, 'D') == 'B'
        assert alternate_move('D', 'D') == 'D'
