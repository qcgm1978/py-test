import os,glob
import unittest
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app.humansize import approximate_size  # pylint: disable=import-error


class TDDDiveIntoPython3(unittest.TestCase):

    def test_compact(self):
        a_list=[1,9,8,4]
        compact=[elem * 2 for elem in a_list]
        self.assertEqual(compact, [2,18,16,8])
        self.assertEqual(a_list,[1,9,8,4])
        a_list=compact
        self.assertEqual(a_list,[2,18,16,8])
        os.chdir('test/comprehensions')
        py=glob.glob('*.py')
        self.assertEqual(type(py),list)
        real_path=[os.path.realpath(f) for f in py]
        [self.assertRegexpMatches(path,'test') for path in real_path]
        big=[f for f in glob.glob('*.py') if os.stat(f).st_size>6000]
        self.assertEqual(big,[])
        a_list=[(os.stat(f).st_size,os.path.realpath(f)) for f in glob.glob('*.py')]
        self.assertEqual(type(a_list[0][0]),int)
        self.assertEqual(type(a_list[0][1]),str)
        size=[(approximate_size(os.stat(f).st_size),f) for f in glob.glob('*.py')]
        self.assertEqual(type(size[0]),tuple)

if __name__ == '__main__':
    unittest.main()
