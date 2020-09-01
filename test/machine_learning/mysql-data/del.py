
import unittest
class TDD_DEL(unittest.TestCase):
    def setUp(self):
        self.m = MysqlOp('customers')
        return super().setUp()
    def test_del(self):
        print(mycursor.rowcount, "record(s) deleted")
# address = 'Mountain 21'
if __name__ == '__main__':
    unittest.main()

                