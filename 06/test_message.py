import unittest

from message import recover_message, load_messages


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.messages = ['eedadn', 'drvtee', 'eandsr',
                         'raavrd', 'atevrs', 'tsrnev',
                         'sdttsa', 'rasrtv', 'nssdts',
                         'ntnada', 'svetve', 'tesnvt',
                         'vntsnd', 'vrdear', 'dvrsen',
                         'enarar']

    def test_recover_message(self):
        assert recover_message(self.messages) == 'easter'


    def test_load_messages(self):
        assert len(load_messages())
