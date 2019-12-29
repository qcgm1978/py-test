import os,glob
import unittest
import re
class TDDDiveIntoPython3(unittest.TestCase):

    def test_re(self):
        s = '100 NORTH MAIN ROAD'
        abbreviation=s.replace('ROAD','RD.')
        self.assertEqual(abbreviation,'100 NORTH MAIN RD.')
        s = '100 NORTH BROAD ROAD'
        abbreviation=s.replace('ROAD','RD.')
        self.assertEqual(abbreviation,'100 NORTH BRD. RD.')
        concat=s[:-4]+s[-4:].replace('ROAD','RD.')
        self.assertEqual(concat,'100 NORTH BROAD RD.')
        sub=re.sub('ROAD$','RD.',s)
        self.assertEqual(sub,'100 NORTH BROAD RD.')
        s = '100 BROAD'
        sub=re.sub('BROAD$','RD.',s)
        self.assertEqual(sub,'100 RD.')
        sub=re.sub('\\bBROAD$','RD.',s)
        self.assertEqual(sub,'100 RD.')
        s = '100 BROAD ROAD APT. 3'
        sub=re.sub(r'\bBROAD$','RD.',s)
        self.assertEqual(sub,'100 BROAD ROAD APT. 3')
        sub=re.sub(r'\bROAD\b','RD.',s)
        self.assertEqual(sub,'100 BROAD RD. APT. 3')
    
    def test_thousand_roman_numbral(self):
        pattern = '^M?M?M?$'
        self.assertTrue(re.search(pattern, 'M'))
        self.assertTrue(re.search(pattern, 'MM'))
        self.assertTrue(re.search(pattern, 'MMM'))
        self.assertFalse(re.search(pattern, 'MMMM'))
        self.assertTrue(re.search(pattern, ''))

    def test_hundred(self):
        pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
        self.assertTrue(re.search(pattern, 'MCM'))
        self.assertTrue(re.search(pattern, 'MD'))
        self.assertTrue(re.search(pattern, 'MMMCCC'))
        self.assertFalse(re.search(pattern, 'MCMC'))
        self.assertTrue(re.search(pattern, ''))

    def test_between(self):
        pattern = '^M{0,3}$'
        self.assertTrue( re.search(pattern, 'M') )
        self.assertTrue( re.search(pattern, 'MM') )
        self.assertTrue( re.search(pattern, 'MMM') )
        self.assertFalse( re.search(pattern, 'MMMM') )

    def test_tens_ones(self):
        pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)$'
        self.assertTrue(re.search(pattern, 'MCMXL'))
        self.assertTrue(re.search(pattern, 'MCML'))
        self.assertTrue(re.search(pattern, 'MCMLX'))
        self.assertTrue(re.search(pattern, 'MCMLXXX'))
        self.assertFalse(re.search(pattern, 'MCMLXXXX'))
        pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        self.assertTrue(re.search(pattern, 'MDLV') )
        self.assertTrue(re.search(pattern, 'MMDCLXVI') )
        self.assertTrue(re.search(pattern, 'MMMDCCCLXXXVIII') )
        self.assertTrue(re.search(pattern, 'I') )

    def test_verbose(self):
        pattern = '''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    '''
        self.assertTrue(re.search(pattern, 'M', re.VERBOSE))
        self.assertTrue(re.search(pattern, 'MCMLXXXIX', re.VERBOSE))
        self.assertTrue(re.search(pattern, 'MMMDCCCLXXXVIII', re.VERBOSE))
        self.assertFalse(re.search(pattern, 'M'))


if __name__ == '__main__':
    unittest.main()
