import unittest
from plural_iterator import LazyRules
class Fib:
    '''iterator that yields numbers in the Fibonacci sequence'''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        # self.a= self.b
        # self.b=fib+self.b
        # (self.a, self.b) = (self.b, self.a + self.b)
        # This is just a special case of the tuple abbreviation: 
        # you could equivalently write the above like the following:
        self.a, self.b = self.b, self.a + self.b
        return fib
class PapayaWhip:
    pass

class TDDDiveIntoPython3(unittest.TestCase):
    def test_class(self):
        self.assertTrue(Fib)
        self.assertTrue(type(PapayaWhip))
        fib=Fib(100)
        self.assertTrue(type(fib))
        self.assertTrue(fib.__class__)
        self.assertEqual(fib.__doc__,'iterator that yields numbers in the Fibonacci sequence')
        self.assertEqual(fib.max,100)
        self.assertEqual(Fib(200).max,200)
        iter(fib)
        self.assertEqual(fib.a,0)
        self.assertEqual(fib.b,1)
        next(fib)
        self.assertEqual(fib.a,1)
        self.assertEqual(fib.b,1)
        arr=[]
        for n in Fib(10):
            arr.append(n)
        self.assertEqual(arr,[0,1,1,2,3,5,8])

    def test_class(self):
        rules=LazyRules()
        self.assertEqual(rules.pattern_file.closed,False)
        self.assertEqual(rules.cache,[])
        file = './test/test_regular_expressions/plural4-rules.txt'
        self.assertEqual(rules.rules_filename,file)
        self.assertEqual(rules.__class__.rules_filename,file)
        self.rules_filename=None
        self.assertIsNone(self.rules_filename)
        self.rules_filename=file
        self.assertEqual(self.rules_filename,file)


if __name__ == '__main__':
    unittest.main()