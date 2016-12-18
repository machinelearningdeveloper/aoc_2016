import unittest

from room import (extract_checksum, create_checksum,
                  is_valid_checksum, extract_sector_id,
                  sum_sector_ids, load_rooms, decrypt)

class TestSumSectorIds(unittest.TestCase):
    def setUp(self):
        self.valid_room_a = 'aaaaa-bbb-z-y-x-123[abxyz]'
        self.valid_room_b = 'a-b-c-d-e-f-g-h-987[abcde]'
        self.valid_room_c = 'not-a-real-room-404[oarel]'
        self.invalid_room = 'totally-real-room-200[decoy]'

    def test_extract_checksum(self):
        assert extract_checksum(self.valid_room_a) == 'abxyz'
        assert extract_checksum(self.valid_room_b) == 'abcde'
        assert extract_checksum(self.valid_room_c) == 'oarel'
        assert extract_checksum(self.invalid_room) == 'decoy'

    def test_create_checksum(self):
        assert create_checksum(self.valid_room_a) == 'abxyz'
        assert create_checksum(self.valid_room_b) == 'abcde'
        assert create_checksum(self.valid_room_c) == 'oarel'
        assert create_checksum(self.invalid_room) == 'loart'

    def test_is_valid_checksum(self):
        assert is_valid_checksum(self.valid_room_a) == True
        assert is_valid_checksum(self.valid_room_b) == True
        assert is_valid_checksum(self.valid_room_c) == True
        assert is_valid_checksum(self.invalid_room) == False

    def test_extract_sector_id(self):
        assert extract_sector_id(self.valid_room_a) == '123'
        assert extract_sector_id(self.valid_room_b) == '987'
        assert extract_sector_id(self.valid_room_c) == '404'

    def test_sum_sector_ids(self):
        assert sum_sector_ids([self.valid_room_a, self.valid_room_b,
                               self.valid_room_c, self.invalid_room]) == 1514

    def test_load_room(self):
        assert len(load_rooms())

    def test_decrypt(self):
        assert decrypt('qzmt-zixmtkozy-ivhz-343') == 'very encrypted name'

