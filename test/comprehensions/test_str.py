import os, glob
import unittest
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app.humansize import approximate_size  # pylint: disable=import-error


class TDDDiveIntoPython3(unittest.TestCase):
    def test_str(self):
       s = '''Finished files are the re-
... sult of years of scientif-
... ic study combined with the
... experience of years.'''
       lines=s.splitlines()
       self.assertEqual(lines,[
           'Finished files are the re-',
'... sult of years of scientif-',
'... ic study combined with the',
'... experience of years.'
       ])
       lower=s.lower()
       self.assertEqual(lower,'''finished files are the re-
... sult of years of scientif-
... ic study combined with the
... experience of years.''')
       count=lower.count('f')
       self.assertEqual(count,6)
       query = 'user=pilgrim&database=master&password=PapayaWhip'
       a_list=query.split('&')
       a_list=['user=pilgrim','database=master','password=PapayaWhip']
       a_lists_of_list=[v.split('=',1) for v in a_list if '=' in v]
       self.assertEqual(a_lists_of_list,[['user','pilgrim'],['database','master'],['password','PapayaWhip']])
       a_dict=dict(a_lists_of_list)
       self.assertEqual(a_dict,{
           'user':'pilgrim','database':'master','password':'PapayaWhip'
       })
       a_string = 'My alphabet starts where your alphabet ends.'
       three_eleven=a_string[3:11]
       self.assertEqual(three_eleven,'alphabet')
       three_negative_three=a_string[3:-3]
       self.assertEqual(three_negative_three,'alphabet starts where your alphabet en')
       eighteen=a_string[:18]
       self.assertEqual(eighteen,'My alphabet starts')
       from_eighteen=a_string[18:]
       self.assertEqual(from_eighteen,' where your alphabet ends.')

    def test_bytes_str(self):
        by = b'abcd\x65'
        self.assertEqual(by,b'abcde')
        x='\x65'
        self.assertEqual(x,'e')
        x=b'\x65'
        self.assertEqual(x,b'e')
        self.assertEqual(type(by),bytes)
        self.assertEqual(len(by),5)
        by+=b'\xff'
        self.assertEqual(by,b'abcde\xff')
        self.assertEqual(len(by),6)
        self.assertEqual(by[0],97)
        barr=bytearray(by)
        self.assertEqual(barr,bytearray(b'abcde\xff'))
        self.assertEqual(len(barr),6)
        self.assertEqual(barr[0],97)
        by=b'd'
        s='abcde'
        self.assertRaises(TypeError,lambda: by+s)
        self.assertRaises(TypeError,lambda: s.count(by))
        try:
            s.count('d')
        except TypeError:
            self.fail("lambda raised ExceptionType unexpectedly!")
        count=s.count(by.decode('ascii'))
        self.assertEqual(count,1)
        a_string = '深入 Python'
        self.assertEqual(len(a_string),9)
        by=a_string.encode('utf-8')
        self.assertEqual(by,b'\xe6\xb7\xb1\xe5\x85\xa5 Python')
        self.assertEqual(len(by),13)
        by=a_string.encode('big5')
        self.assertEqual(by,b'\xb2`\xa4J Python')
        self.assertEqual(len(by),11)
        roundtip=by.decode('big5')
        self.assertEqual(roundtip,'深入 Python')
        self.assertEqual(roundtip,a_string)

if __name__ == '__main__':
    unittest.main()
