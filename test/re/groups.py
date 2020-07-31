
import unittest,re
class TDD_GROUPS(unittest.TestCase):
    def test_groups(self):
        # [abc] matches the a, which is captured in group #1. Then it matches b and captures it in group #1, overwriting the a. Then again with the c, and that's what's left in group #1 at the end of the match.
        m = re.match("([abc])+", "abc")
        self.assertEqual(m.group(),'abc')
        self.assertEqual(m.groups(),('c',))
        self.assertEqual(m.groups(0),('c',))
        self.assertEqual(m.groups(1),('c',))
        self.assertEqual(m.groups(20),('c',))
        self.assertEqual(re.match('[abc]+','abc').group(),'abc')
        self.assertEqual(re.match('[abc]+','abc').group(0),'abc')
        self.assertRaises(IndexError,lambda x:re.match('[abc]+','abc').group(10),'abc')
        self.assertEqual(re.match('[abc]+', 'abc').group(0), 'abc')
        f = re.finditer('([abc])', 'abc')
        t=()
        for i in f:
            t += (i.groups())
        self.assertEqual(t, ('a', 'b', 'c'))
        m = re.match("(?:[abc])+", "abc")
        self.assertIsInstance(m.groups(),tuple)
        self.assertEqual(m.groups(), ())
    def test_named_groups(self):
        p = re.compile(r'(?P<word>\b\w+\b)')
        m = p.search('(((( Lots of punctuation )))')
        self.assertEqual(m.group('word'),'Lots')
        self.assertEqual(m.group(),'Lots')
        self.assertEqual(m.group(0),'Lots')
        self.assertEqual(m.group(1), 'Lots')
        m = re.match(r'(?P<first>\w+) (?P<last>\w+)', 'Jane Doe')
        self.assertEqual(m.groupdict(),{'first':'Jane','last':'Doe'})
    def test_handy_names(self):
        InternalDate = re.compile(r'INTERNALDATE "'
r'(?P<day>[ 123][0-9])-(?P<mon>[A-Z][a-z][a-z])-' r'(?P<year>[0-9][0-9][0-9][0-9])'
r' (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9])' r' (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])' r'"')
    def test_name_point(self):
        p = re.compile(r'\b(?P<word>\w+)\s+(?P=word)\b')
        self.assertEqual(p.search('Paris in the the spring').group(),'the the')

if __name__ == '__main__':
    unittest.main()

                