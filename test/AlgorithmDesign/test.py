import unittest
from how import Solution as Solution1
class TDD_HOW(unittest.TestCase):
    def test_how(self):
        self.assertEqual(Solution1().addTwo(1,2),3)
    def test_binary_search(self):
        # Initialize the sorted list
        list = [2, 7, 19, 34, 53, 72]
        ins=Solution1()
        self.assertEqual(ins.bsearch(list,72),5)
        self.assertIsNone(ins.bsearch(list,11))
if __name__ == '__main__':
    unittest.main()

                