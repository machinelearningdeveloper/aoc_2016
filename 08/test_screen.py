import unittest

from screen import (explode, implode, load_instructions,
                    parse_command, rect, redraw_screen,
                    rotate, rotate_column, rotate_row,
                    transpose)


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

    def test_rotate_column(self):
        assert rotate_column(self.screen_b, 1, 1) \
                   == self.screen_c

    def test_rotate_row(self):
        assert rotate_row(self.screen_c, 0, 4) \
                   == self.screen_d

    def test_rotate(self):
        assert rotate(['#', '.', '.', '.', '.', '.', '.'], 4) \
                   == ['.', '.', '.', '.', '#', '.', '.']
        assert rotate(['.', '.', '.', '.', '#', '.', '.'], 4) \
                   == ['.', '#', '.', '.', '.', '.', '.']

    def test_explode(self):
        assert explode(self.screen_b) == self.exploded_b

    def test_transpose(self):
        assert transpose(self.exploded_b) == self.transposed_b

    def test_implode(self):
        assert implode(self.exploded_b) == self.screen_b

    def test_parse_command(self):
        assert parse_command(self.instructions['a_to_b']) \
                   == (rect, 3, 2)
        assert parse_command(self.instructions['b_to_c']) \
                   == (rotate_column, 1, 1)
        assert parse_command(self.instructions['c_to_d']) \
                   == (rotate_row, 0, 4)

    def test_rect(self):
        assert rect(self.screen_a, 3, 2) == self.screen_b
