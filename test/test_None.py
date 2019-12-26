import unittest
import fractions
import math
class TddInPythonExample(unittest.TestCase):

    def test_none(self):
        self.assertEqual(None, None)
        self.assertIsNone(None)
        self.assertNotEqual(None,False)
        self.assertNotEqual(None,0)
        self.assertNotEqual(None,'')
        x=None
        self.assertEqual(None,x)
        y=None
        self.assertEqual(y,x)

    def test_none_as_bool(self):
        self.assertFalse(None)
        self.assertTrue(not None)


























    

if __name__ == '__main__':
    unittest.main()
