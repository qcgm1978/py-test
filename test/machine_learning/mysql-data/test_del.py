from mysqlOp import MysqlOp
import unittest
class TDD_DEL(unittest.TestCase):
    def setUp(self):
        self.m = MysqlOp('customers')
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = ("John", "Mountain 21")
        self.m.insertInto(sql,val)
        return super().setUp()
    def test_del(self):
        ret=self.m.delete({'address' : 'Mountain 21'})
        self.assertEqual(ret,1 )
if __name__ == '__main__':
    unittest.main()
