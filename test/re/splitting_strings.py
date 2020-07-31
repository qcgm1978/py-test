
import unittest,re
class TDD_SPLITTING_STRINGS(unittest.TestCase):
    def test_splitting_strings(self):
        p = re.compile(r'\W+')
        self.assertEqual(p.split('This is a test, short and sweet, of split().'),['This', 'is', 'a', 'test', 'short', 'and', 'sweet', 'of', 'split', ''])
        self.assertEqual(p.split('This is a test, short and sweet, of split().', 3),['This', 'is', 'a', 'test, short and sweet, of split().'])
    def test_delimiter(self):
        p = re.compile(r'\W+')
        p2 = re.compile(r'(\W+)')
        self.assertEqual(p.split('This... is a test.'),     ['This', 'is', 'a', 'test', ''])
        self.assertEqual(p2.split('This... is a test.'),['This','... ', 'is',' ', 'a',' ', 'test','.', ''])
    def test_re_split(self):
        s = re.split(r'[\W]+', 'Words, words, words.')
        self.assertEqual(s,['Words', 'words', 'words', ''])
        s1 = re.split(r'([\W]+)', 'Words, words, words.')
        self.assertEqual(s1,['Words', ', ', 'words', ', ', 'words', '.', ''])
        s2=re.split(r'[\W]+', 'Words, words, words.', 1)
        self.assertEqual(s2,['Words','words, words.'])

if __name__ == '__main__':
    unittest.main()

                