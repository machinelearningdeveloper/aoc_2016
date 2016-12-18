import unittest

from address import has_reflection, is_compatible


class TestAddress(unittest.TestCase):
    def test_has_reflection(self):
        assert has_reflection(['mnop']) == False
        assert has_reflection(['abba', 'qrst']) == True

    def test_is_compatible(self):
        assert is_compatible('abba[mnop]qrst') == True
        assert is_compatible('abcd[bddb]xyyx') == False
        assert is_compatible('aaaa[qwer]tyui') == False
        assert is_compatible('ioxxoj[asdfgh]zxcvbn') == True
        
