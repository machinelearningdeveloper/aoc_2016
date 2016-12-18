import unittest

from sum_sector_ids import (extract_checksum,
                            create_checksum,
                            is_valid_checksum,
                            extract_sector_id,
                            sum_sector_ids)

class TestSumSectorIds(unittest.TestCase):
    def setUp(self):
        self.valid_room_a = 'aaaaa-bbb-z-y-x-123[abxyz]'
        self.valid_room_b = 'a-b-c-d-e-f-g-h-987[abcde]'
        self.invalid_room = 'not-a-real-room-404[oarel]'

    def test_extract_checksum(self):
        assert extract_checksum(self.valid_room_a) == 'abxyz'
        assert extract_checksum(self.valid_room_b) == 'abcde'
        assert extract_checksum(self.invalid_room) == 'oarel'

    def test_create_checksum(self):
        assert create_checksum(self.valid_room_a) == 'abxyz'
        assert create_checksum(self.valid_room_b) == 'abcde'
        assert create_checksum(self.invalid_room) == 'aelor'

    def test_is_valid_checksum(self):
        assert is_valid_checksum(self.valid_room_a) == True
        assert is_valid_checksum(self.valid_room_b) == True
        assert is_valid_checksum(self.invalid_room) == False

    def test_extract_sector_id(self):
        assert extract_sector_id(self.valid_room_a) == '123'
        assert extract_sector_id(self.valid_room_b) == '987'

    def test_sum_sector_ids(self):
        assert sum_sector_ids([self.valid_room_a, self.valid_room_b,
                               self.invalid_room]) == 1110
