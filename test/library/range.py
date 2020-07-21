
import unittest
class TDDrange(unittest.TestCase):
    def test_range(self):
#         class range(stop)
# class range(start, stop[, step])
# Rather than being a function, range is actually an immutable sequence type, as documented in Ranges and Sequence Types — list, tuple, range.
        self.assertTrue(True)
        self.assertEqual(list(range(10)),
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(list(range(1, 11)),
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(list(range(0, 30, 5)),
        [0, 5, 10, 15, 20, 25])
        self.assertEqual(list(range(0, 10, 3)),
        [0, 3, 6, 9])
        self.assertEqual(list(range(0, -10, -1)),
        [0, -1, -2, -3, -4, -5, -6, -7, -8, -9])
        self.assertEqual(list(range(0)),
        [])
        self.assertEqual(list(range(1, 0)),[])
if __name__ == '__main__':
    unittest.main()

                