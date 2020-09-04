from datatype import DataTypes
import unittest,numpy as np
class TDD_TEST_DATA(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    def test_mysql(self):
        sqlData=[
            { 'speed':[99,86,87,88,111,86,103,87,94,78,77,85,86]}
        ]
        d = DataTypes({'sqlData':sqlData})
if __name__ == '__main__':
    unittest.main()
