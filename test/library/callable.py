
import unittest
class TDDcallable(unittest.TestCase):
    def test_callable(self):
        # Return True if the object argument appears callable, False if not. If this returns True, it is still possible that a call fails, but if it is False, calling object will never succeed. Note that classes are callable (calling a class returns a new instance); instances are callable if their class has a __call__() method.
        self.assertTrue(callable(callable))
        self.assertFalse(callable(Ellipsis))
        self.assertRaises(TypeError, Ellipsis)
        class Person:
            Ellipsis
        self.assertTrue(callable(Person))
        p = Person()
        self.assertFalse(callable(p))
        Person.__call__=lambda:2
        self.assertTrue(callable(p))
        self.assertRaises(TypeError,p.__call__)
        p.__call__ = lambda: 1
        self.assertEqual(p.__call__(),1)
        self.assertTrue(callable(p))
        class Person:
            def __call__(self):
                return 2
        p = Person()
        self.assertTrue(callable(p))
        self.assertEqual(p.__call__(),2)

if __name__ == '__main__':
    unittest.main()

                