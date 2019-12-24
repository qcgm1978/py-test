import unittest
import fractions
import math
class TddInPythonExample(unittest.TestCase):

    def test_immutable(self):
        a_tuple=('a','b','Confucian','z','example')
        self.assertEqual(a_tuple[0], 'a')
        self.assertEqual(a_tuple[-1], 'example')
        self.assertEqual(a_tuple[1:3], ('b','Confucian'))
        def attr_err():
            a_tuple.append('new')
        self.assertRaises(AttributeError)
   
    def test_tuples_as_bool(self):
        self.assertFalse(())
        self.assertTrue(('a','b'))
        self.assertTrue((False,))
        self.assertEqual(type((False)),bool)
        self.assertEqual(type((False,)),tuple)

if __name__ == '__main__':
    unittest.main()
