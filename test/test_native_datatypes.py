import unittest
import fractions
import math
class TddInPythonExample(unittest.TestCase):

    def test_test(self):
        self.assertEqual(4, True*4)
    def test_num_operate(self):
        self.assertEqual(11 / 2, 5.5)
        self.assertEqual(11//2,5)
        self.assertEqual(-11//2,-6)
        self.assertEqual(11.0//2,5.0)
        self.assertEqual(11.0**2,121.0)
        self.assertEqual(11.0 % 2, 1.0)
    def test_fractions(self):
        self.assertTrue(fractions)
        self.assertTrue(callable(fractions.Fraction))
        self.assertFalse(callable(fractions.Fraction(1,3)))
        self.assertFalse(callable(fractions.Fraction(1, 3) * 2))
        self.assertRaises(ZeroDivisionError, fractions.Fraction, 1, 0)

    def test_Trigonometry(self):
        self.assertTrue(math)
        self.assertAlmostEqual(math.pi,3.14,2)
        self.assertEqual(math.sin(math.pi/2),1.0)
        self.assertAlmostEqual(round(math.tan(math.pi/4),2),1.0,2)
   
    a_list=['a','b','mpilgrim','z','example']
    def test_list(self):
        self.assertEqual(self.a_list,['a','b','mpilgrim','z','example'])
        self.assertEqual(self.a_list[0],'a')
        self.assertEqual(self.a_list[4],'example')
        self.assertEqual(self.a_list[-1],'example')
        self.assertEqual(self.a_list[-3],'mpilgrim')

    def test_slicing(self):
        self.assertEqual(self.a_list[1:3],['b','mpilgrim'])
        self.assertEqual(self.a_list[1:-1],['b','mpilgrim','z'])
        self.assertEqual(self.a_list[0:3],['a','b','mpilgrim'])
        self.assertEqual(self.a_list[:3],['a','b','mpilgrim'])
        self.assertEqual(self.a_list[3:],['z','example'])
        self.assertEqual(self.a_list[:],self.a_list)

    def test_add_items_to_list(self):
        a_list=['a']
        self.assertEqual(a_list+[2.0,3],['a',2.0,3])
        self.assertEqual(a_list.append(True),None)
        self.assertEqual(a_list,['a',True])
        self.assertEqual(a_list.extend(['four','Ω']),None)
        self.assertEqual(a_list,['a',True,'four','Ω'])
        self.assertEqual(a_list.insert(0,'Ω'),None)
        self.assertEqual(a_list,['Ω','a',True,'four','Ω'])
        a_list=['a','b','c']
        a_list.extend(['d','e','f'])
        self.assertEqual(a_list,['a','b','c','d','e','f'])
        self.assertEqual(len(a_list),6)
        self.assertEqual(a_list[-1],'f')
        a_list.append(['g','h','i'])
        self.assertEqual(a_list,['a','b','c','d','e','f',['g','h','i']])
        self.assertEqual(len(a_list),7)
        self.assertEqual(a_list[-1],['g','h','i'])

if __name__ == '__main__':
    unittest.main()
