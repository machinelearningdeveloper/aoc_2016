import unittest

from find_password import find_password


class TestFindPassword(unittest.TestCase):
    def test_find_password(self):
        assert find_password('abc', length=8) == '18f47a30'
        assert find_password('abc', length=8, complex=True) == '05ace8e3'
