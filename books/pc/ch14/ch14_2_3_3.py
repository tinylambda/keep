import io
import unittest
from unittest.mock import patch

from books.pc.ch14 import mymodule

sample_data = io.BytesIO(
    b"""\
"IBM",91.1\r
"AA",13.25\r
"MSFT",27.72\r
\r
"""
)


class Tests(unittest.TestCase):
    @patch("books.pc.ch14.mymodule.urlopen", return_value=sample_data)
    def test_dowproces(self, mock_urlopen):
        p = mymodule.dowprices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p, {"IBM": 91.1, "AA": 13.25, "MSFT": 27.72})


if __name__ == "__main__":
    unittest.main()

# or pytest books/pc/ch14/ch14_2_3_3.py
