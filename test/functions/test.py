import os
import unittest
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app.humansize import approximate_size  # pylint: disable=import-error


class TDDDiveIntoPython3(unittest.TestCase):

    def test_current(self):
        size=approximate_size(4000, a_kilobyte_is_1024_bytes=False)
        self.assertEqual( size,'4.0 KB')

    
if __name__ == '__main__':
    unittest.main()
