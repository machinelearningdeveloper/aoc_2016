from move import normalize_index, move
import unittest

class TestMove(unittest.TestCase):
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
