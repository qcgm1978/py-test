import unittest
from generateParenthesis import Solution

class TDD_TEST11(unittest.TestCase):
    def test_generateParenthesis(self):
        ins = Solution()
        n = ins.generateParenthesis(3)
        n1 = ins.generateParenthesis(1)
        self.assertCountEqual(n, [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
        ])
        self.assertCountEqual(n1,['()'])
   
if __name__ == '__main__':
    unittest.main()

                