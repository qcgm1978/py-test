import unittest
class TDDDiveIntoPython3(unittest.TestCase):
    def test_all(self):
        # The all() method returns True when all elements in the given iterable are true. If not, it returns False.
        # all values true
        l = [1, 3, 4, 5]
        self.assertTrue(all(l))

        # all values false
        l = [0, False]
        self.assertFalse(all(l))

        # one false value
        l = [1, 3, 4, 0]
        self.assertFalse(all(l))

        # one true value
        l = [0, False, 5]
        self.assertFalse(all(l))

        # empty iterable
        l = []
        self.assertTrue(all(l))
        actual = [
            -0.2896346,
            -0.4064693,
            0.66847844,
            0.54833631,
        ]
        self.assertTrue(all(x < 1 and x>-1 for x in actual))
if __name__ == '__main__':
    unittest.main()
