from triangle import load_triangles, is_impossible
import unittest


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangles = [(1, 2, 3), (2, 2, 4), (2, 2, 3)]

    def test_load_triangles(self):
        assert load_triangles('example.txt') == self.triangles

    def test_is_possible(self):
        assert is_possible(1, 2, 3) == False
        assert is_possible(2, 2, 5) == False
        assert is_possible(2, 2, 3) == True
