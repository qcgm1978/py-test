
import unittest
from mysqlOp import MysqlOp
class TDD_READ(unittest.TestCase):
    def setUp(self):
        self.m = MysqlOp('customers')
        return super().setUp()
    def test_select(self):
        s = self.m.select()
        self.assertEqual(len(s),self.m.mycursor.rowcount)
        first=('John', 'Highway 21', 441)
        self.assertEqual(s[0],first)
        s1 = self.m.selectColumns(['name', 'address'])
        self.assertEqual(s1[0],('John', 'Highway 21'))
        self.assertEqual(self.m.fetchOne(), first)
    def test_unique(self):
        self.assertIsNone(self.m.unique('address'))
    def test_filter(self):
        f=self.m.where({'address' :'Park Lane 38'})
        self.assertEqual(f,[('Ben', 'Park Lane 38', 451)])
if __name__ == '__main__':
    unittest.main()

                