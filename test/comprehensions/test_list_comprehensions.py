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

    def test_dict(self):
        metadata=[(f,os.stat(f)) for f in glob.glob('*test*.py')]
        self.assertRegexpMatches(metadata[0][0],'test')
        metadata_dict={f:os.stat(f) for f in glob.glob('*test*.py')}
        self.assertEqual(type(metadata_dict),dict)
        list_dict=list(metadata_dict.keys())
        self.assertRegexpMatches(list_dict[0],'.py')
        size=metadata_dict['test_list_comprehensions.py'].st_size
        self.assertTrue(size>0)
        metadata_dict={f:os.stat(f) for f in glob.glob('*')}
        # humansize_dict={os.path.splitext(f)[0]:approximate_size(meta.st_size) for f, meta in metadata_dict.items() if meta.st_size>6000}
        # a_list=list(humansize_dict.keys)
        # self.assertEqual(a_list,[])

    def test_swap(self):
        a_dict={'a':1,'b':2,'c':3}
        two_dict={value:key for key,value in a_dict.items()}
        self.assertEqual(two_dict,{1:'a',2:'b',3:'c'})
        a_dict={'a':[1,2,3],'b':4,'c':5}
        self.assertRaises(TypeError,lambda: {value:key for key,value in a_dict.items()} )

if __name__ == '__main__':
    unittest.main()
