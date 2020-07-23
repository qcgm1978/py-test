import collections
import unittest
class TDDgenerators(unittest.TestCase):
    def test_generators(self):
        # Generators are a special class of functions that simplify the task of writing iterators. Regular functions compute a value and return it, but generators return an iterator that returns a stream of values.
        def generate_ints(N):
            for i in range(N):
                 yield i
        gen = generate_ints(3)
        self.assertIsInstance(gen,collections.Iterable)
        self.assertEqual(next(gen),0)
        self.assertEqual(next(gen),1)
        self.assertEqual(next(gen),2)
        self.assertRaises(StopIteration,lambda:next(gen))
    def test_tree(self):
        class Tree:
    
         def __init__(self, label, left=None, right=None):
             self.label = label
             self.left = left
             self.right = right
    
         def __repr__(self, level=0, indent="    "):
             s = level*indent + repr(self.label)
             if self.left:
                 s = s + "\\n" + self.left.__repr__(level+1, indent)
             if self.right:
                 s = s + "\\n" + self.right.__repr__(level+1, indent)
             return s
    
         def __iter__(self):
             return inorder(self)
        def tree(list):
         n = len(list)
         if n == 0:
             return []
         i = n // 2
         return Tree(list[i], tree(list[:i]), tree(list[i+1:]))
        t = tree("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        # print(t)
    def test_pass_val(self):
        def counter(maximum):
            i=0
            while i < maximum:
                val = (yield i)
                    # If value provided, change counter
                if val is not None:
                    i = val
                else:
                    i += 1
        it = counter(10)
        self.assertIsInstance(it,collections.Iterable)
        self.assertEqual(next(it),0)
        self.assertEqual(next(it),1)
        it.send(8) 
        self.assertEqual(next(it),9)
        self.assertRaises(StopIteration,lambda:next(it))
if __name__ == '__main__':
    unittest.main()

                