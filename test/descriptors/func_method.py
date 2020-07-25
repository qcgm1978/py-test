
import unittest
class TDDfunc_method(unittest.TestCase):
    def test_func_method(self):
        class Function(object): 
            def __get__(self, obj, objtype=None):
                "Simulate func_descr_get() in Objects/funcobject.c"
                if obj is None:
                    return self
                return types.MethodType(self, obj)
        ins=Function()
        self.assertRaises(NameError,lambda:ins.__get__({}))
    def test_func_descriptor(self):
        class D(object):
            def f(self, x):
                return x
        d = D()
        self.assertEqual(d.f(2), 2)
        # Access through the class dictionary does not invoke __get__.
        # It just returns the underlying function object.
        # Dotted access from a class calls __get__() which just returns
        # the underlying function unchanged.
        self.assertIs(D.__dict__['f'],D.f)
        self.assertEqual(D.__dict__['f'](D,2), 2)
        # The function has a __qualname__ attribute to support introspection
        self.assertEqual(D.f.__qualname__,'TDDfunc_method.test_func_descriptor.<locals>.D.f')
        # Dotted access from an instance calls __get__() which returns the function wrapped in a bound method object
        self.assertTrue(callable(d.f))
        # Internally, the bound method stores the underlying function,
        # the bound instance, and the class of the bound instance.
        self.assertIs(d.f.__func__, D.f)
        self.assertIsInstance(d.f.__self__,object)
        self.assertIsInstance(d.f.__class__,object)
if __name__ == '__main__':
    unittest.main()

                