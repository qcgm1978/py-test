
import unittest
import operator,functools,collections,itertools

class TDDFunctools(unittest.TestCase):
    def test_functools(self):
        def log(message, subsystem):
            """Write the contents of 'message' to the specified subsystem."""
            return subsystem, message
        server_log = functools.partial(log, subsystem='server')
        self.assertIsInstance(server_log,functools.partial)
        s=server_log('Unable to open socket')
        self.assertEqual(s,('server', 'Unable to open socket'))
    def test_operator(self):
        n=functools.reduce(operator.add, [1, 2, 3, 4], 0)
        self.assertEqual(n, 10)
        n1 = sum([1, 2, 3, 4])
        self.assertEqual(n1, 10)
        self.assertEqual(sum([]),0)
        product = functools.reduce(operator.mul, [1, 2, 3], 1)
        self.assertEqual(product, 6)
        i=itertools.accumulate([1, 2, 3, 4, 5])
        self.assertEqual(list(i), [1, 3, 6, 10, 15])
        i1=itertools.accumulate([1, 2, 3, 4, 5], operator.mul)
        self.assertEqual(list(i1),[1,2,6,24,120])
if __name__ == '__main__':
    unittest.main()

                