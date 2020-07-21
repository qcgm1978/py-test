
import unittest
class TDDdir(unittest.TestCase):
    def test_dir(self):
        # The resulting list is sorted alphabetically. For example:
        self.assertTrue(True)
        import struct
        d=dir()   # show the names in the module namespace  
        self.assertEqual(d,['self','struct'])
        s=dir(struct)   # show the names in the struct module 
        self.assertEqual(s,['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_clearcache', 'calcsize', 'error', 'iter_unpack', 'pack', 'pack_into', 'unpack', 'unpack_from'])
        class Shape:
            pass
        s = Shape()
        self.assertEqual(len( dir(s)),26)
        def dir1(self):
                return ['area', 'perimeter', 'location']
        Shape.__dir__=dir1
        self.assertEqual(s.__dir__(),['area', 'perimeter', 'location'])
        self.assertCountEqual(dir(s),['area', 'perimeter', 'location'])

if __name__ == '__main__':
    unittest.main()

                