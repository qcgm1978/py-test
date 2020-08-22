
import unittest
from findSubstring import Solution
class TDD_TEST30(unittest.TestCase):
    def test_findSubstring(self):
        ins = Solution()
        l = ins.findSubstring(s="barfoothefoobarman", words=["foo", "bar"])
        self.assertEqual(l,[0,9])
        

if __name__ == '__main__':
    unittest.main()

                