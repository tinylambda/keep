import bisect
import unittest


class SortedList(list):
    def __init__(self, iterable):
        super(SortedList, self).__init__(sorted(iterable))

    def insort(self, item):
        bisect.insort(self, item)

    def extend(self, other):
        for item in other:
            self.insort(item)

    @staticmethod
    def append(o):
        raise RuntimeError('cannot append to a sorted list')

    def index(self, value, start=None, stop=None):
        place = bisect.bisect_left(self[start:stop], value)
        if start:
            place += start
        end = stop or len(self)
        if place < end and self[place] == value:
            return place
        raise ValueError('%s is not in list' % value)


class TestSortedList(unittest.TestCase):
    def setUp(self) -> None:
        self.mylist = SortedList(['a', 'c', 'd', 'x', 'f', 'g', 'w'])

    def test_sorted_init(self):
        self.assertEqual(sorted(['a', 'c', 'd', 'x', 'f', 'g', 'w']), self.mylist)

    def test_sorted_insort(self):
        self.mylist.insort('z')
        self.assertEqual(sorted(['a', 'c', 'd', 'x', 'f', 'g', 'w', 'z']), self.mylist)
        self.mylist.insort('b')
        self.assertEqual(['a', 'b', 'c', 'd', 'f', 'g', 'w', 'x', 'z'], self.mylist)

    def test_index(self):
        self.assertEqual(0, self.mylist.index('a'))
        self.assertEqual(1, self.mylist.index('c'))
        self.assertEqual(5, self.mylist.index('w'))
        self.assertEqual(0, self.mylist.index('a', stop=0))
        self.assertEqual(0, self.mylist.index('a', stop=2))
        self.assertEqual(0, self.mylist.index('a', stop=20))
        self.assertRaises(ValueError, self.mylist.index, 'w', stop=3)
        self.assertRaises(ValueError, self.mylist.index, 'a', start=3)
        self.assertRaises(ValueError, self.mylist.index, 'a', start=333)

    def test_extend(self):
        self.mylist.extend(['b', 'h', 'j', 'c'])
        self.assertEqual(['a', 'b', 'c', 'c', 'd', 'f', 'g', 'h', 'j', 'w', 'x'], self.mylist)

