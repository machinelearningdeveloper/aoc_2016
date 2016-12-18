import unittest

from address import has_reflection, is_compatible, load_addresses


class TestAddress(unittest.TestCase):
    def test_has_reflection(self):
        assert has_reflection(['mnop']) == False
        assert has_reflection(['abba', 'qrst']) == True

    def test_is_compatible(self):
        assert is_compatible('abba[mnop]qrst') == True
        assert is_compatible('abcd[bddb]xyyx') == False
        assert is_compatible('aaaa[qwer]tyui') == False
        assert is_compatible('ioxxoj[asdfgh]zxcvbn') == True
        assert is_compatible('aba[bab]xyz', protocol=2) == True
        assert is_compatible('xyx[xyx]xyx', protocol=2) == False
        assert is_compatible('aaa[kek]eke', protocol=2) == True
        assert is_compatible('zazbz[bzb]cdb', protocol=2) == True
        
    def test_load_addresses(self):
        assert len(load_addresses())
