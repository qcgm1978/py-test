import unittest,mysql
from mysqlOp import MysqlOp
class TDD_TEST_MYSQL(unittest.TestCase):
    def setUp(self):
        self.m = MysqlOp()
        return super().setUp()
    def test_test_mysql(self):
        self.m.showTables()
        self.assertIsInstance(self.m.mycursor, object)
        for k in self.m.mycursor:
            self.assertEqual(k, ('customers',))
    def test_key(self):
        self.assertRaises(mysql.connector.errors.ProgrammingError,lambda:self.m.createPrimaryKey())
if __name__ == '__main__':
    unittest.main()
