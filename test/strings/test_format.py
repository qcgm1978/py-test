import os,glob
import unittest
import sys


class TDDDiveIntoPython3(unittest.TestCase):

    def test_abstractions(self):
        s='深入 python'
        self.assertEqual(len(s),9)
        self.assertEqual(s[0],'深')
        self.assertEqual(s+'3','深入 python3')
        username='mark'
        password='PapayaWhip'
        s="{0}'s password is {1}".format(username,password)
        self.assertEqual(s,'mark\'s password is PapayaWhip')
    

if __name__ == '__main__':
    unittest.main()
