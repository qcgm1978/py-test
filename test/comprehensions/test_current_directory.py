import os
import unittest
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app.humansize import approximate_size  # pylint: disable=import-error


class TDDDiveIntoPython3(unittest.TestCase):

    def test_current(self):
        self.assertEqual(os.getcwd(), '/Users/philipp/py-test')
        os.chdir('/Users/philipp/Liyongle')
        self.assertEqual(os.getcwd(), '/Users/philipp/Liyongle')

    def test_filename_dirname(self):
        path = os.path.join('/Users/philipp/', 'test.py')
        self.assertEqual(path, '/Users/philipp/test.py')
        path = os.path.join('/Users/philipp', 'test.py')
        self.assertEqual(path, '/Users/philipp/test.py')
        path = os.path.expanduser('~')
        self.assertEqual(path, '/Users/philipp')
        path = os.path.join(os.path.expanduser(
            '~'), 'test-dir', 'test-dir2', 'test.py')
        self.assertEqual(path, '/Users/philipp/test-dir/test-dir2/test.py')
        pathname = '/Users/pilgrim/diveintopython3/examples/humansize.py'
        path_split = os.path.split(pathname)
        self.assertEqual(
            path_split, ('/Users/pilgrim/diveintopython3/examples', 'humansize.py'))
        (dirname,filename)=path_split
        self.assertEqual(dirname,'/Users/pilgrim/diveintopython3/examples')
        self.assertEqual(filename,'humansize.py')
        (shortname,extension)=os.path.splitext(filename)
        self.assertEqual(shortname,'humansize')
        self.assertEqual(extension,'.py')
    def test_lst_dir(self):
        os.chdir('/Users/philipp/py-test')
        self.assertEqual(os.getcwd(),'/Users/philipp/py-test')
        import glob
        a_list=glob.glob('examples/*.xml')
        self.assertEqual(a_list,[])
        a_list=glob.glob('test/**/test_*.py')
        self.assertTrue(len(a_list)>0)
        os.chdir('test/comprehensions')
        a_list=glob.glob('*test*.py')
        self.assertTrue(len(a_list)>0)

    def test_metadata(self):
        self.assertEqual(os.getcwd(),'/Users/philipp/py-test/test/comprehensions')
        metadata=os.stat('test_current_directory.py')
        self.assertEqual(type(metadata.st_mtime),float)
        import time
        localtime=time.localtime(metadata.st_mtime)
        self.assertEqual(type(localtime),time.struct_time)
        self.assertTrue(metadata.st_size>0)
        size=approximate_size(metadata.st_size)
        self.assertEqual(type(size),str)
        real_path=os.path.realpath('test_current_directorh.py')
        self.assertEqual(real_path,'/Users/philipp/py-test/test/comprehensions/test_current_directorh.py')

if __name__ == '__main__':
    unittest.main()
