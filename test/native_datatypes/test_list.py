import unittest

class test_list(unittest.TestCase):
    def test_slicing(self):
        a_list=['a','b','mpilgrim','z','example']
        self.assertEqual(a_list[1:3],['b','mpilgrim'])
        self.assertEqual(a_list[1:-1],['b','mpilgrim','z'])
        self.assertEqual(a_list[0:3],['a','b','mpilgrim'])
        self.assertEqual(a_list[:3],['a','b','mpilgrim'])
        self.assertEqual(a_list[3:],['z','example'])
        self.assertEqual(a_list[:],a_list)

    def test_add_item(self):
        a_list=['a']
        a_list+=[2.0,3]
        self.assertEqual(a_list,['a',2.0,3])
        a_list.append(True)
        self.assertEqual(a_list,['a',2.0,3,True])

    def test_remove(self):
        a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
        a_list.remove('new')
        self.assertEqual(a_list,['a', 'b', 'mpilgrim','new'])











if __name__ == "__main__":
    unittest.main()