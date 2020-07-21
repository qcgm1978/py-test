
import unittest
class TDDdict(unittest.TestCase):
    def test_dict(self):
        # Create a new dictionary. The dict object is the dictionary class. 
        d=dict(a=1, b=2, c=3)
        self.assertTrue(d)
        self.assertDictContainsSubset(d,{'a':1,'b':2,'c':3})
        self.assertDictEqual(d,{'a':1,'b':2,'c':3})
        self.assertIsInstance(d,dict)
if __name__ == '__main__':
    unittest.main()

                