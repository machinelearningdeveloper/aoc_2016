import unittest

from message import calc_decomp_sz, load_data, parse_marker, read_data


class TestMessage(unittest.TestCase):
    def test_calc_decomp_sz(self):
        assert calc_decomp_sz('(3x3)XYZ') == 9
        assert calc_decomp_sz('X(8x2)(3x3)ABCY') == 20
        assert calc_decomp_sz('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920 
        assert calc_decomp_sz('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445
 
    def test_parse_marker(self):
        assert parse_marker('(1x2)') == (1, 2)

    def test_load_data(self):
        assert len(load_data())

    def test_read_data(self):
        assert read_data('abcdef (1x2)z bh') == 'abcdefzzbh'
        assert read_data('A(1x5)BC') == 'ABBBBBC'
        assert read_data('(3x3)XYZ') == 'XYZXYZXYZ'
        assert read_data('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
        assert read_data('(6x1)(1x3)A') == '(1x3)A'
        assert read_data('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'
