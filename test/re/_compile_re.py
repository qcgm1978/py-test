
import unittest,re,collections
class TDD_COMPILE_RE(unittest.TestCase):
    def test__compile_re(self):
        p = re.compile('ab*')
        self.assertTrue(p)
        self.assertEqual(p, re.compile('ab*'))
        self.assertIsInstance(p, re.Pattern)
        p = re.compile('ab*', re.IGNORECASE)
    def test_perform_matches(self):
        p = re.compile('[a-z]+')
        self.assertIsNone(p.match(''))
        m = p.match('tempo')
        self.assertIsInstance(m,re.Match)
        self.assertEqual(m.group(),'tempo')
        self.assertEqual((m.start(), m.end()),(0,5))
        self.assertEqual(m.span(),(0,5))
        self.assertIsNone(p.match('::: message'))
        m = p.search('::: message')
        self.assertEqual((m.start(), m.end()),(4,11))
        self.assertEqual(m.group(),'message')
        self.assertEqual(m.span(),(4,11))
    def test_style(self):
        p = re.compile( '[a-z]+' )
        m = p.match('string goes here')
        self.assertEqual(m.group(), 'string')
        p = re.compile(r'\d+')
        l=p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
        self.assertEqual(l,['12','11','10'])
        iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
        self.assertIsInstance(iterator, collections.Iterable)
        t=()
        for match in iterator:
            t+= match.span(),
        self.assertEqual(t,((0, 2), (22, 24), (29, 31)))
if __name__ == '__main__':
    unittest.main()

                