from datatype import DataTypes
import unittest, numpy as np
from mysql_data.decorators_func import singleton
class TDD_TEST_DATA(unittest.TestCase):
    @singleton
    def setUp(self):
        sqlData=[
            { 'speed':[99,86,87,88,111,86,103,87,94,78,77,85,86]}
        ]
        self.__class__.d = DataTypes({'sqlData':sqlData,'unique':['address','speed']})
        return super().setUp()
    def test_mean(self):
        m=self.d.getMean()
        self.assertAlmostEqual(m,89.77,2)
        middle=self.d.getMedian()
        self.assertAlmostEqual(middle,87,0,1)
        l=[99,86,87,88,86,103,87,94,78,77,85,86]
        count=self.d.updateField({'field':'speed','to':l})
        self.assertEqual(count, 1)
        mode = self.d.getMode()[0]
        self.assertEqual(mode, 86)
    def test_std(self):
        l=[86,87,88,86,87,85,86]
        count=self.d.updateField({'field':'speed','to':l})
        self.assertEqual(count, 1)
        self.assertAlmostEqual(self.d.getStd(),.9,1)
        
        
if __name__ == '__main__':
    unittest.main()
