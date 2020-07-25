
import unittest
class TDDinvoking(unittest.TestCase):
    def test_invoking(self):
        def __getattribute__(self, key):
            "Emulate type_getattro() in Objects/typeobject.c"
            v = object.__getattribute__(self, key)
            if hasattr(v, '__get__'):
                return v.__get__(None, self)
            return v
        self.assertTrue(True)
    def test_obj(self):
        class RevealAccess(object):
            """A data descriptor that sets and returns values
            normally and prints a message logging their access. """
            def __init__(self, initval=None, name='var'):
                self.val = initval
                self.name = name
            def __get__(self, obj, objtype):
                # print('Retrieving', self.name)
                return self.val
            def __set__(self, obj, val):
                # print('Updating', self.name)
                self.val = val
        class MyClass(object):
            x = RevealAccess(10, 'var "x"')
            y = 5
            def __get__(self, obj, objtype):
                # print('Retrieving', self.name)
                return self.val
        m =MyClass()
        self.assertEqual(m.x, 10)
        m.x = 20
        self.assertEqual(m.x, 20)
        # https://stackoverflow.com/a/40464415/2630686
        # descriptor: a descriptor is an object attribute with “binding behavior”
        # 1, C.foo is looked up. If it is not a data descriptor(regular attribute), Python will store this result for step 3
        # 2, If C.foo is a regular attribute, If bar.__dict__['foo'] not exists, go to step 3
        # 3, C.foo exists, then C.foo is used
        self.assertEqual(m.y,5)
if __name__ == '__main__':
    unittest.main()

                