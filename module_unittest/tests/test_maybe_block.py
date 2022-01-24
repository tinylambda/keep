import logging
import os
import unittest


class TestMaybeBlock(unittest.TestCase):
    def setUp(self):
        self.saved = os.environ.copy()

    def tearDown(self):
        os.environ = self.saved

    def test_one(self):
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        datefmt = r"%b %d %H:%M:%S"



    def test_two(self):
        pass
