import unittest
import re,os,sys

from plural import plural  # pylint: disable=import-error
from plural_pattern import plural_pattern ,rules # pylint: disable=import-error
from plural_file import plural_file ,rules # pylint: disable=import-error
class TDDDiveIntoPython3(unittest.TestCase):

    def plural(noun):          
        if re.search('[sxz]$', noun):             
            return re.sub('$', 'es', noun)        
        elif re.search('[^aeioudgkprt]h$', noun):
            return re.sub('$', 'es', noun)       
        elif re.search('[^aeiou]y$', noun):      
            return re.sub('y$', 'ies', noun)     
        else:
            return noun + 's'

    def test_re(self):
        abc=re.search('[abc]', 'Mark')
        self.assertEqual(abc.regs[0],(1,2))
        sub=re.sub('[abc]', 'o', 'Mark')
        self.assertEqual(sub,'Mork')
        sub=re.sub('[abc]', 'o', 'Maraka')
        self.assertEqual(sub,'Moroko')
        sub= re.sub('[abc]', 'o', 'rock')
        self.assertEqual(sub,'rook')
        sub=re.sub('[abc]', 'o', 'caps') 
        self.assertEqual(sub,'oops')
        sub=re.search('[^aeiou]y$', 'vacancy')
        self.assertEqual(sub.regs[0],(5,7))
        sub=re.search('[^aeiou]y$', 'boy')
        self.assertEqual(sub,None)
        sub=re.search('[^aeiou]y$', 'day')
        self.assertEqual(sub,None)
        sub=re.search('[^aeiou]y$', 'pita') 
        self.assertEqual(sub,None)
        sub=re.sub('y$', 'ies', 'vacancy') 
        self.assertEqual(sub,'vacancies')
        sub=re.sub('y$', 'ies', 'agency')
        self.assertEqual(sub,'agencies')
        sub=re.sub('([^aeiou])y$', r'\1ies', 'vacancy')
        self.assertEqual(sub,'vacancies')

    


    def test_plural(self):
        self.assertTrue(plural)
        plural1=plural('face')
        self.assertEqual(plural1,'faces')
        self.assertEqual(len(rules),4)
        plural1=plural_pattern('house')
        self.assertEqual(plural1,'houses')
        plural1=plural_file('bicycle')
        self.assertEqual(plural1,'bicycles')





















if __name__ == '__main__':
    unittest.main()
