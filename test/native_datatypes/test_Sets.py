import unittest
import fractions
import math
class TddInPythonExample(unittest.TestCase):

    def test_set_create(self):
        a_set={1}
        self.assertEqual(a_set,{1})
        self.assertEqual(type(a_set),set)
        a_set={1,2}
        self.assertEqual(a_set,{1,2})
        a_list=['a','b']
        a_set=set(a_list)
        self.assertEqual(a_set,{'a','b'})
        self.assertEqual(a_list,['a','b'])
        a_set=set()
        self.assertEqual(a_set,set())
        self.assertNotEqual(a_set,{})
        self.assertEqual(type({}),dict)
        self.assertEqual(len(a_set),0)
    a_set=set()
    def test_modify_set(self):
        self.a_set={1,2}
        self.a_set.add(4)
        self.assertEqual(self.a_set,{1,2,4})
        self.assertEqual(self.a_set,{2,1,4})
        self.assertEqual(len(self.a_set),3)
        self.a_set.update({2,4,6})
        self.assertEqual(self.a_set,{1,2,4,6})
        self.a_set.update({5,7},{7,8})
        self.assertEqual(self.a_set,{1,2,4,5,6,7,8})
        self.a_set.update([19,20,21])
        self.assertEqual(self.a_set,{1,2,4,5,6,7,8,19,20,21})

    def test_remove_set(self):
        self.assertEqual(self.a_set,set())
        a_set= {1, 3, 6, 10, 15, 21, 28, 36, 45}
        a_set.discard(10)
        self.assertEqual(a_set, {1, 3, 6, 15, 21, 28, 36, 45})
        def remove():
            a_set.remove(21)
        remove()
        self.assertEqual(a_set, {1, 3, 6, 15, 28, 36, 45})
        self.assertRaises(KeyError,remove)
        a_set.pop()
        self.assertEqual(len(a_set),6)
        a_set.clear()
        self.assertEqual(a_set,set())
        self.assertRaises(KeyError,a_set.pop)

    def test_set_operation(self):
        a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
        self.assertFalse(31 in a_set)
        self.assertTrue(30 in a_set)
        b_set={1,2}
        self.assertEqual(a_set.union(b_set), {1,2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195})
        self.assertEqual(a_set.intersection(b_set), {2})
        self.assertEqual(a_set.difference(b_set), {4, 5, 9, 12, 21, 30, 51, 76, 127, 195})
        self.assertEqual(a_set.symmetric_difference(b_set), {1,4, 5, 9, 12, 21, 30, 51, 76, 127, 195})
        self.assertEqual(b_set.symmetric_difference(a_set), {1,4, 5, 9, 12, 21, 30, 51, 76, 127, 195})
        self.assertEqual(b_set.symmetric_difference(a_set), a_set.symmetric_difference(b_set))
        self.assertEqual(a_set.union(b_set),b_set.union(a_set))
        self.assertEqual(a_set.intersection(b_set),b_set.intersection(a_set))
        self.assertNotEqual(a_set.difference(b_set),b_set.difference(a_set))
        a_set={1,2,3}
        b_set={1,2,3,4}
        self.assertTrue(a_set.issubset(b_set))
        self.assertTrue(b_set.issuperset(a_set))
        a_set.add(5)
        self.assertFalse(a_set.issubset(b_set))
        
    def test_set_as_bool(self):
        self.assertFalse(set())
        self.assertTrue({'a'})
        self.assertTrue({False})


























    

if __name__ == '__main__':
    unittest.main()
