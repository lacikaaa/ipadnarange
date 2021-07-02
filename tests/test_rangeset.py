import unittest

from rangeset import RangeSet


class TestRangeSet(unittest.TestCase):
    def test_minus(self):
        original = RangeSet([(0, 1000)])
        occupied = RangeSet([(3, 10), (123, 500), (600, 950)])
        result = original - occupied
        self.assertEqual([(0, 2), (11, 122), (501, 599), (951, 1000)], result.ranges)

    def test_no_occupied(self):
        original = RangeSet([(0, 1000)])
        occupied = RangeSet([])
        result = original - occupied
        self.assertEqual([(0, 1000)], result.ranges)

    def test_whole_occupied(self):
        original = RangeSet([(0, 1000)])
        occupied = RangeSet([(0, 1000)])
        result = original - occupied
        self.assertEqual([], result.ranges)

    def test_whole_occupied_with_two(self):
        original = RangeSet([(0, 1000)])
        occupied = RangeSet([(0, 500), (501, 1000)])
        result = original - occupied
        self.assertEqual([], result.ranges)

    def test_one_element_range(self):
        original = RangeSet([(0, 1000)])
        occupied = RangeSet([(0, 500), (502, 1000)])
        result = original - occupied
        self.assertEqual([(501, 501)], result.ranges)


if __name__ == '__main__':
    unittest.main()
