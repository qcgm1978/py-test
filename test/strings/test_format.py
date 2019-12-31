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

    def test_compound_field_names(self):
        si_suffixes=['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
        s="1000{0[0]} = 1{0[1]}".format(si_suffixes)
        self.assertEqual(s,'1000KB = 1MB')
        s='{0:.1f} {1}'.format(698.24,'GB')
        self.assertEqual(s,'698.2 GB')
        s='{0:.1f} {1}'.format(698.29,'GB')
        self.assertEqual(s,'698.3 GB')

if __name__ == '__main__':
    unittest.main()
