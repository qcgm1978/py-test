import unittest
from mysqlOp import MysqlOp
class TDD_TEST_MYSQL(unittest.TestCase):
    def test_test_mysql(self):
        m = MysqlOp()
        m.showTables()
        self.assertIsInstance(m.mycursor, object)
        for k in m.mycursor:
            self.assertEqual(k,('customers',))
if __name__ == '__main__':
    unittest.main()
