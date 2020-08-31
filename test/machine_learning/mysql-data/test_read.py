
import unittest
from mysqlOp import MysqlOp
class TDD_READ(unittest.TestCase):
    def setUp(self):
        self.m = MysqlOp('customers')
        return super().setUp()
    def test_select(self):
        s = self.m.select()
        self.assertEqual(len(s),self.m.mycursor.rowcount)
        first=('John', 'Highway 21', 1)
        self.assertEqual(s[0],first)
        s1 = self.m.selectColumns(['name', 'address'])
        self.assertEqual(s1[0],('John', 'Highway 21'))
        self.assertEqual(self.m.fetchOne(),first)
if __name__ == '__main__':
    unittest.main()

                