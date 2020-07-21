
import unittest
class TDDid(unittest.TestCase):
    def test_id(self):
        # Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
        self.assertTrue(callable(id))
        i = {}
        iId=id(i)
        self.assertIsInstance(iId, int)
        m = {}
        self.assertNotEqual(iId, id(m))
        i = None
        n={}
        self.assertEqual(iId, id(n))

if __name__ == '__main__':
    unittest.main()

                