
import unittest
class TDDstatic_class_method(unittest.TestCase):
    def test_static_class_method(self):
        class E(object):
            def f(x):
                return (x)
            f = staticmethod(f)
        self.assertIs(E.f(3),3)
        self.assertIs(E().f(3),3)
    def test_implementation(self):
        class StaticMethod(object):
            "Emulate PyStaticMethod_Type() in Objects/funcobject.c"
            def __init__(self, f): self.f = f
            def __get__(self, obj, objtype=None): return self.f
    def test_class_method(self):
        class E(object):
            def f(klass, x):
                return klass.__name__, x
            f = classmethod(f)
        self.assertEqual(E.f(3), ('E', 3))
        self.assertEqual(E.f(3), E().f(3))
        e=E()
        self.assertEqual(e.f(3), ('E', 3))
    def test_fromkeys(self):
        from collections import defaultdict
        class Dict(object): 
            def fromkeys(klass, iterable, value=None):
                "Emulate dict_fromkeys() in Objects/dictobject.c"
                d = klass()
                for key in iterable:
                    d[key] = value
                return d
            fromkeys = classmethod(fromkeys)
        self.assertRaises(TypeError,lambda:Dict.fromkeys('abracadabra'))
    def test_classmethod(self):
        class ClassMethod(object):
            "Emulate PyClassMethod_Type() in Objects/funcobject.c"
            def __init__(self, f): self.f = f
            def __get__(self, obj, klass=None):
                if klass is None:
                    klass = type(obj)
                def newfunc(*args):
                    return self.f(klass, *args)
                return newfunc
if __name__ == '__main__':
    unittest.main()

                