
import unittest
class TDDisinstance(unittest.TestCase):
    def test_isinstance(self):
        # Return True if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the given type, the function always returns False. If classinfo is a tuple of type objects (or recursively, other such tuples), return True if object is an instance of any of the types. If classinfo is not a type or tuple of types and such tuples, a TypeError exception is raised.
        self.assertTrue( isinstance(True, bool))
        self.assertTrue( isinstance(True, int))
        self.assertFalse( isinstance(True, float))
        self.assertFalse( isinstance(True, tuple))
        self.assertFalse( isinstance('True', bool))
        self.assertTrue( isinstance(True, (bool,int)))
        self.assertTrue( isinstance(True, (bool,int,float)))
        self.assertFalse( isinstance(True, (tuple,float)))
        self.assertRaises(TypeError,lambda:isinstance(True,[]))
if __name__ == '__main__':
    unittest.main()

                