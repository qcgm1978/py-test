
import unittest
class TDDlen(unittest.TestCase):
    def test_len(self):
        # Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
        s = ' '
        by = b'\x65'
        t = ('t')
        l = ['']
        r = range(1)
        d = {'d': ''}
        st = {''}
        # tuple of vowels
        vowels = ('a')
        fSet = frozenset(vowels)
        self.assertEqual(len(s),1)
        self.assertEqual(len(by),1)
        self.assertEqual(len(t),1)
        self.assertEqual(len(l),1)
        self.assertEqual(len(r),1)
        self.assertEqual(len(d),1)
        self.assertEqual(len(st),1)
        self.assertEqual(len(fSet),1)

if __name__ == '__main__':
    unittest.main()

                