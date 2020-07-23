
import unittest
import collections
class TDDgen_comprehensions(unittest.TestCase):
    def test_gen_comprehensions(self):
        line_list = [' line 1\n', 'line 2 \n','']
        # Generator expression -- returns iterator
        stripped_iter = (line.strip() for line in line_list)
        # List comprehension -- returns list
        stripped_list = [line.strip() for line in line_list]
        self.assertRaises(SyntaxError,lambda: eval('line.strip() for line in line_list'))
        self.assertIsInstance(stripped_iter,collections.Iterable)
        self.assertIsInstance(stripped_list, list)
        stripped_list1 = [line.strip() for line in line_list if line != ""]
        self.assertEqual(len(stripped_list), len(stripped_list1) + 1)
        self.assertEqual(stripped_list1,['line 1','line 2'])
    def test_clauses(self):
        seq1 = 'abc'
        seq2 = (1, 2, 3)
        l=[(x, y) for x in seq1 for y in seq2]
        self.assertIsInstance(l, list)
        # iterated over from left to right, not in parallel.    
        self.assertEqual(l, [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)])

if __name__ == '__main__':
    unittest.main()

                