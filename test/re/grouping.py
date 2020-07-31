
import unittest,re
class TDD_GROUPING(unittest.TestCase):
    def test_grouping(self):
        p = re.compile('(ab)*')
        self.assertEqual(p.match('ababababab').span(),(0,10))
        p = re.compile('(a)b')
        m = p.match('ab')
        self.assertEqual(m.group(),'ab')
        self.assertEqual(m.group(0),'ab')
        self.assertEqual(m.group(1),'a')
        p = re.compile('(a(b)c)d')
        m = p.match('abcd')
        self.assertEqual(m.group(0),        'abcd')
        self.assertEqual(m.group(1),        'abc')
        self.assertEqual(m.group(2), 'b')
        self.assertEqual(m.group(2,1,2),('b','abc','b'))
        self.assertEqual(m.group(),('abcd'))
        self.assertEqual(m.groups(),('abc','b'))
        p = re.compile(r'\b(\w+)\s+\1\b')
        g=p.search('Paris in the the spring').group()
        self.assertEqual(g,'the the')
        
if __name__ == '__main__':
    unittest.main()

                