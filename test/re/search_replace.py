
import unittest,re
class TDD_SEARCH_REPLACE(unittest.TestCase):
    def test_search_replace(self):
        p = re.compile('(blue|white|red)')
        p1=p.sub('colour', 'blue socks and red shoes')
        self.assertEqual(p1,'colour socks and colour shoes')
        p2=p.sub('colour', 'blue socks and red shoes', count=1)
        self.assertEqual(p2,'colour socks and red shoes')
    def test_subn(self):
        p = re.compile('(blue|white|red)')
        p1=p.subn('colour', 'blue socks and red shoes')
        self.assertEqual(p1,('colour socks and colour shoes', 2))
        p2=p.subn('colour', 'no colours at all')
        self.assertEqual(p2,('no colours at all', 0))
    def test_empty_match(self):
        p = re.compile('x*')
        p1 = p.sub('-', 'abxd')
        # Empty matches are replaced only when they’re not adjacent to a previous empty match.
        self.assertEqual(p1,'-a-b--d-')
        p = re.compile('section{ ( .*? ) }', re.VERBOSE)
        p_ = re.compile('section{ ( [^}]* ) }', re.VERBOSE)
        p1 = p.sub(r'subsection{\1}', 'section{First} section{second}')
        p2 = p_.sub(r'subsection{\1}', 'section{First} section{second}')
        self.assertEqual(p1,'subsection{First} subsection{second}')
        self.assertEqual(p2,'subsection{First} subsection{second}')
    def test_replace(self):
        p = re.compile('section{ (?P<name> [^}]* ) }', re.VERBOSE)
        s=p.sub(r'subsection{\1}', 'section{First}')
        self.assertEqual(s,'subsection{First}')
        s1=p.sub(r'subsection{\g<1>}', 'section{First}')
        self.assertEqual(s1,'subsection{First}')
        s2=p.sub(r'subsection{\g<name>}', 'section{First}')
        self.assertEqual(s2, 'subsection{First}')
    def test_translate(self):
        def hexrepl(match):
            "Return the hex string for a decimal number"
            value = int(match.group())
            return hex(value) 
        p = re.compile(r'\d+')
        s=p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
        self.assertEqual(s,'Call 0xffd2 for printing, 0xc000 for user code.')
if __name__ == '__main__':
    unittest.main()

                