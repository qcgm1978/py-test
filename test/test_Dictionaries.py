import unittest
import fractions
import math
class TddInPythonExample(unittest.TestCase):

    a_dict={'server': 'db.diveintopython3.org', 'database': 'mysql'}
    def test_dictionary_create(self):
        self.assertEqual(self.a_dict,{'server': 'db.diveintopython3.org', 'database': 'mysql'})
        self.assertEqual(self.a_dict['server'],'db.diveintopython3.org')
        self.assertRaises(KeyError,lambda :self.a_dict['a'])

    def test_dictionary_modify(self):
        self.a_dict['database']='mark'
        self.assertEqual(self.a_dict,{'database':'mark','server': 'db.diveintopython3.org'})

    def test_mixed_dict(self):
        SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
        self.assertEqual(len(SUFFIXES),2)
        self.assertTrue(1000 in SUFFIXES)
        self.assertEqual(SUFFIXES[1000][3],'TB')

    def test_dict_as_bool(self):
        self.assertFalse({})
        self.assertTrue({"a":1})


























    

if __name__ == '__main__':
    unittest.main()
