
import unittest,re
class TDD_MODULE_LEVEL(unittest.TestCase):
    def test_module_level(self):
        self.assertIsNone(re.match(r'From\s+', 'Fromage amk'))
        l=re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998')
        self.assertEqual(l.group(),'From ')
    def test_Compilation_Flags(self):
        charref = re.compile(r"""
            &[#] (          # Start of a numeric entity reference
            0[0-7]+         # Octal form
            | [0-9]+        # Decimal form
            | x[0-9a-fA-F]+ # Hexadecimal form
            )
            ;               # Trailing semicolon
        """ , re.VERBOSE)
    def test_metacharacters(self):
        self.assertEqual(re.search('^From', 'From Here to Eternity').span(),(0,4))
        self.assertIsNone(re.search('^From', 'Reciting From Memory'))
        self.assertEqual(re.search('}$', '{block}').group(), '}')
        # either the end of the string, or any location followed by a newline character.
        self.assertIsNone(re.search('}$', '{block} '))
        self.assertEqual(re.search('}$', '{block}\n').span(),(6,7))
    def test_word_boundary(self):
        p = re.compile(r'\bclass\b')
        self.assertIsInstance(p,re.Pattern)
        self.assertEqual(p.search('no class at all').span(),(3,8))
        self.assertIsNone(p.search('the declassified algorithm')) 
        self.assertIsNone(p.search('one subclass is'))
        p = re.compile('\bclass\b')
        self.assertIsNone(p.search('no class at all'))
        self.assertTrue(p.search('\b' + 'class' + '\b'))
        self.assertTrue(p.search('\bclass\b'))
        self.assertFalse(p.search('bclassb'))
if __name__ == '__main__':
    unittest.main()

                