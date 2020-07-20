
import unittest
class TDDclassmethod(unittest.TestCase):
    def test_classmethod(self):
        
        class C:
            @classmethod
            def f(cls, arg1, arg2):
                return cls
        a = C()
        c=a.f(1,2)
        self.assertIs(c, C)
        d = c()
        self.assertIs(d.f(1,2),C)
if __name__ == '__main__':
    unittest.main()

                