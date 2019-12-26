import os
import unittest


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


if __name__ == '__main__':
    unittest.main()
