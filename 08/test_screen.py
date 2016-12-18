import unittest

from screen import (explode, load_instructions,
                    redraw_screen, rotate, transpose)


class TestScreen(unittest.TestCase):
    def setUp(self):
        self.screen_a = '.......\n.......\n.......'
        self.screen_b = '###....\n###....\n.......'
        self.screen_c = '#.#....\n###....\n.#.....'
        self.screen_d = '....#.#\n###....\n.#.....'
        self.screen_e = '.#..#.#\n#.#....\n.#.....'
        self.instructions = {
            'a_to_b': 'rect 3x2',
            'b_to_c': 'rotate column x=1 by 1',
            'c_to_d': 'rotate row y=0 by 4',
            'd_to_e': 'rotate column x=1 by 1'
        }
        self.exploded_b = [['#', '#', '#', '.', '.', '.', '.'],
                           ['#', '#', '#', '.', '.', '.', '.'],
                           ['.', '.', '.', '.', '.', '.', '.']]
        self.transposed_b = [['#', '#', '.'],
                             ['#', '#', '.'],
                             ['#', '#', '.'],
                             ['.', '.', '.'],
                             ['.', '.', '.'],
                             ['.', '.', '.'],
                             ['.', '.', '.']]

    def test_load_instructions(self):
        assert len(load_instructions())

    def test_redraw_screen(self):
        assert redraw_screen(self.screen_a, self.instructions['a_to_b']) \
                   == self.screen_b
        assert redraw_screen(self.screen_b, self.instructions['b_to_c']) \
                   == self.screen_c
        assert redraw_screen(self.screen_c, self.instructions['c_to_d']) \
                   == self.screen_d
        assert redraw_screen(self.screen_d, self.instructions['d_to_e']) \
                   == self.screen_e

    def test_rotate(self):
        assert rotate(['#', '.', '.', '.', '.', '.' '.'], 4) \
                   == ['.', '.', '.', '.', '#', '.' '.']
        assert rotate(['.', '.', '.', '.', '#', '.' '.'], 4) \
                   == ['.', '#', '.', '.', '.', '.' '.']

    def test_explode(self):
        assert explode(self.screen_b) == self.exploded_b

    def test_transpose(self):
        assert transpose(self.exploded_b) == self.transposed_b
