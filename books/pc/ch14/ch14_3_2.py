import errno
import sys
import unittest


def parse_int(s):
    return int(s)


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, 'N/A')

    def test_bad_int2(self):
        with self.assertRaises(ValueError):
            parse_int('N/A')


class TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open('/file/not/found')
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
        else:
            self.fail('IOError not raised')
