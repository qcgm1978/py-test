
import unittest
class TDDdelattr(unittest.TestCase):
    def test_delattr(self):
        # This is a relative of setattr(). The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it. For example, delattr(x, 'foobar') is equivalent to del x.foobar.
        o = {'foobar': 1}
        self.assertRaises(AttributeError,lambda:delattr(o,'foobar'))
        self.assertEqual(o['foobar'],1)
        class Person:
            name = 'Adam'
            
        p = Person()
        self.assertEqual(p.name,'Adam')

        # setting name to 'John'
        setattr(p, 'name', 'John')

        self.assertEqual(p.name, 'John')
        self.assertRaises(TypeError, lambda: p['name'])
        delattr(p, 'name')
        self.assertEqual(p.name,'Adam')
        self.assertRaises(AttributeError,lambda:delattr(p, 'name'))

if __name__ == '__main__':
    unittest.main()

                