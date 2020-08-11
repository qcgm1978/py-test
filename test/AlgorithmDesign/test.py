import unittest,sys
from how import Solution as Solution1
from backtracking import permute
from treeTraversal import Node,NodePreOrder
from sorting import bubblesort,merge_sort,insertion_sort,shellSort,selection_sort
from searching import linear_search
class TDD_HOW(unittest.TestCase):
    def test_how(self):
        self.assertEqual(Solution1().addTwo(1,2),3)
    def test_binary_search(self):
        # Initialize the sorted list
        list = [2, 7, 19, 34, 53, 72]
        ins=Solution1()
        # self.assertEqual(ins.bsearch(list,72),5)
        # self.assertIsNone(ins.bsearch(list, 11))
        self.assertEqual(ins.maxV, 2**63-1)
        r = range(sys.maxsize+10)
        # self.assertEqual(ins.bsearch(r, 72), 72)
        list = [8,11,24,56,88,131]
        self.assertEqual(ins.bsearch(list, 0, 5, 24),2)
        self.assertIsNone(ins.bsearch(list, 0, 5, 51))
    def test_backtracking(self):
        self.assertEqual(permute(1, ["a","b","c"]),['a','b','c'])
        self.assertEqual(permute(2, ["a","b","c"]),['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'])
        self.assertEqual(permute(3, ["a", "b", "c"]), ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc'])
    def test_inorder_traversal(self):
        root = Node(27)
        root.insert(14)
        root.insert(35)
        root.insert(10)
        root.insert(19)
        root.insert(31)
        root.insert(42)
        self.assertEqual(root.inorderTraversal(root),[10, 14, 19, 27, 31, 35, 42])
    def test_preorder_traversal(self):
        root = NodePreOrder(27)
        root.insert(14)
        root.insert(35)
        root.insert(10)
        root.insert(19)
        root.insert(31)
        root.insert(42)
        self.assertEqual(root.PreorderTraversal(root), [27, 14, 10, 19, 35, 31, 42])
        self.assertEqual(root.PostorderTraversal(root),[10, 19, 14, 31, 42, 35, 27])
    def test_bubblesort(self):
        list = [19,2,31,45,6,11,121,27]
        bubblesort(list)
        self.assertEqual(list,[2, 6, 11, 19, 27, 31, 45, 121])
    def test_merge(self):
        unsorted_list = [64, 34, 25, 12, 22, 11, 90]
        self.assertEqual(merge_sort(unsorted_list), [11, 12, 22, 25, 34, 64, 90])
    def test_insertion_sort(self):
        list = [19,2,31,45,30,11,121,27]
        list1 = [19,2,31,45,30,11,121,27]
        list2=insertion_sort(list)
        self.assertEqual(list2,merge_sort(list1))
    def test_shell_sort(self):
        list = [19,2,31,45,30,11,121,27]
        l=shellSort(list)
        self.assertEqual(l,[2, 11, 19, 27, 30, 31, 45, 121])
    def test_selection_sort(self):
        l = [19,2,31,45,30,11,121,27]
        l1=selection_sort(l)
        self.assertEqual(l1,[2, 11, 19, 27, 30, 31, 45, 121])
        self.assertEqual(l1,shellSort(l))
    def test_searching(self):
        l = [64, 34, 25, 12, 22, 11, 90]
        self.assertTrue(linear_search(l, 12))
        self.assertFalse(linear_search(l, 91))
if __name__ == '__main__':
    unittest.main()
