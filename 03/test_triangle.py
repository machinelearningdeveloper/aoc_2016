from triangle import load_triangles, is_possible, load_triangles_from_cols
import unittest


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangles = [(1, 2, 3), (2, 2, 4), (2, 2, 3)]
        self.col_triangles = [(1, 2, 2), (2, 2, 2), (3, 4, 3)]

    def test_load_triangles(self):
        assert load_triangles('example.txt') == self.triangles

    def test_is_possible(self):
        assert is_possible(1, 2, 3) == False
        assert is_possible(2, 2, 5) == False
        assert is_possible(2, 2, 3) == True

    def test_load_triangles_from_cols(self):
        assert load_triangles_from_cols('example.txt') == self.col_triangles
